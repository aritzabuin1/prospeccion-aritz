"""
Calcula acciones pendientes para hoy según proxima_accion.fecha en pipeline.json.
Output JSON a stdout para consumo del slash command /estado-pipeline.

Uso:
    python scripts/toques_pendientes.py [--fecha YYYY-MM-DD]

Sin argumento, usa la fecha de hoy.
"""

import json
import sys
from datetime import datetime

from scripts.pipeline_utils import load_pipeline


def calcular_pendientes(fecha_ref: str = None) -> dict:
    """
    Para cada lead, comprueba si proxima_accion.fecha <= fecha_ref.
    Agrupa por tipo de acción.
    """
    if fecha_ref is None:
        fecha_ref = datetime.now().strftime("%Y-%m-%d")

    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})

    pendientes = {
        "email_t2": [],
        "email_t3": [],
        "email_breakup": [],
        "linkedin_verificar_aceptacion": [],
        "linkedin_paso2": [],
        "linkedin_paso3": [],
        "linkedin_breakup": [],
        "reactivar": [],
        "otros": [],
    }

    for slug, lead in leads.items():
        prox = lead.get("proxima_accion", {})
        fecha_accion = prox.get("fecha")
        tipo = prox.get("tipo")

        if not fecha_accion or not tipo:
            continue

        # Solo acciones cuya fecha es hoy o anterior (vencidas)
        if fecha_accion > fecha_ref:
            continue

        # Calcular días desde último contacto
        dias_desde = None
        if lead.get("historial"):
            ultimo_envio = None
            for ev in reversed(lead["historial"]):
                if ev.get("tipo") in ("mensaje_enviado", "mensaje_generado"):
                    ultimo_envio = ev.get("fecha")
                    break
            if ultimo_envio:
                try:
                    d1 = datetime.strptime(ultimo_envio[:10], "%Y-%m-%d")
                    d2 = datetime.strptime(fecha_ref, "%Y-%m-%d")
                    dias_desde = (d2 - d1).days
                except ValueError:
                    pass

        entry = {
            "slug": slug,
            "empresa": lead.get("empresa", slug),
            "tipo_accion": tipo,
            "fecha_prevista": fecha_accion,
            "dias_desde_ultimo_contacto": dias_desde,
            "estado_email": lead.get("estado_email"),
            "estado_linkedin": lead.get("estado_linkedin"),
            "temperatura": lead.get("temperatura"),
        }

        # Clasificar en el bucket correcto
        bucket = pendientes.get(tipo, pendientes["otros"])
        bucket.append(entry)

    # Limpiar buckets vacíos para output limpio
    return {k: v for k, v in pendientes.items() if v}


def _self_test():
    """Test básico con pipeline actual."""
    fecha_test = datetime.now().strftime("%Y-%m-%d")
    result = calcular_pendientes(fecha_test)
    total = sum(len(v) for v in result.values())
    print(f"Toques pendientes para {fecha_test}: {total}")
    for tipo, items in result.items():
        print(f"  {tipo}: {len(items)}")
        for item in items:
            print(f"    - {item['empresa']} (desde hace {item['dias_desde_ultimo_contacto']} días)")
    if total == 0:
        print("  (ninguno — normal si no hay leads con envíos)")
    print("toques_pendientes: test OK")


if __name__ == "__main__":
    fecha = None
    if len(sys.argv) > 2 and sys.argv[1] == "--fecha":
        fecha = sys.argv[2]

    result = calcular_pendientes(fecha)
    print(json.dumps(result, ensure_ascii=False, indent=2))
