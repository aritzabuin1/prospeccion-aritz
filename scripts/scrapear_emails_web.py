"""
Scraper gratuito de emails desde la web pública de cada lead.

Estrategia:
1. Bajar home + páginas tipo /contacto /contact /quienes-somos /about /equipo /team
2. Extraer mailto: y emails en texto.
3. Filtrar emails del propio dominio (descartar @gmail, @hotmail).
4. Guardar el mejor candidato en pipeline.contacto.email.

Prioridad de candidatos:
  1. Email con nombre.apellido@dominio (probable decisor)
  2. comercial@, ventas@, direccion@, gerencia@, ceo@
  3. info@, contacto@ (último recurso, bajo riesgo de rebote)

Uso:
    python scripts/scrapear_emails_web.py [--solo-aprobados]
"""
import argparse
import io
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_PATH = ROOT / "data" / "pipeline.json"

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SUBPAGES = ["", "contacto", "contact", "es/contacto",
            "aviso-legal", "equipo", "nosotros"]
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Prospeccion/1.0)"}
TIMEOUT = 5

GENERICOS_BAJOS = {"info", "contacto", "contact", "hello", "hola", "admin",
                   "administracion", "office", "oficina", "rrhh", "hr",
                   "marketing", "soporte", "support", "ayuda", "help",
                   "newsletter", "noreply", "no-reply", "webmaster", "postmaster"}
DECISORES = {"comercial", "ventas", "sales", "direccion", "gerencia",
             "ceo", "cto", "cfo", "general", "operaciones", "manager"}


def normalizar_dominio(web: str) -> str:
    if not web:
        return ""
    if not web.startswith("http"):
        web = "https://" + web
    netloc = urlparse(web).netloc.lower()
    return netloc.replace("www.", "")


def fetch(url: str) -> str:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200 and "text/html" in r.headers.get("Content-Type", ""):
            return r.text
    except Exception:
        return ""
    return ""


def extraer_emails(html: str, dominio: str) -> set:
    soup = BeautifulSoup(html, "html.parser")
    encontrados = set()

    # mailto: links
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.lower().startswith("mailto:"):
            addr = href[7:].split("?")[0].strip().lower()
            if "@" in addr:
                encontrados.add(addr)

    # texto plano (con desofuscación SOLO si vienen entre corchetes/paréntesis)
    texto = soup.get_text(" ")
    texto = re.sub(r"\s*[\[\(]\s*(?:arroba|at)\s*[\]\)]\s*", "@", texto, flags=re.IGNORECASE)
    texto = re.sub(r"\s*[\[\(]\s*(?:punto|dot)\s*[\]\)]\s*", ".", texto, flags=re.IGNORECASE)
    for m in EMAIL_RE.findall(texto):
        m = m.lower().rstrip(".")
        # Filtrar TLDs basura (e.g. .en .el .es.en de mala separación de frases)
        tld = m.split(".")[-1]
        if len(tld) >= 2 and tld in {"com","es","net","org","eu","uk","de","fr","it","io","co","biz","info","cat","gal"}:
            encontrados.add(m)

    # Filtrar: solo del dominio del lead (evita @gmail, @microsoft, etc.)
    base_dom = dominio.split(".")[0] if dominio else ""
    return {e for e in encontrados
            if dominio in e.split("@")[1] or base_dom in e.split("@")[1]}


def priorizar(emails: set) -> list:
    """Devuelve lista ordenada por probabilidad de ser decisor real."""
    def score(email: str) -> int:
        local = email.split("@")[0]
        if "." in local and not any(g in local for g in GENERICOS_BAJOS):
            return 3  # nombre.apellido
        if any(d in local for d in DECISORES):
            return 2
        if local in GENERICOS_BAJOS:
            return 1
        return 2  # otro patrón
    return sorted(emails, key=score, reverse=True)


def scrapear_lead(web: str) -> dict:
    if not web:
        return {"emails": [], "paginas": 0}
    dominio = normalizar_dominio(web)
    base = f"https://{dominio}"
    todos = set()
    paginas_ok = 0
    for sub in SUBPAGES:
        url = base if not sub else urljoin(base + "/", sub)
        html = fetch(url)
        if html:
            paginas_ok += 1
            todos.update(extraer_emails(html, dominio))
            # Si ya hay decisor (nombre.apellido), no seguir buscando.
            if any("." in e.split("@")[0] and len(e.split("@")[0]) > 4 for e in todos):
                break
        time.sleep(0.1)
    return {"emails": priorizar(todos), "paginas": paginas_ok}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-aprobados", action="store_true",
                    help="Solo leads con estado_email=nuevo o reserva")
    ap.add_argument("--limite", type=int, default=0,
                    help="Procesar solo N leads (0 = todos)")
    args = ap.parse_args()

    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))
    leads = pipeline["leads"]

    objetivos = []
    for slug, l in leads.items():
        if slug.startswith("_"):
            continue
        if l.get("contacto", {}).get("email"):
            continue
        estado = l.get("estado_email", "")
        if args.solo_aprobados and estado not in ("nuevo", "reserva"):
            continue
        if not l.get("web"):
            continue
        objetivos.append(slug)

    if args.limite:
        objetivos = objetivos[:args.limite]

    print(f"Leads a scrapear: {len(objetivos)}\n")
    encontrados = 0
    for i, slug in enumerate(objetivos, 1):
        l = leads[slug]
        web = l.get("web")
        print(f"[{i:3}/{len(objetivos)}] {slug} | {web}")
        try:
            res = scrapear_lead(web)
        except Exception as exc:
            print(f"   ERROR: {exc}")
            continue
        if res["emails"]:
            best = res["emails"][0]
            l.setdefault("contacto", {})["email"] = best
            l.setdefault("contacto", {})["email_fuente"] = "scrape_web"
            l.setdefault("contacto", {})["email_alternativos"] = res["emails"][1:5]
            encontrados += 1
            print(f"   ✓ {best}  (alt: {res['emails'][1:3]})")
        else:
            print(f"   - sin email ({res['paginas']} páginas exploradas)")

        # Persistir cada 5 para no perder progreso
        if i % 5 == 0:
            PIPELINE_PATH.write_text(
                json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8")

    PIPELINE_PATH.write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n=== Resumen ===")
    print(f"Leads procesados: {len(objetivos)}")
    print(f"Emails encontrados: {encontrados} ({encontrados/max(1,len(objetivos))*100:.0f}%)")


if __name__ == "__main__":
    main()
