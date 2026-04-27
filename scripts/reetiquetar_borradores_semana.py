"""
Añade la etiqueta PROSPECCION-{fecha} a borradores ya existentes cuya
proxima_accion cae entre --desde y --hasta, pero que fueron creados
antes de existir las etiquetas por día.

Uso:
    python -m scripts.reetiquetar_borradores_semana --desde 2026-04-21 --hasta 2026-04-24
"""
import argparse
import datetime as dt
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
LABEL_BASE = "PROSPECCION"


def ensure_label(service, name):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desde", required=True)
    parser.add_argument("--hasta", required=True)
    args = parser.parse_args()
    desde = dt.date.fromisoformat(args.desde)
    hasta = dt.date.fromisoformat(args.hasta)

    service = get_gmail_service()
    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))

    label_cache = {}
    reetiquetados = 0
    sin_draft = 0
    errores = []

    for slug, lead in pipeline.get("leads", {}).items():
        if slug.startswith("_"):
            continue
        accion = lead.get("proxima_accion") or {}
        fecha_str = accion.get("fecha")
        if not fecha_str:
            continue
        try:
            fecha_obj = dt.date.fromisoformat(fecha_str)
        except ValueError:
            continue
        if fecha_obj < desde or fecha_obj > hasta:
            continue

        message_id = lead.get("draft_message_id")
        if not message_id:
            sin_draft += 1
            continue

        label_name = f"{LABEL_BASE}-{fecha_obj.isoformat()}"
        if label_name not in label_cache:
            label_cache[label_name] = ensure_label(service, label_name)
        label_id = label_cache[label_name]

        try:
            service.users().messages().modify(
                userId="me", id=message_id,
                body={"addLabelIds": [label_id]},
            ).execute()
            print(f"  [ok] {slug} → {label_name}")
            reetiquetados += 1
        except HttpError as e:
            print(f"  [err] {slug}: {e.resp.status}")
            errores.append((slug, str(e.resp.status)))

    print(f"\nRe-etiquetados: {reetiquetados}")
    print(f"Sin draft_message_id: {sin_draft}")
    if errores:
        print(f"Errores: {len(errores)}")
        for s, e in errores:
            print(f"  - {s}: {e}")


if __name__ == "__main__":
    main()
