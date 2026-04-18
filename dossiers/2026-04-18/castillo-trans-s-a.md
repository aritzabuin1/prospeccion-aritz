# Dossier: Castillo Trans S.A.
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Castillo Trans S.A. es una transportista de referencia en el sur peninsular, con más de 40 años operando transporte por carretera a temperatura dirigida entre España y el resto de Europa. Sede en Benejúzar (Alicante), flota propia de ~200 camiones Renault Trucks T520 y otros ~400 subcontratados, plantilla en torno a 390-400 empleados (2024) y facturación >40 M€ con crecimiento sostenido (+17% interanual). Líderes en la provincia de Alicante en su sector y 52º a nivel nacional. Certificaciones IFS Logistics, QS y PRODAT apuntan a clientes del sector alimentario/perecedero que exigen trazabilidad estricta. Perfil de gran cuenta operativa con presión fuerte en planificación de rutas, tracking de temperatura y comunicación con cargadores en varios idiomas.

- **Sector:** Logística y transporte frigorífico internacional
- **Tamaño:** ~400 empleados · facturación >40 M€ · flota propia +200 vehículos
- **Sede:** Benejúzar, Alicante (oficinas y naves propias)

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Castillo Trans, S.A. |
| CIF | A03054715 (registro mercantil Alicante) |
| Año fundación | Más de 40 años de actividad |
| Actividad | Transporte por carretera de mercancía a temperatura controlada (nacional + EU) |
| Empleados | ~392-399 (2024), 83% fijos |
| Facturación | >40 M€ (rango 43,1 M€ reportados en 2018; +17,3% último ejercicio) |
| Flota | ~200 propios + ~400 subcontratados (todos Renault T520) |
| Certificaciones | IFS Logistics, QS, PRODAT |
| Idiomas web | ES, EN, DE, FR |
| Teléfono | +34 966 736 737 |
| Web | castillotrans.com / castillotrans.eu |

## 3. Madurez digital

- Web multilingüe operativa (4 idiomas), orientada a cargadores industriales europeos. Sistema de monitorización online de temperatura de la carga, señal de que ya consumen telemetría de los camiones.
- Perfil LinkedIn corporativo activo con reclutamiento continuo (crecimiento sostenido de plantilla). YouTube y Facebook menos cuidados.
- Certificación PRODAT (protección de datos sectorial del transporte) indica procesos documentales maduros, pero típicamente soportados por ERP de transporte (probable Transporteca/Tisa/SAP TM) + Excel + email para lo no cubierto.
- No hay evidencia pública de proyectos de IA, RAG interno, dashboards consolidados ni automatización de tramitación documental. Sector clásico donde el margen de mejora con IA aplicada es enorme.
- Flota 100% Renault T520 con telemática propia: existe infraestructura de datos en tiempo real, pero la explotación analítica y operativa de esos datos suele estar subexplotada.

## 4. Puntos de dolor (hipótesis priorizadas)

1. **Tramitación documental de exportación frigorífica.** CMR, albaranes, registros de temperatura, incidencias de frío, certificados sanitarios por país. Mucho papel y Excel por cada viaje; susceptibles a orquestación con IA (extracción, validación, archivo).
2. **Planificación de rutas y subcontratación.** 600 camiones totales con 2/3 subcontratados implica una operativa de asignación/confirmación/seguimiento que vive en llamadas y correos. Hueco claro para agentes que coordinen disponibilidad.
3. **Atención al cargador multilingüe.** Clientes alemanes, franceses e ingleses preguntando por ETAs, estado de carga y temperatura por email y teléfono. RAG multilingüe + integración con ERP/telemetría descarga al equipo de tráfico.
4. **Reporting operativo consolidado.** Margen por ruta, por cliente, por subcontratista, por lane. Suele estar fragmentado entre ERP, telemetría y hojas del controller. Panel unificado habilita decisiones más finas en un sector de márgenes estrechos.
5. **Gestión de incidencias de cadena de frío.** Alertas de temperatura fuera de rango que hoy probablemente se reciben por SMS o pantalla y se gestionan reactivamente. Agente que clasifique, escale y documente automáticamente.
6. **Reclutamiento continuo de conductores.** Plantilla de 400 con rotación del sector: cribado de CVs, respuestas iniciales, agendado. Automatizable en gran parte.

## 5. Contacto decisor

- **Dirección General / CEO** — búsqueda en LinkedIn por "Castillo Trans" + "CEO/Director General". Estructura familiar típica del transporte español.
- **Director de Operaciones / Tráfico** — propietario del dolor 1, 2 y 5. Perfil más técnico, accesible por LinkedIn.
- **Director Financiero / Controller** — propietario del dolor 4.
- LinkedIn empresa: es.linkedin.com/company/castillo-trans-s-a (activo).
- Canal secundario: teléfono +34 966 736 737 (centralita) y formulario web.
- Recomendación: primer toque por LinkedIn al Director de Operaciones/Tráfico; email como respaldo si no responde en 7 días.

## 6. Ángulo de entrada

- **Propuesta:** orquestación documental del ciclo de exportación frigorífica (extracción de CMR/albaranes, matching con orden de transporte, archivo estructurado) + panel operativo consolidado cruzando telemetría, ERP y finanzas. Piloto acotado a una lane europea en 4-6 semanas.
- **Mensaje:** reconocimiento del posicionamiento (+40 años, liderazgo provincial, IFS+QS) + hipótesis específica (tramitación documental multilingüe por viaje) + pregunta calibrada sobre cómo lo resuelven hoy. Sin caso. Sin pitch.
- **Canal:** LinkedIn al Director de Operaciones como primario. Email centralita como respaldo con asunto personal y curioso.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (transporte frigorífico, procesos repetitivos, multilingüe) | 25% | 9 | 2,25 |
| Tamaño adecuado (gran cuenta regional, decisión accesible) | 15% | 9 | 1,35 |
| Madurez digital (telemetría sí, explotación no) | 15% | 8 | 1,20 |
| Señales de dolor (crecimiento rápido, flota grande, certificaciones) | 20% | 8 | 1,60 |
| Accesibilidad del decisor | 10% | 7 | 0,70 |
| Capacidad de pago (40 M€ facturación, crecimiento 17%) | 15% | 9 | 1,35 |
| **Total** | 100% | | **8,45 / 10** |

**Veredicto:** Lead A. Tamaño, sector y señales de dolor encajan 1:1 con el portfolio. El crecimiento continuado de plantilla y flota sugiere fricciones operativas que escalan más rápido que la estructura administrativa. Proceder con identificación del Director de Operaciones o Tráfico esta semana.
