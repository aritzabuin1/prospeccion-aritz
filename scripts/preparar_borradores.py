"""
Prepara borradores de prospección en Gmail con etiqueta PROSPECCION-PENDIENTE.

Corre cada madrugada (00:30). Para cada lead del pipeline cuya proxima_accion
sea un email (t1/t2/t3) y cuya fecha caiga en el siguiente día óptimo:

  1. Lee outbox/{fecha_gen}/{slug}/email-t{N}.html y .md (asunto).
  2. Crea un borrador en Gmail (cuenta autenticada = aritzabuin1).
  3. Añade etiqueta PROSPECCION-PENDIENTE.
  4. Marca pipeline.json: estado_email=pendiente_envio + draft_id + fecha_prog.

El envío real lo hace scripts/enviar_pendientes.py a las 9:30.

Aritz revisa los borradores en Gmail entre 08:00-09:30. Para vetar un envío,
basta con borrar el borrador desde Gmail.
"""

import base64
import datetime as dt
import json
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from googleapiclient.errors import HttpError

from scripts.gmail_auth import get_gmail_service
from scripts.workday import es_dia_optimo, siguiente_dia_optimo

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_PATH = ROOT / "data" / "pipeline.json"
OUTBOX = ROOT / "outbox"
LABEL_NAME = "PROSPECCION-PENDIENTE"


def load_pipeline():
    with open(PIPELINE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pipeline(data):
    with open(PIPELINE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def ensure_label(service) -> str:
    """Devuelve el labelId de PROSPECCION-PENDIENTE, creándola si no existe."""
    labels = service.users().labels().list(userId="me").execute().get("labels", [])
    for lbl in labels:
        if lbl["name"] == LABEL_NAME:
            return lbl["id"]
    created = service.users().labels().create(
        userId="me",
        body={"name": LABEL_NAME, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
    ).execute()
    return created["id"]


def encontrar_archivo_email(slug: str, toque: str) -> tuple[Path, Path] | None:
    """Busca el email más reciente del slug para el toque dado."""
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


def crear_borrador(service, destinatario: str, asunto: str, html_body: str) -> str:
    msg = MIMEMultipart("alternative")
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(html_body, "html"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw}}
    ).execute()
    return draft["id"], draft["message"]["id"]


def etiquetar_mensaje(service, message_id: str, label_id: str):
    service.users().messages().modify(
        userId="me", id=message_id, body={"addLabelIds": [label_id]}
    ).execute()


def procesar():
    hoy = dt.date.today()
    maniana = hoy + dt.timedelta(days=1)
    service = get_gmail_service()
    label_id = ensure_label(service)

    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})
    preparados = []

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        accion = lead.get("proxima_accion") or {}
        tipo = (accion.get("tipo") or "").lower()
        # aceptar formatos 'enviar_t2_si_no_responde' o 'email_t1'
        toque = None
        for t in ("t1", "t2", "t3"):
            if t in tipo:
                toque = t
                break
        if not toque:
            continue

        # ¿toca mañana?
        fecha_accion = accion.get("fecha")
        if fecha_accion:
            try:
                fecha_obj = dt.date.fromisoformat(fecha_accion)
            except ValueError:
                fecha_obj = maniana
        else:
            fecha_obj = maniana

        # Solo preparar si mañana es el día óptimo para este toque Y coincide con la fecha programada
        if fecha_obj > maniana:
            continue
        if not es_dia_optimo(maniana, toque):
            # Re-programar a siguiente óptimo
            nueva = siguiente_dia_optimo(maniana, toque)
            lead["proxima_accion"]["fecha"] = nueva.isoformat()
            continue

        # Destinatario
        destinatario = (lead.get("contacto") or {}).get("email")
        if not destinatario:
            print(f"[skip] {slug}: sin email de contacto")
            continue

        # Ya tiene borrador en vuelo
        if lead.get("estado_email") == "pendiente_envio" and lead.get("draft_id"):
            continue

        archivos = encontrar_archivo_email(slug, toque)
        if not archivos:
            print(f"[skip] {slug}: no encuentro email-{toque}.html en outbox")
            continue
        md_path, html_path = archivos
        asunto = extraer_asunto(md_path)
        html_body = html_path.read_text(encoding="utf-8")

        try:
            draft_id, message_id = crear_borrador(service, destinatario, asunto, html_body)
            etiquetar_mensaje(service, message_id, label_id)
        except HttpError as e:
            print(f"[error] {slug}: {e}")
            continue

        lead["estado_email"] = "pendiente_envio"
        lead["draft_id"] = draft_id
        lead["draft_message_id"] = message_id
        lead["fecha_programada_envio"] = maniana.isoformat()
        lead.setdefault("historial", []).append({
            "tipo": "borrador_creado",
            "canal": "email",
            "toque": toque,
            "fecha": hoy.isoformat(),
            "programado_para": maniana.isoformat(),
        })
        preparados.append({"slug": slug, "empresa": lead.get("empresa"), "asunto": asunto, "destinatario": destinatario, "toque": toque})
        print(f"[ok] borrador creado para {slug} ({toque}) → {destinatario}")

    save_pipeline(pipeline)

    # Escribir lista para que notificar_revision.py la consuma
    (ROOT / "data" / "borradores_pendientes.json").write_text(
        json.dumps({"fecha_envio": maniana.isoformat(), "borradores": preparados}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nTotal borradores preparados: {len(preparados)} para envío {maniana}")


if __name__ == "__main__":
    procesar()
