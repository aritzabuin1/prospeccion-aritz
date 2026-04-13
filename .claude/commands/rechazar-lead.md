# /rechazar-lead $ARGUMENTS

Registra el rechazo de un lead con motivo para que el sistema aprenda.

## Parametros

Argumentos: `<dominio-o-numero> <motivo>`

- **dominio-o-numero**: dominio de la empresa (ej: `constructorasanjose.com`) o numero de la tabla de validacion
- **motivo**: uno de los siguientes:
  - `pequena` — demasiado pequeña, pocos empleados
  - `sector` — sector equivocado, no encaja con mi target
  - `web_muerta` — web no funciona o es un placeholder
  - `no_empresa` — no es una empresa (portal, directorio, medio)
  - `contactada` — ya la contacté por otra vía
  - `sin_potencial` — no veo potencial de transformación tecnológica
  - `otro` — otro motivo (especificar)

Ejemplo: `/rechazar-lead scholpp.es pequena`
Ejemplo: `/rechazar-lead 3,5,8 sector`

## Pasos

1. Lee `data/validados-{fecha_hoy}.json` para encontrar los candidatos.
   Si se pasan numeros, usa los indices de la tabla.

2. Para cada lead rechazado:
   - Ejecuta `scripts/feedback_leads.py` registrar_rechazo() con el motivo
   - Muestra confirmación

3. Si se rechazan varios con el mismo motivo, aceptar formato: `3,5,8 pequena`

4. Tras registrar, muestra resumen:
   ```
   Rechazados: {N} leads
   Motivo: {motivo}
   
   El sistema no volverá a presentar estos dominios.
   Feedback acumulado: {total_rechazos} rechazos, motivo más frecuente: {top_motivo}
   ```

5. Si se acumulan más de 5 rechazos por el mismo motivo, sugiere ajuste:
   - `pequena` x5+: "Considera subir el filtro minimo de empleados"
   - `sector` x5+: "Considera revisar los sectores en config/objetivos.json"
   - `web_muerta` x3+: "La validacion de web deberia ser mas estricta"
