"""
Resincronizador one-shot. Lee el pipeline.json y para cada lead en
estado_email=pendiente_envio comprueba en Gmail (Sent) si su email T1 ya se
envió. Si lo encuentra:
  - cambia estado_email a enviado_t1 con la fecha real del Sent
  - registra historial mensaje_enviado
  - calcula proxima_accion T2 a +7 días desde la fecha real
  - limpia draft_id/draft_message_id

También detecta envíos duplicados (>1 mensaje en Sent al mismo destinatario
con mismo Subject en menos de 24h) y los anota en notas del lead.
"""
import datetime as dt
import json
import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.gmail_auth import get_gmail_service

PIPELINE_PATH = ROOT / "data" / "pipeline.json"


def load_pipeline():
    return json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))


def save_pipeline(data):
    PIPELINE_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def buscar_sent_para(service, destinatario: str, asunto: str, desde: dt.date):
    """Devuelve lista de (fecha, message_id) ordenados ascendente."""
    desde_str = desde.strftime("%Y/%m/%d")
    asunto_q = asunto.replace('"', '\\"')
    q = f'in:sent to:{destinatario} subject:"{asunto_q}" after:{desde_str}'
    res = service.users().messages().list(userId="me", q=q, maxResults=10).execute()
    out = []
    for m in res.get("messages", []):
        meta = service.users().messages().get(
            userId="me", id=m["id"], format="metadata",
            metadataHeaders=["Date", "Subject", "To"],
        ).execute()
        ts_ms = int(meta.get("internalDate", "0"))
        fecha = dt.datetime.utcfromtimestamp(ts_ms / 1000).date()
        out.append((fecha, m["id"]))
    out.sort()
    return out


def extraer_asunto_borrador(service, draft_message_id: str) -> str:
    if not draft_message_id:
        return ""
    try:
        meta = service.users().messages().get(
            userId="me", id=draft_message_id, format="metadata",
            metadataHeaders=["Subject"],
        ).execute()
        for h in meta.get("payload", {}).get("headers", []):
            if h.get("name", "").lower() == "subject":
                return h.get("value", "")
    except Exception:
        pass
    return ""


def main():
    service = get_gmail_service()
    p = load_pipeline()
    leads = p.get("leads", {})

    cambios = 0
    duplicados = []
    sin_match = []

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        if lead.get("estado_email") != "pendiente_envio":
            continue

        destinatario = (lead.get("contacto") or {}).get("email")
        if not destinatario:
            sin_match.append((slug, "sin email"))
            continue

        asunto = extraer_asunto_borrador(service, lead.get("draft_message_id", ""))
        if not asunto:
            # fallback: si no podemos leer el draft, intentar deducir desde outbox
            sin_match.append((slug, "no pude leer asunto del borrador"))
            continue

        desde = dt.date(2026, 4, 13)
        sents = buscar_sent_para(service, destinatario, asunto, desde)
        if not sents:
            sin_match.append((slug, f"no hay Sent para {destinatario} subject={asunto[:40]}"))
            continue

        primero_fecha, _ = sents[0]
        # Detectar duplicados (>1 envío en mismo día)
        mismas_fecha = [s for s in sents if s[0] == primero_fecha]
        if len(mismas_fecha) > 1:
            duplicados.append((slug, primero_fecha.isoformat(), len(mismas_fecha)))

        # Actualizar pipeline
        lead["estado_email"] = "enviado_t1"
        lead["draft_id"] = None
        lead.pop("draft_message_id", None)
        lead.pop("fecha_programada_envio", None)
        lead.setdefault("historial", []).append({
            "tipo": "mensaje_enviado",
            "canal": "email",
            "toque": "t1",
            "fecha": primero_fecha.isoformat(),
            "fuente": "resincronizado_desde_gmail",
            "envios_detectados": len(sents),
        })
        if len(sents) > 1:
            nota_extra = f" [DUPLICADO: {len(sents)} envíos a {destinatario} el {primero_fecha}]"
            lead["notas"] = (lead.get("notas") or "") + nota_extra

        siguiente = primero_fecha + dt.timedelta(days=7)
        lead["proxima_accion"] = {
            "fecha": siguiente.isoformat(),
            "tipo": "enviar_t2_si_no_responde",
            "generada": False,
        }
        cambios += 1
        print(f"[ok] {slug}: enviado el {primero_fecha} ({len(sents)} envíos), T2 a {siguiente}")

    save_pipeline(p)

    print()
    print(f"=== Resumen ===")
    print(f"Resincronizados: {cambios}")
    print(f"Duplicados detectados: {len(duplicados)}")
    for slug, fecha, n in duplicados:
        print(f"  ! {slug} {fecha} x{n}")
    print(f"Sin match: {len(sin_match)}")
    for slug, motivo in sin_match:
        print(f"  - {slug}: {motivo}")


if __name__ == "__main__":
    main()
