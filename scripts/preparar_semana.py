"""
One-shot: prepara borradores en Gmail para TODOS los leads cuya proxima_accion
caiga en los proximos dias optimos (mar/mie/jue de esta semana), con una
etiqueta por dia para que Aritz pueda programar el envio desde Gmail UI.

Uso:
    python -m scripts.preparar_semana

Se salta leads sin email (esos van por LinkedIn aparte).
"""

import base64
import datetime as dt
import json
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from googleapiclient.errors import HttpError

from scripts.gmail_auth import get_gmail_service
from scripts.preparar_borradores import (
    encontrar_archivo_email,
    extraer_asunto,
    load_pipeline,
    save_pipeline,
)

ROOT = Path(__file__).resolve().parent.parent
LABEL_BASE = "PROSPECCION-PENDIENTE"
DIA_A_LABEL = {
    1: "PROSPECCION-MARTES",
    2: "PROSPECCION-MIERCOLES",
    3: "PROSPECCION-JUEVES",
}


def ensure_label(service, name: str) -> str:
    labels = service.users().labels().list(userId="me").execute().get("labels", [])
    for lbl in labels:
        if lbl["name"] == name:
            return lbl["id"]
    created = service.users().labels().create(
        userId="me",
        body={"name": name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
    ).execute()
    return created["id"]


def crear_borrador(service, destinatario, asunto, html_body):
    msg = MIMEMultipart("alternative")
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(html_body, "html"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw}}
    ).execute()
    return draft["id"], draft["message"]["id"]


def etiquetar(service, message_id, label_ids):
    service.users().messages().modify(
        userId="me", id=message_id, body={"addLabelIds": label_ids}
    ).execute()


def procesar():
    hoy = dt.date.today()
    # Siguiente martes
    dias_a_martes = (1 - hoy.weekday()) % 7
    if dias_a_martes == 0 and hoy.weekday() != 1:
        dias_a_martes = 7
    martes = hoy + dt.timedelta(days=dias_a_martes)
    fechas_objetivo = {
        martes.isoformat(): ("t1-t2-t3", martes),
        (martes + dt.timedelta(days=1)).isoformat(): ("t1-t2", martes + dt.timedelta(days=1)),
        (martes + dt.timedelta(days=2)).isoformat(): ("t1", martes + dt.timedelta(days=2)),
    }

    service = get_gmail_service()
    label_base = ensure_label(service, LABEL_BASE)
    label_por_dia = {d: ensure_label(service, n) for d, n in DIA_A_LABEL.items()}

    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})
    resumen = {martes.isoformat(): [], (martes + dt.timedelta(days=1)).isoformat(): [], (martes + dt.timedelta(days=2)).isoformat(): []}
    sin_email = []
    skip = []

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        acc = lead.get("proxima_accion") or {}
        tipo = (acc.get("tipo") or "").lower()
        toque = next((t for t in ("t1", "t2", "t3") if t in tipo), None)
        if not toque:
            continue
        fecha = acc.get("fecha")
        if fecha not in fechas_objetivo:
            continue

        destinatario = (lead.get("contacto") or {}).get("email")
        if not destinatario:
            sin_email.append((slug, lead.get("empresa", slug), toque, fecha))
            continue

        if lead.get("estado_email") == "pendiente_envio" and lead.get("draft_id"):
            skip.append((slug, "ya tiene borrador"))
            continue

        archivos = encontrar_archivo_email(slug, toque)
        if not archivos:
            skip.append((slug, f"sin email-{toque}.html en outbox"))
            continue
        md_path, html_path = archivos
        asunto = extraer_asunto(md_path)
        html_body = html_path.read_text(encoding="utf-8")

        try:
            draft_id, message_id = crear_borrador(service, destinatario, asunto, html_body)
            fecha_obj = dt.date.fromisoformat(fecha)
            dow = fecha_obj.weekday()
            etiquetar(service, message_id, [label_base, label_por_dia[dow]])
        except HttpError as e:
            skip.append((slug, f"error Gmail: {e}"))
            continue

        lead["estado_email"] = "pendiente_envio"
        lead["draft_id"] = draft_id
        lead["draft_message_id"] = message_id
        lead["fecha_programada_envio"] = fecha
        lead.setdefault("historial", []).append({
            "tipo": "borrador_creado",
            "canal": "email",
            "toque": toque,
            "fecha": hoy.isoformat(),
            "programado_para": fecha,
        })
        resumen[fecha].append({
            "slug": slug,
            "empresa": lead.get("empresa"),
            "asunto": asunto,
            "destinatario": destinatario,
            "toque": toque,
        })
        print(f"[ok] {slug} ({toque}) -> {destinatario}  [envio {fecha}]")

    save_pipeline(pipeline)

    print("\n" + "=" * 70)
    print("RESUMEN BORRADORES CREADOS")
    print("=" * 70)
    for fecha in sorted(resumen):
        dow_nombre = dt.date.fromisoformat(fecha).strftime("%A")
        label = DIA_A_LABEL[dt.date.fromisoformat(fecha).weekday()]
        print(f"\n{fecha} ({dow_nombre})  label Gmail: {label}")
        for r in resumen[fecha]:
            print(f"  [{r['toque'].upper()}] {r['empresa']}  <{r['destinatario']}>")
            print(f"         Asunto: {r['asunto']}")

    if sin_email:
        print("\n" + "-" * 70)
        print("SIN EMAIL (solo LinkedIn, no se crean borradores):")
        for slug, emp, toque, fecha in sin_email:
            print(f"  {fecha}  [{toque.upper()}] {emp}  [{slug}]")

    if skip:
        print("\n" + "-" * 70)
        print("SKIP:")
        for slug, motivo in skip:
            print(f"  {slug}: {motivo}")

    total = sum(len(v) for v in resumen.values())
    print(f"\nTotal borradores creados: {total}")


if __name__ == "__main__":
    procesar()
