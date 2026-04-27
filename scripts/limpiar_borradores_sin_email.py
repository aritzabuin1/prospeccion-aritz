"""
Limpieza definitiva:
  1. Borra permanentemente de Gmail (TRASH) los mensajes cuyo To contiene
     @pendiente.local.
  2. Resetea el estado del pipeline para los leads con email inválido o
     sin email: borra draft_id/draft_message_id/fecha_programada_envio,
     pone estado_email='nuevo'. Mantiene proxima_accion para que al
     obtener el email se pueda regenerar el borrador.

Tras ejecutar, en Gmail solo quedan borradores listos para enviar.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from googleapiclient.errors import HttpError
from scripts.gmail_auth import get_gmail_service

PIPELINE_PATH = ROOT / "data" / "pipeline.json"


def email_valido(email: str) -> bool:
    if not email:
        return False
    email = email.lower().strip()
    if "@" not in email:
        return False
    if "pendiente.local" in email:
        return False
    return True


def main():
    service = get_gmail_service()

    # 1. Borrar permanentemente los de la papelera con pendiente.local
    print("== Fase 1: borrar de papelera ==")
    results = service.users().messages().list(
        userId="me", q="in:trash to:pendiente.local", maxResults=500
    ).execute()
    msgs = results.get("messages", [])
    print(f"En papelera con placeholder: {len(msgs)}")
    borrados = 0
    for m in msgs:
        try:
            service.users().messages().delete(userId="me", id=m["id"]).execute()
            borrados += 1
        except HttpError as e:
            print(f"  [err] {m['id']}: {e.resp.status}")
    print(f"Borrados permanentemente: {borrados}")

    # 2. Reset pipeline para leads sin email válido que tengan estado de borrador
    print("\n== Fase 2: reset pipeline ==")
    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))
    reseteados = 0
    for slug, l in pipeline.get("leads", {}).items():
        if slug.startswith("_"):
            continue
        email = (l.get("contacto") or {}).get("email")
        if email_valido(email):
            continue
        # No tiene email válido — si tiene estado de borrador, resetear
        cambio = False
        if l.get("draft_id") or l.get("draft_message_id"):
            l["draft_id"] = None
            l["draft_message_id"] = None
            cambio = True
        if l.get("estado_email") in ("pendiente_envio", "borrador_creado"):
            l["estado_email"] = "nuevo"
            cambio = True
        if l.get("fecha_programada_envio"):
            l["fecha_programada_envio"] = None
            cambio = True
        if cambio:
            l.setdefault("historial", []).append({
                "tipo": "borrador_limpiado",
                "motivo": "sin_email_valido",
                "fecha": __import__("datetime").date.today().isoformat(),
            })
            reseteados += 1
            print(f"  [reset] {slug}")

    PIPELINE_PATH.write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nLeads reseteados: {reseteados}")

    # 3. Resumen final
    con_draft_valido = sum(
        1 for l in pipeline["leads"].values()
        if not (isinstance(l, dict) and l.get("_")) and l.get("draft_message_id")
    )
    print(f"\nBorradores Gmail activos (con email válido): {con_draft_valido}")


if __name__ == "__main__":
    main()
