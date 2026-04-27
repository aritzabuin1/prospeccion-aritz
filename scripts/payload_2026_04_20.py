# -*- coding: utf-8 -*-
"""
Payload hand-crafted para la tanda 2026-04-20 (40 leads).
Cada entrada = { dossier, email_asunto, email_cuerpo_md,
                  email_cuerpo_html_parrafos, linkedin_md, contacto_md }.
Orden: martes 21, miércoles 22, jueves 23, viernes 24 (10/día).
"""

PAYLOAD = {}


def add(slug, dossier, asunto, cuerpo, li_md, contacto):
    """cuerpo: lista de párrafos en texto plano."""
    cuerpo_md = "\n\n".join(cuerpo)
    PAYLOAD[slug] = {
        "dossier": dossier,
        "email_asunto": asunto,
        "email_cuerpo_md": cuerpo_md,
        "email_cuerpo_html_parrafos": cuerpo,
        "linkedin_md": li_md,
        "contacto_md": contacto,
    }


# ==============================================================
# MARTES 2026-04-21 — 10 LEADS PRIORITARIOS
# ==============================================================

# -- 1. IQE — Industrias Químicas del Ebro (Zaragoza, industria)
add(
    "iqe-industrias-quimicas-del-ebro-s-a",
    dossier="""# Dossier: IQE — Industrias Químicas del Ebro S.A.
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
IQE (Industrias Químicas del Ebro) es un grupo químico zaragozano con sede en el Polígono Malpica y presencia internacional. Fabrica silicatos y derivados para detergencia, cementos, refractarios y aguas. Estructura de grupo (Grupo IQE) con varias plantas productivas y red comercial multipaís. Perfil de industria química media-grande con procesos continuos, cadena documental intensa (fichas de seguridad, ADR, REACH, CLP, certificados de calidad por lote) y gestión técnica-comercial con clientes B2B exigentes.

- **Sector:** Industria química (silicatos, especialidades)
- **Tamaño:** Grupo industrial, múltiples plantas, exportación internacional
- **Sede:** Polígono Malpica, Zaragoza

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca comercial | IQE / Grupo IQE |
| Actividad | Fabricación de silicatos sódicos y derivados |
| Sede | Calle D, Polígono Malpica 97, 50016 Zaragoza |
| Web | iqe.es |
| Mercado | España + exportación internacional |

## 3. Madurez digital
- Web corporativa multilingüe con catálogo de productos y fichas técnicas descargables. Típico de químico industrial: orientado a prescriptor técnico, no al buyer journey digital.
- Sin evidencia pública de transformación digital profunda. Lo habitual en este tipo de planta química: ERP (SAP/Navision) para producción y expediciones, LIMS de laboratorio, Excel para todo lo que queda fuera.
- Exigencia regulatoria fuerte (REACH, CLP, ADR) genera mucho trabajo documental repetitivo difícil de escalar con el equipo técnico actual.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Fichas de seguridad multilingües y su mantenimiento.** Cada cambio regulatorio o de formulación obliga a revisar 15-30 FDS por producto/idioma. Orquestable con IA + validación humana.
2. **Consultas técnico-comerciales entrantes.** Prescriptores y clientes preguntan por compatibilidades, densidades, certificaciones, alternativas. Base de conocimiento + asistente consulta-respuesta descarga al equipo técnico.
3. **Gestión documental de exportación.** Certificados de origen, de análisis, CMR, ADR. Mucho PDF entre ERP, laboratorio y expediciones.
4. **Reporting consolidado de planta.** Producción, rendimientos, calidad por lote, margen por producto suelen vivir en 2-3 sistemas + hojas de controller.

## 5. Contacto decisor
- No hay decisor identificado con nombre en fuentes públicas. **Buscar en LinkedIn:**
  - `site:linkedin.com/in "IQE" "Zaragoza" (Director OR CEO OR Operaciones)`
  - Filtros Sales Nav: empresa "IQE" / "Industrias Químicas del Ebro", zona Zaragoza, seniority director+.
- Perfiles prioritarios: Director General, Director de Operaciones/Producción, Director Técnico/Calidad.
- Canal primario: LinkedIn al Director de Operaciones o Técnico.
- Canal secundario: formulario/centralita web iqe.es.

## 6. Ángulo de entrada
Reconocimiento del posicionamiento (químico zaragozano con tracción internacional) + hipótesis específica sobre mantenimiento documental regulatorio + pregunta calibrada de cómo lo resuelven hoy. Sin pitch, sin reunión.

## 7. Score
Score inicial: 70. Sector encaja (industria con procesos repetitivos documentales), tamaño medio-grande, decisor accesible por LinkedIn pero no identificado. Requiere búsqueda previa antes de envío.
""",
    asunto="Fichas de seguridad y los viernes",
    cuerpo=[
        "Hola,",
        "Miré la web de IQE buscando fabricantes de silicatos con exportación activa y me paré en el catálogo: varias familias de producto, fichas técnicas por mercado, presencia fuera de España. Tengo la sensación de que en un catálogo así cada cambio regulatorio o de formulación obliga a tocar quince o veinte documentos por idioma, y eso suele caer sobre una o dos personas del equipo técnico que ya tienen bastante con la planta.",
        "¿Cómo estáis llevando hoy el mantenimiento de las fichas de seguridad cuando cambia algo?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — iqe-industrias-quimicas-del-ebro-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota (plan básico limita notas de conexión).

Perfil del decisor: identificar previamente. Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Industrias%20Quimicas%20del%20Ebro%22%20Zaragoza&origin=GLOBAL_SEARCH_HEADER
- Filtrar por cargo: "Director", "CEO", "Operaciones", "Técnico".

Empresa (si existe): buscar "IQE" / "Industrias Químicas del Ebro" en linkedin.com/company/.
""",
    contacto="""# Contacto — IQE (Industrias Químicas del Ebro)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director de Operaciones / Director Técnico (primario) o Director General (secundario)
- **Notas:** Sede Polígono Malpica, Zaragoza. Grupo químico con exportación. Perfil técnico-industrial.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda: "Industrias Químicas del Ebro" + Zaragoza + filtro director/operaciones/técnico.
2. **Email (respaldo)** → sin email público. Ir vía formulario iqe.es o centralita tras identificar al decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota) al decisor identificado.
- Email: `email-t1.html` una vez se consiga dirección directa. Asunto: "Fichas de seguridad y los viernes".

## Acciones pendientes del usuario antes de enviar
- Identificar en LinkedIn al Director de Operaciones, Director Técnico o Director General.
- Conseguir email directo (via LinkedIn o centralita) antes de usar `email-t1.html`.
- Sustituir "Hola," por "Hola {nombre}," en ambos archivos de email al identificar al decisor.
""",
)

# -- 2. Transportes Gar&Cía (Sevilla, logística)
add(
    "transportes-gar-cia-s-a",
    dossier="""# Dossier: Transportes Gar&Cía S.A.
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Gar & Cía es una operadora de logística integral con sede en Alcalá de Guadaíra (Sevilla), enfocada a cargadores industriales del sur peninsular. Flota propia + subcontratada, almacenaje y servicios de valor añadido. Perfil de gran cuenta regional con operativa de tráfico intensa y presión creciente por ETAs, trazabilidad y reporting a cliente.

- **Sector:** Logística integral y transporte por carretera
- **Tamaño:** Operador regional medio-grande con base en Alcalá de Guadaíra
- **Sede:** Ctra. Sevilla-Utrera km 8,3

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Gar & Cía Logística Integral |
| Web | garycia.es |
| Actividad | Transporte carretera, almacén, logística integral |
| Zona | Andalucía occidental + nacional |

## 3. Madurez digital
- Web corporativa con pestaña de servicios y contacto. Orientada a cargador, no a transaccional.
- Típico del sector: TMS (Acotral, Transporteca o similar) + ERP financiero + Excel para lo que no entra. Sin evidencia pública de dashboards operativos consolidados ni agentes.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Coordinación con subcontratistas y confirmación de disponibilidad.** Llamadas y correos para cada asignación, sin trazabilidad estructurada.
2. **Atención al cargador sobre ETAs y estado de carga.** Preguntas repetitivas que saturan al equipo de tráfico.
3. **Reporting operativo por cliente / lane / subcontratista.** Margen fragmentado entre TMS y hojas del controller.
4. **Tramitación documental: CMR, albaranes, incidencias.** Papel y PDF.

## 5. Contacto decisor
- No hay decisor con nombre identificado. **Buscar en LinkedIn:**
  - `"Transportes Gar" OR "Gar & Cía" Sevilla (Director OR Tráfico OR Operaciones)`
- Perfiles prioritarios: Director General / Director de Operaciones / Director de Tráfico.
- Canal primario LinkedIn, secundario email tras identificar.

## 6. Ángulo de entrada
Reconocimiento del rol como operador integral andaluz + label sobre dolor de coordinación con subcontratistas + pregunta calibrada. Sin caso, sin reunión.

## 7. Score
70. Sector encaja 1:1, tamaño regional, decisor por identificar.
""",
    asunto="El lunes a las siete y media",
    cuerpo=[
        "Hola,",
        "Entré en Gar & Cía mirando operadores de logística integral en el sur y me paró el perfil: transporte propio, almacén y cargadores industriales andaluces. Parece como si en una operativa de ese tamaño el cuello de botella de verdad no esté en mover camiones, sino en que media mañana del lunes se va en confirmar por teléfono y WhatsApp qué subcontratista toma qué ruta y a qué precio.",
        "¿Cómo lo estáis resolviendo hoy cuando entra un pico de volumen?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — transportes-gar-cia-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Perfil del decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Gar%20%26%20C%C3%ADa%22%20Sevilla&origin=GLOBAL_SEARCH_HEADER
- Filtros: Director, Operaciones, Tráfico, Sevilla.
""",
    contacto="""# Contacto — Transportes Gar & Cía S.A.

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director de Operaciones / Director de Tráfico (primario) o Director General (secundario)
- **Notas:** Sede Alcalá de Guadaíra (Sevilla). Operador integral andaluz.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda: "Gar & Cía" / "Transportes Gar" + Sevilla + director/operaciones/tráfico.
2. **Email (respaldo)** → sin email público. Formulario garycia.es o centralita tras identificar.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al tener dirección directa. Asunto: "El lunes a las siete y media".

## Acciones pendientes del usuario antes de enviar
- Identificar al Director de Operaciones / Tráfico en LinkedIn.
- Conseguir email directo antes de usar `email-t1.html`.
- Sustituir "Hola," por "Hola {nombre}," al identificar al decisor.
""",
)

# -- 3. Bekker Logística (Alicante, logística internacional)
add(
    "bekker-logistica-transporte-internacional",
    dossier="""# Dossier: Bekker Logística — Transporte Internacional
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Bekker Logística es un freight forwarder internacional con sede en Alicante que opera puerta a puerta entre Portugal, España, Reino Unido, Alemania y Austria por aire, mar y carretera. Perfil típico de transitario con operativa multiidioma, mucha documentación aduanera y relación estrecha con cargadores europeos.

- **Sector:** Freight forwarding internacional
- **Tamaño:** Mediana cuenta, operativa pan-europea
- **Sede:** Avinguda Benito Pérez Galdós, 54, Alicante

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | bekkerlogistica.com |
| Modos | Aéreo, marítimo, carretera |
| Corredores | PT / ES / UK / DE / AT |
| Idiomas web | Multilingüe (ES/EN) |

## 3. Madurez digital
- Web bilingüe orientada a cargadores. Descripción clara de rutas y modos.
- Sector con uso habitual de CargoWise o sistemas TMS transitarios + muchos correos externos con aduanas, navieras y agentes de destino. Dolor documental clásico.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Tramitación documental aduanera post-Brexit.** UK requiere documentación específica por cada envío: costoso en horas de operadores.
2. **Gestión de correspondencia multilingüe con agentes extranjeros.** Triangulación de información entre cliente, agente origen, agente destino.
3. **Cotización de tramos puerta-puerta multimodal.** Mucho copy/paste entre tarifas de navieras y plantillas.
4. **Visibilidad de envío a cargador en tiempo real.** Clientes piden estado: respuesta manual.

## 5. Contacto decisor
- No identificado. **Buscar en LinkedIn:**
  - `"Bekker Logistica" OR "Bekker Logistics" Alicante (Director OR Manager)`
- Perfiles: Director General, Responsable de Operaciones, Responsable Comercial.

## 6. Ángulo de entrada
Reconocimiento del corredor UK/DE/PT + label sobre dolor post-Brexit documental + pregunta calibrada.

## 7. Score
70. Sector encaja, cuenta pan-europea.
""",
    asunto="Un envío a Manchester post-Brexit",
    cuerpo=[
        "Hola,",
        "Vi Bekker mirando transitarios peninsulares con tráfico a Reino Unido y me quedé con el mapa de rutas: PT-ES-UK-DE-AT por aire, mar y carretera. Me imagino que desde 2021 cada envío que cruza a UK abre un pequeño bloque de papeles que antes no existía, y que eso no lo absorbe ni un TMS ni un cliente contento, lo absorbe el operador a base de horas.",
        "¿Qué parte de esa tramitación es la que más tiempo se os come hoy?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — bekker-logistica-transporte-internacional

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente de identificar.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Bekker%20Logistica%22&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "Bekker" + Alicante + Director/Manager.
""",
    contacto="""# Contacto — Bekker Logística

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Responsable de Operaciones
- **Notas:** Freight forwarder pan-europeo. Sede Alicante. Foco UK/DE/PT.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Bekker Logistica" en linkedin.com/search.
2. **Email (respaldo)** → sin email público. Formulario bekkerlogistica.com tras identificar al decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un envío a Manchester post-Brexit".

## Acciones pendientes del usuario antes de enviar
- Identificar al decisor en LinkedIn.
- Conseguir email directo antes de enviar email.
- Sustituir "Hola," por "Hola {nombre}," cuando se identifique.
""",
)

# -- 4. Clínica Euskalduna / Grupo Muguerza-Franco (Bilbao, salud)
add(
    "medicina-estetica-y-obesidad-clinica-euskalduna-grupo-muguerza-franco",
    dossier="""# Dossier: Clínica Euskalduna — Grupo Muguerza-Franco
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Muguerza-Franco es un grupo sanitario privado bilbaíno con base en la calle Euskalduna (Abando). Foco en medicina estética, tratamiento de obesidad y cirugía asociada. Perfil de clínica privada premium con captación fuertemente digital, pacientes recurrentes y gestión clínica con historia, consentimientos y seguimiento post-tratamiento.

- **Sector:** Salud privada (estética + obesidad + cirugía)
- **Tamaño:** Clínica privada grupo, equipo médico multidisciplinar
- **Sede:** C. Euskalduna, 10, Abando, Bilbao

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | muguerza-franco.com |
| Servicios | Medicina estética, nutrición, cirugía de obesidad |
| Zona | Bilbao (Abando) |

## 3. Madurez digital
- Web propia con catálogo de tratamientos, formulario de contacto y típicamente WhatsApp Business. Marketing digital activo (ADS, SEO local).
- Historia clínica en software de clínicas (Doctoralia/Clinic Cloud/Dentalink o propietario). Consentimientos en papel + PDF firmado.
- Volumen importante de leads entrantes por web/Instagram que exigen respuesta rápida.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Cualificación y respuesta de leads entrantes 24/7.** Un lead que llega el viernes por la noche pelea con el lunes. Asistente IA + agenda es palanca directa.
2. **Gestión de consentimientos informados y documentación pre-tratamiento.** Volumen alto, plantillas personalizadas.
3. **Seguimiento post-tratamiento.** Recordatorios, revisiones, medición de resultados.
4. **Reporting multicentro y por médico.** Producción, conversión lead→consulta, retención.

## 5. Contacto decisor
- Estructura "Muguerza-Franco": probables socios fundadores con nombre público. **Buscar en LinkedIn:**
  - `"Clínica Euskalduna" OR "Muguerza" OR "Franco" Bilbao`
  - Google: `"muguerza-franco.com" doctor director`
- Perfiles: Director Médico / Director General / Responsable de Marketing.

## 6. Ángulo de entrada
Reconocimiento del posicionamiento premium bilbaíno + label sobre ventana de respuesta a leads + pregunta calibrada.

## 7. Score
70. Sector salud estética encaja (alto volumen de leads, respuesta crítica).
""",
    asunto="Un lead un sábado a las nueve",
    cuerpo=[
        "Hola,",
        "Entré en Clínica Euskalduna mirando clínicas privadas de estética y obesidad en Bilbao y me quedé con el posicionamiento y la presencia en Abando. Parece como si en un negocio donde el paciente decide entre dos o tres clínicas en una misma tarde, lo que marca la diferencia no sean los tratamientos en sí sino quién responde el sábado a las nueve con una respuesta útil y un hueco claro de agenda.",
        "¿Cómo gestionáis hoy los leads que entran fuera del horario de consulta?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — medicina-estetica-y-obesidad-clinica-euskalduna-grupo-muguerza-franco

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente de identificar.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Cl%C3%ADnica%20Euskalduna%22%20Bilbao&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "Muguerza" OR "Franco" Bilbao + filtro director/médico.
""",
    contacto="""# Contacto — Clínica Euskalduna (Grupo Muguerza-Franco)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director Médico / Director General / Responsable Marketing
- **Notas:** Clínica privada premium. Sede Abando, Bilbao. Marca familiar (Muguerza-Franco).

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Clínica Euskalduna" + Bilbao.
2. **Email (respaldo)** → sin email público. Formulario muguerza-franco.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un lead un sábado a las nueve".

## Acciones pendientes del usuario antes de enviar
- Identificar en LinkedIn al Dr. Muguerza o Dr. Franco (fundadores probables) o responsable de marketing.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 5. Grupo LATERAL (Madrid, hostelería)
add(
    "grupo-de-restauracion-lateral-s-l",
    dossier="""# Dossier: Grupo Lateral — Restauración
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Lateral es una cadena de restaurantes de referencia en Madrid con varias ubicaciones en zonas premium (Castellana, Salamanca, Chamartín). Concepto de tapa moderna, equipo consolidado, marca reconocible. Perfil de grupo de restauración multiubicación con volúmenes altos de reservas, rotación de mesa intensa y operativa que depende fuertemente de la sala y de la comunicación entre locales.

- **Sector:** Hostelería / grupo de restauración multiubicación
- **Tamaño:** Grupo multimarca/multilocal Madrid
- **Sede:** C. Núñez Morgado, 6, Chamartín, Madrid

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | LATERAL Restaurants |
| Web | lateral.com |
| Ubicaciones | Varios locales en Madrid |

## 3. Madurez digital
- Web corporativa con reservas integradas (ElTenedor/Cover o propio). Instagram activo.
- Sistema POS estándar del sector (Agora, Ágora, Revo o similar). Reservas online, probablemente CoverManager.
- Dolor típico: consolidación diaria por local, previsión de demanda, coordinación de compras y escandallos.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Reporting diario consolidado por local.** Venta, ticket medio, rotación, covers. Suele llegar tarde y fragmentado.
2. **Respuesta a reservas y comentarios fuera de horario.** WhatsApp + redes + email + TripAdvisor + Google reviews.
3. **Previsión de demanda y escandallos.** Ajuste de compras según fecha/evento.
4. **Formación y onboarding de sala.** Manual operativo + consulta rápida para el turno.

## 5. Contacto decisor
- Marca conocida, probable fundador visible. **Buscar en LinkedIn:**
  - `"Grupo Lateral" OR "Lateral Restaurants" Madrid`
- Perfiles: Director General / Director de Operaciones / Director de Marketing.

## 6. Ángulo de entrada
Reconocimiento del concepto Lateral + label sobre reporting consolidado por local + pregunta calibrada.

## 7. Score
70. Hostelería multilocal encaja.
""",
    asunto="El cierre de caja de los lunes",
    cuerpo=[
        "Hola,",
        "Entré en Lateral mirando grupos de restauración madrileños con varios locales y me quedé con el concepto y la red de sala en la zona norte. Suena a que en un grupo así lo que no escala cómodamente es tener el lunes a primera hora un cuadro limpio de qué pasó ayer en cada local, con covers, ticket medio y rotación, sin tener que perseguir a tres encargados por WhatsApp.",
        "¿Cómo se consolida hoy la foto del fin de semana entre locales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-de-restauracion-lateral-s-l

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Lateral%22%20Madrid&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "Lateral Restaurants" Madrid + filtro director/operaciones.
""",
    contacto="""# Contacto — Grupo Lateral (Restauración)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director de Operaciones
- **Notas:** Grupo de restauración madrileño multilocal. Sede Chamartín.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Lateral" OR "Lateral Restaurants" Madrid.
2. **Email (respaldo)** → sin email público. Formulario lateral.com o contacto directo tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El cierre de caja de los lunes".

## Acciones pendientes del usuario antes de enviar
- Identificar al Director General o Director de Operaciones del grupo.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 6. Pantea Group (Barcelona, hostelería)
add(
    "pantea-group-grupo-de-restauracion-en-barcelona",
    dossier="""# Dossier: Pantea Group — Restauración Barcelona
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Pantea Group es un grupo de restauración barcelonés con base en Sant Martí. Operativa multilocal típica: varios conceptos, equipo de sala por unidad, marketing digital y reservas online. Perfil operativo similar a grupos como Sagardi o Grup Andilana a escala menor: margen apretado, rotación intensa, decisión distribuida entre sala y dirección.

- **Sector:** Hostelería / grupo de restauración
- **Tamaño:** Multilocal Barcelona
- **Sede:** C. Ramon Turró, 186, Sant Martí, Barcelona

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Pantea Group |
| Web | panteagroup.es |
| Zona | Barcelona |

## 3. Madurez digital
- Web propia con landing corporativa. Poca transaccionalidad visible. Reservas probablemente CoverManager/TheFork.
- POS estándar + Excel para consolidación + WhatsApp grupo directivo.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Respuesta a reservas multicanal.** Gmail + web + WhatsApp + redes. Volumen que no escala.
2. **Reporting diario consolidado entre locales.** Covers, ticket medio, margen por local.
3. **Gestión de reseñas y reputación online.** Google + TripAdvisor + TheFork sin respuesta estructurada.
4. **Onboarding y formación de sala.** Rotación del sector.

## 5. Contacto decisor
- No identificado. **Buscar en LinkedIn:**
  - `"Pantea Group" Barcelona`
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del grupo + label sobre respuesta a reservas multicanal + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Reservas por tres canales a la vez",
    cuerpo=[
        "Hola,",
        "Miré Pantea Group buscando grupos de restauración activos en Barcelona y me paró el perfil multilocal en Sant Martí. Me da la impresión de que en un grupo con varios conceptos la fricción ya no está en la cocina sino en la mesa de reservas: Gmail de un local, CoverManager de otro, WhatsApp del encargado, DMs de Instagram, y al final el cliente no sabe cuál es el canal bueno y el equipo responde tres veces el mismo mensaje.",
        "¿Cómo lo estáis unificando hoy entre locales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — pantea-group-grupo-de-restauracion-en-barcelona

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Pantea%20Group%22%20Barcelona&origin=GLOBAL_SEARCH_HEADER
- Empresa: buscar "Pantea Group" en linkedin.com/company/.
""",
    contacto="""# Contacto — Pantea Group

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo restauración Barcelona. Sede Sant Martí.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Pantea Group" Barcelona.
2. **Email (respaldo)** → sin email público. Formulario panteagroup.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Reservas por tres canales a la vez".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 7. Grupo GMI (Sevilla, hostelería) — tiene LinkedIn empresa
add(
    "grupo-gmi",
    dossier="""# Dossier: Grupo GMI — Restauración Sevilla
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo GMI es un grupo hostelero sevillano con sede en el casco histórico (García de Vinuesa). Gestiona varios restaurantes en el centro de Sevilla, zona turística de alta afluencia. Tiene LinkedIn corporativo activo (es.linkedin.com/company/grupogmi), lo que facilita identificar al decisor.

- **Sector:** Hostelería / grupo de restauración turística
- **Tamaño:** Multilocal Sevilla centro
- **Sede:** García de Vinuesa 22, Casco Antiguo, Sevilla

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Grupo GMI |
| Web | grupogmi.eu |
| LinkedIn empresa | es.linkedin.com/company/grupogmi |

## 3. Madurez digital
- Web corporativa. Presencia LinkedIn empresa, algo raro en hostelería sevillana: señal positiva de madurez.
- Operativa multilocal en casco histórico: alta rotación turística, clientela internacional, fuerte dependencia de Google y TripAdvisor.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Atención multilingüe a cliente turista.** Reservas y preguntas en inglés, francés, italiano por varios canales.
2. **Gestión de reseñas.** Google + TripAdvisor son el principal canal de captación.
3. **Reporting multilocal.** Consolidación de covers y ticket medio.
4. **Gestión de compras y escandallos.** Volatilidad de producto en zona turística.

## 5. Contacto decisor
- LinkedIn empresa activo: entrar en la página y ver "Empleados" para identificar directivos.
- Buscar: `"Grupo GMI" Sevilla` en people search.
- Perfiles: CEO/fundador, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del posicionamiento en casco antiguo + label sobre atención multilingüe a turista + pregunta calibrada.

## 7. Score
70. Accesibilidad algo mejor por LinkedIn empresa.
""",
    asunto="Un francés en la puerta a las tres",
    cuerpo=[
        "Hola,",
        "Entré en Grupo GMI buscando grupos hosteleros activos en el casco de Sevilla y me paré al ver la presencia en LinkedIn corporativo, cosa poco común en el sector. Tengo la sensación de que con varios locales en la zona turística lo que más horas consume hoy no es la cocina, es que a las tres de la tarde entran por mensaje directo y por reseña preguntas en inglés, francés e italiano a las que alguien de sala tiene que ir contestando entre servicios.",
        "¿Cómo estáis organizando hoy esa atención multilingüe entre locales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-gmi

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota.

Empresa: https://es.linkedin.com/company/grupogmi (entrar en "Empleados" y filtrar por director/CEO/operaciones).

Perfil del decisor: pendiente (identificar desde la página de empresa).

Búsqueda sugerida de personas:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20GMI%22%20Sevilla&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo GMI (Restauración Sevilla)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** CEO/fundador / Director de Operaciones
- **Notas:** Grupo hostelero Sevilla casco antiguo. Tiene LinkedIn empresa activo.

## Canal recomendado
1. **LinkedIn (preferente)** → ir a https://es.linkedin.com/company/grupogmi → sección Empleados → filtrar por seniority director.
2. **Email (respaldo)** → sin email público. Formulario grupogmi.eu tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota) al decisor desde la página de empresa.
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un francés en la puerta a las tres".

## Acciones pendientes del usuario antes de enviar
- Entrar en la página de empresa en LinkedIn y localizar decisor (Empleados > filtrar Director).
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 8. Grupo Amida (Palma, hostelería/catering lujo)
add(
    "grupo-amida",
    dossier="""# Dossier: Grupo Amida — Catering de Lujo Mallorca
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Amida es un operador de catering de lujo y organización de eventos en Mallorca con sede en Palma. Perfil premium: bodas, eventos corporativos internacionales, clientela HNWI y agencias de wedding planning europeas. Estacionalidad marcada (temporada alta mayo-octubre), coordinación logística intensa y exigencia de personalización por evento.

- **Sector:** Catering premium / organización de eventos
- **Tamaño:** Operador premium regional, cliente internacional
- **Sede:** Polígono Son Castelló, Palma

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Grupo Amida |
| Web | grupoamida.com |
| Servicios | Catering lujo, eventos, bodas |
| Zona | Mallorca (servicio internacional) |

## 3. Madurez digital
- Web propia con portfolio de eventos. Marketing digital orientado a wedding planners y agencias.
- Sector clásico: mucho email con cliente final y agencia, Excel de presupuestación, pizarra de planificación de equipo.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Presupuestación detallada por evento.** Mucho copy/paste, validaciones internas, versiones con cliente.
2. **Atención multilingüe a cliente europeo.** Inglés, alemán principalmente.
3. **Coordinación logística día D.** Timing, proveedores, equipo de sala.
4. **Reporting por evento / temporada.** Margen real por tipología.

## 5. Contacto decisor
- No identificado. **Buscar en LinkedIn:**
  - `"Grupo Amida" Mallorca`
- Perfiles: fundador/CEO, Directora de Eventos.

## 6. Ángulo de entrada
Reconocimiento del segmento premium + label sobre presupuestación por evento + pregunta calibrada.

## 7. Score
70. Estacionalidad + cliente exigente = margen claro para IA en preparación de propuestas.
""",
    asunto="Un presupuesto de 180 comensales en alemán",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Amida mirando operadores de catering premium en Mallorca y me quedé con el perfil: bodas y eventos corporativos con clientela internacional. Parece como si la fricción de verdad en una temporada alta no esté en servir el evento, sino en que cada petición seria entra en inglés o alemán pidiendo un presupuesto detallado, y eso hoy se responde a mano mirando Excel de costes, menús anteriores y la agenda del equipo.",
        "¿Cómo estáis organizando esas primeras respuestas en temporada alta?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-amida

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Amida%22%20Mallorca&origin=GLOBAL_SEARCH_HEADER
- Empresa: buscar "Grupo Amida" en linkedin.com/company/.
""",
    contacto="""# Contacto — Grupo Amida (Catering Lujo Mallorca)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Directora de Eventos
- **Notas:** Catering lujo Mallorca. Clientela internacional. Estacionalidad fuerte.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Amida" Mallorca.
2. **Email (respaldo)** → sin email público. Formulario grupoamida.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un presupuesto de 180 comensales en alemán".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 9. Autodisa / Grupo Palacios (Valencia, automoción)
add(
    "autodisa-concesionario-peugeot-grupo-palacios-automocion",
    dossier="""# Dossier: Grupo Palacios Automoción (Autodisa Peugeot)
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Palacios es un grupo de concesionarios valenciano con varias enseñas y puntos de venta. Autodisa es su concesión oficial Peugeot en Valencia. Perfil de grupo automoción media-grande con venta nueva, VO, posventa y financiación. Sector con digitalización dispar: fuerte en marketing, débil en operativa interna.

- **Sector:** Automoción / concesionarios
- **Tamaño:** Grupo multimarca Valencia
- **Sede:** Camins al Grau, Valencia

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Grupo Palacios / Autodisa Peugeot |
| Web | grupopalacios.es |
| Marcas gestionadas | Peugeot (Autodisa) + otras (ver web) |

## 3. Madurez digital
- Web corporativa moderna con stock de nuevo y VO. Integración con portales (Coches.net, Autocasion).
- DMS estándar del sector (DealerSocket/CDK/ICDP). Sector con mucho uso de WhatsApp y llamada; poca automatización de seguimiento comercial.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Seguimiento a lead de showroom y web.** Leads que pasan por el concesionario y no se cierra el loop hasta semana siguiente.
2. **Preparación de entrega y documentación.** Contrato, matriculación, financiera, seguros.
3. **Cita de taller y recordatorios.** Volumen alto, caída en posventa si no hay reactivación.
4. **Reporting de stock / ratio de conversión por comercial.**

## 5. Contacto decisor
- Grupo familiar "Palacios". **Buscar en LinkedIn:**
  - `"Grupo Palacios" OR "Autodisa" Valencia`
- Perfiles: CEO/director general, Director Comercial, Director de Posventa.

## 6. Ángulo de entrada
Reconocimiento del grupo + label sobre seguimiento comercial post-showroom + pregunta calibrada.

## 7. Score
70.
""",
    asunto="El lead que entró el sábado",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Palacios buscando concesionarios valencianos con varias marcas y me quedé con el perfil de Autodisa Peugeot en Camins al Grau. Tengo la sensación de que en un grupo así lo que más se escapa hoy no es la venta en showroom, es que el lead que entró el sábado por la web pidiendo un VO concreto compite el lunes con las llamadas, las citas de taller y tres leads más nuevos, y cuando se responde ya ha mirado otros dos concesionarios.",
        "¿Cómo lo estáis resolviendo hoy entre comerciales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — autodisa-concesionario-peugeot-grupo-palacios-automocion

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Palacios%22%20Valencia%20automoci%C3%B3n&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "Autodisa" OR "Palacios" Valencia + filtro director comercial/general.
""",
    contacto="""# Contacto — Grupo Palacios (Autodisa Peugeot)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Comercial
- **Notas:** Grupo automoción Valencia. Marca familiar Palacios. Peugeot es Autodisa.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Palacios" Valencia automoción.
2. **Email (respaldo)** → sin email público. Formulario grupopalacios.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El lead que entró el sábado".

## Acciones pendientes del usuario antes de enviar
- Identificar al Director General o Comercial del grupo.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 10. MG Grupo Nieto Málaga (automoción)
add(
    "mg-grupo-nieto-malaga",
    dossier="""# Dossier: MG Grupo Nieto Málaga
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Nieto opera la concesión oficial MG Motor en Málaga y Marbella. Marca en fuerte expansión en España (crecimiento importante 2023-2024), perfil de comprador con alto componente electrificado y urbano. Concesionario medio regional con presencia en dos ciudades de la Costa del Sol.

- **Sector:** Automoción / concesionario MG
- **Tamaño:** Mediano regional (Málaga + Marbella)
- **Sede:** Av. José Ortega y Gasset, Málaga

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | MG Grupo Nieto |
| Web | mggruponieto.com |
| Marcas | MG Motor |
| Puntos de venta | Málaga + Marbella |

## 3. Madurez digital
- Web con stock y configurador. Marketing digital enfocado a un comprador tech/urbano.
- MG es marca en crecimiento acelerado: volumen de leads entrantes superior a la media del sector.

## 4. Puntos de dolor (hipótesis priorizadas)
1. **Gestión de lead de web/ADS.** Volumen alto (MG capta mucho online), respuesta manual no escala.
2. **Preparación de test drive y entrega.** Documentación, agenda, ayudas electrificación.
3. **Coordinación Málaga-Marbella.** Stock compartido, clientes que ven online y quieren en otro punto.
4. **Posventa y revisiones.** Marca con primer ciclo de mantenimientos llegando en 2025-2026.

## 5. Contacto decisor
- Grupo familiar Nieto. **Buscar en LinkedIn:**
  - `"Grupo Nieto" MG Málaga`
- Perfiles: Director General, Gerente comercial.

## 6. Ángulo de entrada
Reconocimiento del crecimiento de MG y la red dual Málaga-Marbella + label sobre volumen de leads entrantes + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un MG4 en Málaga o en Marbella",
    cuerpo=[
        "Hola,",
        "Vi MG Grupo Nieto mirando concesionarios de marcas en crecimiento en la Costa del Sol y me paró la red dual Málaga-Marbella. Me imagino que con el volumen de tráfico que genera MG online el problema ahora ya no es atraer leads, es que la persona que pide un MG4 el viernes por la noche recibe una respuesta útil el sábado y, además, que esa respuesta coordine stock entre los dos puntos sin depender de quien esté ese día.",
        "¿Cómo se está gestionando hoy esa ventana entre lead y primera respuesta?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — mg-grupo-nieto-malaga

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Nieto%22%20MG%20M%C3%A1laga&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "MG Málaga" "Nieto" + filtro director.
""",
    contacto="""# Contacto — MG Grupo Nieto Málaga

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Gerente comercial
- **Notas:** Concesión MG Málaga + Marbella. Marca Nieto familiar.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Nieto" MG Málaga.
2. **Email (respaldo)** → sin email público. Formulario mggruponieto.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un MG4 en Málaga o en Marbella".

## Acciones pendientes del usuario antes de enviar
- Identificar al Director General del grupo Nieto.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)
