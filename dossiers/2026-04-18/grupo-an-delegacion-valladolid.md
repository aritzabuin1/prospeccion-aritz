# Dossier: Grupo AN (Delegación Valladolid)
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

Grupo AN es una de las mayores cooperativas agroalimentarias de España, con sede central en Tajonar (Navarra) y delegación de Castilla y León en Valladolid (Avenida Gloria Fuertes, 4-6 bajo, 47014). Aglutina a 171 cooperativas socias y más de 35.000 agricultores y ganaderos, cubriendo cereales, frutas y hortalizas, cárnicos, alimentación animal (marca Caceco), suministros agrícolas, energéticos y seguros. Facturación ejercicio 2024/25: **1.380 M€** (+8,4% vs. año anterior, desde 1.273 M€). La delegación de Valladolid opera como cabecera regional de Castilla y León, integrando cooperativas como Valduebro (reconocida Entidad Asociativa Prioritaria Regional por la Junta). Gran cuenta por volumen, complejidad operativa elevadísima y sensibilidad política a eficiencia (reparten 70% de beneficios a los socios).

- **Sector:** Cooperativa agroalimentaria multiservicio — cereales, frutas y hortalizas, cárnico, pienso, suministros
- **Tamaño:** 1.380 M€ facturación · 171 cooperativas socias · +35.000 agricultores · plantilla corporativa amplia
- **Sede Valladolid:** Avenida Gloria Fuertes, 4-6 bajo — 47014 Valladolid (delegación CyL)

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Grupo AN, S. Coop. |
| CIF | F31065316 (Grupo AN) |
| Fundación | 1910 (origen cooperativo) |
| Actividad | Cooperativa agroalimentaria de segundo grado; cereales, frutas y hortalizas, cárnico, pienso, suministros, energía, seguros |
| Facturación | 1.380 M€ (2024/25) · +8,4% YoY |
| Cooperativas socias | 171 |
| Agricultores/ganaderos | +35.000 |
| Marcas | Dantza, Diquesí, Caceco, Coc&Coc, AN Energéticos |
| Sede central | Campo de Tajonar, 31192 Tajonar (Navarra) |
| Delegación CyL | Avenida Gloria Fuertes, 4-6 bajo — 47014 Valladolid |
| Teléfono central | +34 948 299 400 |
| Web | grupoan.com |

## 3. Madurez digital

- Web corporativa sólida, presencia en LinkedIn activa ("#EquiposQueAlimentAN"), marcas comerciales con identidad propia. Infraestructura digital propia de una cooperativa con negocio diversificado (agro, pienso, energía, seguros).
- Con 171 cooperativas socias y 5-6 líneas de negocio diferenciadas, los flujos de datos entre socios, delegaciones regionales y matriz son presumiblemente heterogéneos (ERP agrícola + ERP cárnico + SAP/similar en matriz + mucho Excel intermedio).
- Sin señales públicas de proyectos IA ni de data unificada. Al ser cooperativa, las decisiones de digitalización tienden a ser consensuadas y lentas, pero cuando se aprueban escalan a toda la red de socios.
- La reciente reclasificación de Valduebro como Entidad Asociativa Prioritaria Regional implica más reporting regulatorio a la Junta de CyL: oportunidad para orquestación documental.

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Consolidación de datos entre cooperativas socias.** 171 cooperativas reportando cosecha, stocks, pedidos y liquidaciones en formatos dispares. Un data pipeline con validación + panel consolidado por campaña/cultivo/región es el dolor nº 1 de cualquier cooperativa de segundo grado.
2. **Gestión de pedidos a suministro agrícola y pienso.** Ciclo agrario + picos estacionales + pedidos por teléfono/email/WhatsApp desde explotaciones dispersas = alto coste administrativo. Extracción estructurada + volcado al ERP libera horas a delegaciones como Valladolid.
3. **Reparto de beneficios y liquidaciones a socios.** Reparten 70% de beneficios a 171 cooperativas: cálculos de liquidación, documentación fiscal, notificaciones, consultas de socios. Susceptible a automatización documental + asistente interno sobre normativa cooperativa.
4. **Reporting regulatorio autonómico (PAC, EAP, Junta CyL).** Castilla y León exige reporting específico a Entidades Asociativas Prioritarias. Carga documental creciente = oportunidad de orquestación con IA.
5. **Atención a socios y técnicos de campo.** Dudas recurrentes (liquidaciones, suministros, pólizas de seguro agrario, precios de cereal). RAG multilingüe (cast/eusk/cat) sobre documentación interna + histórico de casos descarga al equipo técnico de las delegaciones.
6. **Forecasting de cosecha y planificación industrial.** Pronósticos meteorológicos + datos históricos + siembras declaradas = capacidad de planificar mejor recepciones, capacidad de silo y envasado.

## 5. Contacto decisor

- **Delegación Valladolid — director/a regional CyL.** Punto de entrada natural para conversaciones operativas. Buscar en LinkedIn "Grupo AN" + "Valladolid" / "Castilla y León" / "delegado".
- **Director de Sistemas / CIO / Transformación Digital (matriz Tajonar).** Propietario del dolor nº 1 y nº 4. En cooperativas de este tamaño el CIO suele estar centralizado en matriz.
- **Director Financiero / Controller.** Propietario del dolor nº 3 y nº 5 (liquidaciones, reporting).
- Canal primario: LinkedIn a director CyL; paralelamente mapear CIO/Director TI en matriz. Email corporativo genérico como respaldo. Teléfono +34 948 299 400 para pivotar hacia Valladolid.
- Recomendación: este lead es cuenta grande y ciclo largo. Primer toque de tanteo al delegado CyL (decisión táctica local) y, en paralelo, investigar vía LinkedIn al responsable de sistemas/transformación en matriz.

## 6. Ángulo de entrada

- **Propuesta:** piloto acotado sobre un punto dolor único y demostrable a escala delegación — la más obvia es el procesamiento de pedidos y documentación de socios que llegan por múltiples canales al back-office de la delegación CyL. Piloto 6-8 semanas, ROI medido en horas de administración y errores. Si funciona, replicar a otras delegaciones y conectar con el data pipeline central.
- **Mensaje:** reconocimiento genuino del tamaño y modelo cooperativo (171 cooperativas, 35.000 socios, 1.380 M€, crecimiento 8,4% en un año difícil) + hipótesis concreta sobre carga administrativa en delegación + pregunta calibrada sobre cómo están gestionando hoy el flujo de pedidos y documentación cooperativa-a-matriz. Evitar pitch de IA corporativa; tono de par que conoce el dolor.
- **Canal:** LinkedIn al delegado de Valladolid como primer toque. Email corporativo de respaldo. Para matriz, LinkedIn al CIO/director TI con otro ángulo (consolidación de datos entre socios).

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (agroalim, procesos repetitivos, datos dispersos) | 25% | 9 | 2,25 |
| Tamaño adecuado (gran cuenta, sin techo) | 15% | 10 | 1,50 |
| Madurez digital (margen real de mejora) | 15% | 7 | 1,05 |
| Señales de dolor (crecimiento, reclasificación Valduebro) | 20% | 8 | 1,60 |
| Accesibilidad del decisor (ciclo cooperativo lento) | 10% | 5 | 0,50 |
| Capacidad de pago (1.380 M€ facturación) | 15% | 10 | 1,50 |
| **Total** | 100% | | **8,4 / 10** |

**Veredicto:** Lead A. Gran cuenta agroalimentaria con crecimiento, volumen y complejidad operativa que encaja de lleno con el portfolio de Aritz (automatización de procesos y BI sobre datos dispersos). Ciclo de decisión largo por ser cooperativa, pero ticket potencial muy alto. Estrategia: tanteo a delegación Valladolid + trabajo paralelo sobre matriz. Proceder con investigación LinkedIn del delegado CyL y del responsable de sistemas esta semana.
