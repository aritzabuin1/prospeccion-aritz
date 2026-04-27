# -*- coding: utf-8 -*-
"""Miércoles 2026-04-22 — 10 leads."""

PAYLOAD = {}


def add(slug, dossier, asunto, cuerpo, li_md, contacto):
    cuerpo_md = "\n\n".join(cuerpo)
    PAYLOAD[slug] = {
        "dossier": dossier,
        "email_asunto": asunto,
        "email_cuerpo_md": cuerpo_md,
        "email_cuerpo_html_parrafos": cuerpo,
        "linkedin_md": li_md,
        "contacto_md": contacto,
    }


# -- 1. Grupo Grávalos (Zaragoza, industria)
add(
    "grupo-gravalos",
    dossier="""# Dossier: Grupo Grávalos
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Grávalos es una empresa industrial zaragozana con sede en el Polígono La Noria (El Burgo de Ebro). Actividad de fabricación y servicios industriales, con presencia consolidada en Aragón. Perfil clásico de industria auxiliar aragonesa con operativa de planta y cliente B2B industrial.

- **Sector:** Industria / fabricación
- **Tamaño:** Grupo industrial regional
- **Sede:** Polígono La Noria, El Burgo de Ebro (Zaragoza)

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | gravalos-sa.com |
| Zona | Aragón |

## 3. Madurez digital
- Web corporativa informativa. Sin transaccional aparente.
- Sector industrial tradicional: ERP + Excel + email. Reporting fragmentado, gestión de ofertas manual.

## 4. Puntos de dolor
1. Ofertación técnica a cliente industrial (configuración + precios + plazos).
2. Seguimiento de pedido entre planta, logística y comercial.
3. Reporting de planta (producción, OEE, calidad).
4. Gestión documental con clientes grandes (albaranes, certificados).

## 5. Contacto decisor
- No identificado. Buscar en LinkedIn: `"Grupo Grávalos" Zaragoza` / `"Gravalos SA"`.
- Perfiles: Director General, Director Comercial, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del perfil industrial aragonés + label sobre ofertación + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una oferta técnica antes del viernes",
    cuerpo=[
        "Hola,",
        "Miré Grávalos buscando industrias aragonesas con cartera industrial consolidada y me paró el perfil en El Burgo de Ebro. Tengo la sensación de que en una planta así lo que más horas se lleva a la semana no es la producción, es que cada RFQ de cliente exige mirar precios de materia, capacidad de planta, plazos y condiciones, y eso hoy sale de una hoja Excel que conoce una persona concreta.",
        "¿Cómo estáis preparando hoy esas ofertas técnicas?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-gravalos

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Gr%C3%A1valos%22%20Zaragoza&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Grávalos

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Comercial
- **Notas:** Industria aragonesa. Sede El Burgo de Ebro.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grávalos" Zaragoza.
2. **Email (respaldo)** → sin email público. Formulario gravalos-sa.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una oferta técnica antes del viernes".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 2. Luchana Logística (Palma, logística)
add(
    "luchana-logistica-s-a",
    dossier="""# Dossier: Luchana Logística S.A.
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Luchana Logística es una empresa mallorquina de transporte y logística con sede en Palma. Operativa típica de operador insular: dependencia del corredor marítimo península-Baleares, gestión de última milla en la isla, clientes locales exigentes en plazos por la logística marítima.

- **Sector:** Logística y transporte
- **Tamaño:** Operador regional Baleares
- **Sede:** Carrer Licorers 22, Palma

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | luchanalogistica.com |
| Zona | Baleares + península |

## 3. Madurez digital
- Web corporativa informativa. Sin portal cliente aparente.
- Sector habitual: TMS + llamadas + mucho email con navieras (Baleària, Trasmediterránea) y clientes.

## 4. Puntos de dolor
1. Coordinación con navieras para booking y avisos de retraso.
2. Atención al cargador sobre ETAs (dependencia fuerte del barco).
3. Reporting de margen por ruta insular vs. península.
4. Tramitación documental (CMR, albaranes).

## 5. Contacto decisor
- No identificado. Buscar: `"Luchana Logística" Palma Mallorca`.
- Perfiles: Director General, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento de la operativa insular + label sobre ETAs dependientes del barco + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un barco que sale a las diez",
    cuerpo=[
        "Hola,",
        "Entré en Luchana Logística mirando operadores con base en Mallorca y corredor con península. Me da la impresión de que en una operativa tan dependiente del barco el cliente no está realmente preguntando por el camión, está preguntando por el Baleària de las diez, y cada consulta de ETA acaba pasando por una persona del equipo que tiene ya tres teléfonos abiertos con las navieras.",
        "¿Cómo se está centralizando hoy esa información de estado entre operarios y cargador?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — luchana-logistica-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Luchana%20Log%C3%ADstica%22%20Palma&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Luchana Logística

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director de Operaciones
- **Notas:** Logística Mallorca-península. Sede Palma.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Luchana Logística" Palma.
2. **Email (respaldo)** → sin email público. Formulario luchanalogistica.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un barco que sale a las diez".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 3. Grupo MLN (Zaragoza, construcción)
add(
    "grupo-mln",
    dossier="""# Dossier: Grupo MLN — Construcción
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo MLN es una constructora zaragozana con perfil de obra civil y edificación. Sede en Zaragoza. Típica constructora regional con obras distribuidas, subcontratación intensa, certificaciones mensuales y volumen alto de documentación técnica.

- **Sector:** Construcción / obra civil
- **Tamaño:** Grupo regional
- **Sede:** C. Uncastillo 19, Zaragoza

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupo-mln.com |
| Actividad | Construcción, obra civil, edificación |

## 3. Madurez digital
- Web corporativa con proyectos destacados. Sector con digitalización dispar.
- ERP de construcción (PresWin, Navision) + Excel + BIM en proyectos grandes.

## 4. Puntos de dolor
1. Certificaciones mensuales a cliente/promotor con mediciones.
2. Gestión documental de obra (contratos de subcontratistas, PRL, albaranes).
3. Control de costes por obra en tiempo real.
4. Comunicación entre jefe de obra, encargados y oficina técnica.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo MLN" Zaragoza construcción`.
- Perfiles: CEO/fundador, Director de Producción.

## 6. Ángulo de entrada
Reconocimiento del perfil constructor aragonés + label sobre certificaciones mensuales + pregunta calibrada.

## 7. Score
70.
""",
    asunto="La certificación del mes que viene",
    cuerpo=[
        "Hola,",
        "Vi Grupo MLN buscando constructoras activas en obra civil en Zaragoza y me quedé con el perfil. Parece como si el primer día de cada mes en una constructora así lo que bloquea de verdad no sean los plazos de obra, sino armar la certificación mensual por obra con mediciones, albaranes y cambios, pidiendo hojas a jefe de obra, oficina técnica y subcontrata.",
        "¿Cómo estáis llevando hoy el cierre mensual de certificaciones?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-mln

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20MLN%22%20Zaragoza%20construcci%C3%B3n&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo MLN

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** CEO/fundador / Director de Producción
- **Notas:** Constructora zaragozana. Obra civil y edificación.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo MLN" Zaragoza construcción.
2. **Email (respaldo)** → sin email público. Formulario grupo-mln.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "La certificación del mes que viene".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 4. Grupo GS Promotora (Sevilla, inmobiliaria)
add(
    "grupo-gs-promotora-inmobiliaria",
    dossier="""# Dossier: Grupo GS — Promotora Inmobiliaria
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo GS es una promotora inmobiliaria sevillana con sede en la calle Campana (Casco Antiguo). Promoción y gestión de activos inmobiliarios. Perfil clásico: operaciones con volumen alto de documentación, seguimiento comercial de interesados, y gestión post-venta.

- **Sector:** Inmobiliaria / promoción
- **Tamaño:** Promotora regional
- **Sede:** C. Campana, Casco Antiguo, Sevilla

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupogs.es |
| Actividad | Promoción inmobiliaria |

## 3. Madurez digital
- Web corporativa con portfolio de promociones. CRM inmobiliario estándar o propio.
- Sector con mucho papel (contratos de reserva, escrituras, subrogaciones).

## 4. Puntos de dolor
1. Cualificación de leads entrantes desde portales (Idealista, Fotocasa).
2. Seguimiento comercial post-visita (recordatorios, dudas financieras).
3. Gestión documental de reserva-arras-escritura.
4. Reporting de conversión por promoción y comercial.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo GS" Sevilla promotora inmobiliaria`.
- Perfiles: CEO/fundador, Director Comercial.

## 6. Ángulo de entrada
Reconocimiento de la promotora + label sobre ventana de respuesta a lead + pregunta calibrada.

## 7. Score
70.
""",
    asunto="El interesado que pidió hoja de encargo",
    cuerpo=[
        "Hola,",
        "Entré en Grupo GS mirando promotoras inmobiliarias activas en Sevilla y me paré al ver la sede en Casco Antiguo y el catálogo de promociones. Me imagino que el problema real hoy no es captar interesados, es que el contacto que pidió hoja de encargo ayer a las ocho compite con cuatro visitas de hoy, dos llamadas de un notario y una incidencia post-venta, y la vuelta en frío se queda para mañana o pasado.",
        "¿Cómo se está organizando hoy el seguimiento a interesados entre el equipo comercial?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-gs-promotora-inmobiliaria

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20GS%22%20Sevilla%20promotora&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo GS

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** CEO/fundador / Director Comercial
- **Notas:** Promotora inmobiliaria Sevilla. Sede Casco Antiguo.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo GS" Sevilla promotora.
2. **Email (respaldo)** → sin email público. Formulario grupogs.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El interesado que pidió hoja de encargo".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 5. Grupo Lalala (Madrid, hostelería)
add(
    "grupo-lalala",
    dossier="""# Dossier: Grupo Lalala — Restauración Madrid
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Lalala opera restaurantes en Madrid con sede en López de Hoyos (Chamartín). Grupo multimarca de restauración urbana con locales en barrios residenciales de alto poder adquisitivo. Típico grupo con varias marcas bajo paraguas y operativa compartida.

- **Sector:** Hostelería / grupo de restauración
- **Tamaño:** Multilocal Madrid
- **Sede:** López de Hoyos 27, Chamartín

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupolalala.com |
| Zona | Madrid (Chamartín y alrededores) |

## 3. Madurez digital
- Web corporativa con catálogo de conceptos. Instagram activo.
- Reservas probablemente vía CoverManager/TheFork. POS estándar.

## 4. Puntos de dolor
1. Respuesta a reservas multicanal (web, IG, WhatsApp).
2. Consolidación diaria por local.
3. Reseñas Google/TripAdvisor.
4. Onboarding de personal de sala.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Lalala" Madrid`.
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del grupo + label sobre multicanal de reservas + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un DM en Instagram a las once",
    cuerpo=[
        "Hola,",
        "Miré Grupo Lalala buscando grupos de restauración consolidados en Chamartín y me paró el catálogo de conceptos. Tengo la sensación de que en un grupo así con varias marcas lo que se acaba escapando no son las reservas de la web, son los mensajes directos de Instagram a las once de la noche pidiendo mesa para mañana, que alguien acaba respondiendo desde casa con el móvil porque no hay nadie dedicado a eso.",
        "¿Cómo estáis centralizando hoy esos mensajes entre marcas del grupo?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-lalala

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Lalala%22%20Madrid&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Lalala

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo restauración Madrid-Chamartín. Multimarca.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Lalala" Madrid.
2. **Email (respaldo)** → sin email público. Formulario grupolalala.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un DM en Instagram a las once".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 6. Lombardo Grupo Restauración (Barcelona)
add(
    "lombardo-grupo-restauracion-sl",
    dossier="""# Dossier: Lombardo Grupo Restauración
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Lombardo Grupo Restauración opera varios restaurantes en Barcelona con sede en Aragó (Eixample). Grupo hostelero barcelonés con conceptos urbanos y clientela mixta local-turista.

- **Sector:** Hostelería / restauración
- **Tamaño:** Multilocal Barcelona
- **Sede:** Carrer d'Aragó, Eixample

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupolombardo.com |
| Zona | Barcelona |

## 3. Madurez digital
- Web corporativa. Presencia digital estándar.
- Operativa típica multilocal.

## 4. Puntos de dolor
1. Atención multilingüe al turista.
2. Reservas multicanal.
3. Reporting consolidado.
4. Reseñas Google/TripAdvisor.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Lombardo" OR "Lombardo restauración" Barcelona`.
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del grupo en Eixample + label sobre mix local-turista + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Dos clientes, dos idiomas, misma mesa",
    cuerpo=[
        "Hola,",
        "Vi Lombardo buscando grupos hosteleros en Eixample y me paró el mix de conceptos y el barrio, clientela mezclada local y turista. Me da la impresión de que el equipo de sala pasa mucho tiempo haciendo de recepcionista bilingüe, contestando a la vez preguntas por teléfono, DM y web sobre carta, alérgenos y disponibilidad, cuando podrían estar dedicados a la mesa que ya está dentro del local.",
        "¿Cómo estáis gestionando hoy esa atención pre-servicio?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — lombardo-grupo-restauracion-sl

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Lombardo%22%20Barcelona&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Lombardo Grupo Restauración

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo restauración Barcelona Eixample.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Lombardo" Barcelona.
2. **Email (respaldo)** → sin email público. Formulario grupolombardo.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Dos clientes, dos idiomas, misma mesa".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 7. Grupo Gorki (Málaga)
add(
    "grupo-gorki",
    dossier="""# Dossier: Grupo Gorki — Málaga
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Gorki opera varios locales en el centro de Málaga (C. Bolsa). Perfil de grupo hostelero urbano con afluencia turística intensa, clientela internacional y horarios extendidos.

- **Sector:** Hostelería
- **Tamaño:** Multilocal Málaga centro
- **Sede:** C. Bolsa, Centro, Málaga

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupogorki.es |
| Zona | Málaga centro |

## 3. Madurez digital
- Web corporativa. Digital estándar.

## 4. Puntos de dolor
1. Atención multilingüe turística.
2. Reservas multicanal.
3. Reseñas Google/TripAdvisor.
4. Reporting diario.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Gorki" Málaga`.
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del grupo centro Málaga + label sobre gestión de reseñas + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una reseña de tres estrellas el domingo",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Gorki buscando grupos hosteleros con varios locales en el centro de Málaga y me paró el perfil. Parece como si en un grupo tan expuesto al turismo el trabajo invisible de los domingos sea ir contestando reseñas de Google y TripAdvisor con respuestas pensadas y personales, y eso acabe cayendo en el fundador o en una sola persona de marketing que lo hace cuando puede.",
        "¿Cómo lo estáis cubriendo hoy sin que se acumulen sin respuesta?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-gorki

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Gorki%22%20M%C3%A1laga&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Gorki

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo hostelero Málaga centro.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Gorki" Málaga.
2. **Email (respaldo)** → sin email público. Formulario grupogorki.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una reseña de tres estrellas el domingo".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 8. Energías Renovables Mediterráneas / Renomar (Valencia)
add(
    "energias-renovables-mediterraneas-s-a",
    dossier="""# Dossier: Renomar — Energías Renovables Mediterráneas
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Renomar (Energías Renovables Mediterráneas S.A.) opera en el sector de energías renovables con sede en Valencia (Av. de les Corts Valencianes). Perfil de operador/promotor energético en sector en fuerte expansión. Gestión de proyectos de energía, relación con instaladores, clientes industriales y consumidores finales.

- **Sector:** Energía / renovables
- **Tamaño:** Operador regional-nacional
- **Sede:** Valencia

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | renomar.es |
| Actividad | Energías renovables |

## 3. Madurez digital
- Web corporativa. Sector con mucho proyecto "a medida" y documentación técnica.

## 4. Puntos de dolor
1. Preparación de propuestas/proyectos energéticos (cálculos, legalización, subvenciones).
2. Seguimiento de tramitación administrativa (distribuidora, industria, subvenciones).
3. Atención a cliente final (particular o empresa) sobre estado de su proyecto.
4. Reporting de cartera de proyectos.

## 5. Contacto decisor
- No identificado. Buscar: `"Renomar" OR "Energías Renovables Mediterráneas" Valencia`.
- Perfiles: Director General, Director Técnico.

## 6. Ángulo de entrada
Reconocimiento del sector en expansión + label sobre tramitación administrativa + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un expediente que lleva cuatro meses",
    cuerpo=[
        "Hola,",
        "Vi Renomar mirando operadores de renovables activos en Valencia y me paré al ver el perfil. Suena a que en este sector lo que más frustra al cliente no es la instalación en sí, es que después de firmar se abren cuatro o cinco expedientes en paralelo (distribuidora, industria, subvención, legalización) y cada uno tiene su propio reloj, y al final el cliente te llama a los tres meses preguntando por dónde va lo suyo.",
        "¿Cómo estáis hoy dando visibilidad al cliente del estado de su expediente?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — energias-renovables-mediterraneas-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Renomar%22%20Valencia%20renovables&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Renomar (ER Mediterráneas)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Técnico
- **Notas:** Operador renovables Valencia.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Renomar" Valencia.
2. **Email (respaldo)** → sin email público. Formulario renomar.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un expediente que lleva cuatro meses".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 9. Grupo Terry Automoción (Sevilla)
add(
    "grupo-terry-automocion",
    dossier="""# Dossier: Grupo Terry Automoción — Sevilla
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Terry es un grupo de concesionarios sevillano con sede en el Polígono Amarilla. Opera varias marcas (incluido Maxus, vehículo comercial/eléctrico). Perfil de grupo multimarca con venta nueva, VO, flotas y posventa.

- **Sector:** Automoción / concesionarios multimarca
- **Tamaño:** Grupo regional Sevilla
- **Sede:** Polígono Amarilla, Sevilla

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupoterryautomocion.es |
| Marcas | Varias (Maxus entre ellas) |

## 3. Madurez digital
- Web corporativa moderna con stock. DMS estándar + portales VO.
- Foco en flotas comerciales (Maxus) añade capa adicional: cliente B2B con procesos de compra distintos.

## 4. Puntos de dolor
1. Seguimiento de lead B2B de flotas (ciclo largo, multi-interlocutor).
2. Preparación de ofertas corporativas (TCO, configuración de flota).
3. Coordinación entre marcas y concesiones del grupo.
4. Posventa flotas (citas, urgencias).

## 5. Contacto decisor
- Grupo familiar Terry. Buscar: `"Grupo Terry" Sevilla automoción`.
- Perfiles: Director General, Director Comercial flotas.

## 6. Ángulo de entrada
Reconocimiento de la venta a flotas + label sobre preparación de ofertas B2B + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una flota de doce furgonetas",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Terry mirando concesionarios con cartera de flotas en Sevilla y me paró el peso de Maxus en el catálogo. Tengo la sensación de que en la venta a empresa lo que más tiempo se come hoy no es la decisión del cliente, es preparar por dentro la oferta: configuración por unidad, TCO, plan de entregas, financiación, y eso hoy pasa por varios Excel y tres personas distintas del grupo.",
        "¿Qué parte de esa preparación es la que más se os atasca?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-terry-automocion

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Terry%22%20Sevilla%20automoci%C3%B3n&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Terry Automoción

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Comercial flotas
- **Notas:** Grupo automoción Sevilla. Multimarca con foco flotas (Maxus).

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Terry" Sevilla automoción.
2. **Email (respaldo)** → sin email público. Formulario grupoterryautomocion.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una flota de doce furgonetas".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 10. Grupo Aguinaga (Bilbao, automoción Mercedes)
add(
    "grupo-aguinaga",
    dossier="""# Dossier: Grupo Aguinaga — Mercedes-Benz Bilbao
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Aguinaga es el concesionario oficial Mercedes-Benz en Vizcaya, con sede en Botica Vieja (Deusto). Perfil premium, cliente exigente, ciclo de venta más largo y alto valor medio. Posventa intensiva con plan de mantenimiento de marca.

- **Sector:** Automoción / concesionario premium
- **Tamaño:** Mediano-grande regional
- **Sede:** Botica Vieja, Deusto, Bilbao

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Mercedes-Benz |
| Web | grupoaguinaga.es |
| Zona | Vizcaya |

## 3. Madurez digital
- Web corporativa premium con configurador + stock. DMS Mercedes (Contact.Net / XENTRY).
- Posventa fuerte: campañas de marca, recall, mantenimiento.

## 4. Puntos de dolor
1. Seguimiento de lead premium (Mercedes online + showroom).
2. Recordatorios y captación para posventa (revisiones, neumáticos, campañas).
3. Atención multi-canal a cliente existente (flota y particular).
4. Reporting de conversión y retención.

## 5. Contacto decisor
- Grupo familiar Aguinaga. Buscar: `"Grupo Aguinaga" Bilbao Mercedes`.
- Perfiles: Director General, Director de Posventa.

## 6. Ángulo de entrada
Reconocimiento del posicionamiento Mercedes + label sobre retención posventa + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una revisión a los 30.000",
    cuerpo=[
        "Hola,",
        "Vi Grupo Aguinaga mirando concesionarios premium en Vizcaya y me quedé con la foto: Mercedes oficial en Deusto con cartera de particular y flota. Me imagino que la venta inicial está más o menos estabilizada con el proceso de marca, pero que el reto ahora está en posventa: cómo aseguras que el cliente de 2023 vuelva para la revisión de los 30.000 en 2026 sin depender de que un asesor tenga tiempo de llamarle.",
        "¿Cómo está montada hoy esa reactivación de posventa?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-aguinaga

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Aguinaga%22%20Bilbao%20Mercedes&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Aguinaga (Mercedes-Benz)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director de Posventa
- **Notas:** Concesionario Mercedes Vizcaya. Marca familiar Aguinaga.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Aguinaga" Bilbao Mercedes.
2. **Email (respaldo)** → sin email público. Formulario grupoaguinaga.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una revisión a los 30.000".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)
