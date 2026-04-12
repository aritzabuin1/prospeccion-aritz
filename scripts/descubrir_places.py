"""
Descubrimiento de leads vía Google Places API (New).
Busca negocios por sector y ciudad, filtra cadenas.
"""

import json
import os
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")

API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
PLACES_ENDPOINT = "https://places.googleapis.com/v1/places:searchText"


# Mapeo de sectores a queries de Places
SECTOR_QUERIES = {
    "hosteleria_cadenas": ["cadena restaurantes", "grupo restauración"],
    "clinicas_dentales_esteticas": ["cadena clínicas dentales", "clínicas estéticas"],
    "fitness_cadenas": ["cadena gimnasios", "centros deportivos"],
    "consultoras_rrhh": ["consultora recursos humanos", "empresa selección personal"],
    "gestorias_asesorias": ["gestoría", "asesoría fiscal laboral"],
}


def search_places(query, ciudad):
    """Busca en Google Places API (New) con Text Search."""
    if not API_KEY:
        print("ERROR: GOOGLE_PLACES_API_KEY no configurado en .env")
        return []

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.websiteUri,places.id",
    }

    body = {
        "textQuery": f"{query} en {ciudad}",
        "languageCode": "es",
        "maxResultCount": 10,
    }

    try:
        resp = requests.post(PLACES_ENDPOINT, json=body, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data.get("places", [])
    except requests.RequestException as e:
        print(f"  ERROR en Places '{query} en {ciudad}': {e}")
        return []


def normalize_place(place, sector_id, ciudad):
    """Normaliza un resultado de Places al schema común."""
    web = place.get("websiteUri", "")
    if web:
        from urllib.parse import urlparse
        web = urlparse(web).netloc.replace("www.", "")

    nombre = ""
    display_name = place.get("displayName")
    if isinstance(display_name, dict):
        nombre = display_name.get("text", "")
    elif isinstance(display_name, str):
        nombre = display_name

    return {
        "empresa_nombre_guess": nombre,
        "web": web,
        "sector": sector_id,
        "zona": ciudad,
        "fuente": "google_places",
        "senal": f"Encontrado en Google Places: {place.get('formattedAddress', '')}",
        "url_origen": f"https://www.google.com/maps/place/?q=place_id:{place.get('id', '')}",
        "fecha_deteccion": datetime.now().isoformat(),
    }


def run():
    """Ejecuta descubrimiento Places para todos los sectores/ciudades."""
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)

    ciudades = objetivos["zonas_prioritarias"]
    sectores = objetivos["sectores_prioritarios"]

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    candidatos_path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")

    candidatos = []
    if os.path.exists(candidatos_path):
        with open(candidatos_path, "r", encoding="utf-8") as f:
            candidatos = json.load(f)

    nuevos = 0
    for sector in sectores:
        sector_id = sector["id"]
        queries = SECTOR_QUERIES.get(sector_id, [])
        for query in queries[:1]:  # Solo primera query por sector para no quemar cuota
            for ciudad in ciudades[:3]:  # Top 3 ciudades por ejecución
                print(f"  Places: {query} en {ciudad}...")
                places = search_places(query, ciudad)
                for place in places:
                    candidato = normalize_place(place, sector_id, ciudad)
                    if candidato["web"]:
                        candidatos.append(candidato)
                        nuevos += 1

    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)

    print(f"Places: {nuevos} resultados nuevos")
    return nuevos


def _self_test():
    """Test básico sin llamar a la API."""
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)
    assert len(objetivos["zonas_prioritarias"]) > 0
    assert len(objetivos["sectores_prioritarios"]) > 0
    print("descubrir_places: config cargada OK")
    print("descubrir_places: todos los tests OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
