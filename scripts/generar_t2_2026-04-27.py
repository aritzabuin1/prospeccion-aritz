"""
Genera los 23 emails T2 nurture de la semana 2026-04-27:
- 6 limpios (Grupo A)
- 17 con disculpa por duplicado (Grupo B3)

Distribuye por fecha de envío (mar 28/4, mié 29/4, jue 30/4) y actualiza
pipeline.json con fecha_programada_envio + próxima_acción T2.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
PIPELINE_PATH = ROOT / "data" / "pipeline.json"
OUTBOX = ROOT / "outbox"
FIRMA_TEMPLATE = (ROOT / "config" / "firma-email.html").read_text(encoding="utf-8")
FOTO_URL = "https://raw.githubusercontent.com/aritzabuin1/prospeccion-aritz/main/assets/aritz-linkedin.jpg"
FIRMA_HTML = FIRMA_TEMPLATE.replace("{{FOTO_URL}}", FOTO_URL)

DISCULPA = {
    "martes": "Antes de nada — el martes pasado te llegó dos veces el mismo email por un fallo en mi sistema de envío programado. Disculpa la lata.",
    "miercoles": "Antes de nada — el miércoles pasado te llegó dos veces el mismo email por un fallo en mi sistema de envío programado. Disculpa la lata.",
    "jueves": "Antes de nada — el jueves pasado te llegó dos veces el mismo email por un fallo en mi sistema de envío programado. Disculpa la lata.",
}

# Cuerpos T2 (lista de párrafos). 'disculpa' indica si añadir preámbulo y de qué día.
T2 = {
    # ====== mar 28/4 — Grupo A limpio (3) ======
    "grupo-industrial-ferruz": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Pregunta sobre Ferruz",
        "saludo": "Hola Luis,",
        "disculpa": None,
        "cuerpo": [
            "Te dejo dos patrones que veo repetirse en grupos industriales con varias divisiones:",
            "1. El cierre mensual consolidado tarda 7-10 días porque cada división envía datos en su formato.",
            "2. El 60-70% de las preguntas que recibe el CFO durante el cierre son repetitivas y resolubles consultando dashboards bien montados.",
            "Son dos puntos donde se gana tiempo rápido si interesa explorarlo.",
        ],
    },
    "taymin-sa": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Vi algo sobre TAYMIN",
        "saludo": "Hola,",
        "disculpa": None,
        "cuerpo": [
            "Te dejo un dato concreto del sector mantenimiento industrial: las empresas que pasan de partes en papel/Excel a un flujo digital con captura desde móvil reducen el tiempo entre fin-de-trabajo y facturación de 7-15 días a 24-48 horas.",
            "En vuestra escala (6.000 m² + equipos en campo), eso se traduce en cobrar antes y reducir incidencias en facturas.",
            "Si quieres, te paso un caso anonimizado donde vimos la implantación.",
        ],
    },
    "grupo-aserpaz": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Vi algo sobre Aserpaz",
        "saludo": "Hola,",
        "disculpa": None,
        "cuerpo": [
            "Tres tipos de consultas concentran el 70-80% del volumen en administración de fincas: estado de cuotas, fechas de derramas, y actas/normativa.",
            "Si esos tres bloques se resuelven solos (chat 24/7 + búsqueda en actas), el equipo gana entre 10 y 15 horas por administrador y semana — y los propietarios reciben respuesta inmediata, no dos días después.",
            "Te lo dejo como apunte.",
        ],
    },
    # ====== mar 28/4 — Grupo B3 con disculpa (7) ======
    "grupo-medico-siete-palmas": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Tres centros, una DGT",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Sobre el dato: en redes de centros médicos con tramitación DGT, la mayoría de llamadas son \"¿qué papeles necesito?\", \"¿qué horarios tenéis?\" y \"¿cuánto cuesta?\". Resolverlas en chat 24/7 libera la centralita para citas reales y trámites complejos.",
            "Te lo dejo como apunte.",
        ],
    },
    "grupo-clinica-maisonnave": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Nueve aseguradoras, un solo fax",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Sobre el dato: en clínicas que trabajan con 8-10 aseguradoras, el 30-40% del trabajo administrativo es teclear partes y autorizaciones a portales distintos. Hay flujos que extraen del informe médico y rellenan los portales solos, con revisión humana al final. Suele recuperar 1-2 jornadas por semana del equipo de admisiones.",
            "Te lo dejo como apunte.",
        ],
    },
    "mr-grupo-clinico-alicante": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: El lunes después de Forbes",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Un patrón en clínicas que aparecen en medios grandes: el pico de leads tras una mención en Forbes/Telva/El Mundo dura 48-72 horas. Si ese pico no se atiende en menos de 5 minutos, el 70% se pierde a la competencia.",
            "Bots que cualifican y agendan primera visita en ese rango horario suelen recuperar entre el 20 y el 40% de leads que ahora se enfrían.",
        ],
    },
    "grupo-oter": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: 25 casas, un cierre",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Sobre Oter: con 25 conceptos, el cierre operativo (cuadre caja, mermas, ventas vs forecast) se vuelve costoso si cada local lo manda en su formato. He visto cadenas pasar de cierre semanal en jueves al cierre diario automatizado por local — y los gerentes empezaron a tomar decisiones mejores el lunes, no el viernes.",
            "Te lo dejo como apunte.",
        ],
    },
    "grupo-el-escondite": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Café Comercial y Barracuda",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Un dato del sector restauración multimarca: la pata de eventos por email suele tener un 30-40% de consultas repetitivas (aforos, menús base, fechas libres). Resolverlas con un asistente que tenga acceso al calendario de cada local recupera al equipo comercial para los eventos grandes que sí pagan margen.",
            "Te lo dejo como apunte.",
        ],
    },
    "grupo-sorell": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Una boda, tres WhatsApp",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "En catering de bodas con licencia para 1.000+ comensales, la novia tipo cambia 4-6 cosas entre prereserva y boda — menú, número de comensales, distribución, alérgenos. Si ese cambio entra por WhatsApp y nadie lo registra automáticamente en la ficha del evento, salta a cocina mal el día D.",
            "Una IA que lee los WhatsApp y actualiza la ficha del evento corta ese tipo de fallo casi a cero.",
        ],
    },
    "grupo-d-capricho": {
        "fecha_envio": "2026-04-28",
        "asunto": "Re: Cuatro buzones, una cocina",
        "saludo": "Hola,",
        "disculpa": "martes",
        "cuerpo": [
            "Un patrón en catering que mezcla bodas y corporate: las bodas requieren respuesta emocional y rápida; los corporate, datos exactos y formales. Si los dos tipos de lead caen en el mismo buzón y mismo equipo, uno acaba mal atendido. Triarlos automáticamente al entrar y dirigirlos a la persona adecuada cierra ese gap.",
            "Te lo dejo como apunte.",
        ],
    },
    # ====== mié 29/4 — Grupo A limpio (3, copiar de outbox 2026-04-25) ======
    "grupo-ccommo": {
        "fecha_envio": "2026-04-29",
        "copiar_de": "2026-04-25",
        "fecha_envio_str_dia": None,
    },
    "grupotel": {
        "fecha_envio": "2026-04-29",
        "copiar_de": "2026-04-25",
        "fecha_envio_str_dia": None,
    },
    "capel-vinos": {
        "fecha_envio": "2026-04-29",
        "copiar_de": "2026-04-25",
        "fecha_envio_str_dia": None,
    },
    # ====== mié 29/4 — Grupo B3 con disculpa (5) ======
    "grupo-rafael-afonso-las-palmas": {
        "fecha_envio": "2026-04-29",
        "asunto": "Re: OMODA 5 y cuatro islas",
        "saludo": "Hola,",
        "disculpa": "miercoles",
        "cuerpo": [
            "Sobre concesionarios multi-marca multi-isla: el cliente tipo de OMODA/JAECOO/EBRO tiene preguntas muy básicas (autonomía, garantía, cómo cargar) que se repiten miles de veces. Resolverlas en bot 24/7 con visual + capacidad de agendar prueba dinámica desbloquea al comercial para cierre real.",
            "Te lo dejo como apunte.",
        ],
    },
    "s-a-automocion": {
        "fecha_envio": "2026-04-29",
        "asunto": "Re: El lead del sábado",
        "saludo": "Hola,",
        "disculpa": "miercoles",
        "cuerpo": [
            "Un dato del sector ocasión: el 60% de leads cualificados llegan fines de semana, y los respondidos pasados los 30 minutos convierten 4-5 veces menos. Bots que cualifican (presupuesto, financiación, modelo objetivo) y agendan visita en minutos convierten esos sábados perdidos.",
        ],
    },
    "grupo-sci": {
        "fecha_envio": "2026-04-29",
        "asunto": "Re: Un aviso un viernes a las 18",
        "saludo": "Hola,",
        "disculpa": "miercoles",
        "cuerpo": [
            "En empresas de climatización a escala nacional, el coste real está en los avisos fuera de horario que se traducen en desplazamiento sin información previa. Bots que toman datos del aviso (modelo, error, fotos) antes del desplazamiento ahorran 1 de cada 3 visitas porque se resuelven en remoto o se llevan la pieza correcta a la primera.",
            "Te lo dejo como apunte.",
        ],
    },
    "ica-s-a-canarias": {
        "fecha_envio": "2026-04-29",
        "asunto": "Re: Una petshop y un fax",
        "saludo": "Hola,",
        "disculpa": "miercoles",
        "cuerpo": [
            "Un patrón en distribución B2B de petcare con cientos de petshops cliente: el 70% de los pedidos se pueden adelantar prediciendo demanda por familia de producto y temporada. Y las consultas de stock/precio que llegan por WhatsApp/teléfono se pueden responder solas si el sistema lee el catálogo en vivo.",
            "Eso libera comerciales para visitas que sí mueven cuenta.",
        ],
    },
    "grupo-marsan-marsan-transformaciones-superficiales": {
        "fecha_envio": "2026-04-29",
        "asunto": "Re: Cuatro plantas, un margen",
        "saludo": "Hola,",
        "disculpa": "miercoles",
        "cuerpo": [
            "En grupos industriales con MES ya implantado, el siguiente paso natural es cruzar datos del MES con costes reales (energía, materias, mano) para ver margen por orden de fabricación en tiempo real. Esa visibilidad permite priorizar las órdenes que rentan y rechazar a tiempo las que no.",
            "Te lo dejo como apunte.",
        ],
    },
    # ====== jue 30/4 — Grupo B3 con disculpa (5) ======
    "electroniquel-s-a": {
        "fecha_envio": "2026-04-30",
        "asunto": "Re: Un baño, una hoja Excel",
        "saludo": "Hola,",
        "disculpa": "jueves",
        "cuerpo": [
            "En galvanotecnia, el control de baños sigue dependiendo de hojas Excel y operarios atentos. Pero con sondas conectadas y un modelo que avise cuando la concentración sale de banda, los reprocesos bajan ~40% y las paradas no programadas casi desaparecen.",
            "Te lo dejo como apunte.",
        ],
    },
    "industrial-gijonesa-s-a-ingisa": {
        "fecha_envio": "2026-04-30",
        "asunto": "Re: APQ, ATEX y una oferta",
        "saludo": "Hola,",
        "disculpa": "jueves",
        "cuerpo": [
            "En calderería con normativa APQ/ATEX, cada oferta requiere cruzar pliego con histórico de proyectos similares para no infrapresupuestar. Lo que veo en empresas de vuestro perfil es que ese cruce lo hace 1 persona en 2-3 días por oferta, y a veces se equivoca.",
            "Un asistente que lee el pliego y cruza con vuestro histórico devuelve un primer presupuesto en horas, no días.",
        ],
    },
    "grupo-visier-arquitectura-urbanismo-promocion-desarrollo-e-i": {
        "fecha_envio": "2026-04-30",
        "asunto": "Re: Tres promociones agotadas",
        "saludo": "Hola,",
        "disculpa": "jueves",
        "cuerpo": [
            "Sobre el sector: con tres promociones agotadas y el siguiente lanzamiento a la vuelta, el cuello de botella no es vender — es cualificar leads frescos para no quemar al equipo comercial con curiosos. He visto promotoras pasar de 60 leads/mes contestados a mano a 250 cualificados automáticamente, con conversión a visita igual o mejor.",
        ],
    },
    "el-sol-grupo-inmobiliario": {
        "fecha_envio": "2026-04-30",
        "asunto": "Re: Siete bancos por operación",
        "saludo": "Hola,",
        "disculpa": "jueves",
        "cuerpo": [
            "Un patrón en grupos inmobiliarios con varios bancos partner: en cada operación hay que pedir tasaciones, simulaciones y documentación a 3-4 entidades distintas. Esa coordinación se come el 20-30% del tiempo del cerrador. Hay flujos que automatizan toda la ida y vuelta con cada banco hasta el \"sí\" definitivo.",
            "Te lo dejo como apunte.",
        ],
    },
    "grupo-morgadas": {
        "fecha_envio": "2026-04-30",
        "asunto": "Re: 22 camiones, 15 personas",
        "saludo": "Hola,",
        "disculpa": "jueves",
        "cuerpo": [
            "En transporte con flota propia y +14% de facturación, la trampa típica es que la gestión administrativa (gastos, consumos, mantenimientos por vehículo) escala lineal con la flota — pero el equipo de oficina no. Hay automatizaciones que leen tickets/partes desde el móvil del conductor y los imputan al vehículo correcto, sin tecla.",
            "Cuesta poco probar en 2-3 camiones y ver el ahorro.",
        ],
    },
}


def html_email(parrafos, asunto):
    parrafos_html = "\n".join(f'<p style="margin: 0 0 12px 0;">{p}</p>' for p in parrafos)
    return (
        f"<!-- Asunto: {asunto} -->\n"
        '<div style="font-family: Arial, sans-serif; font-size: 14px; color: #222; line-height: 1.5;">\n'
        f"{parrafos_html}\n"
        "<br/>\n"
        f"{FIRMA_HTML}\n"
        "</div>\n"
    )


def render_md(slug, asunto, saludo, parrafos, fecha_envio):
    cuerpo = "\n\n".join(parrafos)
    return (
        f"# Email T2 — {slug}\n"
        f"**Disparar:** {fecha_envio}\n"
        f"**Generado:** 2026-04-27\n\n"
        f"---\n\n"
        f"**Asunto:** {asunto}\n\n"
        f"---\n\n"
        f"{saludo}\n\n"
        f"{cuerpo}\n\n"
        f"Un saludo,\nAritz\n"
    )


def main():
    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))
    leads = pipeline["leads"]
    cambios = []
    no_encontrado = []

    for slug, cfg in T2.items():
        if slug not in leads:
            no_encontrado.append(slug)
            continue
        lead = leads[slug]
        fecha_envio = cfg["fecha_envio"]
        out_dir = OUTBOX / fecha_envio / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        if "copiar_de" in cfg:
            src = OUTBOX / cfg["copiar_de"] / slug / "email-t2.md"
            if not src.exists():
                no_encontrado.append(f"{slug} (no existe {src})")
                continue
            md_content = src.read_text(encoding="utf-8")
            (out_dir / "email-t2.md").write_text(md_content, encoding="utf-8")
            # Extraer asunto del md
            import re
            m = re.search(r"\*\*Asunto:\*\*\s*(.+)", md_content)
            asunto = m.group(1).strip() if m else "(sin asunto)"
            # Extraer cuerpo (todas las líneas tras el segundo "---")
            partes = md_content.split("---")
            cuerpo_full = partes[2] if len(partes) >= 3 else ""
            parrafos = [p.strip() for p in cuerpo_full.strip().split("\n\n") if p.strip() and not p.strip().startswith("Un saludo") and p.strip() != "Aritz"]
            html = html_email(parrafos, asunto)
            (out_dir / "email-t2.html").write_text(html, encoding="utf-8")
        else:
            asunto = cfg["asunto"]
            saludo = cfg["saludo"]
            parrafos = list(cfg["cuerpo"])
            if cfg.get("disculpa"):
                parrafos = [DISCULPA[cfg["disculpa"]]] + ["Sobre lo que te decía:"] + parrafos if False else [DISCULPA[cfg["disculpa"]]] + parrafos
            md = render_md(slug, asunto, saludo, parrafos, fecha_envio)
            (out_dir / "email-t2.md").write_text(md, encoding="utf-8")
            # Para HTML: añadir saludo como primer párrafo
            html_parrafos = [saludo] + parrafos
            html = html_email(html_parrafos, asunto)
            (out_dir / "email-t2.html").write_text(html, encoding="utf-8")

        # Actualizar pipeline: proxima_accion + fecha_programada_envio
        lead["proxima_accion"] = {
            "fecha": fecha_envio,
            "tipo": "enviar_t2_si_no_responde",
            "generada": True,
        }
        lead.setdefault("historial", []).append({
            "tipo": "mensaje_generado",
            "canal": "email",
            "toque": "t2",
            "fecha": "2026-04-27",
            "fecha_envio": fecha_envio,
            "con_disculpa": bool(cfg.get("disculpa")),
        })
        cambios.append((slug, fecha_envio, "con_disculpa" if cfg.get("disculpa") else "limpio"))

    PIPELINE_PATH.write_text(json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"=== T2 generados: {len(cambios)} ===")
    por_fecha = {}
    for slug, fecha, tipo in cambios:
        por_fecha.setdefault(fecha, []).append((slug, tipo))
    for fecha in sorted(por_fecha):
        print(f"\n{fecha}: {len(por_fecha[fecha])} emails")
        for slug, tipo in por_fecha[fecha]:
            print(f"  [{tipo:14s}] {slug}")
    if no_encontrado:
        print(f"\nNo encontrados: {no_encontrado}")


if __name__ == "__main__":
    main()
