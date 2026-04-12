"""
Descubrimiento de leads vía búsquedas web.
Intenta Google Custom Search API si hay key configurada,
si no usa DuckDuckGo como fallback.
Lee queries.json y objetivos.json, rota queries, y normaliza resultados.
"""

import json
import os
import sys
import time
from datetime import datetime
from urllib.parse import urlparse

import requests as http_requests
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")

API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")
CSE_ENDPOINT = "https://www.googleapis.com/customsearch/v1"

ROTACION_PATH = os.path.join(DATA_DIR, "cse_rotacion.json")


def load_config():
    with open(os.path.join(CONFIG_DIR, "queries.json"), "r", encoding="utf-8") as f:
        queries = json.load(f)
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)
    return queries, objetivos


def load_rotacion():
    if os.path.exists(ROTACION_PATH):
        with open(ROTACION_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"ultima_ejecucion": None, "ultimo_indice": 0}


def save_rotacion(data):
    with open(ROTACION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_queries(queries_config, objetivos):
    """Construye lista de queries expandiendo {ciudad} y {sector}."""
    all_queries = []
    ciudades = objetivos["zonas_prioritarias"]
    sectores = objetivos["sectores_prioritarios"]

    for categoria in ["senales_apertura", "senales_financiacion", "senales_crecimiento"]:
        templates = queries_config["google_custom_search"].get(categoria, [])
        for template in templates:
            for ciudad in ciudades:
                for sector_obj in sectores:
                    for keyword in sector_obj["keywords"][:1]:
                        q = template.replace("{ciudad}", ciudad).replace("{sector}", keyword)
                        all_queries.append({
                            "query": q,
                            "categoria": categoria,
                            "ciudad": ciudad,
                            "sector": sector_obj["id"],
                        })
    return all_queries


def select_queries(all_queries, rotacion, max_queries):
    """Selecciona N queries rotando desde el último índice."""
    inicio = rotacion.get("ultimo_indice", 0)
    if inicio >= len(all_queries):
        inicio = 0
    seleccion = all_queries[inicio:inicio + max_queries]
    if len(seleccion) < max_queries:
        seleccion += all_queries[:max_queries - len(seleccion)]
    return seleccion, inicio + max_queries


def search_google_cse(query_text):
    """Intenta Google Custom Search API. Devuelve lista de {title, url, snippet}."""
    if not API_KEY or not CSE_ID:
        return None  # No configurado, usar fallback

    params = {
        "key": API_KEY,
        "cx": CSE_ID,
        "q": query_text,
        "num": 10,
        "lr": "lang_es",
        "gl": "es",
    }
    try:
        resp = http_requests.get(CSE_ENDPOINT, params=params, timeout=15)
        if resp.status_code != 200:
            return None  # API no disponible, usar fallback
        data = resp.json()
        return [
            {"title": item.get("title", ""), "url": item.get("link", ""), "snippet": item.get("snippet", "")}
            for item in data.get("items", [])
        ]
    except Exception:
        return None


def search_ddg(query_text):
    """Fallback: DuckDuckGo search. Devuelve lista de {title, url, snippet}."""
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query_text, region="es-es", max_results=10))
            return [
                {"title": r.get("title", ""), "url": r.get("href", ""), "snippet": r.get("body", "")}
                for r in results
            ]
    except Exception as e:
        print(f"  ERROR DDG '{query_text[:50]}...': {e}")
        return []


def do_search(query_text):
    """Busca primero con Google CSE, si falla usa DuckDuckGo."""
    results = search_google_cse(query_text)
    if results is not None:
        return results, "google_cse"
    return search_ddg(query_text), "duckduckgo"


def normalize_result(item, query_info, fuente):
    """Normaliza un resultado al schema común de candidatos."""
    url = item["url"]
    parsed = urlparse(url)
    dominio = parsed.netloc.replace("www.", "")

    nombre_guess = item["title"].split(" - ")[0].split(" | ")[0].strip()[:80]
    if not nombre_guess:
        nombre_guess = dominio.split(".")[0].replace("-", " ").title()

    return {
        "empresa_nombre_guess": nombre_guess,
        "web": dominio,
        "sector": query_info["sector"],
        "zona": query_info["ciudad"],
        "fuente": fuente,
        "senal": item.get("snippet", f"Buscando: {query_info['query'][:100]}")[:250],
        "url_origen": url,
        "fecha_deteccion": datetime.now().isoformat(),
    }


def run():
    """Ejecuta la tanda de descubrimiento."""
    queries_config, objetivos = load_config()
    rotacion = load_rotacion()

    all_queries = build_queries(queries_config, objetivos)
    max_q = queries_config["rotacion"]["queries_por_ejecucion"]

    seleccion, nuevo_indice = select_queries(all_queries, rotacion, max_q)

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    candidatos_path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")

    candidatos = []
    if os.path.exists(candidatos_path):
        with open(candidatos_path, "r", encoding="utf-8") as f:
            candidatos = json.load(f)

    nuevos = 0
    motor_usado = ""
    for i, q_info in enumerate(seleccion):
        print(f"  Búsqueda [{i+1}/{len(seleccion)}]: {q_info['query'][:60]}...")
        results, motor = do_search(q_info["query"])
        motor_usado = motor
        for item in results:
            candidato = normalize_result(item, q_info, motor)
            if candidato["web"]:
                candidatos.append(candidato)
                nuevos += 1
        if i < len(seleccion) - 1:
            time.sleep(3)

    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)

    save_rotacion({
        "ultima_ejecucion": fecha_hoy,
        "ultimo_indice": nuevo_indice,
    })

    print(f"Búsqueda web ({motor_usado}): {nuevos} resultados de {len(seleccion)} queries")
    return nuevos


def _self_test():
    """Test básico sin buscar."""
    queries_config, objetivos = load_config()
    all_queries = build_queries(queries_config, objetivos)
    assert len(all_queries) > 0

    rotacion = {"ultima_ejecucion": None, "ultimo_indice": 0}
    seleccion, _ = select_queries(all_queries, rotacion, 6)
    assert len(seleccion) == 6

    print(f"descubrir_cse: {len(all_queries)} queries totales, rotación OK")
    print("descubrir_cse: todos los tests OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
