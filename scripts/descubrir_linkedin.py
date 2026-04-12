"""
Descubrimiento de leads vía búsquedas web con site:linkedin.com.
NO scrapeamos LinkedIn directamente.
Intenta Google CSE, si falla usa DuckDuckGo.
"""

import json
import os
import sys
import time
from datetime import datetime

import requests as http_requests
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")

API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")
CSE_ENDPOINT = "https://www.googleapis.com/customsearch/v1"


def load_config():
    with open(os.path.join(CONFIG_DIR, "queries.json"), "r", encoding="utf-8") as f:
        queries = json.load(f)
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)
    return queries, objetivos


def build_linkedin_queries(queries_config, objetivos):
    """Construye queries de LinkedIn expandiendo {sector}."""
    all_queries = []
    templates = queries_config["google_custom_search"].get("linkedin_site", [])
    sectores = objetivos["sectores_prioritarios"]

    for template in templates:
        for sector_obj in sectores:
            for keyword in sector_obj["keywords"][:1]:
                q = template.replace("{sector}", keyword)
                all_queries.append({
                    "query": q,
                    "sector": sector_obj["id"],
                    "ciudad": "",
                })
    return all_queries


def search_google_cse(query_text):
    """Intenta Google CSE. Devuelve lista o None si no disponible."""
    if not API_KEY or not CSE_ID:
        return None
    try:
        resp = http_requests.get(CSE_ENDPOINT, params={
            "key": API_KEY, "cx": CSE_ID, "q": query_text,
            "num": 10, "lr": "lang_es", "gl": "es",
        }, timeout=15)
        if resp.status_code != 200:
            return None
        return [
            {"title": item.get("title", ""), "url": item.get("link", ""), "snippet": item.get("snippet", "")}
            for item in resp.json().get("items", [])
        ]
    except Exception:
        return None


def search_ddg(query_text):
    """Fallback: DuckDuckGo."""
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query_text, region="es-es", max_results=10))
            return [
                {"title": r.get("title", ""), "url": r.get("href", ""), "snippet": r.get("body", "")}
                for r in results
            ]
    except Exception as e:
        print(f"  ERROR DDG LinkedIn '{query_text[:50]}...': {e}")
        return []


def do_search(query_text):
    results = search_google_cse(query_text)
    if results is not None:
        return results, "google_cse"
    return search_ddg(query_text), "duckduckgo"


def normalize_linkedin_result(item, query_info, fuente):
    """Normaliza resultado de LinkedIn."""
    url = item["url"]
    nombre = item["title"]
    for suffix in [" | LinkedIn", " - LinkedIn", "| LinkedIn"]:
        nombre = nombre.replace(suffix, "")
    nombre = nombre.strip()

    if not nombre and "/company/" in url:
        parts = url.split("/company/")
        if len(parts) > 1:
            nombre = parts[1].strip("/").replace("-", " ").title()

    tipo = "empresa" if "/company/" in url else "persona"

    return {
        "empresa_nombre_guess": nombre,
        "web": "",
        "sector": query_info["sector"],
        "zona": "",
        "fuente": f"linkedin_{fuente}",
        "senal": f"[{tipo}] {item.get('snippet', '')[:200]}",
        "url_origen": url,
        "fecha_deteccion": datetime.now().isoformat(),
    }


def run():
    """Ejecuta descubrimiento LinkedIn."""
    queries_config, objetivos = load_config()
    all_queries = build_linkedin_queries(queries_config, objetivos)
    seleccion = all_queries[:4]

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    candidatos_path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")

    candidatos = []
    if os.path.exists(candidatos_path):
        with open(candidatos_path, "r", encoding="utf-8") as f:
            candidatos = json.load(f)

    nuevos = 0
    motor = ""
    for i, q_info in enumerate(seleccion):
        print(f"  LinkedIn [{i+1}/{len(seleccion)}]: {q_info['query'][:60]}...")
        results, motor = do_search(q_info["query"])
        for item in results:
            if "linkedin.com" in item["url"]:
                candidato = normalize_linkedin_result(item, q_info, motor)
                candidatos.append(candidato)
                nuevos += 1
        if i < len(seleccion) - 1:
            time.sleep(3)

    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)

    print(f"LinkedIn ({motor}): {nuevos} resultados de {len(seleccion)} queries")
    return nuevos


def _self_test():
    queries_config, objetivos = load_config()
    all_queries = build_linkedin_queries(queries_config, objetivos)
    assert len(all_queries) > 0
    print(f"descubrir_linkedin: {len(all_queries)} queries LinkedIn generadas")
    print("descubrir_linkedin: todos los tests OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
