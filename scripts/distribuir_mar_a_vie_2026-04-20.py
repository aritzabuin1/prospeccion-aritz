"""
One-shot: distribuye los 40 aprobados de tanda 2026-04-20 en
martes 21, miércoles 22, jueves 23, viernes 24 (10/día).
"""
import datetime as dt
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "data" / "pipeline.json"

# 40 slugs aprobados hoy (20 abr), ordenados por cómo salieron del validador
SLUGS = """iqe-industrias-quimicas-del-ebro-s-a grupo-gravalos hebico-ingenieros-s-a grupo-volund transportes-gar-cia-s-a luchana-logistica-s-a eurobalear-de-transportes-s-a la-luz-s-a-terminal-de-contenedores bekker-logistica-transporte-internacional grupo-mln perez-moreno-s-a-u grupo-pedro-jaen-serrano-143-clinica-dermatologica-y-estetica-en-madrid medicina-estetica-y-obesidad-clinica-euskalduna-grupo-muguerza-franco grupo-gs-promotora-inmobiliaria grupo-modernia-malaga-oeste grupo-moldatu-home-inmobiliaria-bilbao grupo-de-restauracion-lateral-s-l grupo-lalala grupo-madriz-traspasos-de-restaurantes-y-bares grupo-lezama pantea-group-grupo-de-restauracion-en-barcelona lombardo-grupo-restauracion-sl grupo-gastroadictos grupo-tandem grupo-gmi grupo-gorki grupo-iruna grupo-servera grupo-amida energias-renovables-mediterraneas-s-a grupo-auto-elia-concesionario-oficial-lynk-co-madrid-rios-rosas automotor-llobregat-s-a autodisa-concesionario-peugeot-grupo-palacios-automocion grupo-terry-automocion grupo-angal-automocion-vehiculos-nuevos-de-ocasion-y-km0 maxus-en-sevilla-grupo-terry-automocion mg-grupo-nieto-malaga grupo-aguinaga omoda-grupo-meuri-zubiarte concesionario-oficial-kgm-grupo-ortasa""".split()

assert len(SLUGS) == 40, f"Esperaba 40, hay {len(SLUGS)}"

# Días objetivo esta semana (martes a viernes)
DIAS = [dt.date(2026, 4, 21), dt.date(2026, 4, 22),
        dt.date(2026, 4, 23), dt.date(2026, 4, 24)]

def main():
    # Mezclar sectores para que cada día tenga diversidad
    # Interleave: día 0 obtiene slugs[0,4,8,12,...], día 1 obtiene slugs[1,5,9,13,...], etc
    asignacion = {}
    for i, slug in enumerate(SLUGS):
        dia = DIAS[i % 4]
        asignacion[slug] = dia.isoformat()

    pipeline = json.loads(PIPELINE.read_text(encoding="utf-8"))
    leads = pipeline["leads"]
    asignados = 0
    no_encontrados = []

    for slug, fecha in asignacion.items():
        if slug not in leads:
            no_encontrados.append(slug)
            continue
        leads[slug]["proxima_accion"] = {
            "fecha": fecha,
            "tipo": "enviar_t1",
            "generada": False,
        }
        leads[slug].setdefault("historial", []).append({
            "tipo": "programado_envio",
            "fecha": dt.date.today().isoformat(),
            "fecha_envio": fecha,
            "canal": "email_t1",
        })
        asignados += 1

    PIPELINE.write_text(json.dumps(pipeline, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    print(f"Asignados {asignados} leads. No encontrados: {len(no_encontrados)}")
    for nf in no_encontrados:
        print(f"  [missing] {nf}")

    por_fecha = {}
    for s, f in asignacion.items():
        por_fecha.setdefault(f, []).append(s)
    print()
    for fecha in sorted(por_fecha):
        d = dt.date.fromisoformat(fecha)
        print(f"{fecha} ({d.strftime('%a')}): {len(por_fecha[fecha])} leads")
        for s in por_fecha[fecha]:
            print(f"  - {s}")

if __name__ == "__main__":
    main()
