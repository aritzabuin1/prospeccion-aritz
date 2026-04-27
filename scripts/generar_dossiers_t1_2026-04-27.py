"""
Genera dossiers + email T1 + LinkedIn paso 1 + contacto para los 20 leads
aprobados de la tanda 2026-04-27.

Sin email verificado todavía (Apollo+Hunter pendiente). Los outputs quedan en
outbox/ y dossiers/ listos para que cuando llegue el enrichment se rellene
contacto.email y se metan en preparar_borradores_semana.py.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
FECHA = "2026-04-27"

# (slug, asunto, angulo_apertura, pregunta_cierre, decisor_buscar, busqueda_linkedin)
LEADS = {
    "copisa-constructora": {
        "asunto": "Proyectos singulares y la hoja de cálculo del lunes",
        "apertura": "Vi Copisa repasando constructoras españolas con cartera internacional y me quedé con la frase \"proyectos singulares\". En obra civil grande, lo que se escapa hoy no es la ejecución, es que el reporting de avance, certificaciones y subcontratas viva en un Excel distinto en cada delegación y los lunes la dirección financiera tarda 3 horas en cuadrar la realidad de la semana.",
        "pregunta": "¿Cómo lo estáis consolidando hoy entre delegaciones?",
        "decisor": "Director Financiero / Director de Operaciones",
        "linkedin_q": "\"Copisa\" director financiero OR operaciones",
        "dossier_titulo": "Copisa Constructora",
        "dossier_resumen": "Constructora global española con foco en proyectos singulares (obra civil, edificación, servicios industriales). Estructura multidelegación con cartera internacional. Sector con baja madurez digital interna pese a fortaleza técnica.",
        "dolores": [
            "Consolidación de avance de obra y certificaciones entre delegaciones.",
            "Gestión documental con subcontratas (CAE, albaranes, partes).",
            "Reporting financiero por proyecto vs. plan.",
            "Control de no conformidades y trazabilidad."
        ],
    },
    "grupo-insur": {
        "asunto": "Promoción residencial y la cadena de aprobaciones",
        "apertura": "Entré en Insur revisando promotoras inmobiliarias andaluzas con recorrido y me quedé con el mix patrimonial + promoción. En un grupo así lo que más fricciona hoy no es vender el piso, es la cadena de aprobaciones internas para liberar fases, validar reservas y soltar arras: pasa por comercial, financiero, jurídico y dirección, y cada salto pierde un día.",
        "pregunta": "¿Tenéis ese flujo trazado en algún sitio o vive en email/llamada?",
        "decisor": "Director Comercial / Director de Promoción",
        "linkedin_q": "\"Grupo Insur\" director comercial OR promociones",
        "dossier_titulo": "Grupo Insur",
        "dossier_resumen": "Promotora inmobiliaria andaluza con cartera patrimonial y de promoción. Estructura mediana-grande con presencia en varias provincias. Sector con margen claro para automatizar back-office comercial.",
        "dolores": [
            "Cadena de aprobaciones internas para reservas y arras.",
            "Seguimiento de leads desde web/portal hasta visita.",
            "Reporting de stock disponible por promoción y fase.",
            "Coordinación con notarías y bancos para cierre."
        ],
    },
    "pagina-de-inicio-de-la-web-de-grupo-pinero": {
        "asunto": "Caribe, todo incluido y el revenue de los lunes",
        "apertura": "Vi Piñero mirando grupos hoteleros españoles con peso fuerte en Caribe (Bahia Principe) y me quedé con el modelo todo incluido a gran escala. En un grupo así el dolor que más se repite hoy no es la ocupación, es que el revenue management y el reporting consolidado entre destinos se hace con extracciones manuales del PMS cada lunes y la dirección comercial pierde la primera mañana de la semana.",
        "pregunta": "¿Cómo estáis consolidando hoy datos entre Bahia Principe y el resto de marcas?",
        "decisor": "Director de Revenue / Director de Operaciones Hoteleras",
        "linkedin_q": "\"Grupo Piñero\" OR \"Bahia Principe\" revenue OR operaciones",
        "dossier_titulo": "Grupo Piñero (Bahia Principe)",
        "dossier_resumen": "Grupo hotelero familiar mallorquín con fuerte presencia en Caribe (Bahia Principe). Operación all-inclusive multidestino. Sector con automatización dispar entre marketing y operación.",
        "dolores": [
            "Reporting consolidado de revenue entre destinos.",
            "Integración PMS-CRM-revenue para forecasting.",
            "Onboarding de personal estacional.",
            "Gestión de incidencias en estancia con respuesta sub-15min."
        ],
    },
    "nicolas-correa-s-a-grupo-nicolas-correa": {
        "asunto": "Fresadoras de gran formato y el parte de planta",
        "apertura": "Entré en Nicolás Correa buscando fabricantes españoles de máquina-herramienta con recorrido global y me quedé con el catálogo de fresadoras de gran formato. En una fábrica así lo que más se escapa hoy no es la producción, es que el parte de planta — paradas, OEE, no conformidades — se consolida a mano cada noche y la oficina técnica recibe la foto del día con 18 horas de desfase.",
        "pregunta": "¿Cómo estáis trazando hoy esos datos de planta?",
        "decisor": "Director de Operaciones / Director Industrial",
        "linkedin_q": "\"Nicolás Correa\" director industrial OR operaciones",
        "dossier_titulo": "Nicolás Correa S.A.",
        "dossier_resumen": "Fabricante español de máquina-herramienta de gran formato (fresadoras) con clientes globales. Sede Burgos. Estructura industrial mediana-grande con exportación.",
        "dolores": [
            "Consolidación de OEE y partes de planta entre turnos.",
            "Trazabilidad de no conformidades en serie corta.",
            "Comunicación entre oficina técnica y planta.",
            "Reporting de eficiencia por máquina y operario."
        ],
    },
    "grupo-acura": {
        "asunto": "Salamanca, fabricación y los partes de turno",
        "apertura": "Vi Grupo Acura revisando fabricantes industriales en Salamanca y me quedé con la estructura multiplanta. En grupos industriales así lo que más se repite hoy no es la producción, es que los partes de turno y los datos de calidad pasan a sistema con 12-24 horas de retraso, y cuando producción y calidad se sientan a revisar la semana, hablan de versiones distintas de la realidad.",
        "pregunta": "¿Cómo cerráis hoy ese loop entre planta y oficina?",
        "decisor": "Director de Operaciones / Director Industrial",
        "linkedin_q": "\"Grupo Acura\" Salamanca operaciones OR industrial",
        "dossier_titulo": "Grupo Acura",
        "dossier_resumen": "Grupo industrial con sede en Salamanca. Operación multiplanta. Sector con automatización disparda entre back-office y planta.",
        "dolores": [
            "Captura de partes de turno en tiempo real.",
            "Trazabilidad de calidad y no conformidades.",
            "Reporting de eficiencia por línea y producto.",
            "Coordinación entre planta y compras (rotura de stock)."
        ],
    },
    "grupo-eboli-salamanca": {
        "asunto": "Fabricación en Salamanca y la trazabilidad del lote",
        "apertura": "Entré en Grupo Eboli mirando fabricantes industriales con peso en Salamanca y me quedé con el perfil de operación local con clientes nacionales. En estructuras así lo que más se escapa hoy no es producir, es que la trazabilidad del lote — desde la materia prima al cliente final — vive en albaranes en papel y hojas de Excel, y cuando salta una incidencia de calidad se invierten 2 días en reconstruir el camino.",
        "pregunta": "¿Cómo estáis trazando hoy lotes y materias primas?",
        "decisor": "Director de Calidad / Director de Operaciones",
        "linkedin_q": "\"Grupo Eboli\" Salamanca calidad OR operaciones",
        "dossier_titulo": "Grupo Eboli",
        "dossier_resumen": "Grupo industrial con sede en Salamanca. Operación de fabricación con clientes nacionales. Tamaño mediano.",
        "dolores": [
            "Trazabilidad de lote desde MP hasta cliente.",
            "Gestión documental de albaranes y partes de calidad.",
            "Reporting de no conformidades.",
            "Coordinación con clientes en incidencias."
        ],
    },
    "grupo-espacio-industrial": {
        "asunto": "Naves industriales y el alquiler de mil metros un viernes",
        "apertura": "Vi Espacio Industrial mirando promotores y gestores de suelo industrial en Madrid y me quedé con el portfolio de naves logísticas. En este negocio lo que más fricciona hoy no es comercializar, es que el ciclo lead → visita → reserva → contrato pasa por comercial, técnico, jurídico y dirección, y cuando un cliente pide mil metros un viernes la respuesta llega el martes.",
        "pregunta": "¿Cómo estáis acortando hoy ese ciclo entre departamentos?",
        "decisor": "Director Comercial / Director de Operaciones",
        "linkedin_q": "\"Grupo Espacio Industrial\" Madrid director",
        "dossier_titulo": "Grupo Espacio Industrial",
        "dossier_resumen": "Promotora y gestora de suelo industrial en Madrid. Cartera de naves logísticas e industriales. Sector con back-office artesanal.",
        "dolores": [
            "Tiempo de respuesta a peticiones comerciales.",
            "Coordinación entre comercial, técnico y jurídico.",
            "Reporting de ocupación y rentabilidad por activo.",
            "Gestión documental de contratos de alquiler."
        ],
    },
    "grupo-la-fabrica": {
        "asunto": "Operación industrial y el reporte que llega los miércoles",
        "apertura": "Entré en Grupo La Fábrica revisando grupos industriales con peso en Madrid y me quedé con la estructura multiunidad. En grupos así el dolor que más se repite hoy no es producir, es que el reporting consolidado de la semana llega los miércoles porque cada unidad tiene su propia hoja, y cuando el comité se sienta a decidir la inversión del trimestre la foto que ven está desfasada.",
        "pregunta": "¿Cómo lo estáis consolidando hoy entre unidades?",
        "decisor": "Director Financiero / Director General",
        "linkedin_q": "\"Grupo La Fábrica\" Madrid financiero OR general",
        "dossier_titulo": "Grupo La Fábrica",
        "dossier_resumen": "Grupo industrial con sede en Madrid. Estructura multiunidad. Sector con consolidación financiera artesanal.",
        "dolores": [
            "Consolidación financiera entre unidades.",
            "Reporting de KPIs operativos.",
            "Coordinación de compras corporativas.",
            "Visibilidad de margen por unidad."
        ],
    },
    "grupo-pim": {
        "asunto": "Zaragoza, fabricación y los lunes de planta",
        "apertura": "Vi Grupo PIM mirando fabricantes industriales con base en Zaragoza y me quedé con la operación multiplanta. En grupos así lo que más se escapa hoy no es producir, es que los lunes la dirección de operaciones gasta la primera media jornada cuadrando los partes de fin de semana de cada planta porque cada una los manda en formato distinto.",
        "pregunta": "¿Cómo estáis consolidando hoy datos entre plantas?",
        "decisor": "Director de Operaciones / Director Industrial",
        "linkedin_q": "\"Grupo PIM\" Zaragoza operaciones OR industrial",
        "dossier_titulo": "Grupo PIM",
        "dossier_resumen": "Grupo industrial con sede en Zaragoza. Operación multiplanta. Sector con automatización dispar entre planta y oficina.",
        "dolores": [
            "Consolidación de partes de planta entre centros.",
            "Reporting unificado de OEE.",
            "Coordinación entre planta y compras.",
            "Visibilidad de eficiencia por línea."
        ],
    },
    "grupo-serhos-food-service-s-l": {
        "asunto": "Distribución food service y la ruta del miércoles",
        "apertura": "Entré en Grupo Serhos mirando distribuidores food service con base en el Cantábrico y me quedé con el perfil multicliente HORECA. En este negocio lo que más fricciona hoy no es repartir, es que el routing de las furgonetas se hace a mano cada miércoles para la semana siguiente, y cualquier cliente que cambie pedido el martes obliga a recalcular tres rutas distintas a mano.",
        "pregunta": "¿Cómo estáis planificando hoy el reparto?",
        "decisor": "Director de Operaciones / Director Logístico",
        "linkedin_q": "\"Grupo Serhos\" Santander OR Cantabria operaciones",
        "dossier_titulo": "Grupo Serhos Food Service",
        "dossier_resumen": "Distribuidor food service con base en Santander. Cartera HORECA. Operación con flota propia. Sector con planificación manual.",
        "dolores": [
            "Routing dinámico ante cambios de pedido.",
            "Conciliación de albaranes y devoluciones.",
            "Gestión de stock perecedero.",
            "Comunicación con clientes HORECA en tiempo real."
        ],
    },
    "grupo-merino": {
        "asunto": "Logística madrileña y los albaranes del viernes",
        "apertura": "Vi Grupo Merino revisando operadores logísticos con base en Madrid y me quedé con la operación de transporte y almacén. En este negocio el dolor que más se repite hoy no es mover la mercancía, es que los viernes administración cierra la semana cuadrando albaranes con el TMS y los partes de los conductores, y cualquier discrepancia lleva 20 minutos de llamadas para resolverse.",
        "pregunta": "¿Cómo estáis cuadrando hoy esa información?",
        "decisor": "Director de Operaciones / Director Financiero",
        "linkedin_q": "\"Grupo Merino\" Madrid logística OR operaciones",
        "dossier_titulo": "Grupo Merino",
        "dossier_resumen": "Operador logístico con base en Madrid. Servicios de transporte y almacén. Sector con back-office operativo artesanal.",
        "dolores": [
            "Cuadre de albaranes con TMS.",
            "Trazabilidad de incidencias en ruta.",
            "Reporting de margen por cliente.",
            "Coordinación con conductores subcontratados."
        ],
    },
    "grupo-diresa-distribuidor-de-bebidas-en-valencia": {
        "asunto": "Bebidas en Valencia y el pedido del bar de la esquina",
        "apertura": "Entré en Diresa mirando distribuidores de bebidas valencianos y me quedé con la cartera de hostelería local. En distribución HORECA lo que más fricciona hoy no es servir, es que el bar de la esquina pide por WhatsApp, el restaurante por email y el hotel por EDI, y administración pasa la mañana metiendo a mano en el ERP los pedidos que llegaron de noche.",
        "pregunta": "¿Cómo estáis canalizando hoy esos pedidos?",
        "decisor": "Director Comercial / Director de Operaciones",
        "linkedin_q": "\"Diresa\" Valencia bebidas OR distribución",
        "dossier_titulo": "Grupo Diresa",
        "dossier_resumen": "Distribuidor de bebidas en Valencia. Cartera HORECA. Operación con flota propia. Sector con captura manual de pedidos.",
        "dolores": [
            "Captura unificada de pedidos multicanal.",
            "Routing y reposición HORECA.",
            "Gestión de promociones y precios por cliente.",
            "Conciliación con proveedores y marcas."
        ],
    },
    "grupo-perfecta-energia": {
        "asunto": "Instalación fotovoltaica y la visita del comercial",
        "apertura": "Vi Perfecta Energía mirando instaladoras fotovoltaicas con peso nacional y me quedé con la operación de venta a domicilio. En este negocio lo que más se escapa hoy no es vender la instalación, es que entre la visita comercial y la firma pasan 3-5 contactos manuales (estudio, propuesta, financiación, agenda) que viven en hojas distintas y cada salto pierde leads templados.",
        "pregunta": "¿Cómo estáis trazando hoy ese embudo post-visita?",
        "decisor": "Director Comercial / Director de Operaciones",
        "linkedin_q": "\"Perfecta Energía\" director comercial OR operaciones",
        "dossier_titulo": "Perfecta Energía",
        "dossier_resumen": "Instaladora fotovoltaica residencial con peso nacional. Modelo de venta directa a domicilio. Sector con back-office comercial artesanal y volúmenes altos.",
        "dolores": [
            "Embudo lead → estudio → propuesta → firma.",
            "Coordinación con financieras para aprobación.",
            "Agenda de instaladores y cuadrillas.",
            "Postventa y seguimiento de producción."
        ],
    },
    "grupo-incalexa-oficinas-centrales-grupo-incalexa": {
        "asunto": "Cáceres, instalaciones y la coordinación de cuadrillas",
        "apertura": "Entré en Incalexa mirando grupos de instalaciones y mantenimiento con base en Extremadura y me quedé con la operación multioficio. En instalaciones así lo que más fricciona hoy no es ejecutar la obra, es que la coordinación entre cuadrillas, el parte de cada operario y la facturación al cliente vive en tres sistemas distintos y la administración pierde la mañana del lunes cuadrándolo.",
        "pregunta": "¿Cómo estáis cerrando hoy el ciclo parte → factura?",
        "decisor": "Director de Operaciones / Director Financiero",
        "linkedin_q": "\"Grupo Incalexa\" Cáceres operaciones OR financiero",
        "dossier_titulo": "Grupo Incalexa",
        "dossier_resumen": "Grupo de instalaciones y mantenimiento con base en Cáceres. Operación multioficio (electricidad, climatización, mantenimiento). Sector con back-office operativo manual.",
        "dolores": [
            "Captura de partes de operario en obra.",
            "Cuadre de partes con facturación.",
            "Gestión de mantenimientos preventivos.",
            "Coordinación de cuadrillas multioficio."
        ],
    },
    "control-y-montajes-industriales-cymi-s-a": {
        "asunto": "Montajes industriales y la documentación del proyecto",
        "apertura": "Vi CYMI revisando empresas de montajes industriales con peso en Madrid y me quedé con la operación de proyecto a medida. En este negocio lo que más se escapa hoy no es el montaje, es que la documentación técnica de cada proyecto — planos, cálculos, certificados, partes de obra, CAE — vive en carpetas distintas y cuando llega la auditoría del cliente se invierten 2 días en compilar.",
        "pregunta": "¿Cómo estáis gestionando hoy esa documentación?",
        "decisor": "Director de Proyectos / Director de Calidad",
        "linkedin_q": "\"CYMI\" OR \"Control y Montajes Industriales\" Madrid director",
        "dossier_titulo": "CYMI - Control y Montajes Industriales",
        "dossier_resumen": "Empresa de montajes industriales con base en Madrid. Operación de proyecto a medida. Cartera B2B industrial. Sector con gestión documental dispersa.",
        "dolores": [
            "Gestión documental por proyecto.",
            "Cumplimiento CAE con subcontratas.",
            "Reporting de avance y certificación.",
            "Coordinación entre oficina técnica y obra."
        ],
    },
    "grupo-mibsa-mibair": {
        "asunto": "Climatización industrial y el SAT del martes",
        "apertura": "Entré en Mibsa-Mibair mirando empresas de climatización industrial en Barcelona y me quedé con el perfil instalación + SAT. En este negocio lo que más fricciona hoy no es la instalación, es que el SAT recibe avisos por teléfono, email y WhatsApp, y cada técnico va con su orden de trabajo en papel — la administración no sabe en tiempo real qué máquina está parada en qué cliente.",
        "pregunta": "¿Cómo estáis trazando hoy el ciclo aviso → técnico → resolución?",
        "decisor": "Director de SAT / Director de Operaciones",
        "linkedin_q": "\"Mibsa\" OR \"Mibair\" Barcelona SAT OR operaciones",
        "dossier_titulo": "Grupo Mibsa-Mibair",
        "dossier_resumen": "Empresa de climatización industrial con base en Barcelona. Operación instalación + SAT. Cartera B2B industrial. Sector con captura de avisos multicanal.",
        "dolores": [
            "Captura unificada de avisos de SAT.",
            "Asignación dinámica a técnicos.",
            "Trazabilidad de intervenciones y piezas.",
            "Facturación rápida post-intervención."
        ],
    },
    "grupo-ea2000-instalaciones-y-mantenimiento-en-zaragoza": {
        "asunto": "Mantenimiento industrial y el contrato anual",
        "apertura": "Vi EA2000 mirando empresas de instalaciones y mantenimiento con base en Zaragoza y me quedé con la cartera de contratos anuales. En mantenimientos así el dolor que más se repite hoy no es ejecutar, es que el calendario preventivo de cada cliente vive en un Excel y los avisos correctivos llegan por teléfono, y cuando un cliente pregunta \"¿cuántas intervenciones lleváis este año?\" tarda 30 minutos en sacarlo.",
        "pregunta": "¿Cómo estáis trazando hoy preventivo y correctivo?",
        "decisor": "Director Técnico / Director de Operaciones",
        "linkedin_q": "\"EA2000\" Zaragoza mantenimiento OR técnico",
        "dossier_titulo": "Grupo EA2000",
        "dossier_resumen": "Empresa de instalaciones y mantenimiento con base en Zaragoza. Cartera B2B con contratos anuales. Sector con planificación preventiva manual.",
        "dolores": [
            "Calendario preventivo por cliente.",
            "Captura de avisos correctivos.",
            "Reporting de SLA y consumos por contrato.",
            "Renovación y revisión de contratos."
        ],
    },
    "grupo-confremar": {
        "asunto": "Producto del mar y el albarán del lunes",
        "apertura": "Entré en Confremar mirando distribuidores de producto del mar con base en Cantabria y me quedé con la cartera HORECA + retail. En distribución de fresco lo que más se escapa hoy no es la calidad del género, es que cada lunes la administración cuadra a mano albaranes con peso, lote y caducidad de los pedidos del fin de semana, y cualquier discrepancia abre 30 minutos de llamadas con cliente y central.",
        "pregunta": "¿Cómo estáis cuadrando hoy esa información?",
        "decisor": "Director de Operaciones / Director Comercial",
        "linkedin_q": "\"Confremar\" Santander operaciones OR comercial",
        "dossier_titulo": "Grupo Confremar",
        "dossier_resumen": "Distribuidor de producto del mar con base en Santander. Cartera HORECA y retail. Operación con cadena de frío. Sector con captura de datos manual.",
        "dolores": [
            "Trazabilidad de lote, peso y caducidad.",
            "Cuadre de albaranes multicanal.",
            "Gestión de devoluciones y mermas.",
            "Cumplimiento sanitario y APPCC."
        ],
    },
    "delcom-operador-logistico-s-a": {
        "asunto": "Burgos, almacén y la entrada de mil pallets",
        "apertura": "Vi Delcom revisando operadores logísticos con base en Burgos y me quedé con la operación de almacén + transporte. En operadores así lo que más fricciona hoy no es mover, es que cuando un cliente avisa de una entrada de mil pallets para mañana, jefe de almacén, transporte y administración tienen que coordinar a mano entre tres sistemas y la respuesta al cliente sobre fecha de disposición tarda 2 horas.",
        "pregunta": "¿Cómo estáis coordinando hoy entradas grandes?",
        "decisor": "Director de Operaciones / Director Logístico",
        "linkedin_q": "\"Delcom\" Burgos operaciones OR logística",
        "dossier_titulo": "Delcom - Operador Logístico",
        "dossier_resumen": "Operador logístico con base en Burgos. Servicios de almacenamiento y transporte. Cartera B2B industrial. Sector con coordinación multisistema artesanal.",
        "dolores": [
            "Coordinación entrada/salida en almacén.",
            "Tiempo de respuesta a peticiones cliente.",
            "Trazabilidad de pallet/SKU.",
            "Reporting de ocupación de almacén."
        ],
    },
    "pln-distribucion-s-a": {
        "asunto": "Distribución en Sevilla y la conciliación de marca",
        "apertura": "Entré en PLN mirando distribuidores con base en Sevilla y me quedé con la cartera multimarca. En distribución multimarca lo que más se escapa hoy no es repartir, es que cada marca pide reporting con su formato, sus KPIs y su cadencia, y administración pasa media semana cuadrando ventas, devoluciones y promociones por marca para enviar a fabricantes.",
        "pregunta": "¿Cómo estáis automatizando hoy ese reporting a marca?",
        "decisor": "Director Comercial / Director Financiero",
        "linkedin_q": "\"PLN Distribución\" Sevilla comercial OR financiero",
        "dossier_titulo": "PLN Distribución",
        "dossier_resumen": "Distribuidor multimarca con base en Sevilla. Cartera B2B retail/HORECA. Sector con reporting manual a fabricantes.",
        "dolores": [
            "Reporting estructurado por marca.",
            "Conciliación de promociones y rappels.",
            "Gestión de devoluciones por marca.",
            "Visibilidad de margen real por SKU."
        ],
    },
}


def md_to_html(asunto: str, cuerpo_md: str) -> str:
    parrafos = [p.strip() for p in cuerpo_md.strip().split("\n\n") if p.strip()]
    body = "\n".join(f"<p>{p}</p>" for p in parrafos)
    return f"""<!DOCTYPE html>
<html><head><meta charset=\"utf-8\"><title>{asunto}</title></head>
<body style=\"font-family: -apple-system, sans-serif; max-width: 600px;\">
{body}
</body></html>"""


def main():
    pipeline = json.loads((ROOT / "data" / "pipeline.json").read_text(encoding="utf-8"))
    validados = json.loads((ROOT / "data" / f"validados-{FECHA}.json").read_text(encoding="utf-8"))
    by_slug = {}
    for v in validados:
        nombre = v.get("empresa_nombre_guess", "")
        from scripts.pipeline_utils import slugify
        by_slug[slugify(nombre)] = v

    dossiers_dir = ROOT / "dossiers" / FECHA
    dossiers_dir.mkdir(parents=True, exist_ok=True)
    outbox_dir = ROOT / "outbox" / FECHA
    outbox_dir.mkdir(parents=True, exist_ok=True)

    generados = 0
    for slug, info in LEADS.items():
        v = by_slug.get(slug, {})
        web = v.get("web", "")
        zona = v.get("zona", "")
        sector = v.get("sector", "")
        score = v.get("score", 0)
        linkedin_company = v.get("validacion", {}).get("linkedin_url", "")

        # 1) Dossier
        dossier_md = f"""# Dossier: {info['dossier_titulo']}
**Fecha:** {FECHA}
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
{info['dossier_resumen']}

- **Sector:** {sector}
- **Zona:** {zona}
- **Web:** {web}
- **LinkedIn empresa:** {linkedin_company or 'pendiente'}

## 2. Puntos de dolor (hipótesis priorizadas)
""" + "\n".join(f"{i+1}. **{d}**" for i, d in enumerate(info["dolores"])) + f"""

## 3. Contacto decisor
- Cargo a buscar: {info['decisor']}
- Búsqueda LinkedIn: `{info['linkedin_q']}`
- Email: ⚠ pendiente Apollo+Hunter enrichment

## 4. Ángulo de entrada
{info['apertura']}

## 5. Pregunta calibrada
{info['pregunta']}

## 6. Score
{score}

## 7. Próximas acciones
- Apollo+Hunter para email del decisor (ver `leadsApollo.md`).
- Identificar nombre del decisor en LinkedIn.
- Sustituir "Hola," por "Hola {{nombre}}," antes de enviar.
"""
        (dossiers_dir / f"{slug}.md").write_text(dossier_md, encoding="utf-8")

        # 2) Outbox folder
        lead_dir = outbox_dir / slug
        lead_dir.mkdir(parents=True, exist_ok=True)

        # 2a) Email T1
        cuerpo = f"""Hola,

{info['apertura']}

{info['pregunta']}

Un saludo,
Aritz"""
        email_md = f"""# Email T1 — {slug}

**Fecha:** {FECHA}
**Generado el:** {FECHA}

---

**Asunto:** {info['asunto']}

---

{cuerpo}
"""
        (lead_dir / "email-t1.md").write_text(email_md, encoding="utf-8")
        (lead_dir / "email-t1.html").write_text(md_to_html(info['asunto'], cuerpo), encoding="utf-8")

        # 2b) LinkedIn paso 1
        linkedin_md = f"""# LinkedIn Paso 1 — {slug}

**Fecha:** {FECHA}
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- {info['linkedin_q']}
- LinkedIn empresa: {linkedin_company or 'pendiente'}

Filtrar por cargo: {info['decisor']}.
"""
        (lead_dir / "linkedin-paso1.md").write_text(linkedin_md, encoding="utf-8")

        # 2c) Contacto
        contacto_md = f"""# Contacto — {info['dossier_titulo']}

**Fecha de generación:** {FECHA}

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** {info['decisor']}
- **Web:** {web}
- **Zona:** {zona}

## Canal recomendado
1. **LinkedIn (preferente)** → connection sin nota. Búsqueda: `{info['linkedin_q']}`
2. **Email (respaldo)** → pendiente Apollo+Hunter enrichment.

## Qué enviar
- LinkedIn: `linkedin-paso1.md`
- Email: `email-t1.html` cuando se consiga dirección directa. Asunto: "{info['asunto']}"

## Acciones pendientes antes de enviar
- Apollo+Hunter → email decisor.
- Identificar nombre concreto en LinkedIn.
- Sustituir "Hola," por "Hola {{nombre}},".
"""
        (lead_dir / "contacto.md").write_text(contacto_md, encoding="utf-8")

        # 3) Update pipeline
        if slug in pipeline["leads"]:
            lead = pipeline["leads"][slug]
            lead["dossier_path"] = f"dossiers/{FECHA}/{slug}.md"
            hist = lead.setdefault("historial", [])
            ya = any(ev.get("tipo") == "mensaje_generado" and ev.get("toque") == "t1"
                     and ev.get("tanda") == FECHA for ev in hist)
            if not ya:
                hist.append({
                    "tipo": "mensaje_generado",
                    "fecha": FECHA,
                    "canal": "email",
                    "toque": "t1",
                    "asunto": info["asunto"],
                    "tanda": FECHA,
                })
            lead["proxima_accion"] = {
                "tipo": "enriquecer_apollo_hunter",
                "fecha": FECHA,
                "nota": "Conseguir email decisor antes de programar borrador",
            }
        generados += 1
        print(f"  [{generados:2}/20] {slug}")

    (ROOT / "data" / "pipeline.json").write_text(
        json.dumps(pipeline, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n=== Generados {generados} dossiers + emails T1 + LinkedIn + contacto ===")
    print(f"Dossiers: dossiers/{FECHA}/")
    print(f"Outbox:   outbox/{FECHA}/")
    print("\nSiguiente paso: Apollo+Hunter enrichment para emails de decisores.")


if __name__ == "__main__":
    main()
