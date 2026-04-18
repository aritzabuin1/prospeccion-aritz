# Automatización de envío — Guía de setup

El sistema envía los emails de prospección automáticamente:

- **Borradores se crean de madrugada** (00:30) con etiqueta `PROSPECCION-PENDIENTE`.
- **Aritz recibe un email a `aritzmore1@gmail.com`** a las 08:00 con la lista.
- **A las 09:30** el sistema envía todos los borradores que no se hayan vetado.
- Ventanas óptimas por toque:
  - T1 → martes, miércoles, jueves
  - T2 → martes, miércoles
  - T3 → martes
- Salta sábados, domingos y festivos nacionales de España.

Para vetar un envío: borrar el borrador desde Gmail. El sistema detecta la
ausencia y lo marca como `cancelado_por_usuario`.

## Requisitos previos

1. `.gmail_credentials.json` presente en la raíz del proyecto.
2. Primer OAuth ejecutado (scope = `gmail.modify`):
   ```powershell
   .venv\Scripts\python.exe scripts\gmail_auth.py
   ```
   Si ya estaba autenticado con scope `readonly`, hay que borrar
   `.gmail_token.json` y volver a ejecutar para re-consentir.
3. Dependencia `holidays` instalada (`pip install -r requirements.txt`).

## Crear las tareas en Windows Task Scheduler

Abre PowerShell **como administrador** en la raíz del proyecto y ejecuta:

```powershell
$ProjectPath = "C:\Users\Aritz\Proyectos IA-DRIVEN\prospeccion-aritz"
$Python = "$ProjectPath\.venv\Scripts\python.exe"

# Tarea 1: preparar borradores (00:30 diario)
$Action1 = New-ScheduledTaskAction -Execute $Python `
    -Argument "-m scripts.preparar_borradores" `
    -WorkingDirectory $ProjectPath
$Trigger1 = New-ScheduledTaskTrigger -Daily -At 00:30
Register-ScheduledTask -TaskName "Prospeccion-PrepararBorradores" `
    -Action $Action1 -Trigger $Trigger1 `
    -Description "Crea borradores Gmail con etiqueta PROSPECCION-PENDIENTE para leads programados mañana" `
    -User $env:USERNAME -RunLevel Limited

# Tarea 2: notificar revisión (08:00 diario)
$Action2 = New-ScheduledTaskAction -Execute $Python `
    -Argument "-m scripts.notificar_revision" `
    -WorkingDirectory $ProjectPath
$Trigger2 = New-ScheduledTaskTrigger -Daily -At 08:00
Register-ScheduledTask -TaskName "Prospeccion-NotificarRevision" `
    -Action $Action2 -Trigger $Trigger2 `
    -Description "Envía resumen de borradores pendientes a aritzmore1@gmail.com" `
    -User $env:USERNAME -RunLevel Limited

# Tarea 3: enviar pendientes (09:30 diario)
$Action3 = New-ScheduledTaskAction -Execute $Python `
    -Argument "-m scripts.enviar_pendientes" `
    -WorkingDirectory $ProjectPath
$Trigger3 = New-ScheduledTaskTrigger -Daily -At 09:30
Register-ScheduledTask -TaskName "Prospeccion-EnviarPendientes" `
    -Action $Action3 -Trigger $Trigger3 `
    -Description "Envía borradores etiquetados PROSPECCION-PENDIENTE (solo días laborables óptimos)" `
    -User $env:USERNAME -RunLevel Limited
```

Verificar:
```powershell
Get-ScheduledTask -TaskName "Prospeccion-*" | Select-Object TaskName, State
```

## Condición importante: PC encendido

Windows Task Scheduler solo ejecuta si el PC está encendido y logueado.
Opciones si duermes el PC:

- **Opción A (recomendada):** dejar el PC despierto durante semana laboral.
  Windows → Configuración → Sistema → Inicio/apagado → "Suspender tras":
  nunca cuando está enchufado.
- **Opción B:** programar encendido con BIOS (Wake-on-LAN / RTC) a las 00:15.
- **Opción C (más adelante):** mover los cron jobs a un VPS o a GitHub Actions.
  Implica gestionar `.gmail_token.json` como secret — más trabajo, pero 100%
  independiente del PC local.

## Desactivar temporalmente

```powershell
Disable-ScheduledTask -TaskName "Prospeccion-PrepararBorradores"
Disable-ScheduledTask -TaskName "Prospeccion-NotificarRevision"
Disable-ScheduledTask -TaskName "Prospeccion-EnviarPendientes"
```

Re-activar con `Enable-ScheduledTask`.

## Flujo diario (ejemplo)

**Lunes 22/04 00:30** — `preparar_borradores.py`:
- Mira pipeline: ¿hay leads con `proxima_accion.fecha = 2026-04-21` (martes) y tipo email?
- Para cada uno: crea borrador en Gmail con HTML + firma, etiqueta PROSPECCION-PENDIENTE.
- Escribe `data/borradores_pendientes.json` con la lista.

**Martes 23/04 08:00** — `notificar_revision.py`:
- Lee `borradores_pendientes.json`.
- Envía email resumen a `aritzmore1@gmail.com` con 3 borradores listados + link a Gmail.

**Martes 23/04 08:00-09:30** — Aritz:
- Recibe la notif en móvil.
- Abre Gmail (cuenta aritzabuin1) → etiqueta PROSPECCION-PENDIENTE.
- Revisa en 1 min. Borra 1 borrador que no le convence. Deja 2.

**Martes 23/04 09:30** — `enviar_pendientes.py`:
- Ve los 2 borradores que siguen etiquetados → los envía.
- El borrado manual lo detecta como "vetado" → marca cancelado_por_usuario.
- Pipeline se actualiza: 2 leads pasan a `enviado_t1`, próxima acción T2 a +7 días.

## Troubleshooting

- **Token expirado:** borrar `.gmail_token.json` y re-ejecutar `python scripts/gmail_auth.py`.
- **No se crean borradores:** revisar que los leads tengan `contacto.email` y
  que los archivos `email-t{N}.html` existan en `outbox/{fecha}/{slug}/`.
- **Se envía 2 veces:** el script marca el lead como `enviado_t{N}` al mandarlo,
  así que la segunda ejecución lo salta.
- **Logs:** añadir redirección a Task Scheduler action: `-Argument "-m scripts.enviar_pendientes > logs\envio.log 2>&1"`.
