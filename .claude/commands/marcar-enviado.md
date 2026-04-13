# /marcar-enviado $ARGUMENTS

Marca en el pipeline que un mensaje ha sido enviado manualmente por el usuario.

## Parámetros

Argumentos separados por espacio: `<slug> <canal> <toque>`

- **slug**: slug de empresa (ej: `grupo-ejemplo-sl`)
- **canal**: `email` | `linkedin`
- **toque**: `t1` | `t2` | `t3` | `paso1` | `paso2` | `paso3`

Ejemplo: `/marcar-enviado grupo-ejemplo-sl email t1`

## Pasos

1. Lee `data/pipeline.json` y busca el lead por slug dentro de `leads`.
   Si no existe, avisa al usuario y para.

2. Actualiza el estado del lead según canal y toque:

   | Canal | Toque | Nuevo estado |
   |-------|-------|-------------|
   | email | t1 | `estado_email = "enviado_t1"` |
   | email | t2 | `estado_email = "enviado_t2"` |
   | email | t3 | `estado_email = "enviado_t3"` |
   | linkedin | paso1 | `estado_linkedin = "connection_enviada"` |
   | linkedin | paso2 | `estado_linkedin = "enviado_paso2"` |
   | linkedin | paso3 | `estado_linkedin = "enviado_paso3"` |

3. Añade evento al historial con timestamp:
   ```json
   {
     "tipo": "mensaje_enviado",
     "canal": "{canal}",
     "toque": "{toque}",
     "fecha": "{fecha_hoy}",
     "hora": "{HH:MM}"
   }
   ```

4. Calcula la próxima acción según reglas del playbook y actualiza
   `proxima_accion`:

   | Acción realizada | Próxima acción | Plazo |
   |-----------------|----------------|-------|
   | Email T1 enviado | Email T2 (si no responde) | +7 días |
   | Email T2 enviado | Email T3 (si no responde) | +14 días |
   | Email T3 enviado | Cerrar hilo (si no responde) | +21 días |
   | LinkedIn Paso 1 enviado | Verificar aceptación | +3 días |
   | LinkedIn Paso 2 enviado | Verificar respuesta | +5 días |
   | LinkedIn Paso 3 enviado | Cerrar hilo LinkedIn | +14 días |

   Formato:
   ```json
   {
     "fecha": "{fecha_calculada}",
     "tipo": "{tipo_accion}",
     "generada": false
   }
   ```

5. Guarda `data/pipeline.json`.

6. Confirma al usuario:
   ```
   Marcado: {empresa} — {canal} {toque} enviado el {fecha_hoy}
   Próxima acción: {tipo} el {fecha_proxima}
   ```
