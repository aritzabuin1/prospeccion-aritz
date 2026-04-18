"""
Envío automático de borradores PROSPECCION-PENDIENTE.

Corre a las 09:30 días laborables. Para cada lead en pipeline con
estado_email=pendiente_envio cuya fecha_programada_envio es hoy:

  1. Verifica que el borrador sigue existiendo en Gmail.
  2. Si no existe → el usuario lo vetó → marcar cancelado_por_usuario.
  3. Si existe y no está ya enviado → drafts.send() → pasar a enviado_t{N}.
  4. Actualizar pipeline: historial + proxima_accion (T2 a +7, T3 a +14, cerrar a +21).

Respeta el calendario óptimo del workday.py:
- T1 solo martes/miércoles/jueves
- T2 solo martes/miércoles
- T3 solo martes

Si hoy no toca para un lead concreto, re-programa su fecha al siguiente día óptimo.
"""

import datetime as dt
import json
from pathlib import Path

from googleapiclient.errors import HttpError

from scripts.gmail_auth import get_gmail_service
from scripts.workday import es_dia_optimo, siguiente_dia_optimo

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_PATH = ROOT / "data" / "pipeline.json"

PROXIMOS_PASOS = {
    "t1": ("enviar_t2_si_no_responde", 7),
    "t2": ("enviar_t3_si_no_responde", 14),
    "t3": ("cerrar_hilo_si_no_responde", 21),
}


def load_pipeline():
    with open(PIPELINE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pipeline(data):
    with open(PIPELINE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def borrador_existe(service, draft_id: str) -> bool:
    try:
        service.users().drafts().get(userId="me", id=draft_id, format="minimal").execute()
        return True
    except HttpError as e:
        if e.resp.status == 404:
            return False
        raise


def enviar_borrador(service, draft_id: str):
    return service.users().drafts().send(userId="me", body={"id": draft_id}).execute()


def main():
    hoy = dt.date.today()
    service = get_gmail_service()
    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})

    enviados = 0
    vetados = 0
    reagendados = 0

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        if lead.get("estado_email") != "pendiente_envio":
            continue
        draft_id = lead.get("draft_id")
        if not draft_id:
            continue
        fecha_prog = lead.get("fecha_programada_envio")
        if fecha_prog and fecha_prog != hoy.isoformat():
            continue

        # Identificar toque desde último evento borrador_creado
        toque = None
        for evt in reversed(lead.get("historial", [])):
            if evt.get("tipo") == "borrador_creado":
                toque = evt.get("toque")
                break
        if not toque:
            print(f"[skip] {slug}: no identifico toque del borrador")
            continue

        # Si hoy no es día óptimo, re-programar
        if not es_dia_optimo(hoy, toque):
            nueva = siguiente_dia_optimo(hoy + dt.timedelta(days=1), toque)
            lead["fecha_programada_envio"] = nueva.isoformat()
            print(f"[reagendado] {slug}: hoy no es óptimo para {toque} → {nueva}")
            reagendados += 1
            continue

        # ¿Sigue existiendo el borrador?
        if not borrador_existe(service, draft_id):
            lead["estado_email"] = "cancelado_por_usuario"
            lead["draft_id"] = None
            lead.setdefault("historial", []).append({
                "tipo": "envio_vetado",
                "canal": "email",
                "toque": toque,
                "fecha": hoy.isoformat(),
            })
            vetados += 1
            print(f"[vetado] {slug}: borrador borrado por usuario")
            continue

        # Enviar
        try:
            enviar_borrador(service, draft_id)
        except HttpError as e:
            print(f"[error] {slug}: {e}")
            continue

        lead["estado_email"] = f"enviado_{toque}"
        lead["draft_id"] = None
        lead.setdefault("historial", []).append({
            "tipo": "mensaje_enviado",
            "canal": "email",
            "toque": toque,
            "fecha": hoy.isoformat(),
            "hora": "09:30",
            "automatico": True,
        })
        # Próxima acción
        proximo_tipo, dias = PROXIMOS_PASOS.get(toque, (None, 0))
        if proximo_tipo:
            siguiente = hoy + dt.timedelta(days=dias)
            lead["proxima_accion"] = {
                "fecha": siguiente.isoformat(),
                "tipo": proximo_tipo,
                "generada": False,
            }
        enviados += 1
        print(f"[enviado] {slug} ({toque})")

    save_pipeline(pipeline)
    print(f"\nResumen {hoy}: enviados={enviados} vetados={vetados} reagendados={reagendados}")


if __name__ == "__main__":
    main()
