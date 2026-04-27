"""
One-shot: aprueba los 40 leads VERDE de la tanda 2026-04-20 (excluyendo
índices 11, 43, 44 por ruido editorial/irrelevancia) y los añade al pipeline.
"""
import io
import json
import sys
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.pipeline_utils import load_pipeline, save_pipeline, slugify
from scripts.feedback_leads import registrar_aprobacion

EXCLUIR_IDX_1BASED = {11, 43, 44}

def main():
    validados_path = ROOT / "data" / "validados-2026-04-20.json"
    validados = json.loads(validados_path.read_text(encoding="utf-8"))

    pipeline = load_pipeline()
    hoy = datetime.now().strftime("%Y-%m-%d")

    aprobados_slugs = []
    skipped_excl = []
    skipped_noverde = []
    skipped_existe = []

    for i, lead in enumerate(validados, start=1):
        sem = lead["validacion"]["semaforo"]
        if sem != "VERDE":
            skipped_noverde.append((i, lead.get("empresa_nombre_guess")))
            continue
        if i in EXCLUIR_IDX_1BASED:
            skipped_excl.append((i, lead.get("empresa_nombre_guess")))
            continue

        nombre = lead.get("empresa_nombre_guess", "")
        slug = slugify(nombre)
        if not slug:
            continue
        if slug in pipeline["leads"]:
            skipped_existe.append(slug)
            continue

        v = lead["validacion"]
        entry = {
            "empresa": nombre,
            "web": lead.get("web", ""),
            "sector": lead.get("sector", ""),
            "zona": lead.get("zona", ""),
            "num_empleados": v.get("empleados_estimados"),
            "fuente_descubrimiento": lead.get("fuente", "google_places"),
            "senal_inicial": lead.get("senal", ""),
            "score": lead.get("score", 0),
            "capacidad_economica": None,
            "fecha_descubrimiento": hoy,
            "contacto": {
                "nombre": None,
                "rol": None,
                "email": None,
                "linkedin": v.get("linkedin_url"),
            },
            "estado_email": "nuevo",
            "estado_linkedin": "nuevo",
            "temperatura": None,
            "proxima_accion": None,
            "dossier_path": None,
            "notas": "",
            "historial": [
                {
                    "tipo": "descubierto",
                    "fecha": hoy,
                    "validacion_semaforo": sem,
                    "titulo_web": v.get("titulo_web", ""),
                }
            ],
        }
        pipeline["leads"][slug] = entry
        aprobados_slugs.append(slug)
        try:
            registrar_aprobacion(slug, nombre, lead.get("sector",""), lead.get("zona",""))
        except Exception as e:
            print(f"  [warn] feedback {slug}: {e}")

    save_pipeline(pipeline)

    print(f"Aprobados: {len(aprobados_slugs)}")
    print(f"Excluidos por ruido (11,43,44): {len(skipped_excl)}")
    for i, nom in skipped_excl:
        print(f"  [{i}] {nom}")
    print(f"No VERDE: {len(skipped_noverde)}")
    print(f"Ya existían en pipeline: {len(skipped_existe)}")

    # Imprime slugs (para pipe a distribuir_semana)
    print("\nSLUGS:")
    print(" ".join(aprobados_slugs))

if __name__ == "__main__":
    main()
