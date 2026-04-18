# Dossier: Grupo Concesur
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupo Concesur es uno de los grupos de concesionarios oficiales más grandes de Andalucía, con sede histórica en Sevilla y expansión reciente a Madrid. Lleva más de 50 años en automoción (origen 1973 como concesionario Pegaso y SABA). Hoy representa 17 marcas entre turismos, comerciales, eléctricos y camiones: Mercedes-Benz, Smart, Jaguar, Land Rover, Peugeot, Opel, Fiat, Abarth, Alfa Romeo, Jeep, DS, EVO, Leapmotor, BYD, Lancia, Citroën y Geely. Factura ~450 M€ anuales y emplea a +700 personas. Ofrecen "movilidad 360º": venta, renting/suscripción, taller, recambios y correduría de seguros. Han procesado más de 75.000 vehículos por sus instalaciones. Perfil de grupo grande, multi-marca, con tensión estructural entre sistemas de cada fabricante, posventa intensiva y canal omnicanal.

- **Sector:** Automoción — concesionarios oficiales multi-marca (turismo, eléctrico, camión)
- **Tamaño:** +700 empleados · ~450 M€ facturación · 17 marcas · +75.000 vehículos procesados
- **Sede:** Sevilla (Sevilla capital y Alcalá de Guadaíra), expansión Madrid (camiones Mercedes-Benz)

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social principal | Concesionarios Del Sur, S.A. (+ filiales como Concesur Trucks S.L.) |
| Fundación | 1973 (50+ años en automoción) |
| Actividad | Venta, renting, taller, recambios y correduría de seguros para 17 marcas |
| Empleados | +700 (grupo) · 300 en Concesionarios Del Sur, S.A. |
| Facturación | ~450 M€ anuales (grupo) · +6,73% YoY en Concesionarios del Sur |
| Marcas | Mercedes-Benz, Smart, Jaguar, Land Rover, Peugeot, Opel, Fiat, Abarth, Alfa Romeo, Jeep, DS, EVO, Leapmotor, BYD, Lancia, Citroën, Geely |
| Vehículos procesados | +75.000 históricos |
| Tel | 955 (prefijo Sevilla) |
| Web | grupoconcesur.es |

## 3. Madurez digital

- Web corporativa propia con apartado de "movilidad 360º", localizaciones y contacto. Cada marca tiene además microsites oficiales del fabricante. Presencia LinkedIn corporativa activa.
- Cada fabricante impone su DMS (Dealer Management System) — SAP, Autoline/Keyloop, CDK, Incadea… — de modo que el grupo probablemente convive con 4-6 sistemas distintos simultáneamente y consolida en Excel.
- 17 marcas × múltiples ubicaciones × venta + posventa + renting + seguros = fragmentación extrema de datos de cliente, vehículo, operación y margen.
- Sector automoción español en transición eléctrica + suscripción: presión intensa por optimizar margen por vehículo, rotación de stock y retención en posventa.

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Cuadro de mando consolidado cross-marca.** 17 marcas y 4-6 DMS distintos hacen que la foto única de stock, margen, días-en-patio y ratio venta-posventa viva en Excel manual semanal. BI consolidado que lea de todos los DMS y normalice KPI es el quick-win más claro.
2. **Gestión de leads entrantes multimarca y multicanal.** Formularios web por marca, llamadas, WhatsApp, portales (Coches.net, AutoScout24) generan leads dispersos. Un orquestador que clasifique por marca, enrute al asesor correcto y ejecute primera respuesta en minutos mejora ratio de conversión.
3. **Atención a cliente de posventa (talleres).** Consultas repetitivas sobre cita, estado de reparación, presupuesto, disponibilidad de recambios. Asistente IA sobre sistema de taller + integración WhatsApp descarga al front-desk.
4. **Gestión documental de expedientes de venta y financiación.** Pre-contrato, financiera, seguros, matriculación, entrega — múltiples documentos por operación × 75.000 vehículos. Extracción + checklist automatizado con IA reduce tiempos y errores.
5. **Forecast y rotación de stock multi-marca.** Con 17 marcas y stock de patio significativo, optimizar qué comprar, qué mover entre ubicaciones y qué descontar es tema sensible en un mercado en transición eléctrica.
6. **Conocimiento interno cross-marca para asesores.** Asesor que atiende un Mercedes y un BYD necesita dominar catálogo, financiación y argumentario de ambos: asistente interno tipo copiloto sobre documentación oficial de cada marca.

## 5. Contacto decisor

- **Perfiles LinkedIn objetivo:** "Director General Grupo Concesur", "Director Comercial Grupo Concesur", "Director de Operaciones Grupo Concesur", "Director de Sistemas / CIO Grupo Concesur", "Director Financiero Grupo Concesur".
- Página corporativa LinkedIn: es.linkedin.com/company/grupo-concesur — buena fuente para mapear directiva.
- Canal secundario: formulario web grupoconcesur.es y centralita 955.
- Recomendación: entrada por Director de Operaciones o CIO (propietarios de dolor 1, 2, 5). Director Comercial como alternativa para foco lead-to-cash.

## 6. Ángulo de entrada

- **Propuesta:** consolidar un panel de KPIs cross-marca (stock · margen · lead-to-delivery · tasa posventa) que lea de los distintos DMS + automatizar el triaje de leads entrantes (web/portales/WhatsApp) con enrutamiento automático por marca y franja horaria. Piloto 6-8 semanas sobre 2-3 marcas y escalar al resto. Extensiones: asistente de posventa vía WhatsApp, copiloto cross-marca para asesores.
- **Mensaje:** reconocimiento del tamaño y del movimiento reciente (50 años, 17 marcas, adquisición Madrid camiones) + hipótesis de dolor cross-marca (fragmentación DMS / Excel consolidador).
- **Canal:** LinkedIn a Director de Operaciones o CIO; email corporativo como respaldo.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (automoción multi-marca, backoffice denso) | 25% | 9 | 2,25 |
| Tamaño (grupo grande, ticket alto) | 15% | 10 | 1,50 |
| Madurez digital (fragmentación DMS, margen claro) | 15% | 8 | 1,20 |
| Señales de dolor (17 marcas, 75.000 operaciones, transición EV) | 20% | 9 | 1,80 |
| Accesibilidad del decisor | 10% | 5 | 0,50 |
| Capacidad de pago (450 M€ facturación) | 15% | 10 | 1,50 |
| **Total** | 100% | | **8,75 / 10** |

**Veredicto:** Lead A. Uno de los concesionarios más grandes de Andalucía y en fase expansiva (Madrid). Dolor estructural de fragmentación de sistemas fácilmente atacable. Accesibilidad del decisor es el punto débil (grupo grande, muchas capas): invertir tiempo en mapear directiva antes de lanzar. Proceder esta semana con investigación LinkedIn dirigida.
