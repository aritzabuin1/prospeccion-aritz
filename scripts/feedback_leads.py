"""
Sistema de feedback para aprendizaje continuo del sistema de prospección.
Registra rechazos con motivo, acumula patrones, y ajusta filtros.

Datos en data/feedback.json
"""

import json
import os
from collections import Counter
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FEEDBACK_PATH = os.path.join(DATA_DIR, "feedback.json")


def load_feedback() -> dict:
    if os.path.exists(FEEDBACK_PATH):
        with open(FEEDBACK_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "rechazos": [],
        "patrones_aprendidos": {
            "dominios_rechazados": [],
            "sectores_baja_conversion": {},
            "motivos_frecuentes": {},
            "zonas_baja_conversion": {},
        },
        "estadisticas": {
            "total_presentados": 0,
            "total_aprobados": 0,
            "total_rechazados": 0,
        }
    }


def save_feedback(data: dict):
    with open(FEEDBACK_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def registrar_rechazo(slug_o_dominio: str, motivo: str, candidato: dict = None):
    """
    Registra un rechazo con motivo.
    Motivos estándar: demasiado_pequena | sector_equivocado | web_muerta |
                      no_es_empresa | ya_contactada | sin_potencial | otro
    """
    fb = load_feedback()

    rechazo = {
        "dominio": slug_o_dominio,
        "motivo": motivo,
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "sector": candidato.get("sector", "") if candidato else "",
        "zona": candidato.get("zona", "") if candidato else "",
        "nombre": candidato.get("empresa_nombre_guess", "") if candidato else "",
    }
    fb["rechazos"].append(rechazo)
    fb["estadisticas"]["total_rechazados"] += 1

    # Añadir dominio a lista de rechazados
    if slug_o_dominio not in fb["patrones_aprendidos"]["dominios_rechazados"]:
        fb["patrones_aprendidos"]["dominios_rechazados"].append(slug_o_dominio)

    # Acumular motivos
    motivos = fb["patrones_aprendidos"]["motivos_frecuentes"]
    motivos[motivo] = motivos.get(motivo, 0) + 1

    # Acumular rechazos por sector
    if candidato and candidato.get("sector"):
        sect = fb["patrones_aprendidos"]["sectores_baja_conversion"]
        sector = candidato["sector"]
        if sector not in sect:
            sect[sector] = {"rechazados": 0, "aprobados": 0}
        sect[sector]["rechazados"] += 1

    save_feedback(fb)
    return rechazo


def registrar_aprobacion(candidato: dict):
    """Registra que un lead fue aprobado para dossier."""
    fb = load_feedback()
    fb["estadisticas"]["total_aprobados"] += 1

    if candidato and candidato.get("sector"):
        sect = fb["patrones_aprendidos"]["sectores_baja_conversion"]
        sector = candidato["sector"]
        if sector not in sect:
            sect[sector] = {"rechazados": 0, "aprobados": 0}
        sect[sector]["aprobados"] += 1

    save_feedback(fb)


def registrar_presentados(n: int):
    """Registra cuántos leads se presentaron al usuario."""
    fb = load_feedback()
    fb["estadisticas"]["total_presentados"] += n
    save_feedback(fb)


def obtener_dominios_rechazados() -> set:
    """Devuelve set de dominios rechazados para filtrar en dedupe."""
    fb = load_feedback()
    return set(fb["patrones_aprendidos"].get("dominios_rechazados", []))


def generar_informe_aprendizaje() -> str:
    """Genera informe de qué ha aprendido el sistema."""
    fb = load_feedback()
    stats = fb["estadisticas"]
    patrones = fb["patrones_aprendidos"]

    lines = []
    lines.append("# Informe de aprendizaje del sistema")
    lines.append("")

    # Estadísticas generales
    total_p = stats.get("total_presentados", 0)
    total_a = stats.get("total_aprobados", 0)
    total_r = stats.get("total_rechazados", 0)
    tasa = round(total_a / total_p * 100, 1) if total_p > 0 else 0
    lines.append(f"## Estadísticas globales")
    lines.append(f"- Leads presentados: {total_p}")
    lines.append(f"- Aprobados: {total_a} ({tasa}%)")
    lines.append(f"- Rechazados: {total_r}")
    lines.append("")

    # Motivos de rechazo
    motivos = patrones.get("motivos_frecuentes", {})
    if motivos:
        lines.append("## Motivos de rechazo (top)")
        for motivo, count in sorted(motivos.items(), key=lambda x: -x[1]):
            lines.append(f"- {motivo}: {count}")
        lines.append("")

    # Sectores
    sectores = patrones.get("sectores_baja_conversion", {})
    if sectores:
        lines.append("## Conversión por sector")
        lines.append("| Sector | Aprobados | Rechazados | Tasa aprobación |")
        lines.append("|--------|-----------|------------|-----------------|")
        for sector, data in sorted(sectores.items()):
            a = data.get("aprobados", 0)
            r = data.get("rechazados", 0)
            total = a + r
            tasa_s = round(a / total * 100) if total > 0 else 0
            lines.append(f"| {sector} | {a} | {r} | {tasa_s}% |")
        lines.append("")

    # Recomendaciones
    lines.append("## Recomendaciones automáticas")
    if motivos.get("demasiado_pequena", 0) > 5:
        lines.append("- SUBIR filtro mínimo de empleados — rechazas muchas por pequeñas")
    if motivos.get("sector_equivocado", 0) > 5:
        lines.append("- REVISAR sectores objetivo — muchos rechazos por sector equivocado")
    if motivos.get("web_muerta", 0) > 3:
        lines.append("- REFORZAR validación de web antes de presentar al usuario")

    for sector, data in sectores.items():
        total = data.get("aprobados", 0) + data.get("rechazados", 0)
        if total >= 5 and data.get("aprobados", 0) == 0:
            lines.append(f"- DESACTIVAR sector '{sector}' — 0 aprobaciones en {total} presentados")

    if not motivos and not sectores:
        lines.append("- Sin datos suficientes todavía. Seguir usando el sistema.")

    return "\n".join(lines)


def _self_test():
    """Test básico."""
    fb = load_feedback()
    print(f"Rechazos acumulados: {len(fb.get('rechazos', []))}")
    print(f"Dominios rechazados: {len(fb.get('patrones_aprendidos', {}).get('dominios_rechazados', []))}")
    print("feedback_leads: test OK")


if __name__ == "__main__":
    if "--informe" in __import__("sys").argv:
        print(generar_informe_aprendizaje())
    else:
        _self_test()
