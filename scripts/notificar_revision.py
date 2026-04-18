"""
Notifica a aritzmore1@gmail.com los borradores pendientes de revisión.

Corre a las 08:00. Lee data/borradores_pendientes.json (generado por
preparar_borradores.py) y envía UN ÚNICO email resumen desde la cuenta
aritzabuin1 con:

- Cuántos borradores hay pendientes y a qué hora se enviarán.
- Lista: empresa · asunto · destinatario · link directo al borrador.
- Instrucciones: "Borra el borrador en Gmail para vetar el envío."

Tiempo de revisión objetivo: 1 minuto.
"""

import base64
import datetime as dt
import json
from email.mime.text import MIMEText
from pathlib import Path

from scripts.gmail_auth import get_gmail_service

ROOT = Path(__file__).resolve().parent.parent
PENDIENTES = ROOT / "data" / "borradores_pendientes.json"

DESTINATARIO_NOTIF = "aritzmore1@gmail.com"


def construir_html(data: dict) -> str:
    borradores = data.get("borradores", [])
    fecha_envio = data.get("fecha_envio", "mañana")
    n = len(borradores)

    if n == 0:
        return f"""<p>Hola Aritz,</p>
<p>No hay borradores de prospección pendientes para {fecha_envio}.</p>
<p>— Sistema de prospección</p>"""

    filas = ""
    for b in borradores:
        draft_link = "https://mail.google.com/mail/u/0/#drafts"
        filas += f"""
<tr>
  <td style="padding:8px;border-bottom:1px solid #eee;"><b>{b.get('empresa','')}</b></td>
  <td style="padding:8px;border-bottom:1px solid #eee;">{b.get('toque','').upper()}</td>
  <td style="padding:8px;border-bottom:1px solid #eee;">{b.get('asunto','')}</td>
  <td style="padding:8px;border-bottom:1px solid #eee;font-family:monospace;font-size:13px;">{b.get('destinatario','')}</td>
</tr>"""

    return f"""<div style="font-family:Arial,sans-serif;color:#222;max-width:640px;">
<p>Hola Aritz,</p>
<p><b>{n} borrador{'es' if n != 1 else ''}</b> pendiente{'s' if n != 1 else ''} de tu revisión. Se envía{'n' if n != 1 else ''} <b>hoy a las 09:30</b> desde <code>aritzabuin1@gmail.com</code>.</p>

<p><b>Para vetar uno:</b> abre Gmail (cuenta aritzabuin1) → etiqueta <code>PROSPECCION-PENDIENTE</code> → borra el borrador.<br>
<b>Para editar uno:</b> abre el borrador, modifícalo y envíalo tú mismo (el sistema detecta el envío manual y sigue el flujo).<br>
<b>Si no haces nada:</b> se envían a las 09:30.</p>

<table style="border-collapse:collapse;width:100%;margin-top:12px;font-size:14px;">
<thead>
<tr style="background:#f5f5f5;">
  <th style="padding:8px;text-align:left;border-bottom:2px solid #ddd;">Empresa</th>
  <th style="padding:8px;text-align:left;border-bottom:2px solid #ddd;">Toque</th>
  <th style="padding:8px;text-align:left;border-bottom:2px solid #ddd;">Asunto</th>
  <th style="padding:8px;text-align:left;border-bottom:2px solid #ddd;">Destinatario</th>
</tr>
</thead>
<tbody>{filas}
</tbody>
</table>

<p style="margin-top:20px;"><a href="{'https://mail.google.com/mail/u/0/#label/PROSPECCION-PENDIENTE'}" style="background:#1a73e8;color:white;padding:10px 18px;text-decoration:none;border-radius:4px;">Abrir borradores en Gmail</a></p>

<p style="color:#888;font-size:12px;">Sistema de prospección · aritzabuin1@gmail.com · enviado automáticamente a las 08:00</p>
</div>"""


def enviar(service, to: str, asunto: str, html_body: str):
    msg = MIMEText(html_body, "html")
    msg["To"] = to
    msg["Subject"] = asunto
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw}).execute()


def main():
    if not PENDIENTES.exists():
        print("No hay borradores_pendientes.json — nada que notificar.")
        return

    data = json.loads(PENDIENTES.read_text(encoding="utf-8"))
    borradores = data.get("borradores", [])
    n = len(borradores)

    if n == 0:
        print("0 borradores pendientes — no se envía notificación.")
        return

    service = get_gmail_service()
    hoy = dt.date.today()
    asunto = f"[Prospección] {n} borrador{'es' if n != 1 else ''} para revisar — envío 09:30"
    html = construir_html(data)
    enviar(service, DESTINATARIO_NOTIF, asunto, html)
    print(f"Notificación enviada a {DESTINATARIO_NOTIF} ({n} borradores)")


if __name__ == "__main__":
    main()
