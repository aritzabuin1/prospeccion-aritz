"""
Utilidades para leer/escribir pipeline.json con backup y validación.
"""

import json
import os
import re
import shutil
import unicodedata
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
PIPELINE_PATH = os.path.join(DATA_DIR, "pipeline.json")
BACKUP_PATH = os.path.join(DATA_DIR, "pipeline.backup.json")


def load_pipeline() -> dict:
    """Carga pipeline.json y devuelve el dict completo."""
    with open(PIPELINE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pipeline(data: dict):
    """Guarda pipeline.json con backup previo automático."""
    if os.path.exists(PIPELINE_PATH):
        shutil.copy2(PIPELINE_PATH, BACKUP_PATH)
    with open(PIPELINE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def slugify(nombre_empresa: str) -> str:
    """Normaliza nombre de empresa a kebab-case sin acentos."""
    # Quitar acentos
    texto = unicodedata.normalize("NFKD", nombre_empresa)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    # Minúsculas, reemplazar espacios y caracteres no alfanuméricos
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    texto = texto.strip("-")
    return texto


def add_lead(slug: str, data: dict):
    """Añade un lead nuevo al pipeline. No sobreescribe si ya existe."""
    pipeline = load_pipeline()
    if slug in pipeline["leads"]:
        raise ValueError(f"Lead '{slug}' ya existe en pipeline")
    pipeline["leads"][slug] = data
    save_pipeline(pipeline)


def update_lead(slug: str, patches: dict):
    """Merge parcial de campos en un lead existente."""
    pipeline = load_pipeline()
    if slug not in pipeline["leads"]:
        raise KeyError(f"Lead '{slug}' no encontrado en pipeline")
    lead = pipeline["leads"][slug]
    for key, value in patches.items():
        if isinstance(value, dict) and isinstance(lead.get(key), dict):
            lead[key].update(value)
        else:
            lead[key] = value
    save_pipeline(pipeline)


def add_historial_event(slug: str, event: dict):
    """Append de un evento al historial de un lead."""
    pipeline = load_pipeline()
    if slug not in pipeline["leads"]:
        raise KeyError(f"Lead '{slug}' no encontrado en pipeline")
    if "fecha" not in event:
        event["fecha"] = datetime.now().isoformat()
    pipeline["leads"][slug]["historial"].append(event)
    save_pipeline(pipeline)


def get_lead(slug: str) -> dict | None:
    """Devuelve un lead por slug, o None si no existe."""
    pipeline = load_pipeline()
    return pipeline["leads"].get(slug)


def _self_test():
    """Test básico de pipeline_utils."""
    # Test slugify
    assert slugify("Grupo Café España SL") == "grupo-cafe-espana-sl"
    assert slugify("  Clínica Dental Más  ") == "clinica-dental-mas"
    assert slugify("EUROMANAGER") == "euromanager"

    # Test load (asume que pipeline.json existe con estructura válida)
    data = load_pipeline()
    assert "_schema_version" in data
    assert "leads" in data

    print("pipeline_utils: todos los tests OK")


if __name__ == "__main__":
    _self_test()
