"""
Descubrimiento de leads vía scraping de directorios sectoriales.
Lee directorios.json, descarga las páginas activas y extrae empresas.
"""

import json
import os
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def load_directorios():
    with open(os.path.join(CONFIG_DIR, "directorios.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def scrape_directorio(directorio):
    """Scrape un directorio y devuelve lista de candidatos."""
    url = directorio["url"]
    selector = directorio.get("selector_noticias", "article")
    sector = directorio["sector"]
    resultados = []

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        articulos = soup.select(selector)
        for art in articulos[:15]:  # Máximo 15 por directorio
            # Extraer título y link
            link_tag = art.find("a")
            titulo = art.get_text(strip=True)[:150]
            link = ""
            if link_tag:
                titulo = link_tag.get_text(strip=True)[:150] or titulo
                link = link_tag.get("href", "")
                if link and not link.startswith("http"):
                    link = url.rstrip("/") + "/" + link.lstrip("/")

            if titulo:
                resultados.append({
                    "empresa_nombre_guess": titulo.split(" - ")[0].split(" | ")[0].strip()[:80],
                    "web": "",
                    "sector": sector,
                    "zona": "",
                    "fuente": f"directorio_{directorio['id']}",
                    "senal": titulo,
                    "url_origen": link or url,
                    "fecha_deteccion": datetime.now().isoformat(),
                })

    except requests.RequestException as e:
        error_msg = f"[{datetime.now().isoformat()}] ERROR scraping {directorio['id']} ({url}): {e}\n"
        print(f"  {error_msg.strip()}")
        log_path = os.path.join(LOGS_DIR, "scraping_errors.log")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(error_msg)

    return resultados


def run():
    """Ejecuta scraping de todos los directorios activos."""
    config = load_directorios()
    activos = [d for d in config["directorios"] if d.get("activo")]

    if not activos:
        print("Directorios: ningún directorio activo configurado")
        return 0

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    candidatos_path = os.path.join(DATA_DIR, f"candidatos-{fecha_hoy}.json")

    candidatos = []
    if os.path.exists(candidatos_path):
        with open(candidatos_path, "r", encoding="utf-8") as f:
            candidatos = json.load(f)

    nuevos = 0
    for directorio in activos:
        print(f"  Directorio: {directorio['id']}...")
        resultados = scrape_directorio(directorio)
        candidatos.extend(resultados)
        nuevos += len(resultados)

    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)

    print(f"Directorios: {nuevos} resultados de {len(activos)} directorio(s)")
    return nuevos


def _self_test():
    """Test básico sin hacer scraping real."""
    config = load_directorios()
    assert "directorios" in config
    activos = [d for d in config["directorios"] if d.get("activo")]
    print(f"descubrir_directorios: {len(config['directorios'])} directorios, {len(activos)} activos")
    print("descubrir_directorios: todos los tests OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        run()
