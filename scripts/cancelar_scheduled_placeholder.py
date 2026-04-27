"""
URGENTE: busca mensajes programados (label SCHEDULED) con destinatario
@pendiente.local y los mueve a la papelera para cancelar el envío.

Al hacer trash se quita del schedule y no se envía.
"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.gmail_auth import get_gmail_service


def get_to(msg):
    headers = msg.get("payload", {}).get("headers", [])
    for h in headers:
        if h.get("name", "").lower() == "to":
            return h.get("value", "")
    return ""


def main():
    service = get_gmail_service()

    # Buscar en SCHEDULED los que llevan el placeholder
    query = "in:scheduled to:pendiente.local"
    print(f"Buscando: {query}")
    results = service.users().messages().list(
        userId="me", q=query, maxResults=500
    ).execute()
    msgs = results.get("messages", [])
    print(f"Encontrados: {len(msgs)} mensajes programados con placeholder")

    cancelados = 0
    errores = []
    for m in msgs:
        msg_id = m["id"]
        try:
            full = service.users().messages().get(
                userId="me", id=msg_id, format="metadata",
                metadataHeaders=["To", "Subject"],
            ).execute()
            to = get_to(full)
            subj = next((h["value"] for h in full.get("payload", {}).get("headers", [])
                         if h.get("name", "").lower() == "subject"), "")
            # Mover a papelera — esto cancela el schedule
            service.users().messages().trash(userId="me", id=msg_id).execute()
            print(f"  [cancelado] To={to} Asunto={subj[:60]}")
            cancelados += 1
        except Exception as e:
            print(f"  [err] {msg_id}: {e}")
            errores.append((msg_id, str(e)))

    print(f"\nTotal cancelados: {cancelados}")
    if errores:
        print(f"Errores: {len(errores)}")


if __name__ == "__main__":
    main()
