# Sistema de prospección — Aritz Abuin IA

Proyecto de prospección B2B semi-automatizada. Se ejecuta localmente
en el PC de Aritz cuando él decide (L/X/V típicamente). Sin cron,
sin servicios externos de pago.

## Stack
- Claude Code como orquestador
- Skills del usuario: `prospeccion`, `captacion-leads`, `follow-up` — **fuente de verdad en `C:\Users\Aritz\dev\skills-aritz\` (repo git, rama `main`)**. Instaladas vía junctions en `%USERPROFILE%\.claude\skills\`. Este proyecto las invoca por nombre; NO copia su contenido ni duplica su lógica. Ajustes — editar en el repo y commitear; las junctions reflejan el cambio automáticamente.
- Python 3.11+ para scripts de descubrimiento y Gmail API
- Google Custom Search API + Google Places API (ambas gratis)
- Gmail API (OAuth, gratis) para monitorización de respuestas
- JSON local versionado en git como "base de datos"

## Flujo diario tipo

**Mañana (L/X/V):**
1. Abrir Claude Code en este proyecto
2. Ejecutar `/estado-pipeline` — ver respuestas nuevas + toques pendientes
3. Ejecutar `/prospectar-tanda` — descubrir 15 leads nuevos
4. Revisar top 15, aprobar los buenos
5. Para cada aprobado: ejecutar `/generar-mensajes <empresa>`
6. Copiar mensajes de `outbox/{fecha}/` a Gmail / LinkedIn
7. Enviar manualmente

**Cuando recibe respuesta por LinkedIn:**
- Ejecutar `/marcar-respuesta <empresa> linkedin <temperatura> "<resumen>"`

**Domingos:**
- Ejecutar `/metricas-semanales`

## Reglas duras del sistema (CRITICO)

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
