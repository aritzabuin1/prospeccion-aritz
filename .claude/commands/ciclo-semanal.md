# /ciclo-semanal

Ejecuta todo el ciclo semanal de prospección en un solo comando. Pensado
para lunes por la mañana. Tiempo total ~45 min, ~10-15 min de atención real.

## Qué hace

1. **Descubre 40-50 candidatos** — ejecuta `python -m scripts.descubrir_cse`
   y `python -m scripts.descubrir_places`.
2. **Scoring + dedupe** — `python -m scripts.dedupe_y_score` (aplica pesos
   aprendidos de `config/pesos_scoring.json` si existen).
3. **Validación** — `python -m scripts.validar_leads` asigna semáforo.
4. **Auto-aprobación:** todos los leads VERDE con score ≥70 pasan sin pedir
   confirmación. Solo los AMARILLO (típicamente 3-5) se presentan a Aritz
   para decisión rápida: "aprobar / rechazar / saltar".
5. **Limitar a 30 leads** priorizando por score descendente.
6. **Generar dossieres y mensajes** — para cada aprobado:
   - Invocar skill `prospeccion` → dossier en `dossiers/{fecha}/{slug}.md`.
   - Ejecutar `/generar-mensajes <slug>` → email T1 + LinkedIn Paso 1 + contacto.md en `outbox/{fecha}/{slug}/`.
   - Añadir a `data/pipeline.json` con estado `nuevo`.
7. **Distribuir envíos en mar/mié/jue** — ejecutar
   `python -m scripts.distribuir_semana slug1 slug2 ...` con los 30 slugs.
   Reparto 10/10/10 (ajusta si hay menos de 30).
8. **Mostrar resumen final:**
   ```
   Ciclo semanal completado — {fecha}
   
   Descubiertos: 47 | Aprobados: 30 | Dossieres: 30 | Mensajes: 30
   
   Distribución de envíos T1:
   - Martes {fecha}: 10 leads → {lista slugs}
   - Miércoles {fecha}: 10 leads → {lista slugs}
   - Jueves {fecha}: 10 leads → {lista slugs}
   
   Tus acciones pendientes esta semana:
   - Martes 9:30 → /enviar-prospeccion (3 min)
   - Miércoles 9:30 → /enviar-prospeccion (3 min)
   - Jueves 9:30 → /enviar-prospeccion (3 min)
   - Domingo → /retrospectiva (5 min)
   
   LinkedIn Paso 1 (30 connections sin nota) → enviar manualmente a lo
   largo de la semana. URLs en outbox/{fecha}/{slug}/contacto.md.
   ```

## Reglas de auto-aprobación

- **VERDE + score ≥ 70** → aprobado automáticamente (sin preguntar).
- **VERDE + score 60-69** → presentar a Aritz (puede ser borderline).
- **AMARILLO** → presentar a Aritz con motivo de duda.
- **ROJO** → descartar sin preguntar.
- **Cualquiera con motivo_rechazo=scope_geografico previo** → descartar.
- Si tras auto-aprobación hay más de 30 VERDE ≥70, tomar los 30 de mayor score.
- Si hay menos de 30, completar con VERDE 60-69 previa aprobación rápida.

## Preguntas al usuario (mínimas)

Solo se preguntará en estos casos:
1. Si hay leads AMARILLO: "3 leads dudosos: [lista]. ¿Aprobar todos / ninguno / uno a uno?"
2. Si el total aprobado es < 20: "Solo hay 18 leads viables esta semana. ¿Continuar o esperar siguiente tanda?"

Todo lo demás corre sin pedir confirmación.

## Salida y próximos pasos

Al terminar, el sistema queda así:
- 30 leads en pipeline con `proxima_accion.fecha` asignada a mar/mié/jue.
- 30 carpetas en `outbox/{fecha}/{slug}/` con T1 email, LinkedIn Paso 1 y contacto.md.
- Aritz solo tiene que:
  - Mandar las 30 connection requests LinkedIn manualmente (sin nota) durante la semana.
  - Ejecutar `/enviar-prospeccion` mar/mié/jue a las 9:30 (3 min cada vez).

## Cuándo ejecutar

- **Cada lunes por la mañana** (si lunes es festivo, entonces martes temprano).
- Si la semana anterior aún quedan leads pendientes (no enviados), el script
  los detecta y no duplica trabajo — solo rellena hasta llegar a 30.
