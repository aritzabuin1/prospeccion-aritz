"""
Genera reporte semanal de métricas del pipeline de prospección.
Guarda en reports/semana-{numero}-{año}.md.

Uso:
    python scripts/metricas_semanales.py
"""

import os
from collections import Counter
from datetime import datetime, timedelta

from scripts.pipeline_utils import load_pipeline

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")


def _fecha_en_rango(fecha_str: str, inicio: str, fin: str) -> bool:
    """Comprueba si una fecha ISO está en el rango [inicio, fin]."""
    try:
        return inicio <= fecha_str[:10] <= fin
    except (TypeError, IndexError):
        return False


def generar_metricas(fecha_ref: str = None) -> dict:
    """
    Calcula métricas de los últimos 7 días desde fecha_ref.
    Devuelve dict con todas las métricas.
    """
    if fecha_ref is None:
        fecha_ref = datetime.now().strftime("%Y-%m-%d")

    dt_fin = datetime.strptime(fecha_ref, "%Y-%m-%d")
    dt_inicio = dt_fin - timedelta(days=7)
    inicio = dt_inicio.strftime("%Y-%m-%d")
    fin = fecha_ref

    pipeline = load_pipeline()
    leads = pipeline.get("leads", {})

    # Contadores generales
    total_leads = len(leads)
    leads_semana = 0
    enviados_email = Counter()  # t1, t2, t3
    enviados_linkedin = Counter()  # paso1, paso2, paso3
    respuestas = []
    clasificaciones = Counter()
    reuniones = 0

    # Por sector y fuente
    respuestas_por_sector = Counter()
    contactados_por_sector = Counter()
    respuestas_por_fuente = Counter()
    contactados_por_fuente = Counter()
    respuestas_por_toque = Counter()
    contactados_por_toque = Counter()

    for slug, lead in leads.items():
        sector = lead.get("sector", "desconocido")
        fuente = lead.get("fuente_descubrimiento", "desconocido")

        # Leads descubiertos esta semana
        fecha_desc = lead.get("fecha_descubrimiento", "")
        if _fecha_en_rango(fecha_desc, inicio, fin):
            leads_semana += 1

        # Recorrer historial
        for ev in lead.get("historial", []):
            fecha_ev = ev.get("fecha", "")
            if not _fecha_en_rango(fecha_ev, inicio, fin):
                continue

            tipo = ev.get("tipo", "")
            canal = ev.get("canal", "")
            toque = ev.get("toque", "")

            if tipo == "mensaje_enviado":
                if canal == "email":
                    enviados_email[toque] += 1
                    contactados_por_sector[sector] += 1
                    contactados_por_fuente[fuente] += 1
                    contactados_por_toque[toque] += 1
                elif canal == "linkedin":
                    enviados_linkedin[toque] += 1

            elif tipo in ("respuesta_recibida", "respuesta_manual"):
                temp = ev.get("temperatura", lead.get("temperatura", "sin_clasificar"))
                respuestas.append({
                    "slug": slug,
                    "empresa": lead.get("empresa", slug),
                    "temperatura": temp,
                    "canal": canal,
                })
                clasificaciones[temp] += 1
                respuestas_por_sector[sector] += 1
                respuestas_por_fuente[fuente] += 1
                # Intentar determinar a qué toque respondió
                estado = lead.get("estado_email", "")
                if "respondio_t" in estado:
                    toque_resp = estado.replace("respondio_t", "t")
                    respuestas_por_toque[toque_resp] += 1

            elif tipo == "reunion_agendada":
                reuniones += 1

    # Tasas
    total_enviados_email = sum(enviados_email.values())
    total_respuestas = len(respuestas)
    tasa_respuesta = (
        round(total_respuestas / total_enviados_email * 100, 1)
        if total_enviados_email > 0 else 0
    )

    # Tasas por sector
    tasas_sector = {}
    for sector in set(list(contactados_por_sector) + list(respuestas_por_sector)):
        cont = contactados_por_sector.get(sector, 0)
        resp = respuestas_por_sector.get(sector, 0)
        tasa = round(resp / cont * 100, 1) if cont > 0 else 0
        tasas_sector[sector] = {"contactados": cont, "respuestas": resp, "tasa": tasa}

    # Tasas por fuente
    tasas_fuente = {}
    for fuente in set(list(contactados_por_fuente) + list(respuestas_por_fuente)):
        cont = contactados_por_fuente.get(fuente, 0)
        resp = respuestas_por_fuente.get(fuente, 0)
        tasa = round(resp / cont * 100, 1) if cont > 0 else 0
        tasas_fuente[fuente] = {"contactados": cont, "respuestas": resp, "tasa": tasa}

    # Tasas por toque
    tasas_toque = {}
    for toque in set(list(contactados_por_toque) + list(respuestas_por_toque)):
        cont = contactados_por_toque.get(toque, 0)
        resp = respuestas_por_toque.get(toque, 0)
        tasa = round(resp / cont * 100, 1) if cont > 0 else 0
        tasas_toque[toque] = {"contactados": cont, "respuestas": resp, "tasa": tasa}

    return {
        "periodo": {"inicio": inicio, "fin": fin},
        "total_leads_pipeline": total_leads,
        "leads_descubiertos_semana": leads_semana,
        "enviados_email": dict(enviados_email),
        "enviados_linkedin": dict(enviados_linkedin),
        "total_enviados_email": total_enviados_email,
        "total_respuestas": total_respuestas,
        "tasa_respuesta_pct": tasa_respuesta,
        "clasificaciones": dict(clasificaciones),
        "reuniones_agendadas": reuniones,
        "tasas_por_sector": tasas_sector,
        "tasas_por_fuente": tasas_fuente,
        "tasas_por_toque": tasas_toque,
        "respuestas_detalle": respuestas,
    }


def generar_aprendizajes(metricas: dict) -> list[str]:
    """Genera sugerencias basadas en los datos."""
    tips = []

    # Mejor sector
    tasas = metricas.get("tasas_por_sector", {})
    if tasas:
        mejor = max(tasas.items(), key=lambda x: x[1]["tasa"])
        if mejor[1]["tasa"] > 0 and mejor[1]["contactados"] >= 2:
            tips.append(
                f"Sector '{mejor[0]}' tiene tasa de respuesta del {mejor[1]['tasa']}% "
                f"({mejor[1]['respuestas']}/{mejor[1]['contactados']}). Considerar doblar foco."
            )

    # Fuente sin resultados
    for fuente, data in metricas.get("tasas_por_fuente", {}).items():
        if data["contactados"] >= 3 and data["respuestas"] == 0:
            tips.append(f"Fuente '{fuente}' no generó respuestas en {data['contactados']} contactos. Revisar calidad.")

    # Toque que mejor convierte
    tasas_t = metricas.get("tasas_por_toque", {})
    if tasas_t:
        mejor_t = max(tasas_t.items(), key=lambda x: x[1]["tasa"])
        if mejor_t[1]["tasa"] > 0:
            tips.append(f"Toque {mejor_t[0]} convierte al {mejor_t[1]['tasa']}%. Está funcionando.")

    if not tips:
        tips.append("Datos insuficientes para generar aprendizajes esta semana. Seguir alimentando el pipeline.")

    return tips


def generar_report_md(metricas: dict) -> str:
    """Genera el markdown del reporte semanal."""
    m = metricas
    lines = []
    lines.append(f"# Métricas semanales — {m['periodo']['inicio']} a {m['periodo']['fin']}")
    lines.append("")

    lines.append("## Resumen")
    lines.append("")
    lines.append(f"- Total leads en pipeline: {m['total_leads_pipeline']}")
    lines.append(f"- Leads descubiertos esta semana: {m['leads_descubiertos_semana']}")
    lines.append(f"- Emails enviados: {m['total_enviados_email']}")
    for toque, count in sorted(m.get("enviados_email", {}).items()):
        lines.append(f"  - {toque}: {count}")
    for toque, count in sorted(m.get("enviados_linkedin", {}).items()):
        lines.append(f"- LinkedIn {toque}: {count}")
    lines.append(f"- Respuestas recibidas: {m['total_respuestas']}")
    lines.append(f"- Tasa de respuesta: {m['tasa_respuesta_pct']}%")
    lines.append(f"- Reuniones agendadas: {m['reuniones_agendadas']}")
    lines.append("")

    # Clasificaciones
    if m.get("clasificaciones"):
        lines.append("## Clasificación de respuestas")
        lines.append("")
        for clf, count in sorted(m["clasificaciones"].items()):
            lines.append(f"- {clf}: {count}")
        lines.append("")

    # Por sector
    if m.get("tasas_por_sector"):
        lines.append("## Tasa de respuesta por sector")
        lines.append("")
        lines.append("| Sector | Contactados | Respuestas | Tasa |")
        lines.append("|--------|-------------|------------|------|")
        for sector, data in sorted(m["tasas_por_sector"].items(), key=lambda x: -x[1]["tasa"]):
            lines.append(f"| {sector} | {data['contactados']} | {data['respuestas']} | {data['tasa']}% |")
        lines.append("")

    # Por fuente
    if m.get("tasas_por_fuente"):
        lines.append("## Tasa de respuesta por fuente")
        lines.append("")
        lines.append("| Fuente | Contactados | Respuestas | Tasa |")
        lines.append("|--------|-------------|------------|------|")
        for fuente, data in sorted(m["tasas_por_fuente"].items(), key=lambda x: -x[1]["tasa"]):
            lines.append(f"| {fuente} | {data['contactados']} | {data['respuestas']} | {data['tasa']}% |")
        lines.append("")

    # Por toque
    if m.get("tasas_por_toque"):
        lines.append("## Tasa de respuesta por toque")
        lines.append("")
        lines.append("| Toque | Contactados | Respuestas | Tasa |")
        lines.append("|-------|-------------|------------|------|")
        for toque, data in sorted(m["tasas_por_toque"].items()):
            lines.append(f"| {toque} | {data['contactados']} | {data['respuestas']} | {data['tasa']}% |")
        lines.append("")

    # Aprendizajes
    tips = generar_aprendizajes(metricas)
    lines.append("## Aprendizajes sugeridos")
    lines.append("")
    for tip in tips:
        lines.append(f"- {tip}")
    lines.append("")

    return "\n".join(lines)


def guardar_report(fecha_ref: str = None) -> str:
    """Genera métricas, escribe report y devuelve ruta del archivo."""
    metricas = generar_metricas(fecha_ref)
    md = generar_report_md(metricas)

    os.makedirs(REPORTS_DIR, exist_ok=True)

    if fecha_ref is None:
        fecha_ref = datetime.now().strftime("%Y-%m-%d")
    dt = datetime.strptime(fecha_ref, "%Y-%m-%d")
    num_semana = dt.isocalendar()[1]
    año = dt.year

    filename = f"semana-{num_semana:02d}-{año}.md"
    filepath = os.path.join(REPORTS_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    return filepath


def _self_test():
    """Test básico con pipeline actual."""
    metricas = generar_metricas()
    print(f"Periodo: {metricas['periodo']['inicio']} — {metricas['periodo']['fin']}")
    print(f"Total leads: {metricas['total_leads_pipeline']}")
    print(f"Enviados email: {metricas['total_enviados_email']}")
    print(f"Respuestas: {metricas['total_respuestas']}")
    print(f"Tasa: {metricas['tasa_respuesta_pct']}%")

    filepath = guardar_report()
    print(f"Report guardado en: {filepath}")
    print("metricas_semanales: test OK")


if __name__ == "__main__":
    _self_test()
