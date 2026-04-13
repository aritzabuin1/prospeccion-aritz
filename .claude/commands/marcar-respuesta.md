# /marcar-respuesta $ARGUMENTS

Marca manualmente una respuesta recibida. Se usa principalmente para
LinkedIn (donde no hay API) pero tambien para email si el auto-detect falla.

## Parametros

Argumentos: `<slug> <canal> <temperatura> "<resumen>"`

- **slug**: slug de empresa (ej: `grupo-ejemplo-sl`)
- **canal**: `email` | `linkedin`
- **temperatura**: `caliente` | `templada` | `pide_info` | `fria` | `no_interesado`
- **resumen**: frase corta entre comillas describiendo la respuesta

Ejemplo: `/marcar-respuesta panaderia-mock-sl linkedin templada "Dice que le interesa pero no ahora"`

## Pasos

1. Lee `data/pipeline.json` y busca el lead por slug. Si no existe, avisa y para.

2. Actualiza campos del lead:
   - `temperatura = <temperatura>`
   - Si canal=email: `estado_email = "respondio"`
   - Si canal=linkedin: `estado_linkedin = "respondio"`

3. Anade evento al historial:
   ```json
   {
     "tipo": "respuesta_manual",
     "canal": "<canal>",
     "temperatura": "<temperatura>",
     "resumen": "<resumen>",
     "fecha": "{fecha_hoy}",
     "hora": "{HH:MM}"
   }
   ```

4. Si temperatura es `caliente`, `templada` o `pide_info`:
   - Lee el dossier de la empresa en `dossiers/`
   - Lee `playbook-outreach.md`
   - Genera borrador de respuesta siguiendo el playbook y la skill `prospeccion`
   - Aplica reglas de anonimizacion (sin Euromanager, Cafes Cornella, OpoRuta,
     NOMOS, Telefonica)
   - Guarda en `respuestas/{slug}-borrador-{canal}.md`

5. Guarda `data/pipeline.json`.

6. Confirma al usuario:
   ```
   Marcado: {empresa} — respuesta {temperatura} por {canal}
   Resumen: {resumen}
   [Si hay borrador]: Borrador generado en respuestas/{slug}-borrador-{canal}.md
   ```
