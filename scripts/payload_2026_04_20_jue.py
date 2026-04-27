# -*- coding: utf-8 -*-
"""Jueves 2026-04-23 — 10 leads."""

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


# -- 1. Hebico Ingenieros (Bilbao, automatización industrial)
add(
    "hebico-ingenieros-s-a",
    dossier="""# Dossier: Hebico Ingenieros S.A.
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Hebico Ingenieros es una ingeniería vizcaína especializada en automatización industrial con sede en Basurtu-Zorrotza (Bilbao). Perfil clásico de integrador industrial vasco: PLCs, SCADA, robótica, proyectos llave en mano para industria pesada y automoción del norte.

- **Sector:** Ingeniería industrial / automatización
- **Tamaño:** Mediana cuenta regional
- **Sede:** Basurtu-Zorrotza, Bilbao

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | hebico.es |
| Actividad | Automatización industrial, ingeniería |

## 3. Madurez digital
- Web corporativa con foco en proyectos. Cliente técnico (industria pesada norte).
- Operativa típica: MS Project/Excel + Teams + mucho correo con cliente sobre cambios de scope.

## 4. Puntos de dolor
1. Gestión documental de proyecto (pliegos, As-built, memorias).
2. Ofertación técnica (ingeniería + hardware + mano de obra).
3. Seguimiento de instalación/puesta en marcha multi-proyecto.
4. Post-venta técnica (soporte, garantías, repuestos).

## 5. Contacto decisor
- No identificado. Buscar: `"Hebico" Bilbao ingeniería automatización`.
- Perfiles: Director General, Director Técnico/Ingeniería.

## 6. Ángulo de entrada
Reconocimiento como integrador industrial vasco + label sobre ofertación técnica + pregunta calibrada.

## 7. Score
70. Interesante por ser ingeniería automatizadora: hablan el mismo idioma.
""",
    asunto="Una memoria técnica para un presupuesto",
    cuerpo=[
        "Hola,",
        "Entré en Hebico buscando ingenierías de automatización activas en Vizcaya y me paró el perfil: PLC, robótica y proyectos llave en mano. Un poco paradójico, me da la impresión de que las ingenierías que automatizan líneas de cliente son muchas veces las que peor tienen automatizada su propia ofertación: cada RFQ importante se traduce en una memoria técnica hecha casi a mano a partir de proyectos anteriores que viven en carpetas.",
        "¿Cómo estáis llevando hoy esa preparación de ofertas técnicas?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — hebico-ingenieros-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Hebico%22%20Bilbao%20ingenier%C3%ADa&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Hebico Ingenieros

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Técnico
- **Notas:** Ingeniería automatización Vizcaya.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Hebico" Bilbao ingeniería.
2. **Email (respaldo)** → sin email público. Formulario hebico.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una memoria técnica para un presupuesto".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 2. Eurobalear de Transportes (Palma)
add(
    "eurobalear-de-transportes-s-a",
    dossier="""# Dossier: Eurobalear de Transportes
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Eurobalear de Transportes presta servicio regular y urgente entre Baleares y península. Sede en Polígono Son Castelló (Palma). Perfil de operador con corredor marítimo estable y urgencias como diferenciador.

- **Sector:** Logística / transporte insular
- **Tamaño:** Operador regional
- **Sede:** Son Castelló, Palma

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | eurobalear.es |
| Actividad | Transporte regular + urgente Baleares-península |

## 3. Madurez digital
- Web corporativa con foco en servicios. Sector clásico.

## 4. Puntos de dolor
1. Gestión de urgencias (priorización, comunicación con cliente).
2. Tracking y ETA al cargador.
3. Documentación CMR/albaranes.
4. Reporting margen por ruta y cliente.

## 5. Contacto decisor
- No identificado. Buscar: `"Eurobalear" Palma`.
- Perfiles: Director General, Director de Tráfico.

## 6. Ángulo de entrada
Reconocimiento del servicio urgente insular + label sobre comunicación en urgencias + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una urgencia a las ocho de la tarde",
    cuerpo=[
        "Hola,",
        "Vi Eurobalear buscando operadores con servicio urgente entre Baleares y península. Suena a que el producto urgente os diferencia, pero también a que esas peticiones entran por teléfono, WhatsApp y email en horario raro, y alguien del equipo de tráfico acaba coordinando contra el reloj con poca visibilidad de qué pasó en una urgencia similar la semana pasada.",
        "¿Cómo estáis organizando hoy esa entrada de urgencias fuera de horario?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — eurobalear-de-transportes-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Eurobalear%22%20Palma&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Eurobalear de Transportes

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director de Tráfico
- **Notas:** Operador Baleares-península con urgentes.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Eurobalear" Palma.
2. **Email (respaldo)** → sin email público. Formulario eurobalear.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una urgencia a las ocho de la tarde".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 3. Pérez Moreno (Las Palmas, construcción)
add(
    "perez-moreno-s-a-u",
    dossier="""# Dossier: Pérez Moreno S.A.U. — Constructora Canarias
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Pérez Moreno es una constructora canaria de referencia con sede en Las Palmas de Gran Canaria (C. Francisco Gourié). Perfil de constructora de obra pública y privada canaria, trayectoria larga, cartera significativa de obra en las islas.

- **Sector:** Construcción
- **Tamaño:** Grande regional canario
- **Sede:** Las Palmas de Gran Canaria

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | perezmoreno.com |
| Actividad | Construcción |

## 3. Madurez digital
- Web corporativa con proyectos. Sector clásico.
- Operativa típica: ERP construcción + Excel + obras distribuidas en varias islas, lo cual añade fricción logística.

## 4. Puntos de dolor
1. Certificaciones mensuales con obras en varias islas.
2. Gestión documental PRL y subcontratas.
3. Control de costes por obra (compras insulares).
4. Reporting a dirección consolidado.

## 5. Contacto decisor
- No identificado. Marca familiar probable Pérez Moreno. Buscar: `"Pérez Moreno" Las Palmas construcción`.
- Perfiles: CEO/fundador, Director de Producción.

## 6. Ángulo de entrada
Reconocimiento del peso en obra canaria + label sobre coordinación multi-isla + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Una obra en Tenerife, otra en Fuerteventura",
    cuerpo=[
        "Hola,",
        "Entré en Pérez Moreno mirando constructoras con trayectoria en Canarias y me paré al ver el rango de obra pública y privada. Me da la impresión de que cuando tu cartera está repartida entre islas, lo que bloquea de verdad no es el pliego, es que cada obra tiene su propio cierre mensual con mediciones locales y subcontratas locales, y consolidar esa foto desde Las Palmas cuesta más horas de las que debería.",
        "¿Cómo se está consolidando hoy esa vista multi-obra?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — perez-moreno-s-a-u

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22P%C3%A9rez%20Moreno%22%20Las%20Palmas%20construcci%C3%B3n&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Pérez Moreno S.A.U.

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** CEO/fundador / Director de Producción
- **Notas:** Constructora canaria Las Palmas.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Pérez Moreno" Las Palmas construcción.
2. **Email (respaldo)** → sin email público. Formulario perezmoreno.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Una obra en Tenerife, otra en Fuerteventura".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 4. Grupo Modernia (Málaga, inmobiliaria)
add(
    "grupo-modernia-malaga-oeste",
    dossier="""# Dossier: Grupo Modernia — Inmobiliaria Málaga Oeste
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Modernia es una inmobiliaria consolidada en Málaga Oeste (Carretera de Cádiz). Gestión de venta y alquiler residencial y comercial en una zona con demanda internacional fuerte (costa del sol).

- **Sector:** Inmobiliaria / intermediación
- **Tamaño:** Regional (Málaga Oeste)
- **Sede:** C. Ildefonso Marzo 18, Málaga

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupomodernia.es |

## 3. Madurez digital
- Web con listado de activos. CRM inmobiliario estándar (Inmovilla, eGO).
- Operativa típica: muchas llamadas, visitas, mensajes multicanal.

## 4. Puntos de dolor
1. Atención multilingüe a cliente internacional (norte europeo principalmente).
2. Cualificación de lead entrante (muchos curiosos, pocos decisores).
3. Coordinación de agenda de visitas.
4. Gestión documental reservas/arras.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Modernia" Málaga inmobiliaria`.
- Perfiles: fundador/CEO, Gerente.

## 6. Ángulo de entrada
Reconocimiento del cliente internacional + label sobre cualificación de lead + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un inglés que pide información en agosto",
    cuerpo=[
        "Hola,",
        "Vi Grupo Modernia mirando inmobiliarias activas en Málaga Oeste y me paró el perfil: zona con mucho comprador norte-europeo. Tengo la sensación de que en una cartera así el trabajo fino no está en enseñar los pisos, está en separar al curioso del verdadero decisor entre veinte mensajes diarios en español, inglés y alemán, y ahora mismo eso lo hace manualmente un equipo pequeño a base de olfato.",
        "¿Cómo estáis cualificando hoy esos primeros contactos?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-modernia-malaga-oeste

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Modernia%22%20M%C3%A1laga&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Modernia

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Gerente
- **Notas:** Inmobiliaria Málaga Oeste. Cliente internacional.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Modernia" Málaga.
2. **Email (respaldo)** → sin email público. Formulario grupomodernia.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un inglés que pide información en agosto".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 5. Grupo Madriz (Madrid, traspasos hostelería)
add(
    "grupo-madriz-traspasos-de-restaurantes-y-bares",
    dossier="""# Dossier: Grupo Madriz — Traspasos Hostelería
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Madriz se especializa en traspasos, alquiler y venta de locales de hostelería en Madrid. Sede en Chamartín. Nicho muy específico: intermediación B2B con hosteleros que cambian de local o salen del sector.

- **Sector:** Inmobiliaria especializada / intermediación hostelera
- **Tamaño:** Especialista Madrid
- **Sede:** Menéndez Pidal, Chamartín

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupomadriz.es |

## 3. Madurez digital
- Web con catálogo de locales disponibles. Sector tradicional.

## 4. Puntos de dolor
1. Cualificación del comprador (hay muchos curiosos, pocos hosteleros serios).
2. Documentación del traspaso (licencias, contratos, inventario).
3. Seguimiento entre primera visita y cierre (suele llevar semanas).
4. Actualización del catálogo de locales.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Madriz" traspasos Madrid`.
- Perfiles: fundador/CEO, Director Comercial.

## 6. Ángulo de entrada
Reconocimiento del nicho especializado + label sobre cualificación del hostelero serio + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un traspaso que lleva tres meses",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Madriz mirando intermediación de traspasos de hostelería y me paró el nicho, bastante específico. Me imagino que el volumen de consultas es alto pero la conversión a cierre es lenta: desde la primera visita hasta firmar el traspaso suelen pasar semanas con dudas sobre licencias, inventario y condiciones, y ahí es donde un hostelero serio se acaba confundiendo con dos curiosos que preguntan lo mismo.",
        "¿Cómo estáis separando hoy los contactos que realmente van a cerrar?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-madriz-traspasos-de-restaurantes-y-bares

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Madriz%22%20traspasos%20Madrid&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Madriz

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director Comercial
- **Notas:** Intermediación traspasos hostelería Madrid.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Madriz" traspasos Madrid.
2. **Email (respaldo)** → sin email público. Formulario grupomadriz.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un traspaso que lleva tres meses".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 6. Grupo Gastroadictos (Valencia)
add(
    "grupo-gastroadictos",
    dossier="""# Dossier: Grupo Gastroadictos — Valencia
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Gastroadictos opera varios restaurantes en Valencia desde 1989. Sede en Campanar. Grupo con trayectoria larga, varios conceptos, clientela local consolidada.

- **Sector:** Hostelería
- **Tamaño:** Multilocal Valencia
- **Sede:** Campanar, Valencia

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupogastroadictos.com |
| Desde | 1989 |

## 3. Madurez digital
- Web con conceptos. Presencia digital estándar.

## 4. Puntos de dolor
1. Fidelización de cliente recurrente local.
2. Reservas multicanal.
3. Reporting consolidado multi-marca.
4. Onboarding de sala.

## 5. Contacto decisor
- No identificado. Buscar: `"Gastroadictos" Valencia`.
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento de los 35+ años en Valencia + label sobre fidelización cliente recurrente + pregunta calibrada.

## 7. Score
70.
""",
    asunto="El cliente que vino hace tres meses",
    cuerpo=[
        "Hola,",
        "Vi Grupo Gastroadictos mirando grupos hosteleros con trayectoria larga en Valencia y me paró la fecha, 35 años de historia. Parece como si un grupo con esa base de cliente recurrente tenga la mejor materia prima de fidelización que existe (gente que ya os conoce), pero que hoy ese cliente que vino en enero y no ha vuelto se pierde entre el ruido del día a día porque no hay forma fácil de detectarlo.",
        "¿Cómo estáis hoy identificando a vuestros clientes recurrentes entre locales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-gastroadictos

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Gastroadictos%22%20Valencia&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Gastroadictos

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo restauración Valencia. Desde 1989.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Gastroadictos" Valencia.
2. **Email (respaldo)** → sin email público. Formulario grupogastroadictos.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El cliente que vino hace tres meses".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 7. Grupo Iruña (Bilbao)
add(
    "grupo-iruna",
    dossier="""# Dossier: Grupo Iruña — Bilbao
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Iruña opera locales emblemáticos en el centro de Bilbao (Abando). Referencia histórica de la hostelería bilbaína con varios conceptos y clientela consolidada.

- **Sector:** Hostelería
- **Tamaño:** Multilocal Bilbao centro
- **Sede:** Berástegui Kalea, Abando

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupoiruna.net |
| Zona | Bilbao centro |

## 3. Madurez digital
- Web informativa clásica. Presencia digital modesta.
- Operativa muy tradicional probablemente.

## 4. Puntos de dolor
1. Reservas telefónicas + WhatsApp sin centralizar.
2. Reporting diario.
3. Reseñas sin estructurar.
4. Comunicación entre locales.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Iruña" Bilbao`.
- Perfiles: fundador/CEO.

## 6. Ángulo de entrada
Reconocimiento de la referencia bilbaína + label sobre reservas dispersas + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Reservas por teléfono y por WhatsApp",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Iruña buscando referentes hosteleros en el centro de Bilbao y me paré en el perfil, cartera histórica de la ciudad. Tengo la sensación de que en casas con esa tradición la reserva sigue llegando mucho por teléfono y cada vez más por WhatsApp del encargado, y que consolidar el día a día entre local y dirección depende de que alguien escriba a mano el resumen a última hora.",
        "¿Cómo estáis centralizando hoy esas reservas entre locales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-iruna

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Iru%C3%B1a%22%20Bilbao&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Iruña

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo hostelero Bilbao centro. Referencia histórica.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Iruña" Bilbao.
2. **Email (respaldo)** → sin email público. Formulario grupoiruna.net tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Reservas por teléfono y por WhatsApp".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 8. Grupo Auto Elia (Madrid, Lynk&Co)
add(
    "grupo-auto-elia-concesionario-oficial-lynk-co-madrid-rios-rosas",
    dossier="""# Dossier: Grupo Auto Elia — Lynk&Co Madrid
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Auto Elia opera la concesión oficial Lynk&Co en Madrid (Ríos Rosas, Chamberí). Marca premium nórdica-china con modelo de membresía/suscripción, perfil de cliente urbano y tech.

- **Sector:** Automoción / concesionario premium nuevo
- **Tamaño:** Mediano Madrid
- **Sede:** Ríos Rosas, Chamberí

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Lynk&Co |
| Web | lynkcogrupoautoelia.es |

## 3. Madurez digital
- Web moderna con configurador. Marca con modelo de membresía, lo que añade complejidad al ciclo de venta.
- Cliente tech, expectativas de respuesta digital alta.

## 4. Puntos de dolor
1. Educación del cliente sobre el modelo de membresía (novedoso en España).
2. Cualificación de lead web (marca atrae mucha curiosidad).
3. Test drive + entrega.
4. Posventa Lynk&Co.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Auto Elia" Madrid Lynk&Co`.
- Perfiles: Director General, Gerente comercial.

## 6. Ángulo de entrada
Reconocimiento del modelo membresía + label sobre educación al cliente + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un cliente que pregunta por la membresía",
    cuerpo=[
        "Hola,",
        "Vi Grupo Auto Elia mirando concesionarios premium de marca emergente en Madrid y me paró el modelo de membresía de Lynk&Co, bastante distinto a lo que un comprador español está acostumbrado. Me da la impresión de que un porcentaje importante del tiempo del equipo comercial ahora mismo se va en explicar por teléfono y chat cómo funciona el modelo frente a la compra tradicional, más que en cerrar la venta de verdad.",
        "¿Cómo estáis hoy dando esas primeras explicaciones antes del test drive?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-auto-elia-concesionario-oficial-lynk-co-madrid-rios-rosas

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Auto%20Elia%22%20Madrid%20Lynk&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Auto Elia (Lynk&Co)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Gerente comercial
- **Notas:** Concesión Lynk&Co Madrid Ríos Rosas.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Auto Elia" Madrid.
2. **Email (respaldo)** → sin email público. Formulario lynkcogrupoautoelia.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un cliente que pregunta por la membresía".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 9. Grupo Angal (Sevilla)
add(
    "grupo-angal-automocion-vehiculos-nuevos-de-ocasion-y-km0",
    dossier="""# Dossier: Grupo Angal Automoción — Sevilla
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Angal es un concesionario multimarca sevillano con foco en VO, km0 y vehículo nuevo. Sede en Av. Reino Unido (Sevilla). Perfil clásico de VO-centric con rotación rápida de stock y fuerte presencia en portales.

- **Sector:** Automoción / VO multimarca
- **Tamaño:** Regional Sevilla
- **Sede:** Av. Reino Unido, Sevilla

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupoangal.com |

## 3. Madurez digital
- Web con amplio stock. Presencia fuerte en Coches.net / Autocasion.
- Rotación típica VO: mucho lead por portal.

## 4. Puntos de dolor
1. Volumen de leads de portal (respuesta crítica).
2. Precio dinámico de stock VO.
3. Gestión de financiación por cliente.
4. Tasación de entrega.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Angal" Sevilla automoción`.
- Perfiles: Gerente, Director Comercial.

## 6. Ángulo de entrada
Reconocimiento del perfil VO + label sobre ventana de respuesta a lead de portal + pregunta calibrada.

## 7. Score
70.
""",
    asunto="El primero en llamar al mediodía",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Angal mirando concesionarios con peso en VO en Sevilla y me paró el volumen de stock. Parece como si en un negocio de VO lo único que diferencia de un competidor a tres kilómetros sea quién llama primero al lead que preguntó por el Polo de 2021 a las doce y media, y hoy eso depende de que un comercial libre lo vea en el CRM y no esté con otro cliente dentro.",
        "¿Cómo estáis hoy acortando esa primera respuesta?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-angal-automocion-vehiculos-nuevos-de-ocasion-y-km0

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Angal%22%20Sevilla&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Angal Automoción

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Gerente / Director Comercial
- **Notas:** Multimarca VO Sevilla.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Angal" Sevilla.
2. **Email (respaldo)** → sin email público. Formulario grupoangal.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El primero en llamar al mediodía".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 10. Omoda Grupo Meuri Zubiarte (Bilbao)
add(
    "omoda-grupo-meuri-zubiarte",
    dossier="""# Dossier: Omoda Grupo Meuri — Bilbao Zubiarte
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Meuri opera la concesión Omoda en Bilbao (Zubiarte, Abando). Omoda es marca china en expansión en España con modelos electrificados. Perfil similar a MG: volumen online alto, cliente urbano tech.

- **Sector:** Automoción / concesionario marca emergente
- **Tamaño:** Mediano Bilbao
- **Sede:** Leizaola, Abando

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | Omoda |
| Web | meuri.com |

## 3. Madurez digital
- Web moderna. Marca con captación digital intensa.

## 4. Puntos de dolor
1. Volumen de leads entrantes por web.
2. Educación sobre marca china en cliente desconocedor.
3. Posventa (primer ciclo de mantenimiento llegando).
4. Test drive + entrega.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Meuri" OR "Meuri" Bilbao Omoda`.
- Perfiles: Director General, Gerente comercial.

## 6. Ángulo de entrada
Reconocimiento de marca emergente + label sobre educación de cliente + pregunta calibrada.

## 7. Score
70.
""",
    asunto="El comprador que nunca se sentó en uno",
    cuerpo=[
        "Hola,",
        "Vi Grupo Meuri mirando concesionarios de marcas asiáticas en expansión en Bilbao y me paré al ver la concesión Omoda en Zubiarte. Tengo la sensación de que el reto ahora no es vender al cliente que ya viene convencido, es ayudar al que nunca se sentó en un Omoda a pasar del interés tibio al test drive real, y ese puente hoy lo hace a base de llamadas un equipo comercial pequeño.",
        "¿Cómo estáis hoy convirtiendo ese lead tibio en visita?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — omoda-grupo-meuri-zubiarte

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Meuri%22%20Bilbao&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Omoda Grupo Meuri

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Gerente comercial
- **Notas:** Concesión Omoda Bilbao Zubiarte. Marca emergente.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Meuri" Bilbao.
2. **Email (respaldo)** → sin email público. Formulario meuri.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "El comprador que nunca se sentó en uno".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)
