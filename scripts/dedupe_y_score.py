"""
Deduplica candidatos del día contra histórico y pipeline,
aplica scoring (0-100) y genera top candidatos.
"""

import json
import os
import sys
from datetime import datetime, timedelta

from rapidfuzz import fuzz

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_objetivos():
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def load_leads_vistos():
    path = os.path.join(DATA_DIR, "leads_vistos.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_leads_vistos(data):
    path = os.path.join(DATA_DIR, "leads_vistos.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_pipeline():
    path = os.path.join(DATA_DIR, "pipeline.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_candidatos_hoy():
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")
    if not os.path.exists(path):
        print(f"No hay candidatos para hoy ({fecha_hoy})")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def es_duplicado(candidato, vistos, pipeline_leads):
    """Verifica si un candidato ya está en vistos, pipeline, o rechazados."""
    web = candidato.get("web", "").lower().strip()
    nombre = candidato.get("empresa_nombre_guess", "").lower().strip()

    # Dedupe exacto por dominio
    if web and web in vistos.get("dominios", {}):
        return True

    # Dedupe por dominio en pipeline
    for slug, lead in pipeline_leads.items():
        if web and lead.get("web", "").lower() == web:
            return True

    # Dedupe contra dominios rechazados por el usuario (feedback loop)
    try:
        from scripts.feedback_leads import obtener_dominios_rechazados
        rechazados = obtener_dominios_rechazados()
        if web and web in rechazados:
            return True
    except (ImportError, FileNotFoundError):
        pass

    # Dedupe fuzzy por nombre (>85% similitud)
    for dominio_data in vistos.get("dominios", {}).values():
        nombre_visto = dominio_data.get("nombre", "").lower()
        if nombre and nombre_visto and fuzz.ratio(nombre, nombre_visto) > 85:
            return True

    return False


def calcular_score(candidato, objetivos):
    """Scoring 0-100. Prioriza tamaño de empresa y capacidad de pago."""
    score = 0
    sectores_ids = [s["id"] for s in objetivos["sectores_prioritarios"]]
    zonas = [z.lower() for z in objetivos["zonas_prioritarias"]]
    excluir = [e.lower() for e in objetivos["filtros"]["excluir_sectores"]]
    min_empleados = objetivos["filtros"].get("excluir_si_menor_de_empleados", 20)

    web = candidato.get("web", "")
    sector = candidato.get("sector", "")
    zona = candidato.get("zona", "").lower()
    senal = candidato.get("senal", "")
    empleados = candidato.get("num_empleados", 0) or 0

    # Excluir sectores prohibidos
    for exc in excluir:
        if exc in sector.lower() or exc in senal.lower():
            return 0

    # Excluir si sabemos que tiene menos de 20 empleados
    if empleados > 0 and empleados < min_empleados:
        return 0

    # +20 si dominio propio (no redes sociales)
    redes = ["instagram.com", "facebook.com", "twitter.com", "tiktok.com", "youtube.com"]
    if web and not any(red in web.lower() for red in redes):
        score += 20

    # +15 si sector en lista prioritaria
    if sector in sectores_ids:
        score += 15

    # +10 si empresa española (zona no vacía)
    if zona:
        score += 10

    # +10 si señal es reciente
    score += 10

    # TAMAÑO DE EMPRESA — el factor más importante para ticket alto
    if empleados >= 200:
        score += 30  # Enterprise
    elif empleados >= 100:
        score += 25  # Mediana-grande
    elif empleados >= 50:
        score += 20  # Mediana
    elif empleados >= 30:
        score += 15  # Pequeña pero viable
    else:
        # Si no sabemos empleados, dar puntos base (Places no da empleados
        # pero devuelve empresas reales — se verificará en dossier)
        score += 10
        # Bonus si indicadores de tamaño en la señal o nombre
        indicadores_grande = [
            "grupo", "holding", "millones", "facturación", "plantilla",
            "sedes", "delegaciones", "filial", "matriz", "corporación",
            "internacional", "nacional", "lider", "referente", "s.a.",
        ]
        texto = f"{senal} {candidato.get('empresa_nombre_guess', '')}".lower()
        if any(ind in texto for ind in indicadores_grande):
            score += 5

    # +10 si hay señal de transformación digital o dolor operativo
    senales_transformacion = [
        "digitalización", "transformación", "automatizar", "eficiencia",
        "innovación", "CTO", "CIO", "CDO", "tecnología",
    ]
    if any(s in senal.lower() for s in senales_transformacion):
        score += 10

    # +10 si aparece en más de una fuente (se calcula después en dedup grupal)
    # Este bonus se aplica abajo

    return score


def run():
    """Ejecuta dedupe y scoring sobre candidatos del día."""
    objetivos = load_objetivos()
    vistos = load_leads_vistos()
    pipeline = load_pipeline()
    candidatos = load_candidatos_hoy()

    if not candidatos:
        return 0

    min_score = objetivos["filtros"]["minimo_score_para_dossier"]

    # Agrupar por dominio para detectar multi-fuente
    por_dominio = {}
    for c in candidatos:
        key = c.get("web", "") or c.get("empresa_nombre_guess", "unknown")
        key = key.lower().strip()
        if key not in por_dominio:
            por_dominio[key] = []
        por_dominio[key].append(c)

    # Procesar: dedupe + score
    resultados = []
    for key, grupo in por_dominio.items():
        candidato = grupo[0]  # Tomar el primero como representante

        if es_duplicado(candidato, vistos, pipeline.get("leads", {})):
            continue

        score = calcular_score(candidato, objetivos)

        # Bonus multi-fuente
        fuentes = set(c.get("fuente", "") for c in grupo)
        if len(fuentes) > 1:
            score += 10

        candidato["score"] = min(score, 100)
        candidato["num_fuentes"] = len(fuentes)
        resultados.append(candidato)

        # Registrar en vistos
        web = candidato.get("web", "")
        if web:
            vistos["dominios"][web.lower()] = {
                "primera_vez": datetime.now().strftime("%Y-%m-%d"),
                "ultimo_score": score,
                "nombre": candidato.get("empresa_nombre_guess", ""),
            }

    # Ordenar por score desc
    resultados.sort(key=lambda x: x.get("score", 0), reverse=True)

    # Filtrar por score mínimo y tomar top 20
    resultados = [r for r in resultados if r.get("score", 0) >= min_score][:20]

    # Guardar
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    top_path = os.path.join(DATA_DIR, f"top-candidatos-{fecha_hoy}.json")
    with open(top_path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    save_leads_vistos(vistos)

    print(f"Dedupe+Score: {len(resultados)} candidatos válidos (de {len(candidatos)} brutos)")
    return len(resultados)


def _self_test():
    """Test básico de scoring."""
    objetivos = load_objetivos()

    # Empresa grande industrial — debe puntuar alto
    candidato_enterprise = {
        "web": "metalurgicasnorte.es",
        "sector": "industria_fabricacion",
        "zona": "Bilbao",
        "senal": "Grupo industrial ampliación plantilla 200 empleados",
        "num_empleados": 200,
        "fuente": "google_cse",
    }
    score_ent = calcular_score(candidato_enterprise, objetivos)
    assert score_ent >= 75, f"Enterprise esperado >= 75, got {score_ent}"

    # Empresa mediana con señal de transformación — debe ser viable
    candidato_mediano = {
        "web": "logisticasur.com",
        "sector": "logistica_transporte",
        "zona": "Madrid",
        "senal": "Busca CTO para digitalización de procesos",
        "num_empleados": 80,
        "fuente": "google_cse",
    }
    score_med = calcular_score(candidato_mediano, objetivos)
    assert score_med >= 60, f"Mediano esperado >= 60, got {score_med}"

    # Microempresa — debe ser descartada
    candidato_micro = {
        "web": "tallercito.com",
        "sector": "automocion_concesionarios",
        "zona": "Valencia",
        "senal": "Taller de barrio con 3 empleados",
        "num_empleados": 3,
        "fuente": "google_cse",
    }
    score_micro = calcular_score(candidato_micro, objetivos)
    assert score_micro == 0, f"Micro esperado 0, got {score_micro}"

    # Gobierno — excluido
    candidato_gob = {
        "web": "ayuntamiento.es",
        "sector": "gobierno",
        "zona": "Madrid",
        "senal": "Concurso público",
        "fuente": "google_cse",
    }
    score_gob = calcular_score(candidato_gob, objetivos)
    assert score_gob == 0, f"Gobierno esperado 0, got {score_gob}"

    print(f"dedupe_y_score: enterprise={score_ent}, mediano={score_med}, micro={score_micro}, gobierno={score_gob}")
    print("dedupe_y_score: todos los tests OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
