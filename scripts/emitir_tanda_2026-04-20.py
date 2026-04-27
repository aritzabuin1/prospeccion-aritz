"""
Emisor de tanda 2026-04-20: toma una estructura leads_payload con contenido
hand-crafted (dossier + email T1 + LinkedIn paso 1 + contacto) y:
  - Escribe dossiers/2026-04-20/{slug}.md
  - Escribe outbox/2026-04-20/{slug}/email-t1.md, email-t1.html,
    linkedin-paso1.md, contacto.md
  - Aplica anonimizar sobre cada texto antes de escribir
  - Actualiza data/pipeline.json: dossier_path, historial, proxima_accion.generada
Sin side-effects si falla anonimización.
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from anonimizar import anonimizar  # noqa: E402

FECHA_HOY = "2026-04-20"
FOTO_URL = "https://raw.githubusercontent.com/aritzabuin1/prospeccion-aritz/main/assets/aritz-linkedin.jpg"

FIRMA_TEMPLATE = (ROOT / "config" / "firma-email.html").read_text(encoding="utf-8")
FIRMA_HTML = FIRMA_TEMPLATE.replace("{{FOTO_URL}}", FOTO_URL)


def html_email(cuerpo_parrafos, asunto):
    parrafos_html = "\n".join(
        f'<p style="margin: 0 0 12px 0;">{p}</p>' for p in cuerpo_parrafos
    )
    return (
        f"<!-- Asunto: {asunto} -->\n"
        '<div style="font-family: Arial, sans-serif; font-size: 14px; color: #222; line-height: 1.5;">\n'
        f"{parrafos_html}\n"
        "<br/>\n"
        f"{FIRMA_HTML}\n"
        "</div>\n"
    )


def emitir_lead(pipeline, slug, payload):
    assert slug in pipeline["leads"], f"Slug no encontrado: {slug}"

    # 1. Anonimizar y validar
    dossier_md = anonimizar(payload["dossier"])
    asunto = anonimizar(payload["email_asunto"])
    email_md_cuerpo = anonimizar(payload["email_cuerpo_md"])
    email_parrafos = [anonimizar(p) for p in payload["email_cuerpo_html_parrafos"]]
    li_md = anonimizar(payload["linkedin_md"])
    contacto_md = anonimizar(payload["contacto_md"])

    # Verificación manual adicional: nombres prohibidos de clientes
    blacklist = ["Euromanager", "Cafès Cornellà", "Cafes Cornella", "OpoRuta", "OnTheGo", "NOMOS", "Telefónica", "Telefonica"]
    for blob in (dossier_md, asunto, email_md_cuerpo, li_md, contacto_md):
        for term in blacklist:
            if re.search(rf"(?i)\b{re.escape(term)}\b", blob):
                raise ValueError(f"Término prohibido presente tras anonimizar: {term} en {slug}")

    # 2. Escribir dossier
    dossier_path = ROOT / "dossiers" / FECHA_HOY / f"{slug}.md"
    dossier_path.parent.mkdir(parents=True, exist_ok=True)
    dossier_path.write_text(dossier_md, encoding="utf-8")

    # 3. Escribir outbox
    out_dir = ROOT / "outbox" / FECHA_HOY / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    email_t1_md = (
        f"# Email T1 — {slug}\n\n"
        f"**Fecha:** {FECHA_HOY}\n"
        f"**Generado el:** {FECHA_HOY}\n\n"
        f"---\n\n"
        f"**Asunto:** {asunto}\n\n"
        f"---\n\n"
        f"{email_md_cuerpo}\n"
    )
    (out_dir / "email-t1.md").write_text(email_t1_md, encoding="utf-8")
    (out_dir / "email-t1.html").write_text(html_email(email_parrafos, asunto), encoding="utf-8")
    (out_dir / "linkedin-paso1.md").write_text(li_md, encoding="utf-8")
    (out_dir / "contacto.md").write_text(contacto_md, encoding="utf-8")

    # 4. Actualizar pipeline
    lead = pipeline["leads"][slug]
    lead["dossier_path"] = f"dossiers/{FECHA_HOY}/{slug}.md"
    hist = lead.setdefault("historial", [])
    hist.append({"tipo": "dossier_generado", "fecha": FECHA_HOY})
    hist.append({"tipo": "mensaje_generado", "canal": "email", "toque": "t1", "fecha": FECHA_HOY})
    hist.append({"tipo": "mensaje_generado", "canal": "linkedin", "toque": "paso1", "fecha": FECHA_HOY})
    if isinstance(lead.get("proxima_accion"), dict):
        lead["proxima_accion"]["generada"] = True


def cargar_pipeline():
    return json.loads((ROOT / "data" / "pipeline.json").read_text(encoding="utf-8"))


def guardar_pipeline(p):
    (ROOT / "data" / "pipeline.json").write_text(
        json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    # Carga el payload desde otro módulo (leads_payload_YYYY-MM-DD.py)
    import importlib
    mod_name = sys.argv[1] if len(sys.argv) > 1 else "payload_2026_04_20"
    mod = importlib.import_module(mod_name)
    p = cargar_pipeline()
    errores = []
    hechos = []
    for slug, payload in mod.PAYLOAD.items():
        try:
            emitir_lead(p, slug, payload)
            hechos.append(slug)
        except Exception as e:
            errores.append((slug, str(e)))
    guardar_pipeline(p)
    print(f"OK: {len(hechos)} leads procesados")
    for s in hechos:
        print(f"  + {s}")
    if errores:
        print(f"\nERRORES: {len(errores)}")
        for s, e in errores:
            print(f"  ! {s}: {e}")
