# Dossier: Grupo Médico Siete Palmas
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupo Médico Siete Palmas forma parte de una red canaria de centros de reconocimiento médico-psicotécnico (junto con Grupo Médico Noroeste en Gáldar) operada bajo el paraguas comercial medicaldeconductores.com. Actividad centrada en certificados para permisos de conducir, armas, náutica, seguridad privada, salud laboral y deportiva. Equipo multidisciplinar (médicos, psicólogos, oftalmólogo, laboratorio en Noroeste) y tres centros en Gran Canaria. Volumen alto de pacientes-paso (renovaciones en masa), agendas apretadas en franja mañana/tarde, procesos repetitivos de muy alto peso administrativo. Perfil típico de cadena sanitaria pequeña que factura por volumen y pelea con papel, agenda y tramitación con la DGT.

- **Sector:** Salud — centros de reconocimiento médico-psicotécnico (CRC)
- **Tamaño:** Red de 3 centros en Gran Canaria · ~15-30 empleados estimados entre centros
- **Sede Siete Palmas:** Av. Pintor Felo Monzón, 7 Bajo — Las Palmas de Gran Canaria

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Grupo Médico Siete Palmas (marca comercial de la red medicaldeconductores) |
| CIF | — (no localizado) |
| Año fundación | — (centro consolidado, web corporativa unificada reciente) |
| Actividad | Certificados médicos conductores/armas/náutica/seguridad privada/laboral/deportiva |
| Empleados | Estimado 15-30 en red (médicos, psicólogos, oftalmólogo, administrativo) |
| Facturación | Hipótesis sectorial: CRC con 3 sedes activas, 15.000-30.000 reconocimientos/año |
| Web | reconocimientomedicolaspalmas.com (redirige a medicaldeconductores.com) |
| Teléfono Siete Palmas | +34 928 483 786 |
| Email | sietepalmas@medicaldeconductores.com |
| Centros hermanos | Grupo Médico Noroeste (Gáldar) · Grupo Médico Schamann |

## 3. Madurez digital

- Web unificada para la red (medicaldeconductores.com) con dominio legacy redirigiendo. Indica esfuerzo de consolidación de marca reciente pero sin capa transaccional.
- Agenda: presencia en Doctoralia y Medical-Admin sugiere uso de plataformas de cita online de terceros; no hay CRM propio visible.
- Fotografía gratuita in situ y tramitación gratuita con DGT mencionadas como diferenciales — proceso manual con impresora, cámara y envío físico/telemático de expedientes.
- No se detectan señales de app móvil, portal paciente, automatizaciones de recordatorio vía WhatsApp, ni tableros de producción. Perfil típico: Excel + correo + gestor telefónico.

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Gestión de agenda multi-centro.** Tres sedes, franjas mañana/tarde, picos previos a caducidades masivas de carnets. Hueco para asistente de reservas por WhatsApp que valide documentación antes de dar cita y reduzca no-shows.
2. **Tramitación DGT y expediente digital.** Cada reconocimiento genera un paquete de documentos (fotos, pruebas, informe, tasa) que hoy viajan entre recepción, facultativo y DGT. Orquestación documental con IA quita horas/día al administrativo.
3. **Recordatorios de renovación a pacientes existentes.** Cada carnet tiene fecha de caducidad conocida. Un motor de notificaciones (email + WhatsApp) con el histórico del paciente genera recurrencia sin esfuerzo comercial.
4. **Reporting operativo y financiero por centro.** Volumen de reconocimientos por tipo, ocupación de agendas, facturación por sede y facultativo. Suele vivir en Excel; un Power BI ligero con ingesta diaria cambia la conversación de gestión.
5. **Atención telefónica repetitiva.** Preguntas de horario, precio por tipo de permiso, documentación a traer, ubicación. Voicebot/chatbot RAG sobre la web de la red descarga al mostrador.
6. **Alta de pacientes y firma de consentimientos.** Formularios en papel con transcripción posterior — candidato claro a formulario digital con OCR de DNI y firma en tablet.

## 5. Contacto decisor

- **Dirección / Gerencia de la red** — no identificada públicamente. Buscar en LinkedIn "medicaldeconductores", "Grupo Médico Siete Palmas", "Grupo Médico Noroeste" y nombres propios asociados a la sociedad mercantil.
- **Responsable médico / facultativo titular** — perfil clínico, probable codecisor en temas de agenda y DGT.
- Canales: email sietepalmas@medicaldeconductores.com (bajo ratio, genérico) · teléfono 928 483 786 · LinkedIn una vez identificado el gerente.
- Recomendación: primer toque por email directo al buzón del centro con asunto curioso (gerencia suele leerlo) y, en paralelo, búsqueda LinkedIn del gerente para tocar ahí con Paso 1 sin nota.

## 6. Ángulo de entrada

- **Propuesta:** automatizar el ciclo completo de paciente-renovación — recordatorio antes de caducidad + reserva por WhatsApp con validación documental + expediente digital en la visita + envío telemático a DGT + encuesta post-servicio. Piloto en Siete Palmas 4-6 semanas, medir horas liberadas por administrativo y tasa de renovación recuperada de pacientes antiguos. Extensión a Noroeste y Schamann una vez validado.
- **Mensaje:** observación específica sobre la red (tres centros, fotografía gratis, DGT) + label del dolor (el ratio entre minutos de consulta y minutos de tramitación administrativa) + pregunta calibrada sobre cómo lo están resolviendo hoy.
- **Canal:** email al buzón del centro como canal principal; LinkedIn al gerente en paralelo una vez identificado. No llamar en frío.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (procesos repetitivos, alto volumen administrativo) | 25% | 9 | 2,25 |
| Tamaño adecuado (red pequeña, decisión rápida) | 15% | 6 | 0,90 |
| Madurez digital (margen alto de mejora) | 15% | 8 | 1,20 |
| Señales de dolor (tramitación DGT, agenda multi-sede) | 20% | 8 | 1,60 |
| Accesibilidad del decisor | 10% | 6 | 0,60 |
| Capacidad de pago (volumen alto, ticket bajo pero recurrente) | 15% | 5 | 0,75 |
| **Total** | 100% | | **7,3 / 10** |

**Veredicto:** Lead B. Encaje operativo claro (automatización de proceso administrativo repetitivo con DGT y agenda), pero capacidad de ticket limitada por ser red pequeña. Buen candidato a piloto acotado con ROI medible en horas de administrativo. Proceder con primer toque por email esta semana y localizar gerente en LinkedIn.
