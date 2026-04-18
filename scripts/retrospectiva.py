"""
Retrospectiva semanal — motor de automejora del sistema de prospección.

Lee pipeline.json + feedback.json y detecta patrones:
- Qué sectores responden mejor / peor
- Qué asuntos de email convierten
- Qué aperturas LinkedIn funcionan
- Qué tamaño de empresa (empleados) convierte
- Qué zonas geográficas responden más
- Qué decisores (cargo) son más accesibles

Salida:
- data/retrospectiva-YYYY-MM-DD.json (snapshot analítico)
- config/pesos_scoring.json (pesos aprendidos, leídos por dedupe_y_score.py)
- memory_suggestions.md (borradores de feedback memories para que el humano apruebe)

Filosofía: no sobrescribe decisiones humanas. Propone. El humano aprueba.
"""

import json
import datetime as dt
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "data" / "pipeline.json"
FEEDBACK = ROOT / "data" / "feedback.json"
OBJETIVOS = ROOT / "config" / "objetivos.json"
PESOS_OUT = ROOT / "config" / "pesos_scoring.json"
SUGGESTIONS = ROOT / "memory_suggestions.md"

HOY = dt.date.today().isoformat()
RETRO_OUT = ROOT / "data" / f"retrospectiva-{HOY}.json"


def load_json(p, default):
    if not p.exists():
        return default
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def analizar(leads: dict) -> dict:
    """Calcula métricas segmentadas por sector, zona, tamaño y cargo."""
    buckets = {
        "por_sector": defaultdict(lambda: {"total": 0, "respuestas": 0, "rechazos_scope": 0, "reuniones": 0}),
        "por_zona": defaultdict(lambda: {"total": 0, "respuestas": 0}),
        "por_tamano": defaultdict(lambda: {"total": 0, "respuestas": 0}),
        "por_cargo_decisor": defaultdict(lambda: {"total": 0, "respuestas": 0}),
        "por_asunto_email": defaultdict(lambda: {"enviados": 0, "respuestas": 0}),
    }

    for slug, lead in leads.items():
        if slug.startswith("_"):
            continue
        sector = lead.get("sector", "desconocido")
        zona = lead.get("zona", "desconocida")
        empleados = lead.get("empleados") or lead.get("num_establecimientos") or 0
        tamano = (
            "xs" if empleados < 20 else
            "s" if empleados < 50 else
            "m" if empleados < 200 else
            "l" if empleados < 1000 else
            "xl"
        )
        cargo = (lead.get("contacto") or {}).get("rol") or "desconocido"
        estado_email = lead.get("estado_email", "nuevo")
        estado_li = lead.get("estado_linkedin", "nuevo")
        temperatura = lead.get("temperatura")
        motivo_rechazo = lead.get("motivo_rechazo")

        ha_respondido = estado_email == "respondido" or estado_li == "respondio_paso2" or temperatura in ("caliente", "tibia")
        es_reunion = lead.get("reunion_agendada", False)

        for key, bucket in [("por_sector", sector), ("por_zona", zona), ("por_tamano", tamano), ("por_cargo_decisor", cargo)]:
            buckets[key][bucket]["total"] += 1
            if ha_respondido:
                buckets[key][bucket]["respuestas"] += 1
        if motivo_rechazo == "scope_geografico":
            buckets["por_sector"][sector]["rechazos_scope"] += 1
        if es_reunion:
            buckets["por_sector"][sector]["reuniones"] += 1

        # Asuntos email — buscar en historial
        for evt in lead.get("historial", []):
            if evt.get("tipo") == "mensaje_enviado" and evt.get("canal") == "email":
                asunto = evt.get("asunto") or "(sin asunto registrado)"
                buckets["por_asunto_email"][asunto]["enviados"] += 1
                if ha_respondido:
                    buckets["por_asunto_email"][asunto]["respuestas"] += 1

    # Convertir defaultdict a dict serializable + calcular tasa de respuesta
    resultado = {}
    for key, bucket in buckets.items():
        resultado[key] = {}
        for k, v in bucket.items():
            total = v.get("total") or v.get("enviados") or 0
            respuestas = v.get("respuestas", 0)
            v["tasa_respuesta"] = round(respuestas / total, 3) if total else 0.0
            resultado[key][k] = dict(v)
    return resultado


def derivar_pesos(analisis: dict) -> dict:
    """Traduce el análisis a ajustes de scoring que dedupe_y_score.py puede leer."""
    pesos = {
        "_generado": HOY,
        "_nota": "Ajustes de scoring derivados de la retrospectiva. +N suma al score del lead que encaje con ese criterio.",
        "sector_bonus": {},
        "zona_bonus": {},
        "tamano_bonus": {},
        "cargo_bonus": {},
    }
    # Umbrales: >=15% respuestas = +8; 5-15% = +3; 0% con n>=5 = -5
    for sector, m in analisis["por_sector"].items():
        if m["total"] < 3:
            continue
        tr = m["tasa_respuesta"]
        if tr >= 0.15:
            pesos["sector_bonus"][sector] = 8
        elif tr >= 0.05:
            pesos["sector_bonus"][sector] = 3
        elif m["total"] >= 5 and tr == 0:
            pesos["sector_bonus"][sector] = -5

    for zona, m in analisis["por_zona"].items():
        if m["total"] < 3:
            continue
        tr = m["tasa_respuesta"]
        if tr >= 0.15:
            pesos["zona_bonus"][zona] = 5
        elif m["total"] >= 5 and tr == 0:
            pesos["zona_bonus"][zona] = -3

    for tamano, m in analisis["por_tamano"].items():
        if m["total"] < 3:
            continue
        tr = m["tasa_respuesta"]
        if tr >= 0.15:
            pesos["tamano_bonus"][tamano] = 8
        elif m["total"] >= 5 and tr == 0:
            pesos["tamano_bonus"][tamano] = -5

    for cargo, m in analisis["por_cargo_decisor"].items():
        if m["total"] < 3:
            continue
        tr = m["tasa_respuesta"]
        if tr >= 0.20:
            pesos["cargo_bonus"][cargo] = 6

    return pesos


def derivar_sugerencias(analisis: dict, pesos: dict) -> str:
    """Genera borradores de feedback memories para que el humano revise."""
    lines = [f"# Sugerencias de memoria generadas {HOY}", ""]

    # Sectores ganadores
    winners = [(s, m) for s, m in analisis["por_sector"].items() if m["total"] >= 3 and m["tasa_respuesta"] >= 0.15]
    losers = [(s, m) for s, m in analisis["por_sector"].items() if m["total"] >= 5 and m["tasa_respuesta"] == 0]

    if winners:
        lines.append("## Sectores con mejor conversión (≥15% respuestas)")
        for s, m in sorted(winners, key=lambda x: -x[1]["tasa_respuesta"]):
            lines.append(f"- **{s}**: {m['respuestas']}/{m['total']} = {m['tasa_respuesta']*100:.1f}%")
        lines.append("")
        lines.append("→ Considerar priorizar estos sectores en `/prospectar-tanda` y subir su peso en scoring.")
        lines.append("")

    if losers:
        lines.append("## Sectores sin respuestas (n≥5)")
        for s, m in losers:
            lines.append(f"- **{s}**: 0/{m['total']}")
        lines.append("")
        lines.append("→ Considerar pausar estos sectores o cambiar ángulo de entrada antes de seguir invirtiendo.")
        lines.append("")

    # Asuntos email
    asuntos = analisis["por_asunto_email"]
    ganadores = [(a, m) for a, m in asuntos.items() if m["enviados"] >= 3 and m["tasa_respuesta"] >= 0.15]
    if ganadores:
        lines.append("## Asuntos email que funcionan")
        for a, m in sorted(ganadores, key=lambda x: -x[1]["tasa_respuesta"]):
            lines.append(f"- \"{a}\" — {m['respuestas']}/{m['enviados']} = {m['tasa_respuesta']*100:.1f}%")
        lines.append("")

    if not (winners or losers or ganadores):
        lines.append("_No hay señales estadísticamente útiles todavía (n insuficiente). Seguir acumulando datos._")
        lines.append("")

    lines.append("---")
    lines.append("Revisar y confirmar qué sugerencias convertir en memorias persistentes en `~/.claude/projects/.../memory/`.")
    return "\n".join(lines)


def main():
    data = load_json(PIPELINE, {"leads": {}})
    leads = data.get("leads", {})
    if not leads:
        print("No hay leads en pipeline.json — retrospectiva vacía.")
        return

    analisis = analizar(leads)
    pesos = derivar_pesos(analisis)
    sugerencias = derivar_sugerencias(analisis, pesos)

    with open(RETRO_OUT, "w", encoding="utf-8") as f:
        json.dump(analisis, f, indent=2, ensure_ascii=False, default=dict)
    with open(PESOS_OUT, "w", encoding="utf-8") as f:
        json.dump(pesos, f, indent=2, ensure_ascii=False)
    with open(SUGGESTIONS, "w", encoding="utf-8") as f:
        f.write(sugerencias)

    print(f"[OK] Retrospectiva escrita en {RETRO_OUT.name}")
    print(f"[OK] Pesos actualizados en {PESOS_OUT.name}")
    print(f"[OK] Sugerencias en {SUGGESTIONS.name}")
    print(f"     Sectores analizados: {len(analisis['por_sector'])}")
    print(f"     Zonas analizadas: {len(analisis['por_zona'])}")


if __name__ == "__main__":
    main()
