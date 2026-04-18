"""
Añade al pipeline los leads VERDE (re-validados contra filtro editorial)
de un fichero validados-{fecha}.json. Devuelve los slugs aprobados.

Uso:
    python -m scripts.aprobar_tanda [--fecha YYYY-MM-DD] [--max N]
"""

import datetime as dt
import json
import re
import sys
from pathlib import Path

from scripts.validar_leads import es_editorial, es_fuera_scope

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PIPELINE = DATA / "pipeline.json"


def slugify(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"[áà]", "a", s)
    s = re.sub(r"[éè]", "e", s)
    s = re.sub(r"[íì]", "i", s)
    s = re.sub(r"[óò]", "o", s)
    s = re.sub(r"[úù]", "u", s)
    s = re.sub(r"[ñ]", "n", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]


def load_pipeline():
    with open(PIPELINE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pipeline(data):
    with open(PIPELINE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    fecha = dt.date.today().isoformat()
    max_n = 30
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--fecha" and i + 1 < len(args):
            fecha = args[i + 1]
        if a == "--max" and i + 1 < len(args):
            max_n = int(args[i + 1])

    val_path = DATA / f"validados-{fecha}.json"
    if not val_path.exists():
        print(f"No existe {val_path.name}")
        sys.exit(1)

    with open(val_path, "r", encoding="utf-8") as f:
        validados = json.load(f)

    pipeline = load_pipeline()
    leads = pipeline.setdefault("leads", {})
    aprobados = []
    saltados_editorial = 0
    saltados_otros = 0

    for r in validados:
        v = r.get("validacion", {})
        sem = v.get("semaforo")
        nombre = r.get("empresa_nombre_guess", "")
        dominio = r.get("web", "")
        titulo = v.get("titulo_web", "")

        # Re-aplicar filtro editorial (por si la validación era previa al fix)
        if es_editorial(nombre, titulo, dominio):
            saltados_editorial += 1
            continue
        if es_fuera_scope(nombre):
            saltados_editorial += 1
            continue
        if sem != "VERDE":
            saltados_otros += 1
            continue

        slug = slugify(nombre)
        if not slug:
            continue
        if slug in leads:
            continue  # ya estaba

        leads[slug] = {
            "empresa": nombre,
            "web": dominio,
            "sector": r.get("sector"),
            "zona": r.get("zona"),
            "num_empleados": v.get("empleados_estimados"),
            "fuente_descubrimiento": r.get("fuente"),
            "senal_inicial": r.get("senal"),
            "score": r.get("score"),
            "capacidad_economica": None,
            "fecha_descubrimiento": fecha,
            "contacto": {
                "nombre": None,
                "rol": None,
                "email": None,
                "linkedin": v.get("linkedin_url"),
            },
            "estado_email": "nuevo",
            "estado_linkedin": "nuevo",
            "temperatura": None,
            "historial": [
                {"tipo": "aprobado_tanda", "fecha": fecha, "fuente": "aprobar_tanda.py"}
            ],
            "proxima_accion": {"fecha": None, "tipo": "generar_mensajes", "generada": False},
            "dossier_path": None,
            "notas": "",
        }
        aprobados.append(slug)
        if len(aprobados) >= max_n:
            break

    save_pipeline(pipeline)
    print(f"Aprobados e insertados en pipeline: {len(aprobados)}")
    print(f"Saltados por editorial: {saltados_editorial}")
    print(f"Saltados por no-verde: {saltados_otros}")
    print(f"Total leads en pipeline ahora: {len(leads)}")
    for s in aprobados:
        print(f"  + {s}")


if __name__ == "__main__":
    main()
