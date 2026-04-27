"""
Validación rápida de leads antes de procesar a dossier.
Para cada candidato:
1. Verifica que la web existe y responde
2. Busca empleados estimados vía DuckDuckGo + LinkedIn
3. Extrae señales del meta/título de la web
4. Asigna semáforo: VERDE (>50 empl o señales fuertes), AMARILLO (viable pero sin datos),
   ROJO (web muerta, micro, o irrelevante)

Uso:
    python -m scripts.validar_leads [--fecha YYYY-MM-DD]
"""

import io
import json
import os
import re
import sys
import time
from datetime import datetime
from urllib.parse import urlparse

# Fix Windows console encoding for Unicode output
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def verificar_web(dominio: str) -> dict:
    """Visita la web y extrae info básica."""
    resultado = {
        "web_activa": False,
        "titulo_web": "",
        "descripcion_web": "",
        "tiene_https": False,
        "error": None,
    }

    url = f"https://{dominio}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
        resp.raise_for_status()
        resultado["web_activa"] = True
        resultado["tiene_https"] = resp.url.startswith("https")

        soup = BeautifulSoup(resp.text, "html.parser")

        # Título
        title = soup.find("title")
        if title:
            resultado["titulo_web"] = title.get_text(strip=True)[:150]

        # Meta description
        meta = soup.find("meta", attrs={"name": "description"})
        if meta and meta.get("content"):
            resultado["descripcion_web"] = meta["content"][:250]

    except requests.RequestException as e:
        # Intentar HTTP si HTTPS falla
        try:
            resp = requests.get(f"http://{dominio}", headers=HEADERS, timeout=10,
                                allow_redirects=True)
            resp.raise_for_status()
            resultado["web_activa"] = True
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.find("title")
            if title:
                resultado["titulo_web"] = title.get_text(strip=True)[:150]
        except Exception:
            resultado["error"] = str(e)[:100]

    return resultado


def buscar_empleados_ddg(nombre_empresa: str, dominio: str) -> dict:
    """Busca estimación de empleados vía DuckDuckGo."""
    resultado = {
        "empleados_estimados": None,
        "linkedin_url": None,
        "fuente_empleados": None,
        "info_extra": "",
    }

    try:
        from duckduckgo_search import DDGS
    except ImportError:
        return resultado

    queries = [
        f'"{nombre_empresa}" empleados LinkedIn',
        f'site:linkedin.com/company "{nombre_empresa}"',
    ]

    for query in queries:
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region="es-es", max_results=5))
        except Exception:
            continue

        for r in results:
            url = r.get("href", "")
            snippet = r.get("body", "")
            title = r.get("title", "")

            # Capturar URL de LinkedIn
            if "linkedin.com/company" in url and not resultado["linkedin_url"]:
                resultado["linkedin_url"] = url

            # Buscar números de empleados en snippets
            texto = f"{snippet} {title}".lower()
            patrones = [
                r"(\d[\d.]*)\s*empleados",
                r"(\d[\d.]*)\s*trabajadores",
                r"(\d[\d.]*)\s*employees",
                r"plantilla\D*(\d[\d.]*)",
                r"(\d[\d.]*)\s*personas",
            ]
            for patron in patrones:
                match = re.search(patron, texto)
                if match:
                    num_str = match.group(1).replace(".", "")
                    try:
                        num = int(num_str)
                        if 5 < num < 50000:  # Rango razonable
                            if (resultado["empleados_estimados"] is None or
                                    num > resultado["empleados_estimados"]):
                                resultado["empleados_estimados"] = num
                                resultado["fuente_empleados"] = "ddg_snippet"
                    except ValueError:
                        pass

            # Buscar facturación como indicador
            patrones_fact = [
                r"facturación\D*(\d[\d.,]*)\s*(millones|M)",
                r"(\d[\d.,]*)\s*(millones|M)\s*de?\s*euros?\s*de?\s*facturación",
            ]
            for patron in patrones_fact:
                match = re.search(patron, texto)
                if match:
                    resultado["info_extra"] += f"Facturación ~{match.group(0).strip()}. "

        time.sleep(1)  # Rate limit DDG

    return resultado


DOMINIOS_NO_EMPRESA = {
    "wikipedia.org", "wikimedia.org", "linkedin.com", "infojobs.net",
    "indeed.com", "glassdoor.es", "universidadviu.com", "uoc.edu",
    "universia.net", "protecnium.com", "einforma.com", "europapress.es",
    "expansion.com", "elpais.com", "elmundo.es", "abc.es", "cincodias.com",
    "lavanguardia.com", "20minutos.es", "eleconomista.es", "idealista.com",
    "fotocasa.es", "milanuncios.com", "paginasamarillas.es", "axesor.es",
    "dnb.com", "crunchbase.com", "bloomberg.com", "forbes.com",
    "reuters.com", "ft.com", "youtube.com", "vimeo.com",
    "facebook.com", "twitter.com", "instagram.com", "tiktok.com",
    "pinterest.com", "medium.com", "wordpress.com", "blogspot.com",
    # Medios y blogs sectoriales que colaron en tanda 2026-04-20
    "diariodetransporte.com", "novologistica.com", "definiciones-de.com",
    "formarse.es", "accio.com", "es.accio.com", "fetico.es",
    "cms.tecnalia.com", "tecnalia.com",
    # Plataformas SaaS que aparecen en lugar de la empresa (subdominios de RRHH, etc.)
    "factorial.es", "factorialhr.com", "personio.com", "bizneo.com",
    # TLD educativos (también se filtran por extensión abajo)
    "uloyola.es", "esingenieria.uca.es", "uca.es", "ucm.es", "ub.edu",
    # Grandes cuentas con contenido SEO que colan como lead cuando no lo son
    "repsol.com", "iberdrola.com", "endesa.com", "naturgy.com",
    "santander.com", "bbva.com", "caixabank.es", "mapfre.es",
    "telefonica.com", "movistar.es", "vodafone.es", "orange.es",
}

# Sufijos de dominio que descartan automáticamente
SUFIJOS_NO_EMPRESA = (
    ".edu", ".edu.es", ".gob.es", ".gov", ".mil.es",
)

# Prefijos de dominio que indican medio/blog/editorial
PREFIJOS_NO_EMPRESA = (
    "diario", "revista", "noticias", "periodico", "prensa",
    "blog.", "news.", "info.",
)

EDITORIAL_PATTERNS = [
    r"^(tipos de|¿qu[eé] es|qu[eé] es|c[oó]mo|cu[aá]nto|cu[aá]ndo|d[oó]nde|por qu[eé]|gu[ií]a|todo sobre|descubre|te mostramos|te explicamos|el mejor|los mejores|las mejores|ranking|top \d)",
    r"(definici[oó]n|significado|diferencias entre|ventajas y desventajas|pasos para)",
    r"\b(wikipedia|glosario|diccionario)\b",
    r"^\d+\s+(mejores|tipos|claves|consejos|trucos|ejemplos)",
    r"^(las?|los)\s+\d+\s+(mejores|m[aá]s|principales|grandes|importantes|hoteleros)",
    r"^(listado|lista|directorio|base de datos|cadenas)\s+(de|forbes)",
    r"^whatsapp\b",
    r"^pinterest\b",
    r"\bautob[uú]s de l[ií]nea\b",
    r"(portal de empleo|oferta de empleo|equipo de marketing|equipo ejecutivo)",
    r"(cadenas hoteleras|hoteleros m[aá]s)",
    r"^tf1\b",
    # Añadidos tras tanda 2026-04-20
    r"^d[ií]a (europeo|internacional|mundial|nacional)\b",
    r"^creating growth\b",
    r"^disposici[oó]n \d",
    r"\b(bolet[ií]n oficial|BOE n[úu]m)\b",
    r"^(el|la) (auditor[ií]a|contabilidad|log[ií]stica) (cambia|evoluciona)",
    r"\bsitio web de (la|el) universidad\b",
    r"\b(escuela superior|facultad de|instituto superior)\b",
    r"^fabricantes?:",
]

# Patrones que delatan empresa fuera de scope (LATAM / otros)
LATAM_PATTERNS = [
    r"\bs\.?\s*a\.?\s*de\s*c\.?\s*v\.?\b",   # México
    r"\bs\.?\s*r\.?\s*l\.?\s*de\s*c\.?\s*v\.?\b",  # México
    r"\bcia\.?\s*ltda\.?\b",                  # Chile/Ecuador
    r"\bsac\b",                                # Perú
    r"\beirl\b",                               # Chile/Perú
]

def es_fuera_scope(nombre: str) -> bool:
    texto = (nombre or "").lower()
    for pat in LATAM_PATTERNS:
        if re.search(pat, texto):
            return True
    return False

def es_editorial(nombre: str, titulo: str, dominio: str) -> bool:
    """Detecta si el 'lead' es en realidad contenido editorial (artículo SEO)."""
    # Dominio en lista negra
    host = (dominio or "").lower().replace("www.", "").split("/")[0]
    for bad in DOMINIOS_NO_EMPRESA:
        if host == bad or host.endswith("." + bad):
            return True
    # Sufijos académicos/gubernamentales
    for suf in SUFIJOS_NO_EMPRESA:
        if host.endswith(suf):
            return True
    # Prefijos de medio/blog
    for pref in PREFIJOS_NO_EMPRESA:
        if host.startswith(pref):
            return True
    # Nombre con patrón de artículo
    texto = (nombre or "").lower().strip()
    for pat in EDITORIAL_PATTERNS:
        if re.search(pat, texto):
            return True
    # Título muy largo con signos de artículo (¿? o ¡!) o empieza con pregunta
    t = (titulo or "").lower()
    if len(texto) > 60 and ("..." in texto or "¿" in texto or "..." in t):
        return True
    return False


def clasificar_semaforo(web_info: dict, empleados_info: dict, candidato: dict) -> str:
    """
    Clasifica el lead:
    - VERDE: web activa + (empleados >= 30 O señales fuertes de tamaño)
    - AMARILLO: web activa pero sin datos de tamaño
    - ROJO: web muerta, micro, irrelevante, o contenido editorial (no empresa)
    """
    if not web_info["web_activa"]:
        return "ROJO"

    # Filtro editorial: si el "lead" es un artículo SEO, rojo directo
    nombre = candidato.get("empresa_nombre_guess", "")
    titulo = web_info.get("titulo_web", "")
    dominio = candidato.get("web", "")
    if es_editorial(nombre, titulo, dominio):
        return "ROJO"
    if es_fuera_scope(nombre):
        return "ROJO"

    empleados = empleados_info.get("empleados_estimados")

    if empleados is not None:
        if empleados >= 30:
            return "VERDE"
        elif empleados < 15:
            return "ROJO"
        else:
            return "AMARILLO"

    # Sin datos de empleados: buscar señales en nombre/web
    nombre = candidato.get("empresa_nombre_guess", "").lower()
    titulo = web_info.get("titulo_web", "").lower()
    desc = web_info.get("descripcion_web", "").lower()
    texto = f"{nombre} {titulo} {desc}"

    indicadores_grande = [
        "grupo", "s.a.", "holding", "internacional", "nacional",
        "delegaciones", "sedes", "filial", "corporación",
    ]
    indicadores_micro = [
        "autónomo", "freelance", "blog personal",
    ]

    if any(ind in texto for ind in indicadores_micro):
        return "ROJO"
    if any(ind in texto for ind in indicadores_grande):
        return "VERDE"
    if empleados_info.get("linkedin_url"):
        return "AMARILLO"  # Tiene LinkedIn company, algo de tamaño

    return "AMARILLO"


def validar_candidatos(fecha: str = None) -> list[dict]:
    """
    Valida todos los candidatos del top del día.
    Devuelve lista enriquecida con validación.
    """
    if fecha is None:
        fecha = datetime.now().strftime("%Y-%m-%d")

    top_path = os.path.join(DATA_DIR, f"top-candidatos-{fecha}.json")
    if not os.path.exists(top_path):
        print(f"No hay top-candidatos para {fecha}")
        return []

    with open(top_path, "r", encoding="utf-8") as f:
        candidatos = json.load(f)

    resultados = []

    for i, cand in enumerate(candidatos):
        nombre = cand.get("empresa_nombre_guess", "?")
        dominio = cand.get("web", "")
        print(f"  [{i+1}/{len(candidatos)}] Validando {nombre} ({dominio})...")

        # 1. Verificar web
        web_info = verificar_web(dominio) if dominio else {
            "web_activa": False, "titulo_web": "", "descripcion_web": "",
            "tiene_https": False, "error": "sin dominio"
        }

        # 2. Buscar empleados
        empleados_info = buscar_empleados_ddg(nombre, dominio)

        # 3. Clasificar
        semaforo = clasificar_semaforo(web_info, empleados_info, cand)

        resultados.append({
            **cand,
            "validacion": {
                "semaforo": semaforo,
                "web_activa": web_info["web_activa"],
                "titulo_web": web_info["titulo_web"],
                "descripcion_web": web_info["descripcion_web"],
                "empleados_estimados": empleados_info["empleados_estimados"],
                "linkedin_url": empleados_info["linkedin_url"],
                "fuente_empleados": empleados_info["fuente_empleados"],
                "info_extra": empleados_info["info_extra"],
                "fecha_validacion": datetime.now().isoformat(),
            }
        })

        time.sleep(0.5)

    # Guardar resultados validados
    validados_path = os.path.join(DATA_DIR, f"validados-{fecha}.json")
    with open(validados_path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    # Resumen
    verdes = sum(1 for r in resultados if r["validacion"]["semaforo"] == "VERDE")
    amarillos = sum(1 for r in resultados if r["validacion"]["semaforo"] == "AMARILLO")
    rojos = sum(1 for r in resultados if r["validacion"]["semaforo"] == "ROJO")
    print(f"\nValidación completada: {verdes} VERDE, {amarillos} AMARILLO, {rojos} ROJO")

    return resultados


def imprimir_tabla(resultados: list[dict]):
    """Imprime tabla formateada para el usuario."""
    print(f"\n{'#':>2}  {'Sem':4}  {'Empresa':<45}  {'Empl':>5}  {'Sector':<25}  {'Zona':<12}")
    print("-" * 105)

    for i, r in enumerate(resultados):
        v = r["validacion"]
        sem = v["semaforo"]
        empl = str(v["empleados_estimados"]) if v["empleados_estimados"] else "?"
        nombre = r.get("empresa_nombre_guess", "?")[:44]
        sector = r.get("sector", "?")[:24]
        zona = r.get("zona", "?")[:11]

        print(f"{i+1:>2}  {sem:<4}  {nombre:<45}  {empl:>5}  {sector:<25}  {zona:<12}")

        if v.get("info_extra"):
            print(f"          {v['info_extra'][:90]}")


def _self_test():
    """Test con 1 empresa."""
    web = verificar_web("constructorasanjose.com")
    print(f"Web activa: {web['web_activa']}, Título: {web['titulo_web'][:50]}")
    assert web["web_activa"]
    print("validar_leads: test OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        _self_test()
    else:
        fecha = None
        if len(sys.argv) > 2 and sys.argv[1] == "--fecha":
            fecha = sys.argv[2]
        resultados = validar_candidatos(fecha)
        imprimir_tabla(resultados)
