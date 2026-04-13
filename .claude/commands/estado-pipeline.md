# /estado-pipeline

Dashboard diario. Ejecutar cada mañana al empezar el día.

## Pasos

1. Ejecuta `python -m scripts.check_respuestas` desde la raíz del proyecto
   y captura el output (respuestas nuevas detectadas en Gmail).
   Si Gmail no está configurado (no existe `.gmail_token.json`), avisa
   y salta al paso 3.

2. Busca archivos en `respuestas/` con `estado: sin_clasificar` en sus
   metadatos YAML. Para cada uno:
   - Lee el cuerpo de la respuesta
   - Lee el dossier original de la empresa en `dossiers/`
   - Lee el email enviado original en `outbox/`
   - Clasifica en: caliente | templada | pide_info | fria | no_interesado | fuera_oficina
   - Genera resumen de 1 frase
   - Si caliente/templada/pide_info: genera borrador de respuesta siguiendo
     `playbook-outreach.md` y la skill `prospeccion`
   - **IMPORTANTE**: aplica reglas de anonimización de `scripts/anonimizar.py`
     al borrador (sin Euromanager, Cafès Cornellà, OpoRuta, NOMOS, Telefónica)
   - Actualiza metadatos al inicio del archivo de respuesta:
     ```
     ---
     clasificacion: caliente
     resumen: "Pide ver demo esta semana"
     borrador: respuestas/{slug}-borrador.md
     ---
     ```
   - Actualiza `data/pipeline.json`:
     - `temperatura = clasificacion`
     - Añade evento al historial

3. Ejecuta `python -m scripts.toques_pendientes` y captura output JSON.

4. Calcula métricas rápidas de la semana actual desde `data/pipeline.json`:
   - Enviados esta semana (por tipo)
   - Respuestas esta semana
   - Calientes esta semana
   - Tasa respuesta acumulada (últimos 30 días)

5. Muestra al usuario un dashboard markdown formateado:

   ```
   # Pipeline estado — {fecha_hoy}

   ## CALIENTES ({N}) — accion hoy

   - **{Empresa}**: {resumen respuesta}
     Borrador: respuestas/{slug}-borrador.md

   ## Respuestas nuevas ({N})

   - **{Empresa}** ({clasificacion}): {resumen}

   ## Toques pendientes hoy

   ### Email T2 ({N})
   - {Empresa} — ultimo contacto hace {N} dias

   ### Email T3 break-up ({N})
   - {Empresa}

   ### LinkedIn Paso 2 ({N})
   - {Empresa}

   ## Metricas semana

   - Enviados: {N}
   - Respuestas: {N} ({tasa}%)
   - Calientes: {N}
   - Reuniones agendadas: {N}

   ## Siguiente accion sugerida

   {accion concreta basada en lo de arriba}
   ```

6. Si hay calientes, pregunta: "Quieres que te abra los borradores de los calientes?"
