# /enviar-prospeccion

Dispara el ciclo completo de envío de prospección **cuando tú decidas**.
Pensado para cuando el PC no está siempre encendido y el cron no puede correr.

## Qué hace

1. Verifica que hoy es día óptimo para al menos uno de los toques pendientes
   (T1/T2/T3). Si no lo es, avisa y para.
2. Ejecuta `python -m scripts.preparar_borradores` → crea drafts en Gmail
   con etiqueta `PROSPECCION-PENDIENTE` para los leads cuyo `proxima_accion.fecha`
   sea hoy o está vencida.
3. Lee `data/borradores_pendientes.json` y muestra al usuario una tabla:
   ```
   #  Empresa              Toque  Asunto                          Destinatario
   1  Capel Vinos          T2     Re: Un pedido en alemán...      ...
   2  Grupo CCOMMO         T2     Re: Los 36 en Semana Santa      ...
   ...
   ```
4. Pregunta al usuario:
   ```
   Revisa los borradores en Gmail (etiqueta PROSPECCION-PENDIENTE).
   Para vetar un envío: borra el borrador desde Gmail AHORA.
   ¿Envío los que queden? (s/n, o "esperar 30min" para darte tiempo)
   ```
5. Si el usuario responde `s` → ejecuta `python -m scripts.enviar_pendientes`.
   Si responde `esperar 30min` → espera 30 min y luego ejecuta.
   Si responde `n` → deja los borradores para siguiente sesión (no se envían,
   siguen etiquetados).

6. Al terminar, muestra resumen:
   ```
   Enviados: X | Vetados: Y | Reagendados: Z
   Próximas acciones programadas:
   - capel-vinos: T3 el 2026-05-09
   - ...
   ```

## Cuándo usarlo

- Cuando enciendas el PC por la mañana en día laborable óptimo.
- Si el PC estuvo apagado varios días, al volver: lanza `/enviar-prospeccion`
  para ponerte al día con los toques pendientes.
- Si no quieres enviar hoy: no ejecutes el comando. El sistema no hace nada
  hasta que lo dispares.

## Reglas

- Solo envía si hoy es óptimo para el toque correspondiente:
  - T1 → martes, miércoles, jueves
  - T2 → martes, miércoles
  - T3 → martes
- Si hoy no es óptimo para un toque concreto, ese lead se re-programa al
  siguiente día óptimo (no se envía hoy).
- Si hoy es festivo nacional de España, se re-programa todo.
- Un lead solo puede tener un borrador activo a la vez (evita duplicados).
