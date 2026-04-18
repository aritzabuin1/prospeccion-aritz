# Dossier: Grupo Oter
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupo Oter es una de las referencias históricas de la restauración madrileña. Fundado en 1972 por Gerardo Oter, opera aproximadamente 25 conceptos de restaurantes en Madrid (asadores, marisquerías, arrocerías, tabernas, sidrerías, vinotecas), entre ellos Asador Gerardo, El Telégrafo, Gayarre, Pez Fuego, Gran Barril de Castellana, La Lenera, Teitu, Taberna Moderna y toda la línea "Barril" (Goya, Recoletos, Orense, Las Letras...). Según fuentes sectoriales (Baco&Boca, Gastroeconomy) genera en torno a 600 empleos directos y factura ~46 M€/año; la sociedad central (Restaurantes Gerardo Oter S.L.) declara 58 empleados en 2025. Perfil clásico de grupo multi-marca con central en Madrid que pelea con nóminas, compras, reservas y reporting entre 25 sitios.

- **Sector:** Hostelería — grupo multi-restaurante tradicional madrileño
- **Tamaño:** ~25 restaurantes · ~600 empleados directos · facturación ~46 M€
- **Sede central:** C/ Don Ramón de la Cruz, 100 — 28006 Madrid

## 2. Datos clave

| Campo | Valor |
|---|---|
| Marca comercial | Grupo Oter |
| Sociedad central | Restaurantes Gerardo Oter S.L. |
| Año fundación | 1972 (Gerardo Oter) |
| Actividad | Gestión y explotación de restaurantes multi-concepto en Madrid |
| Nº restaurantes | ~25 (Asador Gerardo, El Telégrafo, Gayarre, Pez Fuego, línea Barril, Teitu, La Lenera, etc.) |
| Empleados | ~600 directos (grupo) · 58 en Restaurantes Gerardo Oter S.L. 2025 |
| Facturación | ~46 M€/año (fuentes sectoriales) |
| Teléfono | 914 013 443 |
| Email | informacion@grupo-oter.com |
| Web | grupo-oter.net |
| Redes | Instagram @grupooter, Facebook, X |

## 3. Madurez digital

- Web corporativa limpia con listado de restaurantes y plataforma de delivery propia enlazada. Cada restaurante suele tener su microsite dentro del dominio del grupo.
- Presencia activa en Instagram/Facebook; newsletter abierta. No se detecta CRM de cliente unificado ni programa de fidelización del grupo.
- Reservas gestionadas por múltiples vías (teléfono de cada local, TheFork, formulario web). No hay motor de reservas corporativo centralizado visible.
- Sin señales públicas de Power BI, data warehouse ni IA. Perfil típico del grupo tradicional madrileño: TPV sectorial (Ágora, Revo, Hosteltáctil), ERP/contabilidad central (probablemente Dynamics o A3), Excel para reporting semanal de 25 locales.
- Cumple 53 años en 2025. Transición generacional probable (fundador Gerardo Oter + segundas generaciones en operativa).

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Reporting diario/semanal de 25 locales.** Ventas, ticket medio, food cost, mermas, ocupación por turno — datos disgregados en 25 TPVs, consolidación manual. Caso anonimizado equivalente existe (cadena >100 establecimientos) con entrega automática por WhatsApp y email a responsables.
2. **Central de compras y escandallos.** Un grupo con asadores, marisquerías y arrocerías maneja catálogos de proveedores cruzados (pescado, carne, vino, arroces). Optimización de compras por datos + control de desviación de escandallo es palanca de margen muy alta.
3. **Gestión de reservas multicanal.** 25 locales recibiendo reservas por teléfono, web, TheFork e Instagram — sin un orquestador central se pierden oportunidades y se duplican reservas. Asistente conversacional (WhatsApp/web) que unifique el flujo por marca.
4. **Atención al cliente y posventa.** Preguntas repetitivas (horario, menú, alergenos, aparcamiento, grupos). RAG multi-marca sobre el catálogo del grupo libera a recepción y mostrador.
5. **Onboarding y formación de equipos.** 600 personas con alta rotación en hostelería — asistente de IA para protocolos de servicio, alergenos, carta y ticketing ahorra semanas de curva de aprendizaje.
6. **Control financiero consolidado.** Cierre mensual entre 25 cuentas de resultados, 25 nóminas, 25 flujos de caja. Dashboards tipo Power BI sobre el ERP central acortan el cierre de semanas a días.

## 5. Contacto decisor

- **Gerardo Oter (fundador) y familia** — núcleo directivo histórico; la segunda generación suele llevar operaciones y expansión.
- **Dirección General / COO del grupo** — decisor natural para proyectos transversales de operación y reporting.
- **Dirección Financiera / Controller** — dueño del dolor nº 1 y nº 6.
- Canales: email informacion@grupo-oter.com (genérico, ratio bajo) · teléfono 914 013 443 · LinkedIn corporativo https://www.linkedin.com/company/grupo-oter/ · Instagram @grupooter.
- Recomendación: primer toque por email a informacion@grupo-oter.com con asunto curioso + búsqueda en LinkedIn del COO/Director Financiero para Paso 1 sin nota en paralelo.

## 6. Ángulo de entrada

- **Propuesta:** consolidar datos operativos diarios de los 25 locales en un panel único (Power BI o similar) alimentado automáticamente desde los TPVs + entrega diaria por WhatsApp/email a los gerentes de marca con KPIs clave (venta, ticket, food cost, mermas). Piloto 4-6 semanas sobre 3 restaurantes de la línea Barril + Asador Gerardo; extensión al resto una vez validado. En segunda fase: asistente de reservas multicanal y RAG de atención.
- **Mensaje:** reconocimiento de la dimensión del grupo (25 conceptos, 53 años, Gerardo Oter) + label sobre la fricción de consolidar operación entre 25 casas diferentes + pregunta abierta sobre cómo les llega hoy el pulso diario a dirección.
- **Canal:** email primero (asunto curioso) + LinkedIn al COO/Dir. Financiero en paralelo. Evitar pitch de IA — hablar de "ordenar el pulso del día".

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (hostelería multi-local, procesos repetitivos) | 25% | 9 | 2,25 |
| Tamaño adecuado (grupo consolidado, decisión accesible) | 15% | 9 | 1,35 |
| Madurez digital (margen real de mejora) | 15% | 8 | 1,20 |
| Señales de dolor (25 locales, cierre consolidado, reservas fragmentadas) | 20% | 9 | 1,80 |
| Accesibilidad del decisor | 10% | 6 | 0,60 |
| Capacidad de pago (46 M€ facturación, 600 empleados) | 15% | 9 | 1,35 |
| **Total** | 100% | | **8,55 / 10** |

**Veredicto:** Lead A. Encaje 1:1 con el caso anonimizado de cadena con más de 100 establecimientos (aunque Oter tiene 25, la lógica de consolidación diaria por WhatsApp/email es idéntica). Capacidad de pago sobrada y dolor evidente en un grupo con 53 años y transición generacional en curso. Proceder con primer toque esta semana y localizar COO/Dir. Financiero en LinkedIn como canal paralelo.
