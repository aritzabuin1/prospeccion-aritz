# Dossier: Grupo Marsan – Transformaciones Superficiales
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupo Marsan (Marsan Transformaciones Superficiales, S.L.) es una empresa industrial gallega fundada en 1951 como taller familiar de estampación y evolucionada hacia un grupo especializado en recubrimientos superficiales (cataforesis, pintura líquida, pintura en polvo), transformación metálica, ensamblaje y logística para automoción, aeronáutica y naval. Sede central en el Parque Tecnolóxico e Loxístico de Vigo (PAR 10.09, 36315) con plantas en Valença (Portugal) y dos en México (Celaya y Vilagrán). Proveedor integrado del sector automoción gallego (Ceaga). Datos recientes: Grupo Marsan Sociedad Cartera figura con 16 empleados corporativos y caída de facturación del 25,95% último ejercicio, señal de stress operativo claro en un sector (automoción) que está en reconversión. Implementaron MES en 2023 para control de producción. Perfil mediana industrial tecnificada con margen real para data y orquestación.

- **Sector:** Industria — transformaciones superficiales y tratamientos de metal para automoción, aeronáutica y naval
- **Tamaño:** Grupo con 4 plantas (Vigo, Valença, Celaya, Vilagrán) · 16 corporativos + personal de planta · caída 25,95% facturación último año
- **Sede principal:** Parque Tecnolóxico e Loxístico, PAR 10.09 — 36315 Vigo (Pontevedra)

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Marsan Transformaciones Superficiales, S.L. |
| Fundación | 1951 (origen estampación familiar) |
| Actividad | Recubrimientos superficiales (cataforesis, pintura polvo y líquida), transformación metálica, ensamblaje, logística |
| Empleados corporativos | 16 (Grupo Marsan Sociedad Cartera 2024) + plantilla de planta |
| Facturación | Caída 25,95% último ejercicio (stress claro) |
| Plantas | Vigo (España), Valença (Portugal), Celaya + Vilagrán (México) |
| Sectores cliente | Automoción (Ceaga), aeronáutico, naval |
| Certificaciones | ISO 9001, ISO 14001 |
| Iniciativas recientes | MES para control de producción (2023), placas solares planta Sur Europa (2022) |
| Teléfono | +34 986 27 08 04 |
| Email | info@grupomarsan.com |
| Web | grupomarsan.com |

## 3. Madurez digital

- Web corporativa multipaís, presencia en Ceaga (clúster automoción gallego). Implementación de MES en 2023 indica ya inversión en digitalización de planta.
- Con plantas en 3 países (España, Portugal, México) y clientes Tier-1 de automoción, presumiblemente tienen ERP industrial (probable SAP o Microsoft Dynamics) + MES + múltiples Excel para control de calidad, trazabilidad de lote y conciliación entre plantas.
- Caída del 25,95% de facturación es señal dura: el sector de automoción europeo está en reconversión (electrificación, caída de volúmenes OEM) y los proveedores Tier-2 sufren. Contexto favorable para conversaciones sobre eficiencia y reducción de coste operativo.
- Nota scope geográfico: la empresa tiene plantas en México pero el decisor está en Vigo (matriz española). OK para prospección.

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Trazabilidad de lote y calidad multi-planta.** Recubrimientos superficiales en 4 plantas distintas para clientes que exigen trazabilidad total (automoción premium, aeronáutico). Si MES no está perfectamente integrado con ERP y calidad, hay Excel intermedio. Orquestación documental y data pipeline sobre registros de calidad = ROI rápido.
2. **Reporting consolidado planta × cliente × pieza × margen.** Con caída del 25,95% la dirección necesita visibilidad casi diaria de rentabilidad por cliente y por pieza para decidir qué OEM priorizar. BI consolidado sobre datos MES + ERP + calidad es palanca clave.
3. **Gestión de no conformidades y reclamaciones de OEM.** Automoción exige 8D, reportes de no conformidad, trazabilidad a pieza en horas. Flujo hoy típicamente Excel + email. Automatizable con extracción estructurada + orquestación documental.
4. **Pedidos y programas de entrega con Tier-1.** EDI con OEMs grandes suele estar resuelto, pero los cambios de programa (releases semanales, ajustes de mix) generan mucho trabajo manual de planning. Asistente IA sobre programa+stock+capacidad descarga al planner.
5. **Documentación de homologación y certificaciones por pieza.** Cada pieza nueva lleva un expediente (PPAP/APQP en automoción, EN9100 en aero). Orquestación documental con IA reduce meses de elaboración a semanas.
6. **Eficiencia energética y costes en líneas de cataforesis/pintura.** Son líneas intensivas en energía. Dashboard de consumo × horno × pieza × OEM abre conversaciones con dirección y con sostenibilidad.

## 5. Contacto decisor

- **CEO / Director General (matriz Vigo).** Buscar en LinkedIn "Grupo Marsan" + "CEO" / "Director General". En industria gallega familiar, el propietario-director suele estar accesible.
- **Director Industrial / Director de Operaciones.** Propietario del dolor nº 1, 2, 3, 4. Decisor técnico que suele pedir ROI medible.
- **Director Financiero.** Propietario del dolor nº 2 (reporting). En contexto de caída 25,95%, estará muy presente.
- Canal primario: LinkedIn al Director Industrial o al Director General. Email corporativo info@grupomarsan.com como respaldo.
- Recomendación: primer toque LinkedIn al Director Industrial con ángulo de reporting consolidado multi-planta y calidad. El contexto de caída facilita abrir conversación.

## 6. Ángulo de entrada

- **Propuesta:** piloto 6-8 semanas sobre reporting consolidado planta × cliente × pieza × margen (con datos MES + ERP + calidad), o bien automatización del flujo de no conformidades 8D. ROI medible en horas de administración y en reducción de tiempo de respuesta a reclamación OEM.
- **Mensaje:** reconocimiento honesto del momento del sector (automoción europea en reconversión) + observación específica (4 plantas, MES 2023, Ceaga) + hipótesis concreta sobre dolor de visibilidad cruzada planta-cliente-pieza + pregunta calibrada. Tono de par que entiende que una caída del 25% es señal de que hay que mover piezas, no otro pitch de transformación digital.
- **Canal:** LinkedIn al Director Industrial. Email como respaldo con asunto curioso.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (industria, proceso multi-planta, trazabilidad) | 25% | 8 | 2,00 |
| Tamaño adecuado (mediana industrial, 4 plantas) | 15% | 7 | 1,05 |
| Madurez digital (MES ya implementado, margen de mejora) | 15% | 7 | 1,05 |
| Señales de dolor (caída 25,95%, sector en reconversión) | 20% | 9 | 1,80 |
| Accesibilidad del decisor (industria gallega familiar) | 10% | 7 | 0,70 |
| Capacidad de pago (stress actual pero grupo multiplanta) | 15% | 6 | 0,90 |
| **Total** | 100% | | **7,5 / 10** |

**Veredicto:** Lead B+. Encaja bien con el portfolio (industria, multi-planta, calidad y reporting) y tiene palanca comercial clara (caída facturación → presión por eficiencia). Riesgo: en contexto de stress financiero el ciclo de decisión puede alargarse y el ticket apretarse. Estrategia: entrar con piloto muy acotado de ROI medible en 6-8 semanas, no propuesta grande. Proceder esta semana.
