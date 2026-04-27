# /prospectar-tanda

Ejecuta la tanda completa: descubrimiento, scoring, validacion y presentacion.

**Objetivo de volumen: 40 leads por tanda, 2 tandas/semana = 80 leads/semana.**
El límite anterior era 15-30; se escaló para aumentar pipeline. Si el
descubrimiento devuelve menos de 40 validados, seguir adelante y logear
en `logs/tandas-bajas.log` para revisar queries.

## Distribución de la tanda (40 leads/tanda, 80/semana)

Cada tanda se reparte en tres tiers para asegurar mix de tickets:

- **Tier A — Mid-market España (60%):** 20-200 empleados, dolor operativo
  identificable. Base del pipeline, ciclos cortos.
- **Tier B — Gran cuenta (25%):** 200-1000 empleados en sectores objetivo,
  grupos con múltiples divisiones/sedes. Ciclos medios, tickets altos.
- **Tier C — Multinacional (15%):** >1000 empleados o presencia en múltiples
  países con decisor en España/UE/UK/EEUU/etc. Ciclos largos, tickets muy
  altos, posibles pilotos de departamento. Reservar queries específicas:
  "corporate AI adoption", "digital transformation director", anuncios de
  inversión en IA/automatización en medios sectoriales.

Regla: si una tanda sale sin Tier C, añadir una query extra enfocada a
grandes cuentas antes de cerrar.

## Pasos

1. Ejecuta los scripts de descubrimiento en secuencia desde la raiz del proyecto.
   Muestra progreso:
   - `python -m scripts.descubrir_cse`
   - `python -m scripts.descubrir_places`
   Si alguno falla, logea y continua con el siguiente.

2. Ejecuta dedupe y scoring:
   - `python -m scripts.dedupe_y_score`

3. Ejecuta validacion automatica de los top candidatos:
   - `python -m scripts.validar_leads`
   Esto visita las webs, busca empleados en LinkedIn/DDG, y asigna
   semaforo VERDE/AMARILLO/ROJO.

4. Lee `data/validados-{fecha_hoy}.json` y muestra al usuario una tabla
   con TODOS los leads validados, ordenados por semaforo (VERDE primero):

   ```
   #   Sem   Empresa                                        Empl   Sector                     Zona
   ----------------------------------------------------------------------------------------------------------
    1  VERDE SCHOLPP Madrid (maquinaria industrial)           120   industria_fabricacion       Madrid
    2  VERDE Grupo Monllor (transporte Valencia)               85   logistica_transporte       Valencia
    3  AMAR  Constructora XYZ                                   ?   construccion_ingenieria    Sevilla
    4  ROJO  Web Muerta SL                                      3   retail_cadenas             Barcelona
   ```

5. Registra en feedback cuantos leads se presentaron:
   `scripts/feedback_leads.py` registrar_presentados()

6. Pregunta al usuario:
   "¿Que leads quieres procesar a dossier? Numeros (ej: 1,3,5), 'verdes', o 'ninguno'.
   Para rechazar: /rechazar-lead <numeros> <motivo>"

7. Para cada lead aprobado:
   - Registra aprobacion en feedback: `scripts/feedback_leads.py` registrar_aprobacion()
   - Invoca la skill `prospeccion` **por nombre** con el contexto del candidato
   - **CRITICO**: Aplica `scripts/anonimizar.py` al output antes de guardar
   - Guarda dossier en `dossiers/{fecha_hoy}/{slug-empresa}.md`
   - Anade lead a `data/pipeline.json` con estado `nuevo` via `pipeline_utils.add_lead()`
   - Registra evento: `{tipo: "dossier_generado", fecha: ...}`

8. Al terminar, muestra resumen:
   ```
   Tanda completada — {fecha}
   Descubiertos: N | Validados: M | Aprobados: K | Rechazados: J
   Dossiers generados: K
   
   Feedback acumulado: X presentados, Y aprobados (Z%), top motivo rechazo: {motivo}
   
   Para generar mensajes: /generar-mensajes <slug-empresa>
   Para rechazar leads: /rechazar-lead <numeros> <motivo>
   ```

## Reglas

- Si algun script de descubrimiento falla, logea en `logs/` y continua
- No procesar a dossier ningun lead con score < 60 ni semaforo ROJO
- Leads AMARILLO: procesar solo si el usuario los aprueba explicitamente
- Leads rechazados NO vuelven a aparecer en tandas futuras (feedback loop)
- Si la skill `prospeccion` genera mensaje con nombres prohibidos, rechazar
  y pedir regenerar
