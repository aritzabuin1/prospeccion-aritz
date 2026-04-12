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
   - **CRITICO**: Al generar cualquier texto de mensaje o ángulo, aplica
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
