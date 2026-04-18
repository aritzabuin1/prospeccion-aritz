# Dossier: Emicela S.A.
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Emicela S.A. es una compañía agroalimentaria canaria fundada en 1963 por Emiliano Arencibia Rivero, con sede en Agüimes (Las Palmas). Torra, envasa y comercializa café, frutos secos, snacks y derivados lácteos, y además distribuye amenities, menaje, textil, uniformes y artículos promocionales a retailers, cadenas de supermercados, grupos HORECA y hoteles. Catálogo de más de 4.000 referencias. Facturación 121,67 M€ (2024, +12,76% YoY) y 298 empleados. Opera filiales en Cabo Verde, República Dominicana, México y Jamaica. Perfil de grupo mediano-grande canario, multiproducto, multicanal, con complejidad logística insular y oceánica: terreno fértil para automatización de backoffice y BI consolidado.

- **Sector:** Agroalimentario — café, alimentación, amenities, menaje y textil para HORECA y GDO
- **Tamaño:** ~298 empleados · 121,67 M€ facturación (+12,76% YoY) · 12 administradores
- **Sede:** Agüimes, Las Palmas de Gran Canaria · Filiales en Cabo Verde, RD, México y Jamaica

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Emicela S.A. |
| Fundación | 15 febrero 1985 (actividad comercial desde 1963) |
| Actividad | Torrefacción, envasado y comercialización de café, alimentación, amenities, menaje, uniformes y publicidad |
| Empleados | ~298 (2024) |
| Facturación | 121,67 M€ (2024, +12,76% YoY) |
| Referencias | +4.000 SKU en catálogo |
| Canales | HORECA, GDO, hoteles, retail, propia |
| Filiales | Cabo Verde, República Dominicana, México, Jamaica |
| Web | emicela.com |
| Sede | Agüimes, Las Palmas de Gran Canaria |

## 3. Madurez digital

- Web corporativa multilingüe (ES/EN) operativa, con catálogo segmentado por línea de negocio y mercado. Tienen landing institucional bien cuidada (señal de inversión en marca) pero no se observa portal B2B de cliente ni e-commerce para HORECA.
- Presencia en LinkedIn corporativo activa, pero la función de compras/HORECA sigue circulando principalmente por email y comercial de campo.
- +4.000 referencias × 5 líneas de negocio × multicanal (HORECA, GDO, retail, propio) × 4 geografías internacionales + España implica un ERP vertical cargado (tipo SAP Business One o similar) pero con mucho Excel alrededor para forecast, precios y márgenes por canal.
- Crecimiento de +12,76% en facturación un año, con exposición a materia prima (café) con volatilidad alta, sugiere tensión real en planificación y margen por SKU-canal.

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Gestión de pedidos HORECA multicanal (email/WhatsApp/teléfono) contra ERP.** Cadenas hoteleras, restaurantes y cafeterías envían pedidos en formatos dispares, con referencias propias y plantillas distintas. Extracción estructurada + matching contra catálogo de 4.000 SKU + volcado al ERP es un clásico que libera horas de backoffice comercial.
2. **Reporting de ventas consolidado producto × canal × geografía × margen.** Con 5 líneas de negocio y 4 filiales internacionales, consolidar rentabilidad por SKU-canal-país suele vivir en Excel manual mensual. BI ligero con refresco diario desbloquea decisiones de pricing y listado.
3. **Atención a clientes HORECA y red de distribución.** Consultas repetitivas (disponibilidad, ficha técnica, plazos, copia de albarán, estado de pedido). RAG multilingüe sobre catálogo + integración ERP descarga al equipo comercial.
4. **Planificación de compra de café y forecast por campaña.** Precio del café en máximos históricos 2024-2026. Mejor forecast de demanda por SKU reduce rotura y obsolescencia, y permite comprar mejor.
5. **Gestión documental de exportación a filiales y terceros países.** Documentación aduanera, certificados sanitarios, registros de lote para Cabo Verde, RD, México, Jamaica. Orquestación documental con IA sobre carpetas operativas.
6. **Onboarding y formación de equipo comercial en catálogo amplio.** +4.000 referencias es mucho que memorizar; asistente interno tipo copiloto sobre ficha de producto reduce curva y errores.

## 5. Contacto decisor

- **Perfiles LinkedIn a buscar:** "Director General Emicela", "Director Comercial Emicela", "Director de Operaciones Emicela", "Director de Sistemas / IT Emicela". Con 298 empleados y 12 administradores, hay estructura directiva real a mapear.
- Página corporativa de empresa en LinkedIn activa (es.linkedin.com/company/emicela-sa) como punto de entrada para identificar nombres.
- Canal secundario: web corporativa (formulario) y centralita sede Agüimes.
- Recomendación: entrada por Director Comercial o Director de Operaciones (propietarios de dolor nº 1, 2 y 4). Director General solo si estos dos no responden.

## 6. Ángulo de entrada

- **Propuesta:** automatizar la entrada de pedidos HORECA desde email/WhatsApp al ERP y montar panel consolidado de márgenes por SKU × canal × filial. Piloto 4-6 semanas con ROI medible en horas liberadas al equipo comercial y reducción de errores de pedido. Extensiones: RAG sobre catálogo de 4.000 referencias y asistente interno para fuerza comercial.
- **Mensaje:** reconocimiento del posicionamiento (1963, 4.000 referencias, filiales en 4 países, +12% crecimiento) + hipótesis concreta de dolor sobre el ciclo de pedido HORECA. Evitar tono de ficha corporativa.
- **Canal:** LinkedIn a Director Comercial/Operaciones primero; email corporativo como respaldo.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (agroalim multicanal, backoffice HORECA) | 25% | 9 | 2,25 |
| Tamaño (grande, decisión con estructura, ticket alto) | 15% | 9 | 1,35 |
| Madurez digital (margen real, +4000 SKU) | 15% | 8 | 1,20 |
| Señales de dolor (crecimiento + complejidad multicanal) | 20% | 9 | 1,80 |
| Accesibilidad del decisor | 10% | 6 | 0,60 |
| Capacidad de pago (121M€ facturación) | 15% | 10 | 1,50 |
| **Total** | 100% | | **8,7 / 10** |

**Veredicto:** Lead A. Encaje casi ideal con el portfolio (automatización backoffice operativo, BI ligero, RAG sobre catálogo amplio). Crecimiento del 12,76% y complejidad multicanal-multigeografía son palancas comerciales, no obstáculos. Proceder: identificar Director Comercial/Operaciones y lanzar LinkedIn + email esta misma semana.
