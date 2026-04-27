"""
One-shot: aprueba 20 leads de la tanda 2026-04-27 (opción B) y guarda los
restantes VERDES como cartera (estado_pipeline=reserva) para próximas tandas.
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

# Selección manual: 20 mejores VERDES con variedad sectorial (#índice 1-based en validados)
APROBAR_IDX = [1, 12, 13, 17, 18, 19, 21, 22, 30, 32, 33, 35, 36, 38, 41, 44, 46, 53, 55, 60]

# Excluir explícitamente del flujo VERDE (ruido):
EXCLUIR_RUIDO_IDX = {10, 58}  # "Firma de Abogados en España", ANGED


def main():
    validados_path = ROOT / "data" / "validados-2026-04-27.json"
    validados = json.loads(validados_path.read_text(encoding="utf-8"))

    pipeline = load_pipeline()
    hoy = datetime.now().strftime("%Y-%m-%d")

    aprobados = []
    cartera = []
    skip_existe = []

    for i, lead in enumerate(validados, start=1):
        sem = lead["validacion"]["semaforo"]
        if sem != "VERDE":
            continue
        if i in EXCLUIR_RUIDO_IDX:
            continue

        nombre = lead.get("empresa_nombre_guess", "")
        slug = slugify(nombre)
        if not slug:
            continue
        if slug in pipeline["leads"]:
            skip_existe.append(slug)
            continue

        v = lead["validacion"]
        es_aprobado = i in APROBAR_IDX
        estado_email = "nuevo" if es_aprobado else "reserva"

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
            "estado_email": estado_email,
            "estado_linkedin": "nuevo",
            "temperatura": None,
            "proxima_accion": None,
            "dossier_path": None,
            "notas": "" if es_aprobado else "En reserva — procesar en próxima tanda",
            "historial": [
                {
                    "tipo": "descubierto",
                    "fecha": hoy,
                    "validacion_semaforo": sem,
                    "titulo_web": v.get("titulo_web", ""),
                    "tanda": "2026-04-27",
                    "rol_tanda": "aprobado" if es_aprobado else "reserva",
                }
            ],
        }
        pipeline["leads"][slug] = entry
        if es_aprobado:
            aprobados.append((i, slug, nombre))
        else:
            cartera.append((i, slug, nombre))

    save_pipeline(pipeline)

    print(f"=== Tanda 2026-04-27 ===")
    print(f"Aprobados (procesar esta semana): {len(aprobados)}")
    for i, slug, nombre in aprobados:
        print(f"  [{i:2}] {slug}")
    print(f"\nReserva (radar próximas semanas): {len(cartera)}")
    for i, slug, nombre in cartera:
        print(f"  [{i:2}] {slug}")
    print(f"\nYa existían: {len(skip_existe)}")
    for s in skip_existe:
        print(f"  - {s}")


if __name__ == "__main__":
    main()
