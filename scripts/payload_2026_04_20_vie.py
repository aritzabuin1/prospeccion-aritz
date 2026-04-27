# -*- coding: utf-8 -*-
"""Viernes 2026-04-24 — 10 leads."""

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


# -- 1. Grupo Volund (Alicante, industria)
add(
    "grupo-volund",
    dossier="""# Dossier: Grupo Volund — Alicante
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Volund es una industria alicantina dedicada a fabricación y mantenimiento de maquinaria industrial. Sede en Alacant. Perfil de industria auxiliar con servicio técnico y mantenimiento in-situ en cliente.

- **Sector:** Industria / maquinaria industrial
- **Tamaño:** Mediana cuenta regional
- **Sede:** Carrer Poeta Pastor, Alacant

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupovolund.com |
| Actividad | Fabricación + mantenimiento maquinaria |

## 3. Madurez digital
- Web corporativa informativa. Sector tradicional.
- Operativa típica: ERP + Excel + partes de servicio en papel/móvil.

## 4. Puntos de dolor
1. Partes de trabajo del técnico de mantenimiento (transcripción a ERP).
2. Planificación de intervenciones en cliente.
3. Gestión de repuestos/almacén.
4. Ofertación de proyectos de maquinaria.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Volund" Alicante`.
- Perfiles: Director General, Director Técnico/Mantenimiento.

## 6. Ángulo de entrada
Reconocimiento del mantenimiento in-situ + label sobre partes de trabajo + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un parte de trabajo en la furgoneta",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Volund mirando industrias de maquinaria con servicio técnico en Alicante. Parece como si en un negocio con técnicos que van a cliente lo que más tiempo pierde la oficina los viernes por la tarde sea transcribir partes de trabajo que llegan en papel, en foto de WhatsApp o medio escritos desde la furgoneta, y reconciliar eso con qué había que facturar.",
        "¿Cómo se está cerrando hoy ese círculo entre técnico y administración?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-volund

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Volund%22%20Alicante&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Volund

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Técnico
- **Notas:** Industria maquinaria Alicante.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Volund" Alicante.
2. **Email (respaldo)** → sin email público. Formulario grupovolund.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un parte de trabajo en la furgoneta".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 2. La Luz S.A. Terminal Contenedores (Las Palmas — Boluda)
add(
    "la-luz-s-a-terminal-de-contenedores",
    dossier="""# Dossier: La Luz S.A. — Terminal Contenedores Las Palmas (Boluda)
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
La Luz S.A. opera terminal de contenedores en el Muelle Virgen del Pino (Las Palmas) dentro del grupo Boluda Corporación Marítima. Terminal de referencia de Canarias. Perfil de operador portuario integrado en multinacional marítima española.

- **Sector:** Logística portuaria / terminal contenedores
- **Tamaño:** Gran cuenta (parte del grupo Boluda)
- **Sede:** Muelle Virgen del Pino, Las Palmas de Gran Canaria

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | boluda.com.es |
| Grupo | Boluda Corporación Marítima |

## 3. Madurez digital
- Terminal con sistemas TOS (Terminal Operating System) estándar del sector.
- Operativa portuaria altamente digitalizada a nivel sistema, pero con huecos en comunicación al cargador final.

## 4. Puntos de dolor
1. Atención al cargador/agente sobre estado de contenedor (consultas repetitivas).
2. Gestión documental aduanera de exportación/importación.
3. Reporting operativo consolidado al grupo.
4. Comunicación con consignatarios.

## 5. Contacto decisor
- Parte de Boluda. Buscar: `"La Luz" Boluda Las Palmas terminal` o directamente gente en Boluda Las Palmas.
- Perfiles: Director de Terminal, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento del peso portuario canario + label sobre consultas de estado al cliente + pregunta calibrada.

## 7. Score
70. Interesante por ser gran cuenta (grupo Boluda).
""",
    asunto="Un consignatario que pregunta por un contenedor",
    cuerpo=[
        "Hola,",
        "Entré en La Luz mirando terminales de contenedores canarias y vi que sois Boluda, terminal de referencia en el Virgen del Pino. Me imagino que dentro de la terminal la pila tecnológica está razonablemente resuelta, pero que el último paso (responder al consignatario o al cargador sobre dónde está su contenedor, cuándo carga, si hubo incidencia) sigue cayendo sobre personas concretas que mantienen una bandeja de correo abierta todo el día.",
        "¿Cómo estáis hoy centralizando esas consultas de estado?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — la-luz-s-a-terminal-de-contenedores

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=Boluda%20%22Las%20Palmas%22%20terminal&origin=GLOBAL_SEARCH_HEADER
- Alternativa: "La Luz" Boluda Las Palmas.
""",
    contacto="""# Contacto — La Luz Terminal (Boluda)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director de Terminal / Director de Operaciones
- **Notas:** Terminal contenedores Las Palmas. Grupo Boluda.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Boluda Las Palmas terminal" o directivos Boluda.
2. **Email (respaldo)** → sin email público. Formulario boluda.com.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un consignatario que pregunta por un contenedor".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor (probable Director de Terminal Las Palmas dentro de Boluda).
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 3. Grupo Pedro Jaén (Madrid, clínica dermatológica)
add(
    "grupo-pedro-jaen-serrano-143-clinica-dermatologica-y-estetica-en-madrid",
    dossier="""# Dossier: Grupo Pedro Jaén — Dermatología Madrid
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Pedro Jaén es una clínica dermatológica premium en Madrid con sede en Serrano 143 (Chamartín). Referencia en dermatología privada madrileña, captación digital alta, clientela de alto poder adquisitivo.

- **Sector:** Salud privada / dermatología
- **Tamaño:** Clínica grupo premium
- **Sede:** Serrano 143, Chamartín, Madrid

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupopedrojaen.com |
| Referencia | Dr. Pedro Jaén (marca personal) |

## 3. Madurez digital
- Web premium con catálogo de tratamientos. Marca personal fuerte del Dr. Jaén. Captación digital intensa.
- Software clínico probablemente propio o Doctoralia/Clinic Cloud.

## 4. Puntos de dolor
1. Cualificación de lead + primera respuesta (premium exige rapidez).
2. Gestión de consentimientos y documentación pre-tratamiento.
3. Seguimiento post-tratamiento y recurrencia.
4. Reporting por médico / tratamiento / sede.

## 5. Contacto decisor
- Marca personal Dr. Pedro Jaén visible. Buscar: `"Pedro Jaén" dermatología Madrid` o `"Grupo Pedro Jaén"`.
- Perfiles: Dr. Jaén (fundador), Gerente, Director Médico.

## 6. Ángulo de entrada
Reconocimiento de la marca personal y la referencia + label sobre cualificación premium + pregunta calibrada.

## 7. Score
70. Bueno: marca personal = decisor identificable.
""",
    asunto="La paciente que pidió cita un domingo",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Pedro Jaén mirando clínicas dermatológicas de referencia en Madrid y me paró el perfil en Serrano 143. Tengo la sensación de que en una clínica premium el valor real del primer contacto con un paciente potencial no está en lo que se responde, está en cuánto se tarda: el domingo por la tarde entra una consulta por la web, y la clínica que responde el lunes a las ocho con la opción correcta es la que se queda con el paciente.",
        "¿Cómo se está hoy cubriendo esa ventana fuera de horario?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-pedro-jaen-serrano-143-clinica-dermatologica-y-estetica-en-madrid

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor probable: Dr. Pedro Jaén (marca personal). Localizar su perfil personal en LinkedIn.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Pedro%20Ja%C3%A9n%22%20dermatolog%C3%ADa%20Madrid&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Pedro Jaén

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar (probablemente Dr. Pedro Jaén como fundador, o Gerente del grupo)
- **Cargo:** Fundador / Director Médico / Gerente
- **Notas:** Clínica dermatológica premium Madrid Serrano. Marca personal Dr. Jaén.

## Canal recomendado
1. **LinkedIn (preferente)** → buscar Dr. Pedro Jaén directamente o Gerente del grupo.
2. **Email (respaldo)** → sin email público. Formulario grupopedrojaen.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "La paciente que pidió cita un domingo".

## Acciones pendientes del usuario antes de enviar
- Identificar al Dr. Pedro Jaén en LinkedIn o al Gerente del grupo.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 4. Grupo Moldatu Home (Bilbao, inmobiliaria)
add(
    "grupo-moldatu-home-inmobiliaria-bilbao",
    dossier="""# Dossier: Grupo Moldatu Home — Inmobiliaria Norte
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Moldatu Home es una inmobiliaria con oficinas en Irún, Donostia, Hondarribia y Bilbao (Alameda de Recalde). Expansión regional en el norte (Bizkaia-Gipuzkoa). Perfil en crecimiento.

- **Sector:** Inmobiliaria
- **Tamaño:** Regional norte en expansión
- **Sede:** Alameda de Recalde 37, Abando, Bilbao

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | moldatuhome.com |
| Zonas | Bilbao, Donostia, Irún, Hondarribia |

## 3. Madurez digital
- Web con listado de activos. CRM inmobiliario estándar.
- Crecimiento multi-oficina implica coordinación entre equipos.

## 4. Puntos de dolor
1. Coordinación entre oficinas (lead de Bilbao pregunta por un piso en Donostia).
2. Cualificación de leads de portal.
3. Seguimiento de visita a firma.
4. Reporting por oficina/comercial.

## 5. Contacto decisor
- No identificado. Buscar: `"Moldatu Home" Bilbao OR Donostia`.
- Perfiles: fundador/CEO.

## 6. Ángulo de entrada
Reconocimiento de la expansión norte + label sobre coordinación entre oficinas + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un lead de Bilbao que pregunta por Irún",
    cuerpo=[
        "Hola,",
        "Vi Moldatu Home mirando inmobiliarias con expansión en el norte y me paró el dato: cuatro oficinas entre Bizkaia y Gipuzkoa. Suena a que la oportunidad en una red así no es solo captar en cada oficina, es lo contrario: que un lead que entra en Bilbao preguntando por Donostia no se pierda entre los dos comerciales que deberían tratarlo, sino que llegue al que tiene el piso real que encaja.",
        "¿Cómo estáis hoy compartiendo esos leads entre oficinas?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-moldatu-home-inmobiliaria-bilbao

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Moldatu%20Home%22&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Moldatu Home

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO
- **Notas:** Inmobiliaria norte. Bilbao + Donostia + Irún + Hondarribia.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Moldatu Home".
2. **Email (respaldo)** → sin email público. Formulario moldatuhome.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un lead de Bilbao que pregunta por Irún".

## Acciones pendientes del usuario antes de enviar
- Identificar fundador/CEO en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 5. Grupo Lezama (Madrid, hostelería)
add(
    "grupo-lezama",
    dossier="""# Dossier: Grupo Lezama — Restauración Madrid
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Lezama opera locales emblemáticos en el centro de Madrid, con sede en Plaza de Oriente 3 (ubicación icónica frente al Palacio Real). Referencia histórica de la hostelería madrileña con clientela institucional y turística premium.

- **Sector:** Hostelería premium
- **Tamaño:** Multilocal Madrid centro
- **Sede:** Pl. de Oriente, Centro, Madrid

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | grupolezama.es |

## 3. Madurez digital
- Web corporativa con conceptos. Presencia digital estándar de grupo tradicional.

## 4. Puntos de dolor
1. Reservas multicanal con clientela internacional.
2. Gestión de eventos/privados (mucha personalización).
3. Reseñas y reputación online.
4. Reporting consolidado.

## 5. Contacto decisor
- No identificado. Marca familiar probable Lezama. Buscar: `"Grupo Lezama" Madrid`.
- Perfiles: fundador/CEO, Director de Operaciones.

## 6. Ángulo de entrada
Reconocimiento de la ubicación icónica + label sobre eventos privados + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un privado para veinte personas en octubre",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Lezama mirando hostelería premium en el centro de Madrid y me paró la ubicación en Plaza de Oriente. Me da la impresión de que en casas con clientela institucional y de eventos el verdadero reto hoy no está en la mesa del día, está en que una petición seria de reservado para octubre para veinte personas entra por email con tres preguntas sobre menús y disponibilidad, y la respuesta depende de que alguien saque tiempo entre servicios para mirarlo en agenda y menú.",
        "¿Cómo estáis hoy atendiendo esas peticiones de eventos privados?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-lezama

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Lezama%22%20Madrid&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Lezama

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Hostelería premium Madrid centro. Plaza de Oriente.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Lezama" Madrid.
2. **Email (respaldo)** → sin email público. Formulario grupolezama.es tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un privado para veinte personas en octubre".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 6. Grupo Tándem (Zaragoza, hostelería)
add(
    "grupo-tandem",
    dossier="""# Dossier: Grupo Tándem — Zaragoza
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Tándem opera varios locales en Zaragoza con sede en Héroes del Silencio. Perfil de grupo hostelero urbano con conceptos consolidados en la capital aragonesa.

- **Sector:** Hostelería
- **Tamaño:** Multilocal Zaragoza
- **Sede:** Héroes del Silencio, Zaragoza

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | tandemgrupo.com |

## 3. Madurez digital
- Web corporativa con portfolio de locales. Presencia digital estándar.

## 4. Puntos de dolor
1. Reservas multicanal.
2. Reporting consolidado.
3. Reseñas.
4. Operativa compra + escandallos.

## 5. Contacto decisor
- No identificado. Buscar: `"Grupo Tándem" Zaragoza hostelería`.
- Perfiles: fundador/CEO.

## 6. Ángulo de entrada
Reconocimiento del grupo aragonés + label sobre reporting entre locales + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Los números del fin de semana, el lunes",
    cuerpo=[
        "Hola,",
        "Vi Grupo Tándem buscando grupos de restauración consolidados en Zaragoza y me paré al ver el portfolio. Suena a que en un grupo con varios locales lo que cuesta no es tener los datos, cada local tiene su POS, es sentarse el lunes y tener una foto limpia del fin de semana ya consolidada entre todos los locales sin tener que exportar tres ficheros distintos y cuadrarlos en Excel.",
        "¿Cómo estáis hoy armando ese cuadro semanal?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-tandem

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20T%C3%A1ndem%22%20Zaragoza&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Tándem

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Grupo hostelero Zaragoza.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Tándem" Zaragoza.
2. **Email (respaldo)** → sin email público. Formulario tandemgrupo.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Los números del fin de semana, el lunes".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 7. Grupo Servera (Palma, hostelería)
add(
    "grupo-servera",
    dossier="""# Dossier: Grupo Servera — Mallorca
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Servera opera en hostelería con sede en Marratxí (Mallorca). Operador local mallorquín.

- **Sector:** Hostelería
- **Tamaño:** Regional Mallorca
- **Sede:** Carrer Celleters, Marratxí

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | gruposervera.com |

## 3. Madurez digital
- Web presente (título vacío en captura inicial). Presencia digital limitada.

## 4. Puntos de dolor
1. Reservas multicanal + temporada alta con turismo internacional.
2. Reporting multi-local.
3. Reseñas.
4. Compras y escandallos.

## 5. Contacto decisor
- Marca familiar Servera probable. Buscar: `"Grupo Servera" Mallorca`.
- Perfiles: fundador/CEO.

## 6. Ángulo de entrada
Reconocimiento del operador mallorquín + label sobre estacionalidad + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Mayo entra con reserva llena",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Servera mirando operadores hosteleros en Mallorca y me paró el perfil local. Me imagino que mayo os entra ya con reserva prácticamente llena y la pregunta ya no es si va a haber demanda, es si los locales están preparados para absorberla sin que la gestión de reservas, comentarios y reseñas acabe cayendo otra vez sobre el móvil del encargado fuera de horario.",
        "¿Cómo os estáis preparando hoy para el pico de temporada?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — grupo-servera

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Servera%22%20Mallorca&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Grupo Servera

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Fundador/CEO / Director de Operaciones
- **Notas:** Hostelería Mallorca. Marratxí.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Servera" Mallorca.
2. **Email (respaldo)** → sin email público. Formulario gruposervera.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Mayo entra con reserva llena".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 8. Automotor Llobregat (Barcelona)
add(
    "automotor-llobregat-s-a",
    dossier="""# Dossier: Automotor Llobregat S.A. — Barcelona
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Automotor Llobregat es un concesionario en Barcelona con sede en Sant Martí (Joan d'Àustria). Perfil de concesionario tradicional catalán.

- **Sector:** Automoción
- **Tamaño:** Mediano regional
- **Sede:** Joan d'Àustria, Sant Martí, Barcelona

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | automotor.cat |

## 3. Madurez digital
- Web corporativa. DMS estándar. Presencia en portales.

## 4. Puntos de dolor
1. Seguimiento de lead (showroom + portales).
2. Entrega y documentación.
3. Citas de taller.
4. Reporting comercial.

## 5. Contacto decisor
- No identificado. Buscar: `"Automotor Llobregat" Barcelona`.
- Perfiles: Director General, Director Comercial.

## 6. Ángulo de entrada
Reconocimiento del concesionario catalán + label sobre seguimiento post-visita + pregunta calibrada.

## 7. Score
70.
""",
    asunto="La llamada que queda pendiente del miércoles",
    cuerpo=[
        "Hola,",
        "Vi Automotor Llobregat mirando concesionarios con base en Sant Martí. Tengo la sensación de que en un concesionario así lo que se escapa por el fondo del embudo no es la visita, es la llamada pendiente: el cliente que se fue el miércoles sin cerrar, al que el comercial pensaba llamar el jueves y acaba llamando la semana siguiente porque dentro se cruza otra venta más urgente.",
        "¿Cómo estáis hoy evitando que esos hilos se enfríen entre comerciales?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — automotor-llobregat-s-a

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Automotor%20Llobregat%22%20Barcelona&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Automotor Llobregat

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Director Comercial
- **Notas:** Concesionario Barcelona Sant Martí.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Automotor Llobregat" Barcelona.
2. **Email (respaldo)** → sin email público. Formulario automotor.cat tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "La llamada que queda pendiente del miércoles".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 9. Maxus Sevilla Grupo Terry (Sevilla)
add(
    "maxus-en-sevilla-grupo-terry-automocion",
    dossier="""# Dossier: Maxus Sevilla — Grupo Terry Automoción
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Maxus Sevilla es la concesión Maxus (vehículos comerciales eléctricos y diésel) de Grupo Terry en Sevilla. Av. Roberto Osborne. Enfoque claro a flotas y pymes con necesidades comerciales, segmento B2B.

- **Sector:** Automoción / vehículo comercial
- **Tamaño:** Especialista Terry Sevilla
- **Sede:** Av. Roberto Osborne, Sevilla

## 2. Datos clave
| Campo | Valor |
|---|---|
| Web | maxussevilla.com |
| Marca | Maxus |
| Grupo | Terry |

## 3. Madurez digital
- Web con stock comercial. Marketing orientado a flotas y autónomos.

## 4. Puntos de dolor
1. Cualificación B2B: autónomo puntual vs. flota corporativa.
2. Preparación de TCO para flotas.
3. Entrega vehículo comercial (rotulación, preparación).
4. Posventa flotas.

## 5. Contacto decisor
- Parte de Terry. Buscar: `"Maxus Sevilla" OR "Grupo Terry" Sevilla comerciales`.
- Perfiles: Gerente Maxus Sevilla, Director Comercial Terry.

## 6. Ángulo de entrada
Reconocimiento del enfoque flotas + label sobre cualificación B2B + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un autónomo y una flota de ocho",
    cuerpo=[
        "Hola,",
        "Vi Maxus Sevilla dentro de Grupo Terry mirando especialistas en vehículo comercial en Andalucía. Me imagino que en este segmento las dos conversaciones que entran por la misma web son muy distintas: un autónomo que quiere reemplazar la furgoneta vieja y una empresa que está pensando en renovar ocho de golpe, y ambas suelen llevar al mismo formulario de contacto que responde la misma persona con el mismo guion.",
        "¿Cómo estáis separando hoy esos dos tipos de lead?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — maxus-en-sevilla-grupo-terry-automocion

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Maxus%22%20%22Grupo%20Terry%22%20Sevilla&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — Maxus Sevilla (Grupo Terry)

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Gerente Maxus Sevilla / Director Comercial Grupo Terry
- **Notas:** Concesión Maxus Sevilla. Vehículo comercial. Parte de Grupo Terry.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Maxus" + "Grupo Terry" Sevilla.
2. **Email (respaldo)** → sin email público. Formulario maxussevilla.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un autónomo y una flota de ocho".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)

# -- 10. Concesionario oficial KGM Grupo Ortasa (Bilbao)
add(
    "concesionario-oficial-kgm-grupo-ortasa",
    dossier="""# Dossier: KGM Grupo Ortasa — Bilbao
**Fecha:** 2026-04-20
**Preparado para:** Aritz Abuin — AI Solutions Architect

---

## 1. Resumen ejecutivo
Grupo Ortasa opera la concesión oficial KGM (antigua SsangYong) en Bizkaia, con sede en Luis Briñas (Basurtu-Zorrotza, Bilbao). Concesionario de referencia en Bizkaia según su propia web.

- **Sector:** Automoción / concesionario KGM
- **Tamaño:** Regional Bizkaia
- **Sede:** Luis Briñas, Basurtu-Zorrotza, Bilbao

## 2. Datos clave
| Campo | Valor |
|---|---|
| Marca | KGM (antes SsangYong) |
| Web | grupoortasa.com |

## 3. Madurez digital
- Web corporativa con stock. Marca en transición de identidad (SsangYong → KGM), lo cual añade ruido comunicativo.

## 4. Puntos de dolor
1. Educación del cliente sobre cambio de marca (SsangYong → KGM).
2. Captación + seguimiento de lead.
3. Posventa de parque SsangYong existente.
4. Reporting comercial.

## 5. Contacto decisor
- Marca familiar Ortasa. Buscar: `"Grupo Ortasa" Bilbao KGM`.
- Perfiles: Director General, Gerente.

## 6. Ángulo de entrada
Reconocimiento del reto del renombrado SsangYong→KGM + label sobre educación de cliente + pregunta calibrada.

## 7. Score
70.
""",
    asunto="Un cliente que aún busca SsangYong",
    cuerpo=[
        "Hola,",
        "Entré en Grupo Ortasa mirando la concesión KGM en Bilbao y me quedé pensando en el cambio de marca. Parece como si el reto diario no esté tanto en el producto, sino en que mucho cliente todavía entra a Google buscando SsangYong y llega a la web con una pregunta de partida ya confusa sobre si son vosotros, y esa pequeña fricción la está resolviendo hoy el equipo comercial caso por caso por teléfono.",
        "¿Cómo estáis gestionando hoy esas primeras consultas con la transición SsangYong a KGM?",
        "Un saludo,\nAritz",
    ],
    li_md="""# LinkedIn Paso 1 — concesionario-oficial-kgm-grupo-ortasa

**Fecha:** 2026-04-20
**Tipo:** Connection SIN NOTA

---

Enviar connection SIN nota. Decisor pendiente.

Búsqueda sugerida:
- https://www.linkedin.com/search/results/people/?keywords=%22Grupo%20Ortasa%22%20Bilbao&origin=GLOBAL_SEARCH_HEADER
""",
    contacto="""# Contacto — KGM Grupo Ortasa

**Fecha de generación:** 2026-04-20

## Destinatario
- **Nombre:** ⚠ Identificar antes de enviar
- **Cargo:** Director General / Gerente
- **Notas:** Concesión KGM Bizkaia. Marca familiar Ortasa.

## Canal recomendado
1. **LinkedIn (preferente)** → pendiente. Búsqueda "Grupo Ortasa" Bilbao.
2. **Email (respaldo)** → sin email público. Formulario grupoortasa.com tras identificar decisor.

## Qué enviar
- LinkedIn: `linkedin-paso1.md` (connection sin nota).
- Email: `email-t1.html` al conseguir dirección directa. Asunto: "Un cliente que aún busca SsangYong".

## Acciones pendientes del usuario antes de enviar
- Identificar decisor en LinkedIn.
- Conseguir email directo.
- Sustituir "Hola," por "Hola {nombre},".
""",
)
