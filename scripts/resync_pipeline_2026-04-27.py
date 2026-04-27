"""
One-shot offline resync. Datos extraídos de Gmail Sent vía MCP el 2026-04-27.
Marca los 17 leads pendiente_envio como enviado_t1 con fecha real y T2 a +7,
anota duplicados detectados (todos los del 21-23/4 fueron enviados 2 veces).
"""
import datetime as dt
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_PATH = ROOT / "data" / "pipeline.json"

# slug -> (fecha_real_envio, num_envios_detectados)
ENVIOS_REALES = {
    "grupo-medico-siete-palmas": ("2026-04-21", 2),
    "grupo-clinica-maisonnave": ("2026-04-21", 2),
    "mr-grupo-clinico-alicante": ("2026-04-21", 2),
    "grupo-oter": ("2026-04-21", 2),
    "grupo-el-escondite": ("2026-04-21", 2),
    "grupo-sorell": ("2026-04-21", 2),
    "grupo-d-capricho": ("2026-04-21", 2),
    "grupo-rafael-afonso-las-palmas": ("2026-04-22", 2),
    "s-a-automocion": ("2026-04-22", 2),
    "ica-s-a-canarias": ("2026-04-22", 2),
    "grupo-sci": ("2026-04-22", 2),
    "grupo-marsan-marsan-transformaciones-superficiales": ("2026-04-22", 2),
    "electroniquel-s-a": ("2026-04-23", 2),
    "industrial-gijonesa-s-a-ingisa": ("2026-04-23", 2),
    "grupo-visier-arquitectura-urbanismo-promocion-desarrollo-e-i": ("2026-04-23", 2),
    "el-sol-grupo-inmobiliario": ("2026-04-23", 2),
    "grupo-morgadas": ("2026-04-23", 2),
}


def main():
    p = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))
    leads = p["leads"]
    cambios = 0
    for slug, (fecha_str, n_envios) in ENVIOS_REALES.items():
        if slug not in leads:
            print(f"  [missing] {slug}")
            continue
        lead = leads[slug]
        if lead.get("estado_email") != "pendiente_envio":
            print(f"  [skip] {slug}: estado={lead.get('estado_email')}")
            continue
        fecha = dt.date.fromisoformat(fecha_str)
        lead["estado_email"] = "enviado_t1"
        lead["draft_id"] = None
        lead.pop("draft_message_id", None)
        lead.pop("fecha_programada_envio", None)
        lead.setdefault("historial", []).append({
            "tipo": "mensaje_enviado",
            "canal": "email",
            "toque": "t1",
            "fecha": fecha_str,
            "fuente": "resincronizado_2026-04-27",
            "envios_detectados": n_envios,
        })
        if n_envios > 1:
            nota = f" [DUPLICADO: {n_envios} envíos el {fecha_str}]"
            lead["notas"] = (lead.get("notas") or "") + nota
        siguiente = fecha + dt.timedelta(days=7)
        lead["proxima_accion"] = {
            "fecha": siguiente.isoformat(),
            "tipo": "enviar_t2_si_no_responde",
            "generada": False,
        }
        cambios += 1
        print(f"  [ok] {slug}: t1 {fecha_str} (x{n_envios}) -> T2 {siguiente}")

    PIPELINE_PATH.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nResincronizados: {cambios}")


if __name__ == "__main__":
    main()
