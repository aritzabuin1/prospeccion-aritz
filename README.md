# Sistema de prospección — Aritz Abuin IA

Sistema local de prospección B2B con Claude Code como orquestador.

## Arranque rápido

1. **Prerrequisito crítico:** el repo de skills debe estar en `C:\Users\Aritz\dev\skills-aritz\` con las 3 junctions activas (`prospeccion`, `captacion-leads`, `follow-up`) en `%USERPROFILE%\.claude\skills\`. Verificar con: `Get-Item $env:USERPROFILE\.claude\skills\prospeccion | Select LinkType,Target` — debe ser `Junction` apuntando a `skills-aritz`. Si no, parar y reinstalar junctions desde el repo antes de seguir.
2. Clonar / copiar este proyecto
3. Crear entorno virtual (PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Copiar `.env.example` a `.env` y rellenar credenciales
5. Seguir sección "Setup inicial" abajo

## Setup inicial (una sola vez)

### Google Cloud Console
1. Crear proyecto en https://console.cloud.google.com
2. Activar las 3 APIs:
   - Custom Search API
   - Places API (New)
   - Gmail API
3. Crear API Key (Credenciales — Crear credencial — API Key)
4. Pegar en `.env` como `GOOGLE_API_KEY` y `GOOGLE_PLACES_API_KEY`

### Programmable Search Engine
1. Ir a https://programmablesearchengine.google.com/
2. Crear nuevo motor, activar "Buscar en toda la web"
3. Copiar el Search Engine ID — `.env` como `GOOGLE_CSE_ID`

### Gmail OAuth
1. En Google Cloud Console — Credenciales — Crear credencial — ID de cliente OAuth
2. Tipo: "Aplicación de escritorio"
3. Descargar JSON — guardar como `.gmail_credentials.json` en raíz del proyecto
4. Ejecutar `python scripts\gmail_auth.py` — abre navegador, autoriza
5. Se genera `.gmail_token.json` automáticamente

### Foto para firma
1. Subir tu foto de LinkedIn a ImgBB (https://imgbb.com) — gratis, sin cuenta
2. Copiar la URL directa (termina en .jpg o .png)
3. Pegar en `.env` como `FOTO_URL`

## Uso diario

Ver `CLAUDE.md` sección "Flujo diario tipo".

## Troubleshooting

- **Gmail API da error de permisos** — borra `.gmail_token.json` y corre `gmail_auth.py` otra vez
- **Custom Search devuelve 0 resultados** — revisa que el motor tenga "Buscar en toda la web" activado
- **Places API da quota exceeded** — revisa cuota en GCP, por defecto son 200$/mes gratis
