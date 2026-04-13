"""
Busca respuestas en Gmail para leads con estado enviado en pipeline.
Guarda cada respuesta nueva en respuestas/{slug}-{timestamp}.md
y actualiza pipeline.json.

Uso:
    python scripts/check_respuestas.py
"""

import base64
import json
import os
import re
import sys
from datetime import datetime
from email.utils import parsedate_to_datetime

from scripts.gmail_auth import get_gmail_service
from scripts.pipeline_utils import load_pipeline, save_pipeline

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESPUESTAS_DIR = os.path.join(PROJECT_ROOT, "respuestas")

# Estados que indican que hemos enviado email y esperamos respuesta
ESTADOS_ESPERANDO = {"enviado_t1", "enviado_t2", "enviado_t3"}


def _strip_html(html_text: str) -> str:
    """Extrae texto plano de HTML básico."""
    text = re.sub(r"<br\s*/?>", "\n", html_text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _get_message_body(msg: dict) -> str:
    """Extrae cuerpo del mensaje en texto plano."""
    payload = msg.get("payload", {})

    # Intentar texto plano directo
    if payload.get("mimeType") == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")

    # Buscar en parts
    parts = payload.get("parts", [])
    for part in parts:
        if part.get("mimeType") == "text/plain":
            data = part.get("body", {}).get("data", "")
            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")

    # Fallback: HTML
    for part in parts:
        if part.get("mimeType") == "text/html":
            data = part.get("body", {}).get("data", "")
            if data:
                html = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
                return _strip_html(html)

    # Último recurso: body directo (sin parts)
    data = payload.get("body", {}).get("data", "")
    if data:
        raw = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
        if payload.get("mimeType", "").startswith("text/html"):
            return _strip_html(raw)
        return raw

    return "(no se pudo extraer el cuerpo del mensaje)"


def _get_header(msg: dict, name: str) -> str:
    """Extrae un header específico del mensaje."""
    headers = msg.get("payload", {}).get("headers", [])
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def _already_saved(slug: str, msg_id: str) -> bool:
    """Comprueba si ya guardamos esta respuesta (por Gmail message ID)."""
    if not os.path.exists(RESPUESTAS_DIR):
        return False
    for fname in os.listdir(RESPUESTAS_DIR):
        if fname.startswith(slug) and fname.endswith(".md"):
            filepath = os.path.join(RESPUESTAS_DIR, fname)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read(500)  # Solo leer cabecera
            if msg_id in content:
                return True
    return False


def check_respuestas():
    """
    Busca respuestas en Gmail para cada lead con estado enviado.
    Devuelve lista de respuestas nuevas encontradas.
    """
    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})
    service = get_gmail_service()
    os.makedirs(RESPUESTAS_DIR, exist_ok=True)

    respuestas_nuevas = []

    for slug, lead in leads.items():
        estado = lead.get("estado_email", "nuevo")
        if estado not in ESTADOS_ESPERANDO:
            continue

        email_contacto = lead.get("contacto", {}).get("email")
        if not email_contacto:
            continue

        # Buscar mensajes del contacto en los últimos 30 días
        query = f"from:{email_contacto} newer_than:30d"
        try:
            results = service.users().messages().list(
                userId="me", q=query, maxResults=10
            ).execute()
        except Exception as e:
            print(f"  Error buscando emails de {email_contacto}: {e}")
            continue

        messages = results.get("messages", [])
        if not messages:
            continue

        for msg_ref in messages:
            msg_id = msg_ref["id"]

            # Evitar duplicados
            if _already_saved(slug, msg_id):
                continue

            # Obtener mensaje completo
            msg = service.users().messages().get(
                userId="me", id=msg_id, format="full"
            ).execute()

            from_addr = _get_header(msg, "From")
            date_str = _get_header(msg, "Date")
            subject = _get_header(msg, "Subject")
            body = _get_message_body(msg)

            # Timestamp para nombre de archivo
            try:
                dt = parsedate_to_datetime(date_str)
                ts = dt.strftime("%Y%m%d-%H%M")
            except Exception:
                ts = datetime.now().strftime("%Y%m%d-%H%M")

            # Guardar respuesta
            filename = f"{slug}-{ts}.md"
            filepath = os.path.join(RESPUESTAS_DIR, filename)

            content = (
                f"---\n"
                f"gmail_id: {msg_id}\n"
                f"slug: {slug}\n"
                f"from: {from_addr}\n"
                f"date: {date_str}\n"
                f"subject: {subject}\n"
                f"estado: sin_clasificar\n"
                f"---\n\n"
                f"{body}\n"
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            # Determinar toque al que responde
            toque_num = estado.replace("enviado_t", "")

            # Actualizar pipeline
            lead["estado_email"] = f"respondio_t{toque_num}"
            lead["historial"].append({
                "tipo": "respuesta_recibida",
                "canal": "email",
                "archivo": filename,
                "clasificada": False,
                "fecha": datetime.now().strftime("%Y-%m-%d"),
            })

            respuestas_nuevas.append({
                "slug": slug,
                "empresa": lead.get("empresa", slug),
                "archivo": filename,
                "subject": subject,
                "from": from_addr,
            })

            print(f"  Nueva respuesta: {lead.get('empresa', slug)} — {subject}")

    # Guardar cambios en pipeline
    if respuestas_nuevas:
        save_pipeline(pipeline)

    return respuestas_nuevas


def _self_test():
    """Test básico: verifica que el script carga pipeline y se conecta a Gmail."""
    pipeline = load_pipeline()
    leads_esperando = [
        slug for slug, lead in pipeline.get("leads", {}).items()
        if lead.get("estado_email") in ESTADOS_ESPERANDO
    ]
    print(f"Leads esperando respuesta: {len(leads_esperando)}")

    if leads_esperando:
        print("Buscando respuestas en Gmail...")
        nuevas = check_respuestas()
        print(f"Respuestas nuevas encontradas: {len(nuevas)}")
        for r in nuevas:
            print(f"  - {r['empresa']}: {r['subject']}")
    else:
        print("No hay leads con email enviado. Nada que buscar.")

    print("check_respuestas: test OK")


if __name__ == "__main__":
    _self_test()
