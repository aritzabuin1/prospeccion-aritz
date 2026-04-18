# Dossier: IDESA – Ingeniería y Diseño Europeo
**Fecha:** 2026-04-18
**Preparado para:** Aritz Abuin -- AI Solutions Architect

---

## 1. Resumen ejecutivo

IDESA (Ingeniería y Diseño Europeo, S.A.) es una ingeniería y fabricante de bienes de equipo asturiana fundada en 1993, con sede en Gijón (C/ Profesor Potter 105, 33203). Especializada en diseño y fabricación de grandes equipos para el sector energético: coke drums, reactores, suction piles y cimentaciones offshore, equipos para refinerías y transición energética (hidrógeno, captura de CO₂, almacenamiento LNG). Clientela top mundial: **Shell, Equinor, Grupa Lotos**. Referencias recientes: Shell Haven roof replacement, suction piles Shell Vito, coke drums y FCC para Equinor. Plantilla 89-99 empleados, facturación en el rango de decenas de M€ (caída reportada -5,16% último año pero rentabilidad económica 2024 +10,61% vs. 7,63% en 2023 — mejor margen pese a menos ingresos). Certificaciones muy duras: ISO 9001/14001/45001, ASME U/U2, AD2000-Merkblatt HP 0, EN 1090, PED, ISO 3834-2. Perfil de ingeniería industrial de alto valor, proyectos unitarios grandes, mucha documentación técnica y compliance.

- **Sector:** Ingeniería y fabricación de bienes de equipo para energía (oil&gas, offshore, transición energética)
- **Tamaño:** 89-99 empleados · ~decenas M€ facturación · rentabilidad 10,61% (2024, subiendo)
- **Sede:** C/ Profesor Potter 105 — 33203 Gijón (Asturias)

## 2. Datos clave

| Campo | Valor |
|---|---|
| Razón social | Ingeniería y Diseño Europeo, S.A. (IDESA) |
| Fundación | 1993 |
| Actividad | Diseño e ingeniería + fabricación de bienes de equipo para oil&gas, offshore, refino, hidrógeno, CCS, LNG |
| Empleados | 89 (2025) · 99 (2024) |
| Facturación | Caída -5,16% último año; rentabilidad económica 10,61% (2024) vs. 7,63% (2023) |
| Certificaciones | ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018 · ASME U/U2 · AD2000-Merkblatt HP 0 · EN 1090 · PED · ISO 3834-2 |
| Clientes clave | Shell, Equinor, Grupa Lotos |
| Proyectos referencia | Shell Haven roof, suction piles Shell Vito, coke drums, FCC Equinor |
| Teléfono | +34 985 175 705 |
| Email | idesa@idesa.net |
| Web | idesa.net |

## 3. Madurez digital

- Web corporativa profesional con referencias de proyectos y comité de dirección visible (management_committee.php). Presencia B2B en LinkedIn razonable.
- Ingeniería industrial con clientes Tier-0 (Shell, Equinor) implica obligatoriamente stack técnico serio: CAD (Autodesk/PTC), PLM, ERP industrial (probable SAP o IFS), software de cálculo (ANSYS, Abaqus), documentación en Aconex/Documentum y mucho Excel + correo entre ingenieros y planta.
- Proyectos grandes y unitarios (coke drums, offshore foundations) = expedientes técnicos gigantes, calidad muy exigente, varias revisiones cliente por documento. Compliance documental es el centro operativo del negocio.
- Mejora de rentabilidad económica en un año con menos ingresos indica disciplina operativa y margen para conversar sobre eficiencia (más margen por proyecto, no más proyectos).

## 4. Puntos de dolor (hipótesis sectoriales priorizadas)

1. **Gestión documental técnica por proyecto.** Un coke drum o una suction pile genera cientos de documentos (planos, cálculos, procedimientos, QA/QC, NCR, certificados) con múltiples revisiones cliente. Orquestación documental con IA (clasificación, extracción, validación vs. pliego) es el dolor nº 1 en ingenierías oil&gas.
2. **Preparación de ofertas para licitaciones internacionales.** Shell/Equinor exigen RFQ extensos (pliego técnico + comercial + QA + HSE). Reutilizar contenido de proyectos anteriores, extraer requisitos del pliego, montar dossiers — todo automatizable con RAG + asistente interno.
3. **Trazabilidad de material y soldadura (ISO 3834-2, ASME U).** Cada soldadura certificada requiere trazabilidad a soldador, procedimiento, colada, inspección. Típicamente en Excel + sistema QA propio. Data pipeline + validación automatizada = ROI claro y cumplimiento reforzado.
4. **Panel de control por proyecto (horas × fase × margen).** Proyectos unitarios de ingeniería con curvas de coste complejas. Dashboard consolidado de horas imputadas × fase × previsto vs. real × margen. BI ligero sobre ERP + timesheet.
5. **NCR y gestión de no conformidades.** Sector con inspecciones de tercera parte (Lloyd's, DNV). Automatizar el ciclo NCR (detección, registro, root cause, CAPA, cierre) libera horas de QA.
6. **Atención interna a ingeniería sobre normativa.** Equipos de ingenieros consultando ASME, AD2000, PED, EN 1090 constantemente. RAG interno sobre normativa + histórico de decisiones técnicas descarga al PM y al responsable técnico.

## 5. Contacto decisor

- **CEO / Director General.** Comité de dirección publicado en web (idesa.net/management_committee.php). Buscar nombres allí y cruzar con LinkedIn.
- **Director de Ingeniería / Director Técnico.** Propietario de dolores nº 1, 2, 6.
- **Director de Calidad / QA.** Propietario de dolores nº 3 y nº 5.
- **Director de Operaciones / COO.** Propietario del dolor nº 4.
- Canal primario: LinkedIn al Director de Ingeniería o Director de Calidad. Email idesa@idesa.net como respaldo.
- Recomendación: el comité de dirección está publicado → identificar nombres concretos antes del primer toque. Primer toque por LinkedIn al Director de Ingeniería con ángulo de documentación técnica + RFQ.

## 6. Ángulo de entrada

- **Propuesta:** piloto 6-8 semanas sobre uno de dos procesos: (a) extracción estructurada + clasificación de pliegos técnicos de licitación para acelerar ofertas, o (b) data pipeline de trazabilidad de soldadura + paneles QA. Ambas palancas son defendibles ante auditor externo (Shell, DNV) y medibles en horas ingeniería/QA liberadas.
- **Mensaje:** reconocimiento específico de las referencias (Shell Haven, Shell Vito, Equinor), de la evolución de margen (rentabilidad subiendo con ingresos bajando = gestión fina) y del nivel de certificación (ASME U/U2 + ISO 3834-2). Hipótesis sobre dolor documental de proyecto. Pregunta calibrada. Tono técnico de par, no pitch de IA genérico.
- **Canal:** LinkedIn al Director de Ingeniería, identificado previamente en management_committee.php. Email como respaldo a los 7 días.

## 7. Score

| Criterio | Peso | Nota | Subtotal |
|---|---|---|---|
| Fit sectorial (ingeniería industrial, documentación masiva) | 25% | 9 | 2,25 |
| Tamaño adecuado (mediana-grande, ~90 empleados, ticket alto) | 15% | 8 | 1,20 |
| Madurez digital (stack sólido, margen de IA sobre proceso) | 15% | 7 | 1,05 |
| Señales de dolor (proyectos unitarios documentación-intensivos) | 20% | 8 | 1,60 |
| Accesibilidad del decisor (comité publicado en web) | 10% | 8 | 0,80 |
| Capacidad de pago (clientes Shell/Equinor) | 15% | 9 | 1,35 |
| **Total** | 100% | | **8,25 / 10** |

**Veredicto:** Lead A. Encaje excelente por documentación técnica, clientes Tier-0 que exigen trazabilidad, y comité de dirección visible que permite investigar decisor concreto. Ticket potencial alto. Riesgo: ciclo largo y stack técnico muy específico (requerirá demostrar conocimiento de ASME/PED/ISO 3834 en toque 2). Proceder esta semana: mapear comité de dirección vía web + LinkedIn y lanzar primer toque al Director de Ingeniería.
