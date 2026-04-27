# Plan atómico — Enriquecimiento de leads (v2, auditado 2026-04-20)

**Objetivo:** antes de generar dossier/borrador, cada lead VERDE debe llevar `contacto.nombre`, `contacto.rol`, `contacto.email` verificado y `contacto.linkedin` rellenos. Si no se consiguen, el lead queda marcado `canal_primario: linkedin` y NO se crea borrador de email (nunca `info@`, nunca adivinar sin verificar).

**Contexto:** tanda del 2026-04-20 produjo 40 VERDE pero 0 con email → inviable enviar. Este plan cierra el hueco con herramientas gratuitas + fuentes públicas españolas.

**Realismo (auditado):** el tier gratuito combinado cubre **~135 emails/mes** (no 320). El resto va por LinkedIn. Si a 2 meses los emails rinden >2× LinkedIn, escalar a Apollo Basic ($49/mes).

---

## Cascada de enriquecimiento (orden estricto, post-audit)

| # | Fuente | Coste/lead | Cuota real/mes | Qué aporta |
|---|--------|-----------|----------------|------------|
| 0.5 | **BORME** (librebormé/bormeparser, gratis) | 0 | ilimitado | nombre + cargo de administradores |
| 1 | **Apollo.io Free** | 1 export credit si reveal | ~10 | decisor + email + LinkedIn |
| 2 | **Hunter.io Free** | 1 crédito (compartido) | 50 totales (búsqueda+verif) | patrón + email + verificación |
| 3 | **Prospeo.io Free** | 1 | 75 | email finder (cobertura EU buena) |
| 4 | **Wayback Machine** | 0 | ilimitado | scraping páginas "Equipo" archivadas |
| 5 | **DIY Google CSE + patrón + Hunter-verify** | 1 verif Hunter | N/A | último recurso antes de LinkedIn-only |
| 6 | **LinkedIn-only** | 0 | ilimitado | marcar `canal_primario: linkedin`, no borrador email |

Snov.io eliminado de la cascada: **su API no está disponible en el tier trial**, sólo en paid.

---

## Fase 0 — Prerrequisitos (10 min, una sola vez)

### 0.1 Crear cuentas y obtener API keys

- [ ] **Apollo.io:** https://app.apollo.io/#/signup con `aritzabuin1@gmail.com` → Settings → Integrations → API → copiar API key.
  - **Importante:** Apollo restringe más los email reveals en cuentas gmail.com que en corporativas. Si tienes dominio propio con email (p.ej. aritz@tu-dominio.com con Zoho Mail free), regístrate con ese para obtener reveals más fiables. Si solo tienes gmail, adelante igualmente.
  - En Settings → API Usage, verificar contador real de "export credits" al crear la cuenta (puede ser 5, 10 o 20 según migración interna de Apollo).
- [ ] **Hunter.io:** https://hunter.io/users/sign_up → verificar email → API → copiar API key. **50 créditos totales/mes** (compartidos entre Domain Search y Email Verifier).
- [ ] **Prospeo.io:** https://app.prospeo.io/signup → Dashboard → API → copiar API key. **75 emails/mes** renovables.

### 0.2 Guardar en `.env`

```
APOLLO_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
HUNTER_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
PROSPEO_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
```

Verificar que `.env` está en `.gitignore` (ya lo está).

### 0.3 Dependencias

```bash
.venv/Scripts/pip install requests python-dotenv bormeparser beautifulsoup4 lxml
```

---

## Fase 0.5 — Enriquecimiento BORME (antes de tocar APIs)

**Motivación:** BORME (Boletín Oficial del Registro Mercantil) publica administradores de sociedades (nombre + DNI + cargo). Gratis, 100% legal, cobertura total de empresas españolas. Obtener el nombre desde aquí **reduce el consumo de Apollo drásticamente** (con nombre conocido, Hunter/Prospeo son más baratos y precisos).

### 0.5.1 Instalar `bormeparser`

```bash
.venv/Scripts/pip install bormeparser
```

Repo: https://github.com/PabloCastellano/bormeparser — parsea PDFs del BORME.

### 0.5.2 Crear `scripts/enriquecer_borme.py`

Funciones:

- `buscar_administradores(empresa: str, provincia: str | None) -> list[dict]` — devuelve `[{nombre, cargo, fecha_nombramiento}]`.
- Estrategia: usar la API pública de librebor.me (búsquedas diarias limitadas sin registro) como primer intento. Si falla o se queda sin cuota, fallback a descargar PDFs BORME por provincia y parsear con bormeparser.
- Cache en `data/borme_cache/{empresa_slug}.json` (TTL 90 días — los administradores no cambian a menudo).

### 0.5.3 Uso

Antes de llamar a ninguna API externa, ejecutar `buscar_administradores(lead["empresa"], lead["zona"])`. Si devuelve alguien con cargo válido (administrador único, consejero delegado, presidente, apoderado, director general), guardarlo en `lead["contacto"]["nombre"]` y `lead["contacto"]["rol"]`. Queda pendiente obtener email en Fase 1.

**Límite real librebor.me:** ~10-20 búsquedas/día sin registro. Si se agota, usar el parser local sobre PDFs descargados.

---

## Fase 1 — Módulo `scripts/enriquecer_leads.py`

### 1.1 Esqueleto

```python
def enriquecer(lead: dict) -> dict:
    """Aplica cascada completa. Devuelve lead con contacto relleno y fuente_enriquecimiento."""
```

Fuentes internas por prioridad:

1. `_borme(empresa, zona)` → relleno nombre+rol (NO email)
2. `_apollo_search(dominio, nombre?)` → intenta email verified
3. `_hunter_domain(dominio, nombre?)` → email + confidence ≥ 85
4. `_prospeo_find(dominio, nombre)` → requiere nombre
5. `_wayback_scrape(dominio)` → páginas "equipo", "about", "contacto" archivadas
6. `_diy_cse_patron(empresa, dominio, nombre)` → Google CSE + patrón + verificación Hunter
7. fallback `canal_primario = linkedin`

### 1.2 Control de cuota

Archivo `data/enrichment_usage.json`:

```json
{
  "2026-04": {
    "apollo_export": 3,
    "hunter": 12,
    "prospeo": 8,
    "borme_librebor": 5
  }
}
```

Función `_puede_usar(api) -> bool` con límites **recalibrados a la realidad audit**:

```python
LIMITES_MENSUALES = {
    "apollo_export": 10,   # conservador; verificar real en Settings tras crear cuenta
    "hunter": 50,          # total compartido búsqueda+verif
    "prospeo": 75,
    "borme_librebor": 200  # estimado ~10/día × 20 días
}
```

Incrementar tras cada request **exitoso o fallido** (todas las APIs cobran request, no resultado).

### 1.3 Apollo (ajustes post-audit)

Endpoint: `POST https://api.apollo.io/v1/mixed_people/search`
Header: `X-Api-Key: {APOLLO_API_KEY}`

Payload:

```json
{
  "q_organization_domains": "ejemplo.com",
  "person_titles": ["CEO", "Director General", "Gerente", "Managing Director", "Fundador", "COO", "CFO", "Director de Operaciones"],
  "page": 1,
  "per_page": 5,
  "reveal_personal_emails": false
}
```

**Dos pasadas:**

1. **Search sin reveal** (gratis, no consume export credit). Parsear respuesta: si algún resultado tiene `email` presente y `email_status == "verified"`, usarlo y terminar.
2. **Solo si el lead tiene score ≥ 80 y la pasada 1 no dio email:** segunda llamada con `reveal_personal_emails: true` (consume 1 export credit). Apollo puede devolverlo asíncronamente vía webhook → implementar endpoint simple `/webhook/apollo` o hacer polling `GET /v1/people/{id}`.

**Filtro geográfico:** si `country` del decisor ∉ {España, UE, UK, EEUU, Canadá, Suiza, Noruega, Australia, NZ, Japón, Corea, Singapur}, descartar ese decisor y probar el siguiente.

### 1.4 Hunter

Endpoint 1: `GET https://api.hunter.io/v2/domain-search?domain={dominio}&api_key={key}&limit=5&department=executive`

Parseo:

1. Recorrer `data.emails` ordenando por `confidence` desc.
2. Aceptar el primero con `confidence ≥ 85` y `position` conteniendo CEO/Director/Gerente/Founder/CFO/COO.
3. Si hay nombre de BORME pero no aparece en emails, construir con `data.pattern` + nombre → verificar con `GET /v2/email-verifier?email=...` (consume 1 crédito extra). Aceptar solo `result == "deliverable"`.

**Presupuesto por lead:** máximo 2 créditos Hunter (1 domain + 1 verifier). Con 50 créditos/mes → **~25 leads/mes techo real por Hunter**.

### 1.5 Prospeo

Endpoint: `POST https://api.prospeo.io/email-finder`
Header: `X-KEY: {PROSPEO_API_KEY}`

Payload:

```json
{
  "first_name": "...",
  "last_name": "...",
  "company": "dominio.com"
}
```

**Requiere nombre** (no hace domain-search anónimo). Usar solo cuando BORME o Apollo aportaron nombre pero no email. Respuesta incluye `email` y `response` (`EMAIL_FOUND`, `EMAIL_NOT_FOUND`). Apollo+Hunter no dan nombre → Prospeo también falla.

### 1.6 Wayback Machine (nueva capa gratis)

Módulo `_wayback_scrape(dominio)`:

1. CDX API: `http://web.archive.org/cdx/search/cdx?url={dominio}/equipo/*&output=json&limit=5` (o `/nosotros`, `/about`, `/contacto`, `/team`, `/staff`).
2. Para cada snapshot reciente, hacer GET al archivo: `https://web.archive.org/web/{timestamp}/{url}`.
3. Parsear HTML con BeautifulSoup, buscar patrones:
   - Emails directos (regex `[a-z0-9._%+-]+@{dominio}`)
   - Nombres junto a roles (CEO/Director/Gerente) en tags `<h2>`, `<p class*="role">`, etc.
4. Si encuentra email → verificar sintácticamente y con MX-record (gratis, DNS query).
5. Si hay MX pero no verificación real → pasar a Hunter verifier (consume 1 crédito).

Coste: 0 créditos de APIs pagadas, solo ancho de banda. Rate limit Wayback: generoso (sin documentar, ~10 req/s estable).

### 1.7 DIY Google CSE + patrón (último recurso antes de LinkedIn-only)

Solo si las 4 capas anteriores fallaron:

1. Query CSE: `"{empresa}" (CEO OR "director general" OR gerente OR fundador) site:linkedin.com/in/`
2. Del primer resultado, parsear título LinkedIn: `"Nombre Apellido - Cargo | LinkedIn"` → extraer `first_name`, `last_name`, `role`.
3. Construir 3 patrones: `{first}.{last}@`, `{f}{last}@`, `{first}{last}@`.
4. **Presupuesto Hunter verifier:** máximo 1 pattern verificado por lead (no 3). Tomar el más probable según patrón observado en otros leads del mismo dominio (guardar en `data/patrones_dominio.json`).
5. Si Hunter dice `deliverable` → usar. Si no → `canal_primario: linkedin`, `contacto.linkedin` relleno con la URL encontrada, `contacto.email = None`.

---

## Fase 2 — Integración en `validar_leads.py`

### 2.1 Punto de inyección

```python
from scripts.enriquecer_leads import enriquecer

for lead in candidatos:
    # ... validación actual ...
    if lead["validacion"]["semaforo"] == "VERDE":
        lead = enriquecer(lead)
```

### 2.2 Scope geográfico duro

Si tras la cascada, `contacto.pais` ∉ países aprobados → descartar decisor y marcar `canal_primario: linkedin`. El scope se aplica al decisor, no a la sede (regla del CLAUDE.md).

### 2.3 Logging en `logs/enrichment-{fecha}.log`

```
2026-04-21T09:15 slug=iqe apollo=miss hunter=hit email="..." conf=91 creditos=h12/50
2026-04-21T09:17 slug=grupo-x apollo=miss hunter=miss prospeo=miss wayback=hit email="..."
2026-04-21T09:19 slug=grupo-y diy=miss → canal=linkedin
```

### 2.4 Alertas de cuota

Al arrancar `prospectar-tanda`, si alguna API < 5 créditos restantes → warn al usuario antes de ejecutar.

---

## Fase 3 — Adaptaciones en flujo existente

### 3.1 `aprobar_tanda_*.py`

Si `canal_primario == "linkedin"`, la `proxima_accion` debe ser `linkedin_paso1` (no `enviar_t1`):

```json
{
  "fecha": "...",
  "tipo": "linkedin_paso1",
  "generada": false
}
```

### 3.2 `preparar_borradores_semana.py` (ya corregido hoy)

Filtro activo: `not destinatario or "@" not in destinatario or "pendiente.local" in destinatario → skip`. Verificar que sigue así.

### 3.3 `enviar_pendientes.py` (ya corregido hoy)

Guard activo: si `To:` del draft contiene `@pendiente.local` → no enviar, reagendar.

---

## Fase 4 — Re-enriquecer los 54 leads sin email de la tanda 2026-04-20

Script one-shot `scripts/re_enriquecer_2026-04-20.py`:

1. Cargar pipeline y filtrar `leads` con `proxima_accion.fecha ∈ [2026-04-21..24]` y email vacío/inválido.
2. Para cada uno: `enriquecer(lead)`.
3. Si consigue email verificado → pipeline listo para re-crear borrador (ejecutar después `preparar_borradores_semana.py`).
4. Si no → `canal_primario = linkedin`, `proxima_accion.tipo = linkedin_paso1`.

**Expectativa realista (post-audit):** con 135 créditos totales, aplicados a 54 leads, éxito esperado ~40% → **22 leads con email**, **32 a LinkedIn-only**. El resto del mes queda con menos margen para tandas nuevas (revisar cuota antes de `/prospectar-tanda` siguiente).

---

## Fase 5 — Testing

### 5.1 Lead conocido

```bash
.venv/Scripts/python -c "from scripts.enriquecer_leads import enriquecer; import json; l=json.loads(open('data/pipeline.json',encoding='utf-8').read())['leads']['iqe-industrias-quimicas-del-ebro-s-a']; print(enriquecer(l))"
```

Verificar: decisor español, email verified, fuente registrada, contador incrementado.

### 5.2 Cuota agotada

Manipular `data/enrichment_usage.json` para poner `apollo_export: 10` y repetir test → debe saltar a Hunter.

### 5.3 Empresa sin web

Lead con `web = ""` → cascada salta APIs con dominio, intenta BORME (solo nombre empresa) + CSE para LinkedIn. Termina en LinkedIn-only casi seguro. Verificar que no rompe.

### 5.4 Empresa española con decisor en LATAM

Insertar manualmente un lead con decisor con `country = "MX"`. Debe descartarse y marcar `canal_primario: linkedin` o buscar otro decisor.

---

## Fase 6 — GDPR / LSSI-CE (cumplimiento legal en T1)

**Obligatorio en cold email B2B España:**

1. **Identificación remitente** → ya va en firma HTML.
2. **Fuente de los datos** → añadir línea al T1, ej: *"Obtuve tu contacto desde la web de {empresa} / BORME / LinkedIn."*
3. **Opt-out funcional** → añadir al final del email, antes de firma: *"Si prefieres no recibir más mensajes, respóndeme con 'baja' y dejaré de escribirte."*
4. **Respeto del opt-out** → nuevo script `scripts/procesar_bajas.py` que lea Gmail buscando respuestas con "baja", "unsubscribe", "no más", y marque el lead como `estado_email: baja_solicitada`. Nunca más contactar.
5. **RAT** — documento interno `gdpr/registro-actividades.md` (no publicar). Justificación: interés legítimo en prospección B2B, base legal Recital 47 GDPR + LOPDGDD art. 19.

**Sanción AEPD típica por incumplir:** 1k-5k € para autónomos. Riesgo real pero evitable con opt-out bien implementado.

Actualizar:
- Skill `prospeccion` (en repo skills) para que los T1 generados incluyan las dos líneas (fuente + opt-out).
- `playbook-outreach.md` sección nueva "Cumplimiento legal".
- `CLAUDE.md` reglas duras: añadir "T1 siempre incluye fuente + opt-out".

---

## Fase 7 — Comandos de monitorización

### 7.1 `/estado-enriquecimiento`

Slash command nuevo:

```
Mes actual: 2026-04
  Apollo export:  3/10   (7 restantes)
  Hunter:        12/50  (38 restantes)
  Prospeo:        8/75  (67 restantes)
  BORME librebor: 5/200 (sin alarma)

Este mes: 59 leads enriquecidos
  con email:   22 (37%)
  solo LinkedIn: 37 (63%)

Alertas:
  ⚠ Apollo export < 5: planificar el resto del mes con Hunter/Prospeo.
```

---

## Reglas duras (no negociables)

1. **Nunca** crear borrador de email sin email verificado (`deliverable` / `verified` / `confidence ≥ 85`).
2. **Nunca** adivinar email sin verificar (no construir+enviar).
3. **Nunca** enviar a genéricos: `info@`, `contacto@`, `admin@`, `hola@`, `ventas@`.
4. **Nunca** enriquecer leads AMARILLO o ROJO sin aprobación manual (malgasta créditos).
5. **Siempre** verificar país del decisor antes de aceptar.
6. **Siempre** loguear en `data/enrichment_usage.json`.
7. **Siempre** incluir fuente + opt-out en T1 (GDPR).
8. **Siempre** respetar respuestas "baja"/"unsubscribe" (procesar_bajas.py).
9. **No** usar scrapers LinkedIn desde cuenta real (riesgo ban).
10. **No** montar verificador SMTP propio desde IP doméstica (riesgo blacklist).

---

## Alternativas descartadas (con motivo)

| Opción | Motivo descarte |
|--------|-----------------|
| Snov.io | API no disponible en tier trial/free |
| Kaspr/ContactOut/Wiza | API solo en paid; extensiones no integrables |
| RocketReach/Lusha | 5 créditos/mes es simbólico |
| Scraping LinkedIn | ToS + GDPR + riesgo ban cuenta |
| Common Crawl (Athena) | Overhead alto; cobertura baja pymes ES |
| Verificador SMTP propio | Riesgo blacklist IP; no compensa vs 50 Hunter |
| Empresite/eInforma/Axesor | Sin API free; scraping viola ToS |

---

## Cuándo escalar a tier de pago

Tras 2 meses operando v2:

- Si `ratio_respuesta_email / ratio_respuesta_linkedin ≥ 2` → justifica pagar Apollo Basic ($49/mes, 1.200 export credits) o Hunter Starter ($49/mes, 500 búsquedas). Cualquiera cubre 320 leads/mes sin necesidad del resto.
- Si el ratio es ≤ 1 → LinkedIn es el canal real, no tirar dinero en APIs.
- Métrica clave a trackear: `respuestas_positivas / contactados` por canal.

---

## Incertidumbres pendientes de verificar (hacer antes de Fase 1)

- [ ] **Apollo export credits reales de tu cuenta Free nueva** — tras crear, mirar Settings → API Usage. Puede ser 5, 10 o 20.
- [ ] **Apollo reveal con cuenta gmail.com** — confirmar que funciona antes de invertir en código. Si no, considerar crear la cuenta con dominio propio (p.ej. alias Zoho Mail gratis en dominio custom).
- [ ] **Prospeo free tier oficial 2026** — 75/mes recurrente es dato de terceros; confirmar en https://docs.prospeo.io.
- [ ] **librebor.me límite diario exacto sin registro** — probar empíricamente; si <10/día ajustar ``LIMITES_MENSUALES``.
- [ ] **bormeparser funcional con PDFs BORME actuales 2026** — el formato puede haber cambiado desde la última release del paquete.

---

## Checklist de ejecución (resumen)

- [ ] **Fase 0:** cuentas Apollo+Hunter+Prospeo, keys en `.env`, deps instaladas
- [ ] **Fase 0.5:** `scripts/enriquecer_borme.py` con cache 90d
- [ ] **Fase 1:** `scripts/enriquecer_leads.py` con cascada de 6 capas + cuota
- [ ] **Fase 2:** integrado en `validar_leads.py` tras VERDE
- [ ] **Fase 3:** `aprobar_tanda` respeta `canal_primario`; scripts ya corregidos
- [ ] **Fase 4:** `scripts/re_enriquecer_2026-04-20.py` para los 54 leads pendientes
- [ ] **Fase 5:** 4 tests (lead conocido / cuota agotada / sin web / decisor LATAM)
- [ ] **Fase 6:** GDPR — fuente + opt-out en T1, `procesar_bajas.py`, RAT, skill `prospeccion` actualizada
- [ ] **Fase 7:** `/estado-enriquecimiento` command
- [ ] Memoria: `project_apollo_hunter_enrichment.md` actualizada a v2
