# /retrospectiva

Ejecuta el bucle de automejora del sistema. Corre semanalmente (domingos
junto con `/metricas-semanales`).

## Qué hace

1. Lee `data/pipeline.json` y `data/feedback.json`.
2. Calcula tasas de respuesta segmentadas por sector, zona, tamaño, cargo
   del decisor y asunto de email.
3. Escribe:
   - `data/retrospectiva-{fecha}.json` — snapshot analítico completo.
   - `config/pesos_scoring.json` — bonus/penalty por sector/zona/tamaño/cargo
     para que `scripts/dedupe_y_score.py` los aplique en la próxima tanda.
   - `memory_suggestions.md` — borradores de feedback memories para que Aritz
     apruebe y convierta en memorias persistentes.

## Pasos

1. Ejecutar:
   ```
   python scripts/retrospectiva.py
   ```

2. Leer `memory_suggestions.md` y mostrar al usuario un resumen en
   castellano con:
   - Top 3 sectores que están convirtiendo mejor
   - Sectores/zonas a pausar (n≥5 sin respuestas)
   - Asuntos de email ganadores
   - Cambios automáticos aplicados a `config/pesos_scoring.json`

3. Preguntar al usuario qué sugerencias quiere convertir en memorias
   persistentes en `~/.claude/projects/C--Users-Aritz-Proyectos-IA-DRIVEN-prospeccion-aritz/memory/`.

4. Para cada sugerencia aprobada, crear la memoria con frontmatter
   `type: feedback` (o `project` si aplica) siguiendo la plantilla del
   sistema de memoria.

5. Actualizar `MEMORY.md` del proyecto con el índice de nuevas memorias.

## Filosofía

- El sistema **propone**, el humano **aprueba**. Nunca reescribir decisiones
  sin confirmación.
- No tocar `config/objetivos.json` directamente desde este script — los
  pesos van a `pesos_scoring.json` y el scorer los combina con los fijos.
- Conservar histórico: cada `retrospectiva-{fecha}.json` queda archivada
  para poder auditar cómo ha evolucionado el scoring.

## Integración con scoring

`scripts/dedupe_y_score.py` lee `config/pesos_scoring.json` si existe y
aplica los bonus/penalty sumándolos al score base calculado. Si el archivo
no existe, el scoring funciona con los pesos fijos de siempre.
