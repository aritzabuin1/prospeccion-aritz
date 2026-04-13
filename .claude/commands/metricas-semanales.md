# /metricas-semanales

Ejecuta cada domingo. Genera report completo de la semana.

## Pasos

1. Ejecuta `python -m scripts.metricas_semanales` desde la raiz del proyecto.

2. Lee el archivo generado en `reports/semana-{N}-{año}.md`.

3. Muestralo al usuario completo (resumen, clasificaciones, tasas por sector,
   tasas por fuente, tasas por toque, aprendizajes).

4. Basandote en los datos del report, sugiere 1-2 ajustes concretos:
   - Ajustes al playbook (tono, asunto, longitud)
   - Ajustes a objetivos (sectores a priorizar/descartar)
   - Ajustes a fuentes de descubrimiento (cuales funcionan, cuales no)

5. Pregunta al usuario si quiere aplicar algun ajuste a `config/objetivos.json`
   o `playbook-outreach.md`.
