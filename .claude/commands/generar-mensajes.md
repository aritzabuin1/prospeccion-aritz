# /generar-mensajes $ARGUMENTS

Genera los mensajes de outreach para una empresa concreta según su estado
en el pipeline.

## Entrada

Argumento: slug de empresa (ej: `grupo-ejemplo-sl`)

## Pasos

1. Lee `data/pipeline.json` y encuentra el lead por slug dentro de `leads`.
   Si no existe, avisa al usuario y para.

2. Lee el dossier de la empresa. Busca en `dossiers/` el archivo más reciente
   que coincida con el slug (puede estar en subcarpeta por fecha:
   `dossiers/{fecha}/{slug}.md`). Si no hay dossier, avisa y pregunta si
   continuar sin él.

3. Lee `playbook-outreach.md` entero — contiene las reglas de marca, tono,
   secuencia de emails y casos de éxito permitidos.

4. Determina qué mensaje toca según `estado_email` y `estado_linkedin`:
   - Si `estado_email == "nuevo"` → generar Email T1 + LinkedIn Paso 1 (connection SIN NOTA)
   - Si `estado_email == "enviado_t1"` y han pasado ≥7 días sin respuesta → Email T2 (reciprocidad, 40-60 palabras)
   - Si `estado_email == "enviado_t2"` y han pasado ≥14 días sin respuesta → Email T3 (break-up, 30-40 palabras)
   - Si `estado_linkedin == "connection_aceptada"` → LinkedIn Paso 2 (primer mensaje real de valor, 80-120 palabras)
   - Si `estado_linkedin == "respondio_paso2"` → LinkedIn Paso 3 (puede incluir caso de éxito anonimizado 1:1)

   **LinkedIn Paso 1 (IMPORTANTE):** por defecto el Paso 1 es una connection
   SIN NOTA. No se genera texto de nota. El `linkedin-paso1.md` debe contener
   solo la instrucción: "Enviar connection SIN nota (plan básico limita notas).
   Perfil del decisor: {URL si existe}". Excepción: si el lead tiene
   `score >= 85` Y el decisor está identificado con nombre, sí generar nota
   ≤200 caracteres aplicando P1+P2+P5 del playbook.

5. Para LinkedIn: invoca la skill `prospeccion` con el contexto del dossier
   pidiendo el paso correspondiente. La skill ya tiene la metodología de
   3 pasos (Hormozi, Voss, Klaff).

6. Para email: aplica la metodología del playbook (extensión email):
   - **T1**: asunto 3-5 palabras (SIN "IA", "automatización", "propuesta") +
     60-90 palabras cuerpo + firma HTML
   - **T2**: follow-up de valor puro 40-60 palabras, asunto "Re:" del T1
   - **T3**: break-up educado 30-40 palabras, deja la puerta abierta

7. **CRÍTICO — validación de reglas duras** antes de escribir a outbox:
   - Ejecuta `python scripts/anonimizar.py` mentalmente sobre cada texto:
     - Sustituir Euromanager → "una consultora de RRHH"
     - Sustituir Cafès Cornellà → "una cadena con más de 100 establecimientos de café"
     - Sustituir OpoRuta → "aplicaciones SaaS propias"
   - Verificar que NO aparecen: NOMOS, Telefónica, OpoRuta (case-insensitive)
   - Verificar que NO aparecen nombres reales de clientes
   - En primer contacto NUNCA incluir casos de éxito
   - Si alguna regla falla, regenerar

8. Lee `config/firma-email.html` y sustituye `{{FOTO_URL}}` por el valor
   de la variable `FOTO_URL` del archivo `.env`. NUNCA dejar `{{FOTO_URL}}`
   literal en el output.

9. Escribe los mensajes a `outbox/{fecha_hoy}/{slug}/`:
   - `email-t{N}.md` — asunto + cuerpo en texto plano + nota "Generado el {fecha}"
   - `email-t{N}.html` — cuerpo completo + firma HTML lista para pegar en Gmail
   - `linkedin-paso{N}.md` — texto plano del mensaje LinkedIn
   - `contacto.md` — tarjeta de envío (ver formato abajo). Extrae del dossier:
     nombre del decisor (si existe), canal recomendado (1º y 2º), dirección
     exacta (email / URL LinkedIn / teléfono), y si hay búsqueda pendiente
     que el usuario deba hacer en LinkedIn antes de enviar. Si el dossier
     no identifica decisor con nombre, marcarlo claramente como
     "**⚠ Identificar antes de enviar**" con las instrucciones de búsqueda
     que vengan del dossier (sección "Contacto decisor").

   Formato de `contacto.md`:
   ```
   # Contacto — {empresa}

   **Fecha de generación:** {fecha_hoy}

   ## Destinatario
   - **Nombre:** {nombre o "⚠ Identificar antes de enviar"}
   - **Cargo:** {cargo}
   - **Notas:** {contexto breve del decisor, 1 línea}

   ## Canal recomendado
   1. **{canal_primario}** → {dirección exacta, URL o "pendiente — buscar así: ..."}
   2. **{canal_secundario}** → {dirección o "pendiente"}

   ## Qué enviar
   - {canal_primario}: `{archivo generado}`
   - {canal_secundario}: `{archivo generado}` (como segundo toque si no hay respuesta en {N} días)

   ## Acciones pendientes del usuario antes de enviar
   - {lista concreta: confirmar nombre, sustituir "Hola," por "Hola {nombre},", etc.}
   ```

10. Actualiza `data/pipeline.json`:
    - Añade evento al historial del lead:
      `{"tipo": "mensaje_generado", "canal": "{email|linkedin}", "toque": "{t1|paso1|...}", "fecha": "{fecha_hoy}"}`
    - Marca `proxima_accion.generada = true`

11. Muestra al usuario:
    ```
    Mensajes generados para {empresa}:
    - Email T{N}: outbox/{fecha}/{slug}/email-t{N}.md
    - LinkedIn Paso {N}: outbox/{fecha}/{slug}/linkedin-paso{N}.md

    Copia y envía manualmente. Luego marca como enviado con:
    /marcar-enviado {slug} {canal} {toque}
    ```

## Reglas importantes

- NUNCA incluir `{{FOTO_URL}}` literal en el HTML: sustituir siempre
- El asunto del T1 nunca contiene "IA", "automatización", "propuesta"
- En el primer contacto NUNCA mencionar casos de éxito
- Castellano siempre
- Sin emojis, sin exclamaciones, sin "encantado de conocerte"
- Frases cortas, tono de par curioso, no de vendedor
- Si el lead no tiene email de contacto, generar solo LinkedIn (y avisar)
- Si el lead no tiene LinkedIn de contacto, generar solo email (y avisar)
