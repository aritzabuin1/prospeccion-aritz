"""
Distribuye los leads aprobados de la tanda en lunes-viernes para envío de T1.
Reparto equitativo L-V (ajusta si hay festivos). Objetivo: 80 leads/semana.

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


def siguiente_lunes(desde: dt.date) -> dt.date:
    """Primer lunes >= desde (o el mismo día si es lunes)."""
    dias = (0 - desde.weekday()) % 7
    return desde + dt.timedelta(days=dias)


def dias_envio(desde: dt.date) -> list[dt.date]:
    """Devuelve [lun..vie] de la semana >= desde, saltando festivos."""
    lunes = siguiente_lunes(desde)
    candidatos = [lunes + dt.timedelta(days=i) for i in range(5)]
    return [siguiente_dia_optimo(c, "t1") for c in candidatos]


def distribuir(slugs: list[str]) -> dict:
    """Asigna fechas a los slugs. Reparte equitativamente en L-V."""
    hoy = dt.date.today()
    dias = dias_envio(hoy + dt.timedelta(days=1))
    num_dias = len(dias)

    n = len(slugs)
    por_dia = [n // num_dias] * num_dias
    for i in range(n % num_dias):
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
