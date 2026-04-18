# Dossier: Grupotel
**Fecha:** 2026-04-17
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupotel es una cadena hotelera familiar de origen balear con décadas de trayectoria, presente principalmente en Mallorca, Menorca, Ibiza y con extensión a Cataluña (Barcelona). Opera un portfolio diversificado que cubre hoteles urbanos, resorts familiares, establecimientos sólo adultos y apartamentos, con una base operativa muy marcada por la estacionalidad turística balear y el mix de cliente internacional (UK, Alemania, Francia, nórdicos).

- **Sector:** Hostelería -- cadena hotelera multi-establecimiento (resort, urbano, apartamentos)
- **Tamaño:** Medio-grande. Más de 30 establecimientos entre Baleares y Cataluña (rango aproximado, pendiente de verificar en su web). Plantilla estimada >1.000 empleados en temporada alta
- **Sede:** Can Picafort / Platja de Palma (Mallorca, Illes Balears). Hotel detectado en la señal: Grupotel Playa de Palma Suites & Spa (07600)

Encaje fuerte con el caso de referencia de Aritz en cadena multi-establecimiento (>100 locales): arquitectura BI centralizada, atención multicanal multiidioma y RAG sobre documentación operativa / FAQs de clientes.

---

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social (estimada) | Grupotel Dos, S.A. / Grupo Grupotel (varias sociedades operadoras, pendiente verificar) |
| Web | https://www.grupotel.com |
| Sede | Mallorca (Illes Balears) |
| Zona de operación | Mallorca, Menorca, Ibiza, Barcelona |
| Sector | Hostelería -- cadena hotelera |
| Nº establecimientos | 30+ (rango, a verificar) |
| Tipología | Resort familiar, sólo adultos, urbano, apartamentos, spa |
| Idiomas web | ES / EN / DE / FR (típico del segmento, verificar) |
| Motor de reservas | Propio integrado en web + OTAs (Booking, Expedia, TUI, hoteles alemanes) |
| Estacionalidad | Alta -- mayoría de establecimientos abren abril-octubre |
| Presencia corporativa | Web corporativa unificada bajo marca Grupotel |

> Cifras de facturación, empleados y número exacto de hoteles no verificadas en esta iteración (WebFetch no disponible). Confirmar antes de reunión vía eInforma / Axesor / web oficial.

---

## 3. Madurez digital

**Nivel estimado: Medio.** Típico de cadena hotelera familiar consolidada de Baleares: web corporativa profesional, motor de reservas propio, presencia fuerte en OTAs y channel manager operativo. Pero con gaps clásicos del sector:

- Web con reservas online funcional y multi-idioma -- **tienen músculo digital básico**
- CRM hotelero probable (tipo Revinate, Hotelinking o propio) pero **infrautilizado para personalización real**
- Channel manager + PMS tradicional (probablemente Oracle Opera, Protel o similar). Integraciones vía iCal/API, no event-driven
- Email marketing transaccional sí, pero **segmentación por comportamiento = punto débil habitual**
- Atención al cliente pre-estancia y post-estancia: mayoritariamente humana, con horario limitado y cuellos de botella en picos de temporada
- **Data silos**: PMS, channel manager, CRM, reputación online (TrustYou/ReviewPro) y BI financiero rara vez hablan entre sí en este tipo de cadenas
- IA generativa y RAG: prácticamente sin explotar. Es donde hay más margen de valor inmediato

---

## 4. Puntos de dolor

1. **Atención multiidioma 24/7 pre-estancia y en estancia.** Cliente UK/DE/FR/nórdico pregunta a horas imposibles sobre horarios de spa, transfer, tipos de habitación, restricciones de mascotas, política de niños, check-in anticipado. Recepción de cada hotel resuelve a mano, en temporada alta se satura. Coste oculto enorme y NPS se resiente.

2. **Gestión operativa multi-hotel fragmentada.** 30+ establecimientos con directores de hotel independientes, cada uno con sus Excel, sus protocolos, sus métricas. Dirección corporativa recibe reportes desacompasados, no en tiempo real. Decisiones de revenue, ocupación y staffing se toman con datos con 1-7 días de retraso.

3. **Respuesta a opiniones online (Booking, Google, TripAdvisor).** Volumen altísimo en temporada, respuesta lenta, tono inconsistente entre hoteles. Afecta directamente al ranking en OTAs y al pricing que puede sostener la cadena.

4. **Onboarding y formación de plantilla estacional.** Cada abril-mayo entran cientos de trabajadores temporales que necesitan conocer protocolos, manuales, normas de cada hotel. Formación presencial cara e inconsistente. Asistente RAG sobre manuales internos = win inmediato.

5. **Revenue management reactivo, no predictivo.** Pricing dinámico por OTA existe, pero la toma de decisión sigue siendo manual en muchos puntos: forecast de demanda, ajuste de allotments, detección de eventos locales que mueven la curva. Modelos propios predictivos encima del histórico del PMS = palanca clara.

6. **Up-sell y personalización en estancia.** Cliente llega, se le asigna habitación estándar, y la oportunidad de upgrade pagado, booking de spa, excursiones y F&B se pierde porque nadie le habla en el momento adecuado ni en su idioma. Pre-arrival journey + conserjería automática vía WhatsApp/email = palanca directa sobre RevPAR.

7. **Gestión documental corporativa (RRHH, compliance, protocolos).** Cadenas familiares suelen acumular 20 años de documentación en Sharepoint/Drive sin búsqueda semántica. Un RAG interno lo pone al alcance de directores de hotel en segundos.

---

## 5. Contacto decisor

Para una cadena hotelera de este tamaño, la prospección debe apuntar a tres perfiles en paralelo y que ellos mismos decidan quién lidera:

- **Director Corporativo / Director General**: dueño del P&L consolidado. Si el mensaje habla de RevPAR, ocupación y coste por reserva, entra.
- **Director de Sistemas / IT Manager**: evaluador técnico. Clave para viabilidad y para integrar con PMS/channel manager.
- **Director de Operaciones / Director de Hoteles**: dueño del dolor operativo diario multi-hotel. Suele ser el sponsor real de proyectos de este tipo.
- Alternativa viable: **Director de Marketing / E-commerce / Revenue** (el chatbot y la personalización suelen caer aquí cuando no hay CIO claro).

**Vías de búsqueda recomendadas:** LinkedIn Sales Navigator filtrando por empresa "Grupotel" + cargos "Director / Head / Responsable" en IT, Operaciones, Revenue, Marketing y Corporativo. eInforma para ver administradores de las sociedades del grupo (suelen ser miembros de la familia fundadora).

> Nombres concretos: pendiente validar con LinkedIn antes del primer contacto. No inventar.

---

## 6. Ángulo de entrada

- **Propuesta:** Partir de UN dolor concreto, medible y estacional -- el asistente de atención pre-estancia y en-estancia multiidioma 24/7 sobre WhatsApp/email/chat de la web, con RAG sobre las FAQs y protocolos de cada hotel. Valor cuantificable: reducir X% de consultas que hoy absorbe recepción, mejorar tiempo de respuesta de horas a segundos, capturar upsell (spa, transfer, upgrade) en el journey. Fase 2 natural: dashboard operativo multi-hotel (Power BI sobre datos del PMS + channel manager + reputación online) para que dirección corporativa vea la cadena en tiempo real.

- **Mensaje:** Reconocimiento genuino de Grupotel como cadena consolidada de Baleares con operación multi-establecimiento. Mención a un caso anonimizado: "ayudé a una cadena de más de 100 establecimientos a unificar sus datos en Power BI y a atender a sus clientes por WhatsApp/email con un asistente con IA sobre su propia documentación -- les cambió la operación." Pregunta honesta: "¿cómo estáis resolviendo hoy la atención multiidioma fuera de horario en temporada alta?" Sin listar datos ni ficha técnica -- tono conversación.

- **Canal:** LinkedIn como primer toque (nota de conexión personal <200 caracteres al Director de Operaciones o IT). Email corporativo como segundo toque 72h después si no hay respuesta, con asunto curioso y personal (nunca "Propuesta de automatización"). Si hay contacto, videollamada de 30 min sin pitch: diagnóstico.

---

## 7. Score

| Criterio | Peso | Nota | Comentario |
|---|---|---|---|
| Encaje vertical (cadena multi-local) | 25% | 10 | Réplica casi directa del caso de cadena >100 establecimientos |
| Tamaño / capacidad de pago | 20% | 8 | Cadena familiar consolidada, P&L estable aun con estacionalidad |
| Dolor visible y urgente | 20% | 9 | Temporada 2026 arranca ya -- la presión operativa es inminente |
| Madurez digital (ni verde ni saturada) | 15% | 8 | Tienen base digital, no tienen IA -- sweet spot |
| Accesibilidad del decisor | 10% | 6 | Empresa familiar, entrada requiere paciencia y red |
| Replicabilidad / caso futuro | 10% | 9 | Si entra, abre sector hotelero balear entero |

**Score final: 8.6 / 10**

**Veredicto:** Lead prioritario. Encaje excepcional con el caso de referencia de cadena multi-establecimiento y con ventana temporal óptima (abril = apertura de temporada, el dolor operativo se dispara en semanas). Aprobar para generación de mensajes y contacto inmediato. Antes del envío: verificar en LinkedIn el nombre concreto del Director de Operaciones / IT y el número exacto de hoteles en grupotel.com para que el primer mensaje no tenga imprecisiones.
