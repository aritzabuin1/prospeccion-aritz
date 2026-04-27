# Plan Maestro v2: Canal Partners + Packs Verticales Pre-empaquetados

**Autor:** Aritz Abuin González
**Horizonte:** 120 días
**Ámbito:** Toda España (nacional, no solo País Vasco)
**Destinatario operativo:** Claude Code

---

## 0. Cambio conceptual respecto al plan v1

El plan v1 proponía construir un catálogo de 11 demos sueltas. Ese enfoque tiene un fallo estratégico: ofrecer a un partner "un catálogo" es débil comercialmente. Un partner no vende catálogos — vende productos con nombre, precio y ficha técnica.

**Plan v2:** las demos se empaquetan en **5 Packs Verticales** con marca propia, precio cerrado y arquitectura hub-and-spoke (un dashboard central agrega los outputs de las automatizaciones del pack). Cada demo se construye una vez pero se reutiliza en 2–3 packs, lo que hace que 13 demos cubran 5 verticales.

**Beneficios del enfoque por packs:**
- Partner vende producto nominal ("CFO Copilot"), no servicios abstractos
- Ticket medio por cliente sube de 2–8K (demo suelta) a 12–25K (pack completo)
- Mantenimiento recurrente natural (200–800€/mes por pack)
- Cada pack es una unidad de marketing (1 landing, 1 vídeo, 1 caso, 1 deck)
- Amortización cruzada de demos compartidas entre packs

---

## 1. Análisis de las 50 automatizaciones

**Metodología de scoring.** Cada automatización se ha evaluado en 6 dimensiones:

- **Bajo coste de build** (0–5): inverso al tiempo estimado en Claude Code. 5 = <8h, 1 = >40h
- **Wow factor en demo** (0–5): impacto visible en 2 minutos de demo
- **Replicabilidad** (0–5): cuánto se reutiliza sin customización entre clientes
- **Fit con casos Aritz** (0–5): cuánto apalanca casos ya validados (Euromanager, Cafès Cornellà, viajes lujo)
- **Demanda de mercado** (0–5): dolor real y universal en pymes españolas
- **Diferenciación** (0–5): hueco vs herramientas commodity (5 = nicho defendible, 1 = hay 50 herramientas SaaS)

Score máximo: 30. Corte para entrar a catálogo hero: ≥22.

**Ranking completo de las 50 (solo top 20 por score):**

| # | Automatización | Build | Wow | Repl | Fit | Dem | Dif | **Score** |
|---|---|---|---|---|---|---|---|---|
| 29 | Invoice Processor | 4 | 5 | 5 | 5 | 5 | 3 | **27** |
| 48 | Financial Report Narrator | 4 | 5 | 4 | 5 | 4 | 5 | **27** |
| 30 | Expense Report Builder | 5 | 4 | 5 | 4 | 4 | 3 | **25** |
| 31 | Meeting Notes Processor | 5 | 5 | 5 | 3 | 5 | 2 | **25** |
| 36 | Weekly KPI Dashboard | 3 | 5 | 3 | 5 | 5 | 4 | **25** |
| 46 | Cash Flow Forecaster | 3 | 5 | 3 | 5 | 5 | 4 | **25** |
| 21 | Tier-1 Auto-Responder (RAG) | 3 | 5 | 4 | 5 | 5 | 3 | **25** |
| 04 | Meeting Prep Brief | 5 | 4 | 5 | 3 | 4 | 3 | **24** |
| 35 | Contract Clause Scanner | 4 | 5 | 4 | 3 | 4 | 4 | **24** |
| 39 | Resume Screener | 4 | 5 | 5 | 3 | 5 | 2 | **24** |
| 32 | Document Classifier | 4 | 4 | 5 | 3 | 4 | 3 | **23** |
| 37 | Inventory Alert System | 4 | 4 | 4 | 4 | 4 | 3 | **23** |
| 49 | Tax Document Organizer | 4 | 4 | 4 | 3 | 4 | 3 | **22** |
| 43 | Employee FAQ Bot | 3 | 4 | 4 | 4 | 3 | 3 | **21** |
| 13 | Social Listening Summarizer | 3 | 4 | 4 | 3 | 3 | 3 | **20** |
| 01 | Inbound Lead Qualifier | 4 | 4 | 4 | 2 | 5 | 2 | **21** |
| 47 | Budget Variance Analyzer | 4 | 4 | 3 | 4 | 3 | 3 | **21** |
| 22 | Ticket Classifier Router | 4 | 4 | 5 | 3 | 4 | 3 | **23** |
| 25 | Escalation Summarizer | 5 | 4 | 5 | 2 | 3 | 3 | **22** |
| 50 | Subscription Auditor | 5 | 4 | 5 | 2 | 3 | 4 | **23** |

**Automatizaciones descartadas y por qué:**

- **#02, #15, #16 (Cold email personalizer, Blog drafter, Ad variants)**: mercado saturado por Instantly, Apollo, Jasper, ChatGPT directo. No hay hueco defendible.
- **#05 Proposal Drafter**: cada empresa tiene plantilla distinta, muy customizable, baja replicabilidad.
- **#06 Win/Loss Analyzer**: solo empresas con CRM maduro y datos históricos, mercado estrecho.
- **#09 Pipeline Health Monitor**: HubSpot y Salesforce ya lo hacen nativo.
- **#11 Content Repurposer, #12 SEO Brief, #14 Email Analyzer**: mercado saturado, commodity.
- **#17–#20 (Marketing tools)**: commodity, sin diferenciación posible.
- **#23, #24, #26, #27, #28 (Customer support avanzado)**: requieren stack técnico del cliente muy maduro; fit solo con cuentas grandes difíciles de captar como freelance.
- **#33 Onboarding, #40–#42, #44, #45 (HR operational)**: mercado pequeño por empresa, ticket bajo, alta dispersión.
- **#34 Vendor Comparison, #38 Process Docs**: valiosas pero ticket único, sin recurrencia.

**Los 13 finalistas (score ≥22 + fit con packs verticales):**

#29, #30, #31, #32, #35, #36, #37, #39, #46, #47, #48, #49, y #21 (RAG bot para el pack HORECA).

Añado #22 (Ticket Classifier Router) como módulo del pack HORECA en lugar de #50, porque #22 integra directamente con #21.

---

## 2. Diseño de los 5 Packs Verticales

### Pack 1: **CFO Copilot**
*"La IA que convierte al director financiero en estratega."*

**Cliente final:** pymes industriales, servicios profesionales, consultoras medianas (50–500 empleados, CFO dedicado).
**Módulos (4):** #29 Invoice Processor · #46 Cash Flow Forecaster · #47 Budget Variance Analyzer · #48 Financial Report Narrator
**Hub:** dashboard ejecutivo mensual que agrega los 4 outputs con narrativa en lenguaje natural.
**Precio cliente final:** 15.000–25.000€ setup · 400–800€/mes mantenimiento
**Comisión partner:** 15% (referido) o 25% (co-venta)
**Caso ancla:** Euromanager (360h/año ahorradas a directora financiera).
**Diferenciación:** el Financial Report Narrator es único en mercado español. Los dashboards hay muchos; la **narrativa automática en castellano lista para consejo de administración** no la ofrece prácticamente nadie.

### Pack 2: **Gestoría IA**
*"El stack que hace que una gestoría facture 3x por cliente sin añadir plantilla."*

**Cliente final:** gestorías con 15–60 empleados, cartera 200+ clientes pyme.
**Módulos (5):** #29 Invoice Processor · #30 Expense Report Builder · #32 Document Classifier · #49 Tax Document Organizer · #48 Financial Report Narrator
**Hub:** panel de cartera que muestra ahorro de horas agregado por gestor/cliente.
**Precio cliente final (para la propia gestoría):** 12.000–20.000€ setup · 300–600€/mes
**Modelo alternativo:** gestoría lo revende a SUS clientes como servicio premium, Aritz cobra licencia per-cliente (25–50€/mes por cliente activo de la gestoría).
**Comisión partner:** 20% (alianza recurrente).
**Caso ancla:** Euromanager (asesoría) + subcaso de digitalización de gestoría.
**Diferenciación:** Holded/Xolo lo hacen para autónomos; no existe stack equivalente que gestorías tradicionales de provincia puedan implantar encima de A3 o Sage.

### Pack 3: **HORECA Cockpit**
*"El centro de control para cadenas de restauración multi-establecimiento."*

**Cliente final:** cadenas HORECA con 10+ establecimientos, grupos de restauración, distribuidores horeca con red de clientes.
**Módulos (4):** #36 Weekly KPI Dashboard · #21 Tier-1 Auto-Responder (RAG para baristas/camareros) · #37 Inventory Alert System · #22 Ticket Classifier Router (quejas clientes)
**Hub:** app móvil + dashboard con alertas unificadas por establecimiento.
**Precio cliente final:** 18.000–35.000€ setup · 500–1.200€/mes
**Comisión partner:** 15–25%.
**Caso ancla:** Cafès Cornellà (108 establecimientos, Power BI + WhatsApp + chatbot RAG baristas).
**Diferenciación:** ninguna solución vertical integrada para HORECA en español; todo está fragmentado (Lightspeed, Dishflow, CoverManager son trozos).

### Pack 4: **LegalFlow**
*"Revisión documental inteligente para despachos."*

**Cliente final:** despachos de abogados medianos (20–150 abogados), asesorías jurídicas internas de grandes empresas.
**Módulos (4):** #35 Contract Clause Scanner · #32 Document Classifier · #04 Meeting Prep Brief · #31 Meeting Notes Processor
**Hub:** biblioteca de contratos indexada + alertas de riesgo.
**Precio cliente final:** 15.000–30.000€ setup · 400–900€/mes
**Comisión partner:** 20%.
**Caso ancla:** a construir (es el pack donde menos casos previos hay — construir CASO_5 anonimizado con despacho piloto).
**Diferenciación:** Lefebvre y Sudespacho hacen gestión; Harvey y Spellbook hacen IA pero en inglés y con licencias carísimas. Hueco claro en mediano español.

### Pack 5: **TalentPipe**
*"Screening y entrevistas asistidas por IA para ETTs y headhunters."*

**Cliente final:** ETTs medianas, boutique de headhunting, departamentos RRHH internos de empresas 200+.
**Módulos (4):** #39 Resume Screener · #40 Job Description Writer · #41 Interview Question Generator · #44 Exit Interview Analyzer
**Hub:** pipeline de candidatos con scoring unificado.
**Precio cliente final:** 10.000–18.000€ setup · 300–500€/mes
**Comisión partner:** 15%.
**Caso ancla:** a construir (es el pack de menor prioridad estratégica).
**Diferenciación:** HireVue y similares son caros y enterprise; hueco en mediano español.

### Matriz de reutilización demos → packs

| Demo | CFO Copilot | Gestoría IA | HORECA Cockpit | LegalFlow | TalentPipe |
|---|:-:|:-:|:-:|:-:|:-:|
| #29 Invoice | ✓ | ✓ |  |  |  |
| #30 Expense |  | ✓ |  |  |  |
| #46 Cash Flow | ✓ |  |  |  |  |
| #47 Budget Variance | ✓ |  |  |  |  |
| #48 Financial Narrator | ✓ | ✓ |  |  |  |
| #32 Document Classifier |  | ✓ |  | ✓ |  |
| #49 Tax Docs |  | ✓ |  |  |  |
| #36 KPI Dashboard |  |  | ✓ |  |  |
| #21 RAG Bot |  |  | ✓ |  |  |
| #22 Ticket Router |  |  | ✓ |  |  |
| #37 Inventory |  |  | ✓ |  |  |
| #35 Contract Scanner |  |  |  | ✓ |  |
| #04 Meeting Prep |  |  |  | ✓ |  |
| #31 Meeting Notes |  |  |  | ✓ |  |
| #39 Resume Screener |  |  |  |  | ✓ |
| #40 JD Writer |  |  |  |  | ✓ |
| #41 Interview Q |  |  |  |  | ✓ |
| #44 Exit Interview |  |  |  |  | ✓ |

**Economía de construcción:** 18 demos totales agrupadas en 5 packs. Reutilización: 4 demos comparten entre 2 packs. Inversión efectiva equivalente a construir ≈22 demos independientes.

---

## 3. Priorización: qué packs construir primero

**Criterios de selección:**

| Pack | Vel. build | Acceso partners | Ticket final | Volumen mercado ES | Diferenciación | **Prioridad** |
|---|---|---|---|---|---|---|
| CFO Copilot | Alta (Euromanager) | Media | Alto | Medio | Alta | **1** |
| Gestoría IA | Alta (Euromanager) | Alta (asociaciones) | Medio | Muy alto | Media-Alta | **2** |
| HORECA Cockpit | Alta (Cafès) | Media | Alto | Alto | Alta | **3** |
| LegalFlow | Media | Baja inicial | Alto | Medio | Alta | **4** |
| TalentPipe | Media | Media | Medio | Medio | Media | **5** |

**Plan de construcción escalonado:**

- Mes 1–2: **CFO Copilot** (4 demos + hub). Lanzamiento + primeros partners.
- Mes 2–3: **Gestoría IA** (añadir 2 demos nuevas — #30 y #49 — al construir, aprovechando #29, #32 y #48 ya hechas).
- Mes 3–4: **HORECA Cockpit** (4 demos + hub).
- Mes 5–6: LegalFlow y TalentPipe según señal de mercado.

---

## 4. Estrategia de partners: cobertura nacional

**Regla dura:** no priorizar partners por proximidad geográfica. Priorizar por tamaño de cartera y cobertura. Un implantador Holded con 200 clientes en toda España vale 10× un implantador local con 30 clientes en provincia.

### 4.1 Tres niveles de partner

**Nivel 1: Asociaciones sectoriales (super-partner).** Acuerdo con una asociación = acceso a cientos de socios en toda España. Máximo apalancamiento.

| Vertical | Asociación objetivo | Alcance |
|---|---|---|
| CFO Copilot | AECE (Contabilidad), ASSET (Tesoreros) | Medio |
| Gestoría IA | Consejo General Colegios Gestores Administrativos, AEDAF | Muy alto (30.000+ socios) |
| HORECA Cockpit | FEHR, Hostelería de España | Alto |
| LegalFlow | Consejo General Abogacía, ENATIC (LegalTech) | Alto |
| TalentPipe | AEDRH, AEDIPE, AGETT (ETTs) | Medio |

Target: 2 acuerdos con asociaciones cerrados a 6 meses.

**Nivel 2: Partners nacionales (alcance amplio).** Implantadores y consultoras con >100 clientes en toda España.

Ejemplos candidatos por vertical:
- CFO/Gestoría: partners Holded, Sage, A3 (Wolters Kluwer), Contasimple
- HORECA: partners Lightspeed, Revo, Haddock, Cofiksa
- Legal: partners Lefebvre, Sudespacho, Aranzadi
- Cross: consultoras Grant Thornton Digital, BDO, Auren, MGI

Target: 8 partners nivel 2 activos a 120 días.

**Nivel 3: Partners regionales y boutique.** Consultoras provinciales con cartera específica. Selección según fit vertical, nunca por proximidad geográfica a Bilbao.

Target: 15 partners nivel 3 en pipeline a 120 días, distribuidos por toda la geografía española.

### 4.2 Cómo encontrarlos (proceso Claude Code)

**Fuentes primarias:**
- Google Places API con queries por ciudad española (Madrid, Barcelona, Valencia, Sevilla, Zaragoza, Málaga, Bilbao, Murcia, Palma, Las Palmas, Alicante)
- LinkedIn Company Search (manual + export)
- Directorios de partners oficiales: Holded Partners, Sage Directory, Microsoft Partner Finder
- Registros mercantiles vía eInforma/Axesor/ElEconomista
- Eventos sectoriales pasados (listados de expositores/ponentes)

**Criterios duros de cualificación (mínimo 3 de 5):**
- Cartera 50+ clientes SMB (confirmable vía LinkedIn o web)
- Facturación recurrente (no proyectos únicos)
- Cobertura nacional o multi-autonómica (preferido sobre local)
- Decisor accesible en 1–2 escalones (socio, director comercial, BD manager)
- No tienen equipo IA consolidado

**Red flags:**
- Compiten en precio en su vertical
- Big4 ya implantadas en sus cuentas top
- Partner exclusivo histórico de otro vendor IA

---

## 5. Fases del plan

### FASE 0 — Validación estratégica (días 1–5)

**Entregable:** este plan validado por Aritz. Decisiones clave:
- Packs confirmados y renombrados si procede
- Vertical piloto confirmado (propuesta: CFO Copilot)
- Presupuesto de tiempo semanal asignado (propuesta: 40% del calendario)

### FASE 1 — Construcción MVP CFO Copilot (días 6–40)

**Entregables:**
- 4 demos funcionando end-to-end con dataset dummy
- Hub (dashboard ejecutivo con narrativa)
- Vídeo pitch 3 min del pack completo
- Landing page dedicada `cfocopilot.aritzabuin.com` o ruta dedicada
- One-pager PDF
- Deck comercial 10 slides
- Pitch-partner.md + Pitch-cliente.md

**Criterios de cumplimiento:**
- Demo se puede arrancar en <2 min ante un prospect
- ROI cuantificado con supuestos explícitos
- Caso Euromanager anonimizado integrado en la narrativa

### FASE 2 — Prospección partners nacionales (días 15–50, paralelo a FASE 1)

**Entregables:**
- `partners/directorio-nacional.csv` con 150+ candidatos (todos verticales, toda España)
- `partners/dossiers-cfo/<partner>.md` — 25 dossiers de partners CFO Copilot
- `partners/matriz-matching.md` — partner × pack con score de fit
- `partners/asociaciones.md` — investigación de 5 asociaciones prioritarias con contactos

### FASE 3 — Outreach CFO Copilot (días 40–75)

**Actividad:**
- Contacto a 25 partners CFO Copilot (LinkedIn + email, secuencia 3 touches)
- Contacto a 2 asociaciones prioritarias (AECE, AEDAF)
- Primeras reuniones (objetivo: 8–10)
- Segundas reuniones con propuesta económica (objetivo: 3–5)

**Entregables:**
- `partners/pipeline-partners.csv` actualizado semanalmente
- Primer cliente piloto arrancado con 1 partner

### FASE 4 — Construcción Gestoría IA + Outreach (días 50–90)

**Entregables:**
- Pack Gestoría IA completo (2 demos nuevas + reutilización de 3 ya hechas)
- 25 partners Gestoría IA contactados
- Acuerdo en negociación con 1 asociación

### FASE 5 — HORECA Cockpit + Sistematización (días 80–120)

**Entregables:**
- Pack HORECA Cockpit completo
- 20 partners HORECA contactados
- Skills nuevas en `skills-aritz`:
  - `vertical-pack-builder` — diseña arquitectura de un pack nuevo
  - `partner-prospeccion` — investiga partner individual
  - `asociacion-outreach` — mensajes a asociaciones sectoriales
  - `pack-matching` — empareja pack con cartera de partner
  - `demo-scaffolding` — esqueleto de nueva demo

---

## 6. Criterios de éxito a 120 días

**Construcción:**
- 3 packs completos funcionando en demos (CFO, Gestoría, HORECA)
- 10 demos individuales funcionando
- 3 landings activas + 3 vídeos pitch

**Partners (agregado):**
- 70 partners contactados (25+25+20)
- 15 primeras reuniones cerradas
- 6 segundas reuniones con propuesta económica
- 2–3 acuerdos activos con partners (modelo comisión o revenue share)
- 1 conversación avanzada con asociación sectorial

**Ingresos (señal del canal funcionando):**
- 2–4 proyectos cerrados vía partner (aunque sean pilotos)
- 3–5 proyectos cerrados vía demo directa (catálogo acorta ciclo)
- Ingresos incrementales atribuibles al plan: 35–70K€ en los 120 días + MRR de mantenimiento iniciado

**Contenido (subproducto):**
- 3 posts LinkedIn por pack (9 posts)
- 1 artículo SEO por pack (3 artículos)
- 1 vídeo pitch por pack

---

## 7. Estructura de ficheros

```
packs-verticales/
├── plan-v2-partners-packs.md       (este documento)
├── analisis-50-automatizaciones.md (scoring completo con las 50)
├── packs/
│   ├── cfo-copilot/
│   │   ├── README.md
│   │   ├── arquitectura.md
│   │   ├── demos/
│   │   │   ├── 29-invoice/
│   │   │   ├── 46-cashflow/
│   │   │   ├── 47-budget-variance/
│   │   │   └── 48-report-narrator/
│   │   ├── hub/                     (dashboard central)
│   │   ├── landing.html
│   │   ├── deck-comercial.pdf
│   │   ├── one-pager.pdf
│   │   ├── video-pitch.mp4
│   │   ├── pitch-partner.md
│   │   └── pitch-cliente.md
│   ├── gestoria-ia/                (misma estructura)
│   ├── horeca-cockpit/
│   ├── legalflow/
│   └── talentpipe/
├── partners/
│   ├── directorio-nacional.csv
│   ├── asociaciones.md
│   ├── dossiers-cfo/
│   ├── dossiers-gestoria/
│   ├── dossiers-horeca/
│   ├── matriz-matching.md
│   └── pipeline-partners.csv
└── materiales-cross/
    ├── casos-exito-anonimizados.md
    └── battlecard-partners.md
```

---

## 8. Reglas operativas

- **Alcance nacional obligatorio.** Prospección siempre cubre toda España. No priorizar Euskadi por proximidad. Madrid, Barcelona y Valencia suelen tener más partners cualificados por densidad empresarial.
- **Casos referenciables.** Solo anonimizados ya validados (CASO_1–4, Cafès Cornellà con permiso, Euromanager anonimizado). Nunca mencionar NOMOS/Telefónica ni OpoRuta.
- **Presupuesto de tiempo.** Máximo 40% del tiempo semanal a este plan. Resto sigue en AI Mate y NOMOS.
- **Stop/Go al día 40.** Si 0 de 25 partners CFO Copilot ha llegado a segunda reunión, rediseñar mensaje y ángulo antes de escalar a Gestoría IA.
- **Nunca informar al cliente del uso de Claude Code en la ejecución.**
- **Precios y comisiones son de partida.** Ajustar con los 2–3 primeros partners según negociación real.

---

## 9. Primer arranque (día 1)

1. Validar packs propuestos y vertical piloto.
2. Ejecutar en Claude Code: generación de `analisis-50-automatizaciones.md` con scoring completo como evidencia de decisión.
3. Ejecutar en Claude Code: arquitectura técnica de CFO Copilot (qué tecnologías, qué integraciones, qué dashboard).
4. Arrancar construcción de demo #29 Invoice Processor como primer módulo del pack CFO Copilot.
5. En paralelo: generación del `directorio-nacional.csv` con 50 primeros candidatos de partners CFO Copilot usando Google Places + búsqueda web (alcance nacional, no regional).
