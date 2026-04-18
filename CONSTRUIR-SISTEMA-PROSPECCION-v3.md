# Construir sistema de prospección enterprise — Aritz Abuin IA (v3 Windows, repo + junctions)

> **Instrucciones para Claude Code:** Este documento es la especificación completa de un sistema de prospección B2B que vas a construir de principio a fin en una sola sesión. Léelo entero antes de empezar. Ejecuta las fases en orden (Fase 0 primero, siempre). Al final de cada fase, haz un resumen de lo entregado y pide confirmación antes de pasar a la siguiente. Si encuentras ambigüedad, pregunta — no inventes. Invoca las skills `prospeccion`, `captacion-leads` y `follow-up` del usuario por nombre; **nunca copies su contenido al proyecto ni dupliques su lógica**.
>
> **ENTORNO:** Windows nativo con Claude Code 2.1.104. PowerShell como shell por defecto. Las skills del usuario son **junctions** (enlaces de directorio NTFS) desde `C:\Users\Aritz\.claude\skills\{prospeccion,captacion-leads,follow-up}` → repo fuente de verdad en `C:\Users\Aritz\dev\skills-aritz\`. El proyecto de prospección solo REFERENCIA las skills por nombre; Claude Code las resuelve a través de la junction y ejecuta el contenido canónico del repo. **No copiar, no duplicar, no mover.** Si una skill necesita ajuste, se edita en el repo, se commitea, y todas las junctions lo reflejan automáticamente.

---

## 1. Contexto del usuario

**Aritz Abuin** es freelance AI Solutions Architect en Bilbao operando en toda España. Vende consultoría de IA y automatización a empresas medianas y cadenas. Su approach comercial es **value-first con demo personalizada**: investiga la empresa, construye un ángulo de entrada específico, y propone valor sin pedir reunión en el primer contacto.

Tiene una skill `prospeccion` ya escrita que genera dossiers profundos por empresa y define su metodología de contacto (basada en Hormozi, Voss, Klaff). **Esa skill es la fuente de verdad para el contenido de los mensajes.** Este sistema la envuelve con descubrimiento automático, pipeline de seguimiento y monitorización de respuestas.

### Reglas duras no negociables (aplican a TODO el sistema)

1. **JAMÁS mencionar "NOMOS" ni "Telefónica"** en ningún archivo, plantilla, mensaje o dossier generado. Es un trabajo separado que no existe en contexto comercial.
2. **JAMÁS mencionar "OpoRuta" por nombre**. Se puede decir "he construido aplicaciones SaaS propias" de forma genérica, nada más.
3. **JAMÁS usar nombres reales de clientes** en ningún mensaje de outreach. Todos los casos son anónimos. Si la skill `prospeccion` devuelve "Cafès Cornellà" o "Euromanager", el sistema debe reemplazarlo por su versión anonimizada antes de escribir a `outbox/`.
4. **Idioma: castellano siempre.** Aunque la empresa sea multinacional, el contacto decisor local es español.
5. **Prueba social sin nombres** — usar solo las 4 versiones anonimizadas definidas en el playbook.
6. **Precios siempre en horas-equivalente-manual.** Nunca mencionar Claude Code, aceleración, o cualquier herramienta que el cliente pueda usar como palanca de negociación.
7. **La tasa de apertura de emails NO se trackea.** Solo respuestas. No meter pixels de tracking bajo ningún concepto (mandan a spam y dan falsos positivos con Gmail/Apple Mail).
8. **LinkedIn NO se automatiza.** El sistema genera textos, el usuario los pega manualmente. Intentar scraping o automatización de envío puede banear la cuenta.

### Capacidades comerciales a comunicar

Lo que Aritz SÍ puede decir en outreach:
- Construcción de aplicaciones propias end-to-end (web, móvil, SaaS)
- Agentes de IA personalizados para flujos operativos concretos
- Automatizaciones de procesos con resultados medibles
- Apps nativas móviles (prueba de capacidad técnica completa)
- Mensaje de fondo: *"puedo construir cualquier cosa que necesites"*

### Los 4 casos de éxito anonimizados (única prueba social permitida)

```
CASO_1: "Dirección financiera de una gestoría — 360 horas/año liberadas automatizando el reporting mensual."
CASO_2: "Empleada de agencia de viajes de lujo — 85% de su tiempo operativo liberado mediante agentes de IA personalizados."
CASO_3: "Cadena con más de 100 establecimientos de café — entrega automática de informes diarios por WhatsApp y email + asistente IA para baristas."
CASO_4: "Consultora de recursos humanos — generación automatizada de CVs personalizados a escala."
```

Estos son los **únicos** casos que pueden aparecer en mensajes. Si la skill `prospeccion` genera otro, el sistema lo sustituye.

---

## 2. Datos de configuración del usuario

```yaml
nombre: Aritz Abuin González
rol_publico: Freelance AI Solutions Architect
ubicacion: Bilbao
scope_comercial: Toda España (nacional + multinacionales con oficina en España)
email_envio: aritzabuin1@gmail.com
linkedin_url: https://www.linkedin.com/in/aritz-abuin-gonzalez/
foto_linkedin: (el usuario proporcionará URL cuando configure la firma)
idioma: es-ES
minimo_proyecto_eur: 2000
```

---

## 3. Arquitectura del sistema

### Principio de diseño

El sistema es una **cadena de 6 módulos independientes** orquestados por slash commands de Claude Code. Cada módulo lee/escribe en archivos JSON/MD del proyecto. No hay base de datos, no hay servicios externos de pago, no hay dependencia de n8n. Solo scripts Python, Claude Code + sus skills (referenciadas por nombre vía junctions), y dos APIs gratuitas de Google.

### Modelo de skills: repo único + junctions (crítico)

Las skills NO viven en este proyecto. Viven en un repo git separado (`C:\Users\Aritz\dev\skills-aritz\`, rama `main`) que es la **única fuente de verdad**. Desde `C:\Users\Aritz\.claude\skills\` hay tres junctions (enlaces NTFS tipo `Junction`) apuntando a los subdirectorios `prospeccion\`, `captacion-leads\` y `follow-up\` del repo. Claude Code resuelve las junctions de forma transparente y carga el contenido canónico.

**Implicaciones que este proyecto debe respetar:**

1. **Invocar por nombre, nunca copiar.** Los slash commands y prompts dicen *"Usa la skill `prospeccion` para generar el dossier de `[EMPRESA]`"*, nunca *"lee `SKILL.md` y copia esto"*. Si ves la tentación de volcar contenido de la skill al proyecto (playbook, scripts, prompts), **para**: es un antipatrón que genera drift.
2. **Edición en un único sitio.** Si durante la construcción detectas que una skill necesita ajuste, **no lo hagas en el proyecto**: avisa al usuario, él edita `C:\Users\Aritz\dev\skills-aritz\<skill>\SKILL.md`, commitea, y las tres junctions (más cualquier otro proyecto) reflejan el cambio al instante sin tocar nada.
3. **Versionado automático.** El repo lleva git. No necesitas replicar versionado de skills dentro del proyecto de prospección.
4. **Sin drift entre proyectos.** Si mañana Aritz arranca otro proyecto que también usa `prospeccion`, apuntará a las mismas junctions. Una sola edición, todos consistentes.

Fase 0 verifica que este modelo está intacto antes de construir nada encima.

```
Descubrimiento → Calificación → Dossier → Generación de mensajes →
  → Envío manual (usuario) → Monitorización respuestas → 
  → Clasificación → Dashboard diario → Métricas semanales
```

### Los 6 módulos

1. **Descubrimiento** — Scripts Python que llaman a Google Custom Search + Google Places + scraping de directorios + LinkedIn vía CSE. Normalizan al mismo schema.
2. **Calificación y dossier** — Invoca la skill `prospeccion` por nombre para cada lead aprobado por el usuario (la skill vive en el repo `skills-aritz` vía junction; este módulo solo la referencia, no copia su contenido). Produce dossier `.md`.
3. **Generación de mensajes** — Lee dossier + playbook + estado del lead, produce mensaje listo para pegar en Gmail/LinkedIn en carpeta `outbox/`.
4. **Monitorización de respuestas** — Gmail API (OAuth, gratis) lee la bandeja de Aritz, detecta respuestas a cold emails por `In-Reply-To` header, guarda el cuerpo.
5. **Clasificación de respuestas** — Claude clasifica cada respuesta en `caliente | templada | pide_info | fría | no_interesado | fuera_oficina` y genera borrador de réplica.
6. **Dashboard y métricas** — Slash command `/estado-pipeline` corre cada mañana. Slash command `/metricas-semanales` cada domingo.

### Slash commands que vas a crear

| Comando | Qué hace | Cuándo lo usa Aritz |
|---|---|---|
| `/prospectar-tanda` | Descubre leads nuevos, dedupe, muestra top 15, pide aprobación, genera dossiers con skill `prospeccion` | L/X/V por la mañana |
| `/generar-mensajes <empresa>` | Genera mensaje de Paso 1 / 2 / 3 para una empresa según estado del pipeline | Después de revisar dossiers |
| `/estado-pipeline` | Dashboard diario: respuestas nuevas clasificadas, toques pendientes, métricas live | Cada mañana |
| `/marcar-respuesta <empresa> <canal> <temperatura> "<resumen>"` | Marca manualmente una respuesta recibida por LinkedIn (donde no hay API) | Cada vez que alguien responda en LI |
| `/metricas-semanales` | Genera report de la semana en `reports/` | Domingos |

---

## 4. Estructura completa del proyecto

Crea esta estructura exacta en la ruta que Aritz te indique (por defecto `~/proyectos/prospeccion-auto/` si no dice otra cosa — **pregúntale antes de crear**):

```
prospeccion-auto/
├── .claude/
│   ├── commands/
│   │   ├── prospectar-tanda.md
│   │   ├── generar-mensajes.md
│   │   ├── estado-pipeline.md
│   │   ├── marcar-respuesta.md
│   │   └── metricas-semanales.md
│   └── settings.json
├── CLAUDE.md                         ← contexto del proyecto para futuras sesiones
├── README.md                         ← cómo arrancar, troubleshooting
├── playbook-outreach.md              ← posicionamiento, reglas duras, referencias a skill
├── .env.example                      ← plantilla de API keys
├── .gitignore
├── requirements.txt
├── config/
│   ├── objetivos.json                ← sectores, zonas, filtros
│   ├── queries.json                  ← queries rotativas de descubrimiento
│   ├── directorios.json              ← URLs a scrapear
│   └── firma-email.html              ← firma HTML con foto
├── scripts/
│   ├── __init__.py
│   ├── descubrir_cse.py              ← Google Custom Search
│   ├── descubrir_places.py           ← Google Places API
│   ├── descubrir_directorios.py      ← Scraping BeautifulSoup
│   ├── descubrir_linkedin.py         ← vía CSE con site:linkedin
│   ├── dedupe_y_score.py
│   ├── gmail_auth.py                 ← OAuth setup una sola vez
│   ├── check_respuestas.py           ← Lee Gmail, detecta respuestas
│   ├── clasificar_respuestas.py      ← Invoca Claude para clasificar
│   ├── toques_pendientes.py          ← Calcula qué toca hoy
│   ├── pipeline_utils.py             ← Lectura/escritura pipeline.json
│   ├── anonimizar.py                 ← Sustituye nombres reales por versiones anónimas
│   └── metricas_semanales.py
├── data/
│   ├── pipeline.json                 ← EL archivo central
│   ├── leads_vistos.json             ← Dedupe histórico
│   └── .gitkeep
├── dossiers/
│   └── .gitkeep
├── outbox/                           ← Mensajes listos para copiar y enviar
│   └── .gitkeep
├── respuestas/                       ← Respuestas recibidas y sus borradores
│   └── .gitkeep
├── reports/                          ← Métricas semanales
│   └── .gitkeep
└── logs/
    └── .gitkeep
```

---

## 5. FASE 0 — Verificación de entorno, repo de skills y junctions (OBLIGATORIA, PRIMERA FASE)

**Objetivo:** confirmar que el entorno Windows + Claude Code + **repo de skills + junctions** está correcto antes de construir nada. Si algo falla aquí, paramos y lo arreglamos. Esta fase es defensiva: un drift silencioso entre skills canónicas y skills locales rompería todo el sistema en producción sin avisar.

### 5.0.1 Verificar Claude Code, repo de skills y junctions

Claude Code debe ejecutar este bloque PowerShell entero y validar cada output. Si cualquier bloque marcado como **BLOQUEANTE** falla, parar y pedir instrucciones al usuario antes de seguir.

```powershell
# =========================================================
# Variables (editar aquí si el path del repo cambia)
# =========================================================
$repoSkills     = "C:\Users\Aritz\dev\skills-aritz"
$skillsInstall  = "$env:USERPROFILE\.claude\skills"
$skillsReq      = @("prospeccion", "captacion-leads", "follow-up")
$markerCanonico = "CASO_1"   # string que toda skill canónica v1 debe contener

# =========================================================
# 1. Claude Code version (mínimo 2.0) — BLOQUEANTE
# =========================================================
claude --version

# =========================================================
# 2. Python (requerido para los scripts) — BLOQUEANTE
# =========================================================
python --version

# =========================================================
# 3. Repo fuente de verdad existe y es git — BLOQUEANTE
# =========================================================
if (-not (Test-Path (Join-Path $repoSkills ".git"))) {
    Write-Host "ERROR BLOQUEANTE: no existe repo git en $repoSkills" -ForegroundColor Red
    Write-Host "  → El sistema de skills canónicas no está instalado. Parar y avisar al usuario." -ForegroundColor Red
} else {
    Write-Host "OK: repo skills-aritz presente en $repoSkills" -ForegroundColor Green
}

# =========================================================
# 4. Cada skill es JUNCTION al repo (no carpeta real) — BLOQUEANTE
# =========================================================
foreach ($skill in $skillsReq) {
    $skillDir = Join-Path $skillsInstall $skill
    if (-not (Test-Path $skillDir)) {
        Write-Host "ERROR BLOQUEANTE: no existe $skillDir" -ForegroundColor Red
        continue
    }
    $item = Get-Item $skillDir -Force
    if ($item.LinkType -ne "Junction") {
        Write-Host "ERROR BLOQUEANTE: $skill NO es junction (es $($item.LinkType ?? 'carpeta real'))" -ForegroundColor Red
        Write-Host "  → Peligro de drift. Rehacer junction desde $repoSkills\$skill" -ForegroundColor Red
        continue
    }
    $target = ($item.Target | Select-Object -First 1)
    if ($target -notmatch "skills-aritz") {
        Write-Host "ERROR BLOQUEANTE: $skill apunta a $target (no al repo)" -ForegroundColor Red
        continue
    }
    Write-Host "OK: $skill es Junction → $target" -ForegroundColor Green
}

# =========================================================
# 5. Contenido canónico (no placeholder) — BLOQUEANTE
# =========================================================
foreach ($skill in $skillsReq) {
    $skillFile = Join-Path $skillsInstall "$skill\SKILL.md"
    if (-not (Test-Path $skillFile)) {
        Write-Host "ERROR BLOQUEANTE: falta SKILL.md en $skill" -ForegroundColor Red
        continue
    }
    $contenido = Get-Content $skillFile -Raw
    $esPlaceholder = $contenido -match "TODO|PLACEHOLDER|Lorem ipsum"
    $esCanonico    = $contenido -match $markerCanonico
    if ($esPlaceholder -or -not $esCanonico) {
        Write-Host "ERROR BLOQUEANTE: $skill no tiene contenido canónico (marker '$markerCanonico' ausente o placeholder detectado)" -ForegroundColor Red
    } else {
        Write-Host "OK: $skill contenido canónico verificado" -ForegroundColor Green
    }
}

# =========================================================
# 6. Repo limpio (sin cambios sin commitear) — WARNING (no bloqueante)
# =========================================================
Push-Location $repoSkills
$dirty = git status --porcelain
Pop-Location
if ($dirty) {
    Write-Host "WARNING: repo skills-aritz tiene cambios sin commitear:" -ForegroundColor Yellow
    Write-Host $dirty -ForegroundColor Yellow
    Write-Host "  → Se puede continuar, pero considera commitear antes de construir encima." -ForegroundColor Yellow
} else {
    Write-Host "OK: repo skills-aritz limpio (git status sin cambios)" -ForegroundColor Green
}
```

**Criterio de pase:**
- Claude Code ≥ 2.0 y Python 3.10+ disponibles.
- `C:\Users\Aritz\dev\skills-aritz\.git` existe.
- Las 3 skills son `LinkType -eq 'Junction'` con `Target` conteniendo `skills-aritz`.
- Cada `SKILL.md` contiene el marker canónico (`CASO_1`) y no contiene `TODO`/`PLACEHOLDER`/`Lorem ipsum`.
- `git status --porcelain` del repo idealmente vacío (warning, no bloqueante).

Si cualquier BLOQUEANTE falla: **parar Fase 0**, mostrar el error al usuario, y preguntar cómo proceder. No intentar "reparar" junctions ni copiar skills como fallback — eso rompería el modelo de fuente única.

### 5.0.2 Leer el contenido canónico de las 3 skills vía junction y resumirlo al usuario

Claude Code debe:
1. Leer `C:\Users\Aritz\.claude\skills\prospeccion\SKILL.md` (resuelto a través de la junction al repo).
2. Leer `C:\Users\Aritz\.claude\skills\captacion-leads\SKILL.md`.
3. Leer `C:\Users\Aritz\.claude\skills\follow-up\SKILL.md`.
4. Generar un resumen breve (3-5 líneas por skill): qué hace, cuándo se invoca, qué outputs produce.
5. Mostrárselo al usuario y preguntar: *"¿Este es el comportamiento esperado? ¿Hay algo que deba tener en cuenta al integrarlas en el sistema?"*

Esto garantiza que Claude Code ha leído las skills reales (canónicas del repo) y que el usuario puede confirmar el comportamiento antes de construir dependencias sobre ellas.

### 5.0.3 Confirmar modelo de invocación antes de pasar a Fase 1

Claude Code debe exponer al usuario el contrato de invocación que aplicará durante toda la construcción:

> *"Durante las fases 1–4 invocaré las skills por nombre (`prospeccion`, `captacion-leads`, `follow-up`) en slash commands y prompts. **No voy a copiar su contenido a archivos del proyecto, ni a duplicar su lógica en playbooks o scripts.** Si detecto que alguna skill necesita ajuste, te aviso para que lo edites en `C:\Users\Aritz\dev\skills-aritz\<skill>\SKILL.md`, commitees, y las junctions reflejen el cambio."*

Justificación (explicar al usuario si pregunta): edición en un único sitio, versionado git automático, cero drift entre proyectos que compartan las mismas skills, auditoría clara de cambios.

### 5.0.4 Preguntar al usuario y confirmar antes de pasar a Fase 1

Antes de escribir ningún archivo del proyecto:

1. **Ruta absoluta del proyecto en Windows.** Sugerencia: `C:\Users\Aritz\proyectos\prospeccion-auto`. Confirmar con el usuario.
2. **¿Inicializar git en el proyecto?** Recomendado: sí (independiente del repo `skills-aritz`).
3. **¿Resumen de skills correcto? ¿Contrato de invocación aceptado? ¿Empiezo Fase 1?**

Solo cuando el usuario confirme, pasar a Fase 1.

### Checkpoint Fase 0

Al acabar: entorno validado, **repo `skills-aritz` verificado**, **junctions confirmadas como Junction → repo**, **contenido canónico verificado**, repo limpio (o warning asumido), resumen de skills confirmado por el usuario, contrato de invocación aceptado, ruta del proyecto decidida. Sin esto, NO pasar a Fase 1.

---

## 6. FASE 1 — Cimientos

**Objetivo:** dejar la estructura montada con todos los archivos de configuración, contexto y playbook. Al acabar Fase 1 el proyecto está listo para que el usuario pueda leerlo y ajustarlo antes de montar el descubrimiento.

### 5.1 Crear `CLAUDE.md` del proyecto

Contenido exacto:

```markdown
# Sistema de prospección — Aritz Abuin IA

Proyecto de prospección B2B semi-automatizada. Se ejecuta localmente
en el Mac de Aritz cuando él decide (L/X/V típicamente). Sin cron,
sin servicios externos de pago.

## Stack
- Claude Code como orquestador
- Skills del usuario: `prospeccion`, `captacion-leads`, `follow-up` — **fuente de verdad en `C:\Users\Aritz\dev\skills-aritz\` (repo git, rama `main`)**. Instaladas vía junctions en `%USERPROFILE%\.claude\skills\`. Este proyecto las invoca por nombre; NO copia su contenido ni duplica su lógica. Ajustes → editar en el repo y commitear; las junctions reflejan el cambio automáticamente.
- Python 3.11+ para scripts de descubrimiento y Gmail API
- Google Custom Search API + Google Places API (ambas gratis)
- Gmail API (OAuth, gratis) para monitorización de respuestas
- JSON local versionado en git como "base de datos"

## Flujo diario tipo

**Mañana (L/X/V):**
1. Abrir Claude Code en este proyecto
2. Ejecutar `/estado-pipeline` → ver respuestas nuevas + toques pendientes
3. Ejecutar `/prospectar-tanda` → descubrir 15 leads nuevos
4. Revisar top 15, aprobar los buenos
5. Para cada aprobado: ejecutar `/generar-mensajes <empresa>`
6. Copiar mensajes de `outbox/{fecha}/` a Gmail / LinkedIn
7. Enviar manualmente

**Cuando recibe respuesta por LinkedIn:**
- Ejecutar `/marcar-respuesta <empresa> linkedin <temperatura> "<resumen>"`

**Domingos:**
- Ejecutar `/metricas-semanales`

## Reglas duras del sistema (CRÍTICO)

1. NUNCA mencionar NOMOS ni Telefónica en ningún output
2. NUNCA mencionar OpoRuta por nombre (solo "aplicaciones SaaS propias")
3. NUNCA nombres reales de clientes — usar siempre los 4 casos anonimizados
   del playbook
4. Idioma: castellano siempre
5. No tracking de apertura (solo respuestas)
6. LinkedIn: envío siempre manual, nunca scripted

## Archivos clave

- `playbook-outreach.md` — positioning, reglas, referencias a skill
- `data/pipeline.json` — cerebro del sistema, cada lead con su historial
- `config/objetivos.json` — sectores y zonas objetivo
- `.env` — credenciales (NO commitear)

## Dependencias

Ver `requirements.txt`. Instalación en PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Nota Windows:** si PowerShell da error de ejecución de scripts al activar el venv, el usuario debe correr una vez (solo una vez, como admin):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Setup inicial de Gmail API

Ver `README.md` sección "Setup Gmail API". Es OAuth una sola vez.
```

### 5.2 Crear `playbook-outreach.md`

Este es el archivo más importante del sistema. Va a ser leído por cada slash command que genere un mensaje. Contenido exacto:

```markdown
# Playbook de outreach — Aritz Abuin IA

> Este documento es la guía de marca y metodología para TODOS los mensajes
> generados por el sistema. Se lee en cada generación de mensaje junto con
> el dossier de la empresa y la skill `prospeccion`.

## Positioning (elevator)

Aritz Abuin. Freelance AI Solutions Architect en Bilbao. Construyo
aplicaciones propias, agentes de IA y automatizaciones para empresas
medianas y cadenas en toda España. El objetivo siempre es el mismo:
liberar horas de operación que hoy drenan el negocio.

## Reglas duras (NO NEGOCIABLES)

- NUNCA mencionar "NOMOS" ni "Telefónica"
- NUNCA mencionar "OpoRuta" por nombre (solo "aplicaciones SaaS propias")
- NUNCA nombres reales de clientes (todos los casos son anónimos)
- Idioma: castellano
- Sin jerga de consultor ("dashboards operativos", "pipeline de datos")
- Sin emojis corporativos. Sin exclamaciones. Sin "encantado de conocerte"
- Frases cortas. Cero relleno. Lenguaje de par curioso, no de vendedor.

## Metodología de contacto

**La metodología está definida en la skill `prospeccion`.** Este playbook
NO duplica plantillas — el sistema carga la skill y aplica su metodología
de 3 pasos (nota de conexión / primer mensaje / segundo mensaje), junto
con las reglas de follow-up (7, 14, 21 días; máximo 3 intentos y parar).

Este playbook añade a la skill:
1. Reglas de anonimización (abajo)
2. Los 4 casos de éxito permitidos (abajo)
3. Adaptación para email (la skill está pensada para LinkedIn, aquí extendemos)

## Anonimización de casos

Si la skill `prospeccion` genera un mensaje con cualquiera de estos términos,
el sistema los sustituye automáticamente antes de escribir a `outbox/`:

| Término original (skill) | Sustitución en outreach |
|---|---|
| Euromanager | "una consultora de RRHH" |
| Cafès Cornellà | "una cadena con más de 100 establecimientos de café" |
| "directora financiera" (de caso concreto) | "la dirección financiera de una gestoría" |
| "empresa de viajes de lujo" | "una agencia de viajes de lujo" |
| Cualquier nombre propio de cliente | versión genérica de su sector |

## Casos de éxito permitidos (los únicos)

Estos son los 4 únicos casos que pueden aparecer en mensajes. Se usan
SOLO en el Paso 3 (cuando ya hay respuesta e interés), nunca en primer
contacto. La skill `prospeccion` ya respeta esta regla.

- **CASO_1:** Dirección financiera de una gestoría — 360 horas/año
  liberadas automatizando el reporting mensual.
- **CASO_2:** Empleada de agencia de viajes de lujo — 85% de su tiempo
  operativo liberado mediante agentes de IA personalizados.
- **CASO_3:** Cadena con más de 100 establecimientos de café —
  entrega automática de informes diarios por WhatsApp y email + asistente
  IA para baristas.
- **CASO_4:** Consultora de recursos humanos — generación automatizada
  de CVs personalizados a escala.

**Regla de selección:** usar el caso más cercano al sector del destinatario.
Si es hostelería → CASO_3. Si es servicios profesionales → CASO_1 o CASO_4.
Si es comercio de lujo o retail premium → CASO_2.

## Secuencia de email (extensión para canal email)

La skill `prospeccion` define metodología para LinkedIn. Para email, el
sistema aplica la misma filosofía (valor primero, pregunta que revela dolor,
sin pedir reunión en primer contacto) pero adaptada:

**Email T1 — Primer contacto (día 0)**
- Asunto: 3-5 palabras, específico, sin "IA" ni "automatización" ni "propuesta"
- Apertura: observación concreta sobre SU empresa (del dossier)
- Cuerpo: 60-90 palabras, una sola idea
- Cierre: pregunta que incomoda con respeto. NUNCA "¿agendamos reunión?"
- Firma: con foto (HTML en `config/firma-email.html`)

**Email T2 — Follow-up con valor (día 7, solo si no hubo respuesta)**
- Asunto: "Re:" del T1
- 40-60 palabras
- Aporte de valor puro: un dato del sector, una observación, una idea
- Sin pedir nada

**Email T3 — Último intento (día 21, solo si sigue sin respuesta)**
- Asunto: "¿Cierro el hilo?" o similar
- 30-40 palabras
- Break-up educado, deja la puerta abierta
- Sin presión

**Después de T3 sin respuesta: PARAR.** Marcar en pipeline como
`sin_respuesta_3t` y reactivar a los 3 meses con motivo concreto
(cambio en la empresa, contenido nuevo publicado, etc.).

## Secuencia LinkedIn (paralela al email)

La skill `prospeccion` define los 3 pasos. El sistema los usa tal cual.
Tiempos relativos al T1 del email:

- Día 2 del T1: enviar connection request (Paso 1 de la skill)
- Día 4-5 (si aceptó): primer mensaje LI (Paso 2 de la skill)
- Día 10 (si respondió al Paso 2): segundo mensaje LI (Paso 3 de la skill)
- Si no acepta la conexión en 7 días: no insistir

## Tono y estilo (alineado con la skill)

- De igual a igual. Experto curioso, no vendedor
- Natural. Como hablarías con un conocido de sector en un evento
- Frases cortas. Preguntas directas. Cero relleno
- Si no puedes decirlo en lenguaje normal, no lo digas
- Primera persona del singular ("he construido", "creo que")
- Ningún superlativo ("increíble", "revolucionario", "transformador")

## Firma de email

Archivo: `config/firma-email.html`. HTML mínimo, inline CSS, con:
- Nombre: Aritz Abuin González
- Rol: Freelance AI Solutions Architect
- Foto: URL de foto (el usuario la configura en `.env` como `FOTO_URL`)
- LinkedIn: https://www.linkedin.com/in/aritz-abuin-gonzalez/
- Email: aritzabuin1@gmail.com

Sin teléfono. Sin links adicionales. Sin logos. Minimalista.
```

### 5.3 Crear `config/objetivos.json`

```json
{
  "sectores_prioritarios": [
    {
      "id": "hosteleria_cadenas",
      "descripcion": "Cadenas de restauración con ≥3 establecimientos",
      "keywords": ["cadena restaurantes", "grupo restauración", "franquicia hostelería"],
      "min_establecimientos": 3,
      "caso_exito_preferente": "CASO_3"
    },
    {
      "id": "clinicas_dentales_esteticas",
      "descripcion": "Cadenas de clínicas dentales y estéticas",
      "keywords": ["cadena clínica dental", "grupo clínicas estéticas", "centros odontológicos"],
      "min_establecimientos": 3,
      "caso_exito_preferente": "CASO_1"
    },
    {
      "id": "fitness_cadenas",
      "descripcion": "Cadenas de gimnasios y centros de fitness",
      "keywords": ["cadena gimnasios", "grupo fitness", "centros deportivos"],
      "min_establecimientos": 3,
      "caso_exito_preferente": "CASO_1"
    },
    {
      "id": "consultoras_rrhh",
      "descripcion": "Consultoras de recursos humanos y selección",
      "keywords": ["consultora RRHH", "empresa selección personal", "headhunting"],
      "min_establecimientos": 1,
      "caso_exito_preferente": "CASO_4"
    },
    {
      "id": "gestorías_asesorías",
      "descripcion": "Gestorías y asesorías medianas",
      "keywords": ["gestoría", "asesoría fiscal", "asesoría laboral"],
      "min_establecimientos": 1,
      "caso_exito_preferente": "CASO_1"
    }
  ],
  "zonas_prioritarias": [
    "Madrid",
    "Barcelona",
    "Valencia",
    "Bilbao",
    "Sevilla",
    "Málaga",
    "Zaragoza"
  ],
  "filtros": {
    "excluir_sectores": ["gobierno", "ONG", "religioso"],
    "excluir_si_menor_de_empleados": 5,
    "minimo_score_para_dossier": 60
  }
}
```

### 5.4 Crear `config/queries.json`

```json
{
  "google_custom_search": {
    "senales_apertura": [
      "abre nuevo local {ciudad} {sector}",
      "inaugura restaurante {ciudad}",
      "expansión cadena {sector} España 2026"
    ],
    "senales_financiacion": [
      "ronda financiación {sector} España",
      "inversión cadena {sector} 2026",
      "{sector} cierra ronda millones"
    ],
    "senales_crecimiento": [
      "{sector} contrata responsable operaciones",
      "{sector} director transformación digital",
      "{sector} office manager ofertas empleo"
    ],
    "linkedin_site": [
      "site:linkedin.com/jobs \"director operaciones\" {sector} España",
      "site:linkedin.com/jobs \"responsable digitalización\" {sector}",
      "site:linkedin.com/company {sector} España"
    ]
  },
  "rotacion": {
    "queries_por_ejecucion": 6,
    "dias_antes_de_repetir": 14
  }
}
```

### 5.5 Crear `config/directorios.json`

```json
{
  "directorios": [
    {
      "id": "hosteleria_digital",
      "url": "https://www.hosteleriadigital.es/",
      "sector": "hosteleria_cadenas",
      "activo": true,
      "selector_noticias": "article.post",
      "nota": "Verificar selector antes de activar"
    },
    {
      "id": "restauracion_news",
      "url": "https://www.restauracionnews.com/",
      "sector": "hosteleria_cadenas",
      "activo": false,
      "nota": "Pendiente de explorar estructura"
    }
  ],
  "nota_general": "Este archivo arranca con pocas entradas. Aritz lo expande cuando identifique directorios relevantes de sus sectores. El scraping solo activa los 'activo: true'."
}
```

### 5.6 Crear `config/firma-email.html`

```html
<!-- Firma de email Aritz Abuin — inline CSS para compatibilidad Gmail -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; font-size: 13px; color: #333333; line-height: 1.5;">
  <tr>
    <td style="padding-right: 14px; vertical-align: top;">
      <img src="{{FOTO_URL}}" alt="Aritz Abuin" width="70" height="70" style="border-radius: 50%; display: block;" />
    </td>
    <td style="vertical-align: top; border-left: 2px solid #e0e0e0; padding-left: 14px;">
      <div style="font-weight: bold; font-size: 14px; color: #1a1a1a;">Aritz Abuin González</div>
      <div style="color: #666666; font-size: 12px; margin-top: 2px;">Freelance AI Solutions Architect</div>
      <div style="margin-top: 8px; font-size: 12px;">
        <a href="https://www.linkedin.com/in/aritz-abuin-gonzalez/" style="color: #0077b5; text-decoration: none;">LinkedIn</a>
        &nbsp;·&nbsp;
        <a href="mailto:aritzabuin1@gmail.com" style="color: #666666; text-decoration: none;">aritzabuin1@gmail.com</a>
      </div>
    </td>
  </tr>
</table>
```

**Nota:** `{{FOTO_URL}}` se sustituye en tiempo de generación desde `.env`. Para la foto, Aritz va a subir la que tiene en LinkedIn a un host estable (ImgBB, Cloudinary o su propio dominio) y pegar la URL directa en `.env`.

### 5.7 Crear `data/pipeline.json` con schema documentado

```json
{
  "_schema_version": "1.0",
  "_schema_doc": "Cada clave del nivel superior es un slug-empresa único. Ver README para schema detallado.",
  "_ejemplo_descomentar_para_guiar": {
    "empresa-slug-ejemplo": {
      "empresa": "Nombre SL",
      "web": "nombresl.com",
      "sector": "hosteleria_cadenas",
      "zona": "Madrid",
      "num_establecimientos": 12,
      "fuente_descubrimiento": "google_places",
      "senal_inicial": "apertura nuevo local marzo 2026",
      "score": 87,
      "capacidad_economica": "PYME_MEDIANA",
      "fecha_descubrimiento": "2026-04-08",
      "contacto": {
        "nombre": null,
        "rol": null,
        "email": null,
        "linkedin": null
      },
      "estado_email": "nuevo",
      "estado_linkedin": "nuevo",
      "temperatura": null,
      "historial": [],
      "proxima_accion": {
        "fecha": null,
        "tipo": null,
        "generada": false
      },
      "dossier_path": null,
      "notas": ""
    }
  },
  "leads": {}
}
```

### 5.8 Crear `data/leads_vistos.json`

```json
{
  "_descripcion": "Cache de dominios ya procesados para dedupe rápido. Formato: {dominio: {primera_vez: ISO_date, ultimo_score: int}}",
  "dominios": {}
}
```

### 5.9 Crear `.env.example`

```bash
# ====================================
# Prospección Auto — variables de entorno
# Copia este archivo a .env y rellénalo
# ====================================

# Google Cloud (misma cuenta para las 3 APIs)
GOOGLE_API_KEY=
GOOGLE_CSE_ID=
GOOGLE_PLACES_API_KEY=

# Gmail API — se rellena automáticamente tras correr scripts/gmail_auth.py
# NO editar a mano estos valores
GMAIL_TOKEN_PATH=./.gmail_token.json
GMAIL_CREDENTIALS_PATH=./.gmail_credentials.json

# Foto de Aritz para firma de email
# Sube la foto de LinkedIn a ImgBB (gratis) o Cloudinary y pega la URL directa
FOTO_URL=https://ejemplo.com/foto-aritz.jpg

# Claude API — opcional, solo si en Fase 4 quieres clasificar con API en vez de
# con tu plan de Claude Code. Por defecto, dejar vacío y el sistema usa Claude Code.
ANTHROPIC_API_KEY=
```

### 5.10 Crear `.gitignore`

```
.env
.gmail_token.json
.gmail_credentials.json
.venv/
__pycache__/
*.pyc
.DS_Store
logs/*.log
```

### 5.11 Crear `requirements.txt`

```
google-api-python-client>=2.100.0
google-auth-httplib2>=0.2.0
google-auth-oauthlib>=1.1.0
requests>=2.31.0
beautifulsoup4>=4.12.0
python-dotenv>=1.0.0
rapidfuzz>=3.5.0
```

### 5.12 Crear `README.md`

```markdown
# Sistema de prospección — Aritz Abuin IA

Sistema local de prospección B2B con Claude Code como orquestador.

## Arranque rápido

1. **Prerrequisito crítico:** el repo de skills debe estar en `C:\Users\Aritz\dev\skills-aritz\` con las 3 junctions activas (`prospeccion`, `captacion-leads`, `follow-up`) en `%USERPROFILE%\.claude\skills\`. Verificar con: `Get-Item $env:USERPROFILE\.claude\skills\prospeccion | Select LinkType,Target` → debe ser `Junction` apuntando a `skills-aritz`. Si no, parar y reinstalar junctions desde el repo antes de seguir.
2. Clonar / copiar este proyecto
3. Crear entorno virtual (PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Copiar `.env.example` a `.env` y rellenar credenciales
5. Seguir sección "Setup inicial" abajo

## Setup inicial (una sola vez)

### Google Cloud Console
1. Crear proyecto en https://console.cloud.google.com
2. Activar las 3 APIs:
   - Custom Search API
   - Places API (New)
   - Gmail API
3. Crear API Key (Credenciales → Crear credencial → API Key)
4. Pegar en `.env` como `GOOGLE_API_KEY` y `GOOGLE_PLACES_API_KEY`

### Programmable Search Engine
1. Ir a https://programmablesearchengine.google.com/
2. Crear nuevo motor, activar "Buscar en toda la web"
3. Copiar el Search Engine ID → `.env` como `GOOGLE_CSE_ID`

### Gmail OAuth
1. En Google Cloud Console → Credenciales → Crear credencial → ID de cliente OAuth
2. Tipo: "Aplicación de escritorio"
3. Descargar JSON → guardar como `.gmail_credentials.json` en raíz del proyecto
4. Ejecutar `python scripts\gmail_auth.py` — abre navegador, autoriza
5. Se genera `.gmail_token.json` automáticamente

### Foto para firma
1. Subir tu foto de LinkedIn a ImgBB (https://imgbb.com) — gratis, sin cuenta
2. Copiar la URL directa (termina en .jpg o .png)
3. Pegar en `.env` como `FOTO_URL`

## Uso diario

Ver `CLAUDE.md` sección "Flujo diario tipo".

## Troubleshooting

- **Gmail API da error de permisos** → borra `.gmail_token.json` y corre `gmail_auth.py` otra vez
- **Custom Search devuelve 0 resultados** → revisa que el motor tenga "Buscar en toda la web" activado
- **Places API da quota exceeded** → revisa cuota en GCP, por defecto son 200$/mes gratis
```

### 5.13 Crear `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(python scripts/*)",
      "Bash(python scripts\\\\*)",
      "Bash(.venv\\\\Scripts\\\\Activate.ps1)",
      "Bash(mkdir -p *)",
      "Bash(ls *)",
      "Bash(dir *)",
      "Bash(cat *)",
      "Bash(type *)",
      "Bash(git *)",
      "Read(*)",
      "Write(data/*)",
      "Write(dossiers/*)",
      "Write(outbox/*)",
      "Write(respuestas/*)",
      "Write(reports/*)",
      "Write(logs/*)"
    ]
  }
}
```

**Nota:** Claude Code en Windows nativo usa Git Bash como shell por defecto para `Bash(...)`, por eso funcionan tanto rutas con `/` como con `\`.

### Checkpoint Fase 1

Al terminar esta fase, verifica que existen todos los archivos listados, que `playbook-outreach.md` tiene todas las reglas duras, y que el proyecto puede leerse sin ambigüedad. Haz un resumen al usuario y pregunta si quiere ajustar algo antes de pasar a Fase 2.

---

## 6. FASE 2 — Descubrimiento y dossier

**Objetivo:** que `/prospectar-tanda` funcione end-to-end: descubre → deduplica → muestra → aprueba → dossier.

### 6.1 Crear `scripts/pipeline_utils.py`

Utilidades compartidas para leer/escribir pipeline.json con locking y validación. Funciones mínimas:

- `load_pipeline() -> dict`
- `save_pipeline(data: dict)` — con backup automático en `data/pipeline.backup.json`
- `add_lead(slug: str, data: dict)` — añade un lead nuevo
- `update_lead(slug: str, patches: dict)` — merge parcial
- `add_historial_event(slug: str, event: dict)` — append al historial
- `get_lead(slug: str) -> dict | None`
- `slugify(nombre_empresa: str) -> str` — normaliza a kebab-case sin acentos

### 6.2 Crear `scripts/anonimizar.py`

Función `anonimizar(texto: str) -> str` que recibe un texto y sustituye:

- `Euromanager` → `una consultora de RRHH`
- `Cafès Cornellà` / `Cafes Cornella` → `una cadena con más de 100 establecimientos de café`
- Cualquier aparición de `NOMOS` → lanzar excepción (nunca debería aparecer en outreach)
- Cualquier aparición de `OpoRuta` → `aplicaciones SaaS propias`
- `Telefónica` → lanzar excepción

Esta función se llama **obligatoriamente** antes de escribir cualquier mensaje a `outbox/`. Tests unitarios básicos en el propio archivo (función `_self_test()` al final).

### 6.3 Crear `scripts/descubrir_cse.py`

Script que:
1. Lee `config/queries.json` y `config/objetivos.json`
2. Selecciona N queries rotando (guarda estado de última ejecución en `data/cse_rotacion.json`)
3. Llama a Custom Search API por cada query × ciudad
4. Normaliza resultados a schema común:
   ```json
   {
     "empresa_nombre_guess": "...",
     "web": "...",
     "sector": "...",
     "zona": "...",
     "fuente": "google_cse",
     "senal": "texto del snippet",
     "url_origen": "...",
     "fecha_detección": "2026-04-08T07:15:00"
   }
   ```
5. Escribe output a `data/candidatos-{fecha}.json` (append si ya existe)

### 6.4 Crear `scripts/descubrir_places.py`

Script que:
1. Lee sectores y zonas de `config/objetivos.json`
2. Por cada combo (sector, ciudad), llama a Places Nearby Search
3. Filtra por `min_establecimientos` (usa `formattedAddress` + búsquedas de nombre similares en mismo sector para estimar cadena)
4. Normaliza al mismo schema que CSE
5. Append a `data/candidatos-{fecha}.json`

### 6.5 Crear `scripts/descubrir_directorios.py`

Script que:
1. Lee `config/directorios.json` y filtra `activo: true`
2. Por cada directorio, hace GET + parse con BeautifulSoup
3. Extrae noticias/empresas según `selector_noticias`
4. Normaliza al schema
5. Append a candidatos

**Importante:** este script es el más frágil porque depende de la estructura HTML de cada directorio. Dejarlo robusto a fallos: si un directorio falla, logear y continuar.

### 6.6 Crear `scripts/descubrir_linkedin.py`

Variante de `descubrir_cse.py` que usa queries específicas de `linkedin_site` con `site:linkedin.com/jobs` y `site:linkedin.com/company`. Mismo output.

### 6.7 Crear `scripts/dedupe_y_score.py`

Script que:
1. Lee `data/candidatos-{fecha}.json`
2. Lee `data/leads_vistos.json` y `data/pipeline.json`
3. Dedupe por dominio web (usando `rapidfuzz` para nombres similares)
4. Scoring simple (0-100):
   - +30 si dominio propio (no Instagram/Facebook)
   - +20 si sector en lista prioritaria
   - +15 si zona en lista prioritaria
   - +15 si señal es reciente (<30 días)
   - +10 si hay indicador de cadena (múltiples establecimientos detectados)
   - +10 si aparece en más de una fuente
5. Filtra por `minimo_score_para_dossier` de objetivos.json
6. Ordena desc por score
7. Escribe top 20 a `data/top-candidatos-{fecha}.json`

### 6.8 Crear `.claude/commands/prospectar-tanda.md`

```markdown
# /prospectar-tanda

Ejecuta la tanda de descubrimiento y calificación de leads nuevos.

## Pasos

1. Activa el entorno virtual: `.venv\Scripts\Activate.ps1`

2. Ejecuta los 4 scripts de descubrimiento en secuencia (paralelo innecesario
   para este volumen). Muestra progreso:
   - `python scripts\descubrir_cse.py`
   - `python scripts\descubrir_places.py`
   - `python scripts\descubrir_directorios.py`
   - `python scripts\descubrir_linkedin.py`

3. Ejecuta dedupe y scoring:
   - `python scripts\dedupe_y_score.py`

4. Lee `data/top-candidatos-{fecha_hoy}.json` y muestra al usuario una tabla
   con las primeras 15 empresas: nombre, web, sector, zona, score, señal.

5. Pregunta al usuario: "¿Qué leads quieres procesar a dossier? Responde con
   los números (ej: 1,3,5-8) o 'todos' o 'ninguno'."

6. Para cada lead aprobado, invoca la skill `prospeccion` **por nombre** (NO leer su `SKILL.md` y reproducir la lógica aquí; la skill vive en el repo `skills-aritz` vía junction y Claude Code la resuelve sola):
   - La skill lee la empresa, hace research profundo y genera dossier
   - **CRÍTICO**: Al generar cualquier texto de mensaje o ángulo, aplica
     `scripts/anonimizar.py` al output antes de guardarlo
   - Guarda el dossier en `dossiers/{fecha_hoy}/{slug-empresa}.md`
   - Añade el lead a `data/pipeline.json` con estado `nuevo` usando
     `pipeline_utils.add_lead()`
   - Registra evento en historial: `{tipo: "dossier_generado", fecha: ...}`

7. Al terminar, muestra resumen al usuario:
   ```
   Tanda completada — {fecha}
   Leads descubiertos: N
   Leads aprobados: M
   Dossiers generados: M
   
   Revisa los dossiers en dossiers/{fecha}/
   Para generar mensajes: /generar-mensajes <slug-empresa>
   ```

## Reglas

- Si algún script de descubrimiento falla, logea en `logs/` y continúa
- Si la skill `prospeccion` genera mensaje con nombres prohibidos, rechazar
  y pedir regenerar sin esos términos
- No procesar a dossier ningún lead con score < 60
```

### Checkpoint Fase 2

Verificar que `/prospectar-tanda` funciona en dry-run (sin llamar APIs reales todavía — si el usuario no ha configurado `.env` aún, simular con 3 candidatos mock). Pedir al usuario que configure Google Cloud Console y corra una tanda real. Esperar confirmación antes de Fase 3.

---

## 7. FASE 3 — Generación de mensajes y outbox

**Objetivo:** que `/generar-mensajes <empresa>` produzca mensajes listos para copiar.

### 7.1 Crear `.claude/commands/generar-mensajes.md`

```markdown
# /generar-mensajes <slug-empresa>

Genera los mensajes de outreach para una empresa concreta según su estado
en el pipeline.

## Entrada

Argumento: slug de empresa (ej: `grupo-ejemplo-sl`)

## Pasos

1. Lee `data/pipeline.json` y encuentra el lead por slug. Si no existe,
   avisa al usuario y para.

2. Lee `dossiers/{fecha}/{slug}.md` para tener el contexto de la empresa.

3. Lee `playbook-outreach.md` entero.

4. Determina qué mensaje toca según `estado_email` y `estado_linkedin`:
   - Si `estado_email == "nuevo"` → generar Email T1 + LinkedIn connection (Paso 1 skill)
   - Si `estado_email == "enviado_t1"` y han pasado ≥7 días sin respuesta → Email T2
   - Si `estado_email == "enviado_t2"` y han pasado ≥14 días sin respuesta → Email T3
   - Si `estado_linkedin == "connection_aceptada"` → LinkedIn Paso 2 (skill)
   - Si `estado_linkedin == "respondio_paso2"` → LinkedIn Paso 3 (skill, puede incluir caso de éxito)

5. Para LinkedIn: invoca la skill `prospeccion` con el contexto del dossier
   pidiendo el paso correspondiente. La skill ya tiene la metodología.

6. Para email: aplica la metodología del playbook (extensión email).
   - T1: asunto 3-5 palabras + 60-90 palabras cuerpo + firma HTML
   - T2: follow-up de valor puro 40-60 palabras
   - T3: break-up 30-40 palabras

7. **CRÍTICO — validación de reglas duras** antes de escribir a outbox:
   - Correr `scripts/anonimizar.py` sobre cada texto generado
   - Verificar que NO aparecen: NOMOS, Telefónica, OpoRuta (case-insensitive)
   - Verificar que NO aparecen nombres reales de clientes
   - Si alguna regla falla, regenerar o avisar al usuario

8. Escribe los mensajes a `outbox/{fecha_hoy}/{slug}/`:
   - `email-t{N}.md` — asunto + cuerpo plano + nota al final
   - `email-t{N}.html` — cuerpo + firma HTML lista para pegar en Gmail "modo HTML"
   - `linkedin-paso{N}.md` — texto plano del mensaje

9. Actualiza el pipeline:
   - Añade evento a historial: `{tipo: "mensaje_generado", canal, toque, fecha}`
   - Campo `proxima_accion.generada = true`

10. Muestra al usuario:
    ```
    Mensajes generados para {empresa}:
    - Email T{N}: outbox/{fecha}/{slug}/email-t{N}.md
    - LinkedIn Paso {N}: outbox/{fecha}/{slug}/linkedin-paso{N}.md
    
    Copia y envía manualmente. Luego marca como enviado con:
    /marcar-enviado {slug} {canal} {toque}
    ```

## Importante

- NUNCA incluir `{{FOTO_URL}}` literal: sustituir por el valor de `.env` al generar HTML
- El asunto del T1 nunca contiene "IA", "automatización", "propuesta"
- En el primer contacto NUNCA mencionar casos de éxito (regla de la skill)
```

### 7.2 Crear `.claude/commands/marcar-enviado.md` (pequeño helper)

```markdown
# /marcar-enviado <slug> <canal> <toque>

Marca en el pipeline que un mensaje ha sido enviado manualmente por el usuario.

## Parámetros
- slug: slug de empresa
- canal: `email` | `linkedin`
- toque: `t1` | `t2` | `t3` | `paso1` | `paso2` | `paso3`

## Pasos

1. Carga pipeline.json
2. Actualiza el estado del lead:
   - Si canal=email, toque=t1 → estado_email = "enviado_t1"
   - Si canal=linkedin, toque=paso1 → estado_linkedin = "connection_enviada"
   - etc.
3. Añade evento al historial con timestamp
4. Calcula próxima acción según reglas del playbook:
   - Email T1 enviado → próxima = T2 en 7 días
   - LinkedIn Paso 1 enviado → próxima = verificar aceptación en 3 días
5. Guarda pipeline.json
6. Confirma al usuario
```

### Checkpoint Fase 3

Verificar que para un lead mock (creado manualmente en pipeline.json), `/generar-mensajes` produce output correcto en `outbox/`. Validar que la anonimización se aplica. Validar firma HTML. Pedir confirmación antes de Fase 4.

---

## 8. FASE 4 — Seguimiento enterprise (el módulo más importante)

**Objetivo:** Gmail API detectando respuestas automáticamente + clasificador + dashboard diario + métricas.

### 8.1 Crear `scripts/gmail_auth.py`

Script standalone que hace el OAuth flow de Gmail API la primera vez:
1. Lee `.gmail_credentials.json`
2. Abre navegador para autorizar
3. Guarda token en `.gmail_token.json`
4. Confirma al usuario que el setup está completo

Scopes necesarios: `https://www.googleapis.com/auth/gmail.readonly`

### 8.2 Crear `scripts/check_respuestas.py`

Script que:
1. Autentica con Gmail API
2. Lee `data/pipeline.json` y obtiene todos los leads con `estado_email` en (`enviado_t1`, `enviado_t2`, `enviado_t3`)
3. Para cada lead con email del contacto, busca en la bandeja:
   - Query Gmail: `from:{email_contacto} newer_than:30d`
   - O: `to:{email_envio} subject:Re:{asunto_t1}` (matching por asunto)
4. Para cada mensaje encontrado:
   - Extrae cuerpo (plain text, strip HTML)
   - Guarda en `respuestas/{slug}-{timestamp}.md` con:
     - Metadatos (from, date, subject)
     - Cuerpo
     - Estado: "sin_clasificar"
5. Actualiza pipeline:
   - Añade evento historial: `{tipo: "respuesta_recibida", canal: "email", archivo: "...", clasificada: false}`
   - Cambia estado_email a `respondio_t{N}`
6. Output: lista de respuestas nuevas detectadas

### 8.3 Crear `scripts/clasificar_respuestas.py`

Script que:
1. Busca en `respuestas/` archivos con estado `sin_clasificar`
2. Para cada uno:
   - Lee el cuerpo de la respuesta
   - Lee el dossier original de la empresa
   - Lee el email original enviado (desde outbox)
   - Invoca a Claude (vía Claude Code, no API externa) con prompt:
     ```
     Clasifica esta respuesta en UNA de: caliente | templada | pide_info | fria | no_interesado | fuera_oficina
     
     Devuelve JSON:
     {
       "clasificacion": "...",
       "resumen_una_frase": "...",
       "siguiente_accion_recomendada": "...",
       "borrador_respuesta": "..."
     }
     ```
3. Guarda clasificación en el propio archivo de respuesta (bloque de metadatos al inicio)
4. Si clasificación es `caliente` o `templada` o `pide_info`: crea archivo `respuestas/{slug}-borrador.md` con el borrador sugerido
5. Actualiza pipeline:
   - `temperatura = clasificacion`
   - Añade evento historial
6. Output: resumen de clasificaciones

**Nota importante:** Como este script se ejecuta dentro de una sesión de Claude Code, la "llamada a Claude" en realidad es que el propio Claude Code (la sesión actual) haga la clasificación leyendo los archivos. No necesitas cliente HTTP a la API. El script puede simplemente imprimir el contenido y el slash command que lo orquesta hace la clasificación inline.

**Alternativa limpia:** en vez de un script Python que "llame a Claude", el slash command `/estado-pipeline` hace el loop de clasificación directamente leyendo cada archivo y razonando él mismo.

### 8.4 Crear `scripts/toques_pendientes.py`

Script que:
1. Lee pipeline.json
2. Para cada lead, calcula si hoy toca alguna acción según `proxima_accion.fecha`
3. Agrupa por tipo:
   ```json
   {
     "email_t2": [...],
     "email_t3": [...],
     "linkedin_verificar_aceptacion": [...],
     "linkedin_paso2": [...],
     "linkedin_paso3": [...],
     "break_up": [...]
   }
   ```
4. Output JSON a stdout para consumo del slash command

### 8.5 Crear `.claude/commands/estado-pipeline.md`

```markdown
# /estado-pipeline

Dashboard diario. Ejecutar cada mañana al empezar el día.

## Pasos

1. Activa entorno virtual: `.venv\Scripts\Activate.ps1`

2. Ejecuta `python scripts\check_respuestas.py` y captura output.

3. Busca archivos en `respuestas/` con estado `sin_clasificar`. Para cada uno:
   - Lee el cuerpo de la respuesta
   - Lee el dossier original de la empresa en `dossiers/`
   - Lee el email enviado original en `outbox/`
   - Clasifica en: caliente | templada | pide_info | fria | no_interesado | fuera_oficina
   - Genera resumen de 1 frase
   - Si caliente/templada/pide_info: genera borrador de respuesta siguiendo
     playbook-outreach.md y la skill `prospeccion`
   - **IMPORTANTE**: aplica `scripts/anonimizar.py` al borrador
   - Escribe metadatos al inicio del archivo de respuesta:
     ```
     ---
     clasificacion: caliente
     resumen: "Pide ver demo esta semana"
     borrador: respuestas/{slug}-borrador.md
     ---
     ```
   - Actualiza pipeline.json con temperatura y evento historial

4. Ejecuta `python scripts\toques_pendientes.py` y captura output.

5. Calcula métricas rápidas de la semana actual desde pipeline.json:
   - Enviados esta semana (por tipo)
   - Respuestas esta semana
   - Calientes esta semana
   - Tasa respuesta acumulada (últimos 30 días)

6. Muestra al usuario un dashboard markdown formateado:

   ```
   # 📊 Pipeline estado — {fecha_hoy}
   
   ## 🔥 CALIENTES ({N}) — acción hoy
   
   - **{Empresa}**: {resumen respuesta}
     Borrador: respuestas/{slug}-borrador.md
   
   ## 📨 Respuestas nuevas ({N})
   
   - **{Empresa}** ({clasificación}): {resumen}
   
   ## 📅 Toques pendientes hoy
   
   ### Email T2 ({N})
   - {Empresa} — último contacto hace 7 días
   
   ### Email T3 break-up ({N})
   - {Empresa}
   
   ### LinkedIn Paso 2 ({N})
   - {Empresa}
   
   ## 📈 Métricas semana
   
   - Enviados: {N}
   - Respuestas: {N} ({tasa}%)
   - Calientes: {N}
   - Reuniones agendadas: {N}
   
   ## ⏰ Siguiente acción sugerida
   
   {acción concreta basada en lo de arriba}
   ```

7. Si hay calientes, pregunta: "¿Quieres que te abra los borradores de los calientes?"
```

### 8.6 Crear `.claude/commands/marcar-respuesta.md`

```markdown
# /marcar-respuesta <slug> <canal> <temperatura> "<resumen>"

Marca manualmente una respuesta recibida. Se usa principalmente para
LinkedIn (donde no hay API) pero también para email si el auto-detect falla.

## Parámetros

- slug: slug de empresa
- canal: email | linkedin
- temperatura: caliente | templada | pide_info | fria | no_interesado
- resumen: frase corta entre comillas

## Pasos

1. Carga pipeline.json, encuentra el lead
2. Actualiza campos:
   - `temperatura = <temperatura>`
   - `estado_{canal} = respondio`
3. Añade evento al historial:
   ```json
   {
     "fecha": "now",
     "canal": "<canal>",
     "tipo": "respuesta_manual",
     "temperatura": "<temperatura>",
     "resumen": "<resumen>"
   }
   ```
4. Si temperatura in [caliente, templada, pide_info]:
   - Genera borrador de respuesta siguiendo playbook + skill prospeccion
   - Guarda en `respuestas/{slug}-borrador-{canal}.md`
   - Aplica anonimización
5. Guarda pipeline.json
6. Confirma al usuario
```

### 8.7 Crear `scripts/metricas_semanales.py`

Script que:
1. Lee pipeline.json entero
2. Filtra eventos de los últimos 7 días
3. Calcula:
   - Leads descubiertos, aprobados a dossier, contactados
   - Mensajes enviados por canal y toque
   - Respuestas recibidas
   - Clasificación de respuestas (calientes, templadas, frías, no_int)
   - Reuniones agendadas (si campo existe)
   - Tasa de respuesta global
   - Tasa de respuesta por sector (qué sector convierte mejor)
   - Tasa de respuesta por fuente de descubrimiento
   - Tasa de respuesta por toque (T1 vs T2 vs T3)
4. Genera `reports/semana-{numero}-{año}.md` con markdown formateado
5. Incluye sección "Aprendizajes sugeridos":
   - "Sector X tiene tasa de respuesta {tasa}%, doblar foco"
   - "Fuente Y no generó leads, revisar"
   - "Toque T2 convierte {tasa}%, está funcionando"

### 8.8 Crear `.claude/commands/metricas-semanales.md`

```markdown
# /metricas-semanales

Ejecuta cada domingo. Genera report de la semana.

## Pasos

1. `python scripts\metricas_semanales.py`
2. Lee el archivo generado `reports/semana-{N}-{año}.md`
3. Muéstralo al usuario
4. Sugiere 1-2 ajustes concretos al playbook u objetivos basado en los datos
```

### Checkpoint Fase 4

Verificar:
- `gmail_auth.py` completa OAuth sin errores
- `check_respuestas.py` detecta al menos un email de prueba
- `/estado-pipeline` muestra dashboard correcto
- `/marcar-respuesta` actualiza pipeline correctamente
- `/metricas-semanales` genera report válido

---

## 9. Notas finales para Claude Code

### Orden estricto de construcción

1. **Fase 0 primero, SIEMPRE.** Sin ella el resto falla. Verifica entorno + skills + confirma ruta con usuario.
2. **Fase 1 después, entera.** No empezar Fase 2 hasta que los archivos de Fase 1 existan y el usuario confirme.
3. **No inventar paths.** Usa siempre `C:\Users\Aritz\...` tal como el usuario confirmó en Fase 0.
4. **No escribir código sin tests básicos.** Cada script Python debe tener un `if __name__ == "__main__":` con `_self_test()` que verifique al menos que parsea sus inputs bien.
5. **Preguntar antes de tocar `.env`** — el usuario rellena credenciales él.
6. **Al final de cada fase, commitea a git** con mensaje descriptivo si el usuario tiene git inicializado en el proyecto.

### Qué NO hacer

- NO inventar plantillas de mensaje. La metodología vive en la skill `prospeccion`.
- NO duplicar la lógica de la skill en el playbook ni en los scripts.
- NO hacer scraping de LinkedIn directo (ni Selenium, ni Playwright sobre LI). Solo vía `site:linkedin.com` en Google CSE.
- NO meter pixels de tracking en emails.
- NO usar emojis corporativos en las plantillas (sí se pueden usar en el dashboard para escaneo rápido).
- NO escribir nada a `outbox/` sin pasar por `anonimizar.py` primero.

### Cuando termines todas las fases

Muestra al usuario:
1. Árbol completo del proyecto
2. Checklist de setup pendiente (Google Cloud, OAuth, `.env`, foto)
3. Primer comando a ejecutar para validar: `/prospectar-tanda` con 3 leads mock
4. Documentación de backup: el `README.md` debe servir si el usuario vuelve al proyecto en 3 meses

### Tiempo estimado

- Fase 0: 10 min (verificación + preguntas al usuario)
- Fase 1: 15 min (solo archivos, sin código funcional)
- Fase 2: 60-90 min (4 scripts de descubrimiento + dedupe)
- Fase 3: 45 min (generación de mensajes + slash commands)
- Fase 4: 60-90 min (Gmail API + dashboard + métricas)

**Total: ~4-4.5 horas de trabajo de Claude Code en una sesión focused.**

---

## 10. Información que Claude Code debe pedir al usuario al empezar

**Todo esto está cubierto en Fase 0 (sección 5).** Ejecuta Fase 0 primero y el resto del documento se desbloquea.

Resumen de lo que Fase 0 cubre:
1. Verificación de Claude Code ≥ 2.0 y Python 3.10+
2. Verificación del **repo fuente de verdad** (`C:\Users\Aritz\dev\skills-aritz\.git`)
3. Verificación de las **3 junctions** (`LinkType -eq 'Junction'`, `Target` contiene `skills-aritz`)
4. Verificación de **contenido canónico** (marker `CASO_1` presente, sin `TODO`/`PLACEHOLDER`)
5. Verificación de **repo limpio** (`git status --porcelain` — warning si hay cambios)
6. Lectura y resumen de las skills canónicas al usuario para confirmación
7. Confirmación explícita del **contrato de invocación** (referencia por nombre, nunca copia)
8. Pregunta de ruta del proyecto y de inicialización de git
9. Confirmación explícita antes de arrancar Fase 1

**Recordatorio crítico para Windows:** todas las rutas en scripts y archivos de config usan `/` o `\\` (doble backslash en JSON). PowerShell acepta ambos. No mezcles separadores dentro de una misma ruta.

---

## Changelog v2 → v3

**Cambios estructurales:**

1. **Fase 0 ampliada** (§5). Además de verificar Claude Code, Python y existencia de `SKILL.md`, ahora verifica: repo `skills-aritz` presente con `.git`; las 3 skills son `LinkType -eq 'Junction'` con `Target` apuntando al repo; contenido canónico (marker `CASO_1`, sin placeholders); repo limpio (`git status --porcelain`, warning no bloqueante). Variable `$repoSkills` al inicio del bloque PowerShell para facilitar cambios futuros. Nueva sub-sección §5.0.3 con el contrato explícito de invocación que el usuario debe aceptar.

2. **Modelo de skills formalizado** (nueva sub-sección en §3). Bloque dedicado explicando el modelo *repo único + junctions*: edición en un solo sitio (`C:\Users\Aritz\dev\skills-aritz\<skill>\SKILL.md`), commit, las junctions reflejan el cambio automáticamente en todos los proyectos. Cero drift, versionado git automático.

3. **Referencias por nombre reforzadas**. Cabecera del documento, §3 (módulos), CLAUDE.md (§5.1 stack), README.md (§5.12 arranque rápido) endurecidas con el patrón: *"invocar la skill por nombre, nunca copiar su contenido al proyecto"*. README.md arranque rápido ahora incluye prerrequisito de verificación de junctions antes de instalar dependencias.

**Lo que NO cambia vs v2:** estructura de 8 fases, Windows nativo + PowerShell, slash commands, rutas, arquitectura de 6 módulos, playbook de outreach, 4 casos anonimizados, reglas duras (NOMOS/Telefónica/OpoRuta prohibidos, castellano, precios en horas-equivalente-manual).

Fin del documento maestro v3.
