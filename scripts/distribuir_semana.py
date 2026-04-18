"""
Distribuye los leads aprobados de la tanda semanal en martes/miércoles/jueves
para envío de T1. 10/10/10 por defecto, ajusta si hay menos de 30.

Uso:
    python -m scripts.distribuir_semana slug1 slug2 slug3 ...

Actualiza pipeline.json: cada lead recibe proxima_accion con fecha del día
de envío asignado + tipo 'enviar_t1'.
"""

import datetime as dt
import json
import sys
from pathlib import Path

from scripts.workday import siguiente_dia_optimo

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "data" / "pipeline.json"


def siguiente_martes(desde: dt.date) -> dt.date:
    """Primer martes >= desde (o el mismo día si es martes)."""
    dias = (1 - desde.weekday()) % 7
    return desde + dt.timedelta(days=dias)


def tres_dias_envio(desde: dt.date) -> list[dt.date]:
    """Devuelve [mar, mié, jue] de la semana >= desde, saltando festivos."""
    martes = siguiente_martes(desde)
    candidatos = [martes, martes + dt.timedelta(days=1), martes + dt.timedelta(days=2)]
    # Si alguno es festivo, re-escalar al siguiente día óptimo
    resultado = []
    for c in candidatos:
        resultado.append(siguiente_dia_optimo(c, "t1"))
    return resultado


def distribuir(slugs: list[str]) -> dict:
    """Asigna fechas a los slugs. Devuelve dict {slug: fecha_iso}."""
    hoy = dt.date.today()
    dias = tres_dias_envio(hoy + dt.timedelta(days=1))  # empezar desde mañana

    n = len(slugs)
    # Reparto equitativo
    por_dia = [n // 3] * 3
    for i in range(n % 3):
        por_dia[i] += 1

    asignacion = {}
    idx = 0
    for dia, cantidad in zip(dias, por_dia):
        for _ in range(cantidad):
            if idx >= n:
                break
            asignacion[slugs[idx]] = dia.isoformat()
            idx += 1
    return asignacion


def aplicar_a_pipeline(asignacion: dict):
    with open(PIPELINE, "r", encoding="utf-8") as f:
        pipeline = json.load(f)
    leads = pipeline.get("leads", {})
    for slug, fecha in asignacion.items():
        if slug not in leads:
            print(f"[skip] {slug}: no está en pipeline")
            continue
        leads[slug]["proxima_accion"] = {
            "fecha": fecha,
            "tipo": "enviar_t1",
            "generada": False,
        }
    with open(PIPELINE, "w", encoding="utf-8") as f:
        json.dump(pipeline, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 2:
        print("Uso: python -m scripts.distribuir_semana slug1 slug2 ...")
        sys.exit(1)
    slugs = sys.argv[1:]
    asignacion = distribuir(slugs)
    aplicar_a_pipeline(asignacion)
    # Resumen
    por_fecha = {}
    for s, f in asignacion.items():
        por_fecha.setdefault(f, []).append(s)
    for fecha in sorted(por_fecha):
        print(f"{fecha}: {len(por_fecha[fecha])} leads")
        for s in por_fecha[fecha]:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
