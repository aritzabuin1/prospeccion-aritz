"""
Genera dossier + email T1 + LinkedIn paso 1 + contacto.md para CUALQUIER
lead activo del pipeline que no tenga outbox aún.

Usa templates sectoriales con variedad de aperturas/cierres para mantener
naturalidad sin tener que escribir cada lead a mano.

Uso:
    python scripts/generar_outbox_por_sector.py --fecha 2026-05-04 [--solo-con-email]
"""
import argparse
import io
import json
import random
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.pipeline_utils import slugify  # noqa: E402

PIPELINE_PATH = ROOT / "data" / "pipeline.json"

# Por sector: pool de aperturas (entrada/contexto), pool de pregunta, decisor a buscar.
# Cada apertura usa {empresa} y opcionalmente {senal}.
SECTORES = {
    "industria_fabricacion": {
        "asuntos": [
            "El parte de planta del lunes",
            "Producción y la hoja de cálculo de la noche",
            "OEE y los partes que llegan tarde",
            "Trazabilidad de lote en serie corta",
        ],
        "aperturas": [
            "Vi {empresa} mirando fabricantes industriales con peso en {zona} y me quedé con la operación multiplanta. En grupos así lo que más se escapa hoy no es producir, es que los partes de turno y los datos de calidad se consolidan a mano cada noche y la oficina técnica recibe la foto del día con 12-18 horas de desfase.",
            "Entré en {empresa} buscando fabricantes con base en {zona} y me fijé en la estructura industrial. En operación así el dolor más repetido es que el OEE y las no conformidades viven en tres sistemas distintos; cuando producción y calidad se sientan a revisar la semana, hablan de versiones distintas de la realidad.",
            "Repasando fabricantes industriales con presencia en {zona} aterricé en {empresa}. En este perfil lo que más fricciona hoy no es producir — es que la trazabilidad del lote desde MP hasta cliente final se reconstruye a mano cuando salta una incidencia, y se invierten 2 días en cuadrarla.",
        ],
        "preguntas": [
            "¿Cómo estáis trazando hoy esos datos de planta?",
            "¿Cómo cerráis hoy ese loop entre planta y oficina?",
            "¿Cómo estáis gestionando hoy la trazabilidad del lote?",
        ],
        "decisor": "Director de Operaciones / Director Industrial",
        "dolores": [
            "Consolidación de partes de turno en tiempo real.",
            "Trazabilidad de calidad y no conformidades.",
            "Reporting de OEE por línea/máquina.",
            "Coordinación entre planta y compras (rotura de stock).",
        ],
    },
    "logistica_transporte": {
        "asuntos": [
            "Albaranes y el cuadre del viernes",
            "Una entrada de mil pallets para mañana",
            "El bar que pidió por WhatsApp",
            "Routing dinámico y los cambios del martes",
        ],
        "aperturas": [
            "Vi {empresa} revisando operadores logísticos con base en {zona} y me quedé con la operación de almacén + transporte. En operadores así lo que más fricciona hoy no es mover, es que cuando un cliente avisa de una entrada grande para mañana, almacén, transporte y administración tienen que coordinar a mano entre tres sistemas y la respuesta sobre fecha de disposición tarda 2 horas.",
            "Entré en {empresa} mirando logística con peso en {zona} y me fijé en la operación de transporte y reparto. En este negocio el dolor que más se repite hoy no es mover la mercancía — es que los viernes administración cierra la semana cuadrando albaranes con el TMS y los partes de los conductores, y cualquier discrepancia abre 20 minutos de llamadas.",
            "Repasando distribuidores con base en {zona} aterricé en {empresa}. En distribución HORECA lo que más se escapa hoy es que los pedidos llegan por WhatsApp, email y EDI, y administración pasa la mañana metiendo a mano en el ERP los que entraron de noche.",
        ],
        "preguntas": [
            "¿Cómo estáis cuadrando hoy esa información?",
            "¿Cómo estáis canalizando hoy esos pedidos multicanal?",
            "¿Cómo estáis coordinando hoy entradas grandes en almacén?",
        ],
        "decisor": "Director de Operaciones / Director Logístico",
        "dolores": [
            "Cuadre de albaranes con TMS.",
            "Trazabilidad de incidencias en ruta.",
            "Captura unificada de pedidos multicanal.",
            "Coordinación con conductores subcontratados.",
        ],
    },
    "construccion_ingenieria": {
        "asuntos": [
            "Certificaciones y el Excel del lunes",
            "Cuadrillas y el parte de obra del operario",
            "Documentación de proyecto y la auditoría del cliente",
            "Mantenimiento preventivo y los avisos del sábado",
        ],
        "aperturas": [
            "Vi {empresa} mirando constructoras e ingenierías con peso en {zona} y me fijé en la operación de proyecto. En obra así lo que más se escapa hoy no es la ejecución — es que el reporting de avance, certificaciones y subcontratas vive en un Excel distinto en cada delegación y los lunes la dirección financiera pierde 3 horas cuadrando la realidad de la semana.",
            "Entré en {empresa} repasando empresas de instalaciones y mantenimiento en {zona}. En instalaciones así el dolor que más fricciona es que la coordinación entre cuadrillas, los partes de operario y la facturación al cliente vive en tres sistemas distintos y administración pierde la mañana del lunes cuadrándolo.",
            "Repasando constructoras y proyectos en {zona} aterricé en {empresa}. En este negocio lo que más se escapa hoy no es el montaje — es que la documentación técnica de cada proyecto (planos, cálculos, certificados, CAE) vive en carpetas distintas y cuando llega la auditoría del cliente se invierten 2 días en compilar.",
        ],
        "preguntas": [
            "¿Cómo lo estáis consolidando hoy entre delegaciones?",
            "¿Cómo estáis cerrando hoy el ciclo parte → factura?",
            "¿Cómo estáis gestionando hoy esa documentación?",
        ],
        "decisor": "Director Financiero / Director de Operaciones",
        "dolores": [
            "Consolidación de avance de obra y certificaciones.",
            "Captura de partes de operario en obra.",
            "Gestión documental de subcontratas (CAE).",
            "Reporting financiero por proyecto.",
        ],
    },
    "servicios_profesionales": {
        "asuntos": [
            "Expedientes y la matriz de horas",
            "Despacho, plazo y el calendario del jurídico",
            "Auditoría y el papeleo del cliente",
        ],
        "aperturas": [
            "Vi {empresa} repasando despachos y consultoras con peso en {zona} y me quedé con el perfil multicliente. En despachos así lo que más se escapa hoy no es el caso — es que la matriz de horas, plazos procesales y minutas vive en herramientas distintas, y cuando llega fin de mes facturación pierde días cuadrando.",
            "Entré en {empresa} mirando servicios profesionales en {zona}. En auditoría/consultoría el dolor que más se repite es que cada cliente exige plantillas y formatos distintos, y los becarios pasan la mitad del tiempo rellenando información que ya estaba en otro Excel.",
        ],
        "preguntas": [
            "¿Cómo estáis cuadrando hoy horas y minutas a fin de mes?",
            "¿Cómo lo estáis estandarizando hoy entre clientes?",
        ],
        "decisor": "Socio Director / Director de Operaciones",
        "dolores": [
            "Captura de horas por proyecto y cliente.",
            "Gestión de plazos procesales/auditoría.",
            "Estandarización de entregables.",
            "Facturación con detalle por hito.",
        ],
    },
    "salud_cadenas": {
        "asuntos": [
            "Cita médica y la llamada que se pierde",
            "Historia clínica entre centros",
            "Agenda del especialista y la lista de espera",
        ],
        "aperturas": [
            "Vi {empresa} mirando grupos sanitarios con peso en {zona}. En centros así lo que más fricciona hoy no es la calidad asistencial — es que el ciclo cita → consulta → seguimiento pierde pacientes por una llamada perdida o un email no contestado, y la lista de espera no refleja capacidad real.",
            "Entré en {empresa} revisando cadenas de clínicas en {zona}. En este modelo el dolor más repetido es que la historia clínica vive en sistemas distintos por centro, y cuando un paciente cambia de clínica el especialista invierte 15 minutos buscando el último informe.",
        ],
        "preguntas": [
            "¿Cómo estáis trazando hoy ese ciclo de paciente?",
            "¿Cómo estáis unificando hoy la historia clínica entre centros?",
        ],
        "decisor": "Director Médico / Director de Operaciones",
        "dolores": [
            "Captura unificada de citas multicanal.",
            "Historia clínica entre centros.",
            "Lista de espera y capacidad real.",
            "Reporting asistencial por centro/especialidad.",
        ],
    },
    "inmobiliaria_gestion": {
        "asuntos": [
            "Reservas, arras y la cadena de aprobaciones",
            "Stock disponible y la promoción de la semana",
            "Notarías y el cierre de operación",
        ],
        "aperturas": [
            "Entré en {empresa} mirando promotoras inmobiliarias con presencia en {zona} y me quedé con el mix de cartera. En este perfil lo que más fricciona hoy no es vender — es la cadena de aprobaciones internas para liberar fases, validar reservas y soltar arras: pasa por comercial, financiero, jurídico y dirección, y cada salto pierde un día.",
            "Vi {empresa} revisando gestoras inmobiliarias en {zona}. En este negocio el dolor que más se repite es que el seguimiento de leads desde web/portal hasta visita vive en hojas distintas, y un lead frío se pierde antes de que comercial lo retome.",
        ],
        "preguntas": [
            "¿Tenéis ese flujo trazado o vive en email/llamada?",
            "¿Cómo estáis trazando hoy ese embudo lead → visita?",
        ],
        "decisor": "Director Comercial / Director de Promoción",
        "dolores": [
            "Aprobaciones internas para reservas y arras.",
            "Seguimiento de leads desde portal hasta visita.",
            "Stock disponible por promoción y fase.",
            "Coordinación con notarías y bancos.",
        ],
    },
    "hosteleria_grupos": {
        "asuntos": [
            "Revenue del lunes y los 5 destinos",
            "Reservas, ocupación y la hoja de cálculo del director",
            "Personal estacional y el onboarding del verano",
        ],
        "aperturas": [
            "Vi {empresa} mirando grupos hoteleros con peso en {zona}. En grupos así el dolor más repetido hoy no es la ocupación — es que el revenue management y el reporting consolidado entre destinos se hace con extracciones manuales del PMS cada lunes y la dirección comercial pierde la primera mañana de la semana.",
            "Entré en {empresa} repasando grupos de restauración/hostelería en {zona}. En este perfil lo que más fricciona es que la integración entre PMS, reservas, RRHH estacional y caja vive en cuatro herramientas distintas, y la consolidación financiera tarda 10 días en cerrar el mes.",
        ],
        "preguntas": [
            "¿Cómo estáis consolidando hoy datos entre destinos?",
            "¿Cómo lo estáis cuadrando hoy a fin de mes?",
        ],
        "decisor": "Director de Revenue / Director de Operaciones",
        "dolores": [
            "Reporting consolidado de revenue.",
            "Integración PMS-CRM-revenue.",
            "Onboarding de personal estacional.",
            "Cierre financiero mensual.",
        ],
    },
    "retail_cadenas": {
        "asuntos": [
            "Reposición de la tienda y el lunes de central",
            "Promociones por marca y el reporting al fabricante",
            "Stock real vs. ERP",
        ],
        "aperturas": [
            "Vi {empresa} mirando cadenas y distribuidores con peso en {zona}. En este modelo lo que más fricciona hoy no es vender — es que cada marca pide reporting con su formato y sus KPIs, y administración pasa media semana cuadrando ventas, devoluciones y promociones por marca para enviar a fabricantes.",
            "Entré en {empresa} repasando retail/distribución en {zona}. En cadenas así el dolor más repetido es que la reposición a tienda se planifica con 4 días de antelación pero el stock real diverge del ERP, y cuando la tienda pide urgencia el lunes la central improvisa.",
        ],
        "preguntas": [
            "¿Cómo estáis automatizando hoy ese reporting?",
            "¿Cómo estáis sincronizando hoy stock real vs. ERP?",
        ],
        "decisor": "Director Comercial / Director de Operaciones",
        "dolores": [
            "Reporting estructurado por marca.",
            "Reposición a tienda y stock real.",
            "Conciliación promociones/rappels.",
            "Visibilidad de margen por SKU.",
        ],
    },
    "energia_utilities": {
        "asuntos": [
            "Instalación y la visita del comercial",
            "SAT, agenda y la cuadrilla del martes",
            "Producción fotovoltaica y el seguimiento al cliente",
        ],
        "aperturas": [
            "Vi {empresa} repasando empresas de energía/instalaciones con peso en {zona}. En este negocio lo que más se escapa hoy no es vender la instalación — es que entre la visita comercial y la firma pasan 3-5 contactos manuales (estudio, propuesta, financiación, agenda) que viven en hojas distintas y cada salto pierde leads templados.",
            "Entré en {empresa} mirando instaladoras en {zona}. En instalaciones así el dolor más repetido es que el SAT recibe avisos por teléfono, email y WhatsApp, y cada técnico va con su orden de trabajo en papel — administración no sabe en tiempo real qué máquina está parada en qué cliente.",
        ],
        "preguntas": [
            "¿Cómo estáis trazando hoy ese embudo post-visita?",
            "¿Cómo estáis trazando hoy el ciclo aviso → técnico → resolución?",
        ],
        "decisor": "Director Comercial / Director de Operaciones",
        "dolores": [
            "Embudo lead → estudio → firma.",
            "Asignación dinámica de técnicos SAT.",
            "Trazabilidad de intervenciones.",
            "Postventa y seguimiento de producción.",
        ],
    },
    "automocion_concesionarios": {
        "asuntos": [
            "El lead que entró el sábado",
            "Cita de taller y la llamada que no se devuelve",
            "VO, financiación y los 4 leads del lunes",
        ],
        "aperturas": [
            "Entré en {empresa} mirando concesionarios y grupos de automoción en {zona}. En grupos así lo que más se escapa hoy no es la venta en showroom — es que el lead que entró el sábado por la web pidiendo un VO compite el lunes con las llamadas, las citas de taller y tres leads más, y cuando se responde ya ha mirado otros dos concesionarios.",
            "Vi {empresa} repasando concesionarios con base en {zona}. En este perfil el dolor más repetido es que la cita de taller se gestiona por teléfono, los recordatorios se hacen a mano y caen el 20% de las posventas porque nadie reactivó al cliente.",
        ],
        "preguntas": [
            "¿Cómo lo estáis resolviendo hoy entre comerciales?",
            "¿Cómo estáis automatizando hoy recordatorios y reactivación?",
        ],
        "decisor": "Director General / Director Comercial",
        "dolores": [
            "Seguimiento a lead web y showroom.",
            "Cita de taller y recordatorios.",
            "Preparación de entrega y matriculación.",
            "Reporting de conversión por comercial.",
        ],
    },
    "agroalimentario": {
        "asuntos": [
            "Lote, caducidad y el albarán del lunes",
            "Bodega, exportación y la trazabilidad",
            "Pedido del cliente y la cadena de frío",
        ],
        "aperturas": [
            "Vi {empresa} mirando empresas agroalimentarias con peso en {zona}. En este negocio lo que más se escapa hoy no es la calidad del producto — es que cada lunes la administración cuadra a mano albaranes con peso, lote y caducidad de los pedidos del fin de semana, y cualquier discrepancia abre 30 minutos de llamadas con cliente y central.",
            "Entré en {empresa} repasando bodegas/agroalimentarias en {zona}. En modelo exportador así el dolor más repetido es que la trazabilidad del lote y la documentación aduanera viven en sistemas distintos, y cuando un cliente internacional reclama se invierten 2 días reconstruyendo.",
        ],
        "preguntas": [
            "¿Cómo estáis cuadrando hoy esa información?",
            "¿Cómo estáis trazando hoy lote y documentación aduanera?",
        ],
        "decisor": "Director de Operaciones / Director Comercial",
        "dolores": [
            "Trazabilidad de lote, peso y caducidad.",
            "Cuadre de albaranes multicanal.",
            "Documentación aduanera de exportación.",
            "Cumplimiento APPCC.",
        ],
    },
    "consultoras_rrhh": {
        "asuntos": [
            "Selección activa y los 18 procesos",
            "Candidato, cliente y el seguimiento que se pierde",
        ],
        "aperturas": [
            "Vi {empresa} mirando consultoras de RRHH y selección con peso en {zona}. En este negocio lo que más se escapa hoy no es encontrar candidatos — es que el seguimiento entre proceso, cliente y candidato vive en email + Excel, y cuando un proceso entra en standby los candidatos templados se enfrían en una semana.",
            "Entré en {empresa} repasando ETTs/consultoras en {zona}. En este perfil el dolor más repetido es que cada cliente exige reporting de candidatos con su formato, y administración pasa media semana actualizando hojas de cálculo distintas.",
        ],
        "preguntas": [
            "¿Cómo estáis trazando hoy esos procesos en paralelo?",
            "¿Cómo estáis automatizando hoy ese reporting cliente?",
        ],
        "decisor": "Socio Director / Director de Operaciones",
        "dolores": [
            "Trazabilidad de candidato a través de procesos.",
            "Reporting cliente personalizado.",
            "Reactivación de candidatos templados.",
            "Captura de horas y minutas.",
        ],
    },
}

# Sectores no mapeados → fallback genérico
FALLBACK = {
    "asuntos": ["Operación, Excel y el lunes"],
    "aperturas": [
        "Vi {empresa} con base en {zona} y me quedé con el perfil de operación. En empresas así lo que más se escapa hoy no es el core del negocio — es que datos de varias áreas viven en herramientas distintas y la consolidación de la semana pierde tiempo cuadrando hojas a mano."
    ],
    "preguntas": ["¿Cómo lo estáis consolidando hoy entre áreas?"],
    "decisor": "Director General / Director de Operaciones",
    "dolores": [
        "Consolidación de datos entre áreas.",
        "Reporting interno semanal.",
        "Coordinación entre departamentos.",
        "Captura de información operativa.",
    ],
}


def md_to_html(asunto, cuerpo):
    parrafos = [p.strip() for p in cuerpo.strip().split("\n\n") if p.strip()]
    body = "\n".join(f"<p>{p}</p>" for p in parrafos)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{asunto}</title></head>
<body style="font-family: -apple-system, sans-serif; max-width: 600px;">
{body}
</body></html>"""


def generar_lead(slug: str, lead: dict, fecha: str, rng: random.Random) -> bool:
    sector = lead.get("sector", "")
    cfg = SECTORES.get(sector, FALLBACK)

    empresa = lead.get("empresa") or slug.replace("-", " ").title()
    zona = lead.get("zona") or "España"
    web = lead.get("web") or ""

    asunto = rng.choice(cfg["asuntos"])
    apertura = rng.choice(cfg["aperturas"]).format(empresa=empresa, zona=zona)
    pregunta = rng.choice(cfg["preguntas"])
    decisor = cfg["decisor"]

    cuerpo = f"""Hola,

{apertura}

{pregunta}

Un saludo,
Aritz"""

    # Outbox
    outbox_dir = ROOT / "outbox" / fecha / slug
    outbox_dir.mkdir(parents=True, exist_ok=True)
    (outbox_dir / "email-t1.md").write_text(
        f"# Email T1 — {slug}\n\n**Fecha:** {fecha}\n**Generado el:** {fecha}\n\n---\n\n**Asunto:** {asunto}\n\n---\n\n{cuerpo}\n",
        encoding="utf-8",
    )
    (outbox_dir / "email-t1.html").write_text(md_to_html(asunto, cuerpo), encoding="utf-8")

    linkedin_q = f'"{empresa}" {zona}'
    (outbox_dir / "linkedin-paso1.md").write_text(
        f"# LinkedIn Paso 1 — {slug}\n\n**Fecha:** {fecha}\n**Tipo:** Connection SIN NOTA\n\n---\n\nEnviar connection SIN nota. Decisor pendiente.\n\nBúsqueda: `{linkedin_q}`\nFiltrar por: {decisor}.\n",
        encoding="utf-8",
    )

    email_actual = (lead.get("contacto") or {}).get("email", "")
    (outbox_dir / "contacto.md").write_text(
        f"# Contacto — {empresa}\n\n**Fecha:** {fecha}\n\n## Destinatario\n- **Email:** {email_actual or '⚠ pendiente'}\n- **Cargo:** {decisor}\n- **Web:** {web}\n- **Zona:** {zona}\n\n## Canal\n- Email: `email-t1.html`. Asunto: \"{asunto}\"\n- LinkedIn: `linkedin-paso1.md`\n",
        encoding="utf-8",
    )

    # Dossier
    dossiers_dir = ROOT / "dossiers" / fecha
    dossiers_dir.mkdir(parents=True, exist_ok=True)
    dossier_md = f"""# Dossier: {empresa}
**Fecha:** {fecha}

## 1. Perfil
- **Sector:** {sector}
- **Zona:** {zona}
- **Web:** {web}
- **Score:** {lead.get('score', 0)}

## 2. Dolores hipótesis
""" + "\n".join(f"{i+1}. {d}" for i, d in enumerate(cfg["dolores"])) + f"""

## 3. Decisor a buscar
{decisor}. Búsqueda LinkedIn: `{linkedin_q}`

## 4. Ángulo
{apertura}

## 5. Pregunta calibrada
{pregunta}

## 6. Asunto email
{asunto}
"""
    (dossiers_dir / f"{slug}.md").write_text(dossier_md, encoding="utf-8")

    # Pipeline updates
    lead["dossier_path"] = f"dossiers/{fecha}/{slug}.md"
    hist = lead.setdefault("historial", [])
    if not any(ev.get("tipo") == "mensaje_generado" and ev.get("toque") == "t1"
               and ev.get("tanda") == fecha for ev in hist):
        hist.append({
            "tipo": "mensaje_generado",
            "fecha": fecha,
            "canal": "email",
            "toque": "t1",
            "asunto": asunto,
            "tanda": fecha,
        })
    if email_actual:
        lead["proxima_accion"] = {
            "tipo": "enviar_t1",
            "fecha": fecha,
        }
    else:
        lead["proxima_accion"] = {
            "tipo": "enriquecer_email",
            "fecha": fecha,
            "nota": "Sin email; alternativa LinkedIn",
        }
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fecha", required=True, help="YYYY-MM-DD fecha de envío T1")
    ap.add_argument("--solo-con-email", action="store_true",
                    help="Solo leads con contacto.email ya rellenado")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    pipeline = json.loads(PIPELINE_PATH.read_text(encoding="utf-8"))

    objetivos = []
    for slug, l in pipeline["leads"].items():
        if slug.startswith("_"):
            continue
        if l.get("estado_email") != "nuevo":
            continue
        if l.get("dossier_path"):
            continue
        if args.solo_con_email and not (l.get("contacto") or {}).get("email"):
            continue
        objetivos.append(slug)

    print(f"Leads a generar: {len(objetivos)}")
    n = 0
    for slug in objetivos:
        try:
            generar_lead(slug, pipeline["leads"][slug], args.fecha, rng)
            n += 1
            print(f"  [{n}] {slug}")
        except Exception as exc:
            print(f"  ERROR {slug}: {exc}")

    PIPELINE_PATH.write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n=== Generados {n} dossiers + outbox ===")


if __name__ == "__main__":
    main()
