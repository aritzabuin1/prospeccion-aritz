"""
Descubrimiento de leads vía Google Places API (New).
Busca empresas por sector en toda España. Fuente principal del sistema.
"""

import json
import os
import sys
import time
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")

API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
PLACES_ENDPOINT = "https://places.googleapis.com/v1/places:searchText"


# Queries específicas para Places por sector — buscan empresas reales
SECTOR_QUERIES = {
    "industria_fabricacion": [
        "empresa industrial fabricación",
        "planta producción industrial",
        "grupo industrial manufacturero",
    ],
    "logistica_transporte": [
        "empresa logística transporte mercancías",
        "operador logístico almacén",
        "empresa distribución mayorista",
    ],
    "construccion_ingenieria": [
        "constructora obras empresa",
        "ingeniería industrial empresa",
        "empresa instalaciones industriales",
    ],
    "servicios_profesionales": [
        "despacho abogados bufete",
        "empresa auditoría consultoría",
        "asesoría empresarial fiscal",
    ],
    "salud_cadenas": [
        "grupo clínicas médicas",
        "clínica dental cadena",
        "laboratorio análisis clínicos",
    ],
    "inmobiliaria_gestion": [
        "inmobiliaria gestión patrimonial",
        "promotora inmobiliaria",
        "administración fincas empresa",
    ],
    "hosteleria_grupos": [
        "grupo restauración hostelería",
        "cadena hoteles grupo hotelero",
        "catering industrial empresa",
    ],
    "retail_cadenas": [
        "cadena tiendas retail",
        "franquicia central comercial",
        "distribución comercial empresa",
    ],
    "energia_utilities": [
        "empresa energía renovable instaladora",
        "empresa eficiencia energética",
        "instaladora fotovoltaica empresa",
    ],
    "automocion_concesionarios": [
        "grupo concesionarios automóviles",
        "empresa gestión flotas vehículos",
        "taller industrial automoción",
    ],
    "agroalimentario": [
        "empresa agroalimentaria industria",
        "bodega vinos empresa",
        "cooperativa agraria grande",
    ],
    "consultoras_rrhh": [
        "consultora recursos humanos selección",
        "empresa trabajo temporal ETT",
        "headhunting selección directivos",
    ],
}

# Ciudades por densidad empresarial (plan v2: alcance nacional).
# Las 10 primeras son las prioritarias — se cubren SIEMPRE en cada ejecución.
CIUDADES = [
    "Madrid", "Barcelona", "Valencia", "Zaragoza", "Sevilla",
    "Málaga", "Bilbao", "Palma de Mallorca", "Las Palmas", "Alicante",
    "Murcia", "Córdoba", "Valladolid", "Vigo", "Gijón",
    "A Coruña", "Vitoria", "Granada", "Pamplona", "San Sebastián",
    "Santander", "Burgos", "Salamanca", "Logroño", "Cáceres",
]

CIUDADES_POR_EJECUCION = 10

# Fichero para rotar ciudades entre ejecuciones
ROTACION_PATH = os.path.join(DATA_DIR, "places_rotacion.json")


def load_rotacion():
    if os.path.exists(ROTACION_PATH):
        with open(ROTACION_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"ultimo_indice_ciudad": 0}


def save_rotacion(data):
    with open(ROTACION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def search_places(query, ciudad):
    """Busca en Google Places API (New) con Text Search."""
    if not API_KEY:
        print("ERROR: GOOGLE_PLACES_API_KEY no configurado en .env")
        return []

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.websiteUri,places.id,places.types",
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
        print(f"  ERROR Places '{query} en {ciudad}': {e}")
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

    direccion = place.get("formattedAddress", "")

    return {
        "empresa_nombre_guess": nombre,
        "web": web,
        "sector": sector_id,
        "zona": ciudad,
        "fuente": "google_places",
        "senal": f"{direccion}",
        "url_origen": f"https://www.google.com/maps/place/?q=place_id:{place.get('id', '')}",
        "fecha_deteccion": datetime.now().isoformat(),
    }


def run():
    """Ejecuta descubrimiento Places rotando sectores y ciudades."""
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)

    sectores = objetivos["sectores_prioritarios"]
    rotacion = load_rotacion()

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    candidatos_path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")

    candidatos = []
    if os.path.exists(candidatos_path):
        with open(candidatos_path, "r", encoding="utf-8") as f:
            candidatos = json.load(f)

    # Seleccionar N ciudades por ejecución (10 por defecto, cubre las grandes).
    # Con 12 sectores × 10 ciudades = 120 queries por tanda → pipeline 80/sem.
    idx = rotacion.get("ultimo_indice_ciudad", 0)
    ciudades_hoy = [CIUDADES[(idx + i) % len(CIUDADES)] for i in range(CIUDADES_POR_EJECUCION)]
    nuevo_idx = (idx + CIUDADES_POR_EJECUCION) % len(CIUDADES)

    nuevos = 0
    queries_hechas = 0

    for sector in sectores:
        sector_id = sector["id"]
        queries = SECTOR_QUERIES.get(sector_id, [])
        if not queries:
            continue

        # Una query por sector, rotando entre las disponibles
        query = queries[idx % len(queries)]

        for ciudad in ciudades_hoy:
            print(f"  Places: {query} en {ciudad}...")
            places = search_places(query, ciudad)
            for place in places:
                candidato = normalize_place(place, sector_id, ciudad)
                if candidato["web"]:
                    candidatos.append(candidato)
                    nuevos += 1
            queries_hechas += 1
            time.sleep(0.5)  # Rate limiting suave

    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)

    save_rotacion({"ultimo_indice_ciudad": nuevo_idx})

    print(f"Places: {nuevos} resultados de {queries_hechas} búsquedas ({len(ciudades_hoy)} ciudades)")
    return nuevos


def _self_test():
    """Test básico: verifica config y hace 1 búsqueda real."""
    with open(os.path.join(CONFIG_DIR, "objetivos.json"), "r", encoding="utf-8") as f:
        objetivos = json.load(f)
    assert len(objetivos["sectores_prioritarios"]) > 0
    print(f"Sectores con queries: {len(SECTOR_QUERIES)}")

    # Test real con 1 query
    places = search_places("empresa logística transporte", "Madrid")
    print(f"Test query 'logística Madrid': {len(places)} resultados")
    for p in places[:3]:
        dn = p.get("displayName", {})
        nombre = dn.get("text", "") if isinstance(dn, dict) else dn
        print(f"  {nombre} — {p.get('websiteUri', 'sin web')}")

    print("descubrir_places: test OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
