"""
One-shot post-scraper: prepara la semana siguiente con todos los leads
que tengan email válido.

Pasos:
1. Limpia emails inválidos del pipeline (TLDs basura del scraper).
2. Genera dossier + outbox para todo lead nuevo con email pero sin dossier.
3. Distribuye los slugs a lo largo de L-V de la semana objetivo.
4. (No invoca preparar_borradores_semana — eso necesita Gmail OAuth y va aparte.)

Uso:
    python scripts/preparar_semana_grande.py --semana 2026-05-04
"""
import argparse
import io
import json
import sys
import datetime as dt
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
PIPELINE_PATH = ROOT / "data" / "pipeline.json"

TLDS_VALIDOS = {"com", "es", "net", "org", "eu", "uk", "de", "fr", "it",
                "io", "co", "biz", "info", "cat", "gal", "pt"}


def limpiar_emails_basura(pipeline):
    """Elimina emails con TLD inválido (e.g. .en, .el de scraping mal)."""
    n = 0
    for slug, l in pipeline["leads"].items():
        if slug.startswith("_"):
            continue
        contacto = l.get("contacto") or {}
        email = (contacto.get("email") or "").strip().lower()
        if not email or "@" not in email:
            continue
        tld = email.split(".")[-1]
        if tld not in TLDS_VALIDOS or len(email.split("@")[0]) < 2:
            print(f"  [limpio] {slug}: descarta {email}")
            contacto["email"] = None
            contacto.setdefault("email_alternativos", [])
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--semana", required=True, help="YYYY-MM-DD del lunes objetivo")
    args = ap.parse_args()

    lunes = dt.date.fromisoformat(args.semana)
    if lunes.weekday() != 0:
        print(f"WARNING: {args.semana} no es lunes (weekday={lunes.weekday()})")
    dias = [lunes + dt.timedelta(days=i) for i in range(5)]

    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))

    print("=== 1. Limpieza de emails inválidos ===")
    n_limpios = limpiar_emails_basura(pipeline)
    print(f"   eliminados: {n_limpios}")

    PIPELINE_PATH.write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8")

    # 2. Listar slugs aptos: nuevo + email válido + sin dossier_path o
    #    sin proxima_accion en la semana objetivo.
    aptos = []
    for slug, l in pipeline["leads"].items():
        if slug.startswith("_"):
            continue
        if l.get("estado_email") != "nuevo":
            continue
        email = (l.get("contacto") or {}).get("email")
        if not email or "@" not in email:
            continue
        accion = l.get("proxima_accion") or {}
        f = accion.get("fecha")
        if f and any(d.isoformat() == f for d in dias):
            # ya distribuido
            continue
        aptos.append(slug)

    print(f"\n=== 2. Aptos para distribuir en semana {args.semana} ===")
    print(f"   total: {len(aptos)}")
    if not aptos:
        return

    # 3. Distribuir equitativamente L-V
    n = len(aptos)
    por_dia = [n // 5] * 5
    for i in range(n % 5):
        por_dia[i] += 1

    print(f"\n=== 3. Distribución ===")
    idx = 0
    for dia, cantidad in zip(dias, por_dia):
        print(f"   {dia} ({dia.strftime('%a')}): {cantidad} leads")
        for _ in range(cantidad):
            if idx >= n:
                break
            slug = aptos[idx]
            pipeline["leads"][slug]["proxima_accion"] = {
                "fecha": dia.isoformat(),
                "tipo": "enviar_t1",
                "generada": False,
            }
            idx += 1

    PIPELINE_PATH.write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n=== Listo ===")
    print(f"Siguiente paso: generar dossiers/outbox para los nuevos:")
    print(f"  python scripts/generar_outbox_por_sector.py --fecha {dias[0].isoformat()} --solo-con-email")
    print(f"Y luego, con Gmail OAuth:")
    print(f"  python scripts/preparar_borradores_semana.py --desde {dias[0].isoformat()} --hasta {dias[-1].isoformat()}")


if __name__ == "__main__":
    main()
