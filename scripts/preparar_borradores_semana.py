"""
Prepara en Gmail TODOS los borradores de una semana de golpe, cada uno con
etiqueta específica del día que toca enviar: PROSPECCION-2026-04-21,
PROSPECCION-2026-04-22, etc.

A diferencia de preparar_borradores.py (que solo prepara los del día siguiente
y corre como cron), este script procesa un rango de fechas completo para
que el usuario pueda revisar toda la semana en Gmail de una vez.

Uso:
    python -m scripts.preparar_borradores_semana --desde 2026-04-21 --hasta 2026-04-24
"""
import argparse
import base64
import datetime as dt
import io
import json
import re
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from googleapiclient.errors import HttpError
from scripts.gmail_auth import get_gmail_service

PIPELINE_PATH = ROOT / "data" / "pipeline.json"
OUTBOX = ROOT / "outbox"
LABEL_BASE = "PROSPECCION"


def load_pipeline():
    return json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))


def save_pipeline(data):
    PIPELINE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                             encoding="utf-8")


def ensure_label(service, name: str) -> str:
    """Devuelve labelId, creando la etiqueta si no existe."""
    labels = service.users().labels().list(userId="me").execute().get("labels", [])
    for lbl in labels:
        if lbl["name"] == name:
            return lbl["id"]
    created = service.users().labels().create(
        userId="me",
        body={"name": name, "labelListVisibility": "labelShow",
              "messageListVisibility": "show"},
    ).execute()
    print(f"  [label] creada: {name}")
    return created["id"]


def encontrar_archivo_email(slug: str, toque: str):
    for fecha_dir in sorted(OUTBOX.iterdir(), reverse=True):
        if not fecha_dir.is_dir():
            continue
        lead_dir = fecha_dir / slug
        html = lead_dir / f"email-{toque}.html"
        md = lead_dir / f"email-{toque}.md"
        if html.exists() and md.exists():
            return md, html
    return None


def extraer_asunto(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*Asunto:\*\*\s*(.+)", text)
    return m.group(1).strip() if m else "(sin asunto)"


def crear_borrador(service, destinatario: str, asunto: str, html_body: str):
    msg = MIMEMultipart("alternative")
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(html_body, "html"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw}}
    ).execute()
    return draft["id"], draft["message"]["id"]


def etiquetar_mensaje(service, message_id: str, label_ids: list):
    service.users().messages().modify(
        userId="me", id=message_id, body={"addLabelIds": label_ids}
    ).execute()


def procesar(desde: dt.date, hasta: dt.date):
    service = get_gmail_service()
    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})
    hoy = dt.date.today().isoformat()

    # Etiqueta base común (para mantener compatibilidad con el flujo del 18)
    label_base_id = ensure_label(service, f"{LABEL_BASE}-PENDIENTE")

    preparados_por_fecha = {}
    errores = []

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        accion = lead.get("proxima_accion") or {}
        tipo = (accion.get("tipo") or "").lower()
        toque = next((t for t in ("t1", "t2", "t3") if t in tipo), None)
        if not toque:
            continue

        fecha_accion = accion.get("fecha")
        if not fecha_accion:
            continue
        try:
            fecha_obj = dt.date.fromisoformat(fecha_accion)
        except ValueError:
            continue

        if fecha_obj < desde or fecha_obj > hasta:
            continue

        if lead.get("estado_email") == "pendiente_envio" and lead.get("draft_id"):
            print(f"  [skip] {slug}: ya tiene borrador")
            continue

        # Idempotencia robusta: si el historial ya tiene un borrador_creado para
        # este toque y esta fecha programada, no recrear (evita duplicados si
        # el script se relanza tras un fallo o cambio de versión).
        ya_creado = any(
            ev.get("tipo") == "borrador_creado"
            and ev.get("toque") == toque
            and ev.get("programado_para") == fecha_obj.isoformat()
            for ev in lead.get("historial", [])
        )
        if ya_creado:
            print(f"  [skip] {slug}: ya hay borrador_creado en historial para {toque} {fecha_obj}")
            continue

        # Solo saltar si el lead ya alcanzó este toque o uno posterior.
        # Para T2 el lead estará en enviado_t1 — eso NO es motivo de skip.
        ORDEN = {"t1": 1, "t2": 2, "t3": 3}
        estado = lead.get("estado_email", "")
        if estado.startswith("enviado_"):
            estado_toque = estado.split("_", 1)[1]
            if ORDEN.get(estado_toque, 0) >= ORDEN.get(toque, 0):
                print(f"  [skip] {slug}: estado={estado} ya >= {toque}")
                continue

        destinatario = (lead.get("contacto") or {}).get("email")
        if not destinatario or "@" not in destinatario or "pendiente.local" in destinatario:
            errores.append((slug, "sin email válido"))
            continue

        archivos = encontrar_archivo_email(slug, toque)
        if not archivos:
            errores.append((slug, f"sin email-{toque} en outbox"))
            continue

        md_path, html_path = archivos
        asunto = extraer_asunto(md_path)
        html_body = html_path.read_text(encoding="utf-8")

        # Etiqueta específica del día
        label_dia_name = f"{LABEL_BASE}-{fecha_obj.isoformat()}"
        label_dia_id = ensure_label(service, label_dia_name)

        try:
            draft_id, message_id = crear_borrador(
                service, destinatario, asunto, html_body)
            etiquetar_mensaje(service, message_id, [label_base_id, label_dia_id])
        except HttpError as e:
            errores.append((slug, f"gmail: {e}"))
            continue

        lead["estado_email"] = "pendiente_envio"
        lead["draft_id"] = draft_id
        lead["draft_message_id"] = message_id
        lead["fecha_programada_envio"] = fecha_obj.isoformat()
        lead.setdefault("historial", []).append({
            "tipo": "borrador_creado",
            "canal": "email",
            "toque": toque,
            "fecha": hoy,
            "programado_para": fecha_obj.isoformat(),
            "etiqueta_dia": label_dia_name,
        })
        preparados_por_fecha.setdefault(fecha_obj.isoformat(), []).append({
            "slug": slug, "empresa": lead.get("empresa"),
            "asunto": asunto, "destinatario": destinatario,
        })
        print(f"  [ok] {slug} → {destinatario} (etiqueta {label_dia_name})")

    save_pipeline(pipeline)

    print("\n=== Resumen ===")
    total = sum(len(v) for v in preparados_por_fecha.values())
    print(f"Total borradores preparados: {total}")
    for fecha in sorted(preparados_por_fecha):
        print(f"  {fecha}: {len(preparados_por_fecha[fecha])} borradores "
              f"(etiqueta {LABEL_BASE}-{fecha})")
    if errores:
        print(f"\nErrores ({len(errores)}):")
        for slug, msg in errores:
            print(f"  - {slug}: {msg}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desde", required=True, help="YYYY-MM-DD")
    parser.add_argument("--hasta", required=True, help="YYYY-MM-DD")
    args = parser.parse_args()
    desde = dt.date.fromisoformat(args.desde)
    hasta = dt.date.fromisoformat(args.hasta)
    procesar(desde, hasta)


if __name__ == "__main__":
    main()
