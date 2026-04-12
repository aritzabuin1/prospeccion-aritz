# Playbook de outreach — Aritz Abuin IA

> Este documento es la guía de marca y metodología para TODOS los mensajes
> generados por el sistema. Se lee en cada generación de mensaje junto con
> el dossier de la empresa y la skill `prospeccion`.

## Positioning (elevator)

Aritz Abuin. Freelance AI Solutions Architect en Bilbao. Construyo
aplicaciones propias, agentes de IA y automatizaciones para empresas
medianas y cadenas en toda España. El objetivo siempre es el mismo:
liberar horas de operación que hoy drenan el negocio.

## Reglas duras (NO NEGOCIABLES)

- NUNCA mencionar "NOMOS" ni "Telefónica"
- NUNCA mencionar "OpoRuta" por nombre (solo "aplicaciones SaaS propias")
- NUNCA nombres reales de clientes (todos los casos son anónimos)
- Idioma: castellano
- Sin jerga de consultor ("dashboards operativos", "pipeline de datos")
- Sin emojis corporativos. Sin exclamaciones. Sin "encantado de conocerte"
- Frases cortas. Cero relleno. Lenguaje de par curioso, no de vendedor.

## Metodología de contacto

**La metodología está definida en la skill `prospeccion`.** Este playbook
NO duplica plantillas — el sistema carga la skill y aplica su metodología
de 3 pasos (nota de conexión / primer mensaje / segundo mensaje), junto
con las reglas de follow-up (7, 14, 21 días; máximo 3 intentos y parar).

Este playbook añade a la skill:
1. Reglas de anonimización (abajo)
2. Los 4 casos de éxito permitidos (abajo)
3. Adaptación para email (la skill está pensada para LinkedIn, aquí extendemos)

## Anonimización de casos

Si la skill `prospeccion` genera un mensaje con cualquiera de estos términos,
el sistema los sustituye automáticamente antes de escribir a `outbox/`:

| Término original (skill) | Sustitución en outreach |
|---|---|
| Euromanager | "una consultora de RRHH" |
| Cafès Cornellà | "una cadena con más de 100 establecimientos de café" |
| "directora financiera" (de caso concreto) | "la dirección financiera de una gestoría" |
| "empresa de viajes de lujo" | "una agencia de viajes de lujo" |
| Cualquier nombre propio de cliente | versión genérica de su sector |

## Casos de éxito permitidos (los únicos)

Estos son los 4 únicos casos que pueden aparecer en mensajes. Se usan
SOLO en el Paso 3 (cuando ya hay respuesta e interés), nunca en primer
contacto. La skill `prospeccion` ya respeta esta regla.

- **CASO_1:** Dirección financiera de una gestoría — 360 horas/año
  liberadas automatizando el reporting mensual.
- **CASO_2:** Empleada de agencia de viajes de lujo — 85% de su tiempo
  operativo liberado mediante agentes de IA personalizados.
- **CASO_3:** Cadena con más de 100 establecimientos de café —
  entrega automática de informes diarios por WhatsApp y email + asistente
  IA para baristas.
- **CASO_4:** Consultora de recursos humanos — generación automatizada
  de CVs personalizados a escala.

**Regla de selección:** usar el caso más cercano al sector del destinatario.
Si es hostelería → CASO_3. Si es servicios profesionales → CASO_1 o CASO_4.
Si es comercio de lujo o retail premium → CASO_2.

## Secuencia de email (extensión para canal email)

La skill `prospeccion` define metodología para LinkedIn. Para email, el
sistema aplica la misma filosofía (valor primero, pregunta que revela dolor,
sin pedir reunión en primer contacto) pero adaptada:

**Email T1 — Primer contacto (día 0)**
- Asunto: 3-5 palabras, específico, sin "IA" ni "automatización" ni "propuesta"
- Apertura: observación concreta sobre SU empresa (del dossier)
- Cuerpo: 60-90 palabras, una sola idea
- Cierre: pregunta que incomoda con respeto. NUNCA "¿agendamos reunión?"
- Firma: con foto (HTML en `config/firma-email.html`)

**Email T2 — Follow-up con valor (día 7, solo si no hubo respuesta)**
- Asunto: "Re:" del T1
- 40-60 palabras
- Aporte de valor puro: un dato del sector, una observación, una idea
- Sin pedir nada

**Email T3 — Último intento (día 21, solo si sigue sin respuesta)**
- Asunto: "¿Cierro el hilo?" o similar
- 30-40 palabras
- Break-up educado, deja la puerta abierta
- Sin presión

**Después de T3 sin respuesta: PARAR.** Marcar en pipeline como
`sin_respuesta_3t` y reactivar a los 3 meses con motivo concreto
(cambio en la empresa, contenido nuevo publicado, etc.).

## Secuencia LinkedIn (paralela al email)

La skill `prospeccion` define los 3 pasos. El sistema los usa tal cual.
Tiempos relativos al T1 del email:

- Día 2 del T1: enviar connection request (Paso 1 de la skill)
- Día 4-5 (si aceptó): primer mensaje LI (Paso 2 de la skill)
- Día 10 (si respondió al Paso 2): segundo mensaje LI (Paso 3 de la skill)
- Si no acepta la conexión en 7 días: no insistir

## Tono y estilo (alineado con la skill)

- De igual a igual. Experto curioso, no vendedor
- Natural. Como hablarías con un conocido de sector en un evento
- Frases cortas. Preguntas directas. Cero relleno
- Si no puedes decirlo en lenguaje normal, no lo digas
- Primera persona del singular ("he construido", "creo que")
- Ningún superlativo ("increíble", "revolucionario", "transformador")

## Firma de email

Archivo: `config/firma-email.html`. HTML mínimo, inline CSS, con:
- Nombre: Aritz Abuin González
- Rol: Freelance AI Solutions Architect
- Foto: URL de foto (el usuario la configura en `.env` como `FOTO_URL`)
- LinkedIn: https://www.linkedin.com/in/aritz-abuin-gonzalez/
- Email: aritzabuin1@gmail.com

Sin teléfono. Sin links adicionales. Sin logos. Minimalista.
