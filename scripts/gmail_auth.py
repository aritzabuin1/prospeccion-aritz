"""
OAuth flow standalone para Gmail API.

Uso:
    python scripts/gmail_auth.py

Primera ejecución: abre navegador para autorizar.
Siguientes: reutiliza token guardado.
"""

import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(PROJECT_ROOT, ".gmail_credentials.json")
TOKEN_PATH = os.path.join(PROJECT_ROOT, ".gmail_token.json")

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def authenticate():
    """
    Ejecuta el flujo OAuth de Gmail API.
    - Si ya existe token válido, lo reutiliza.
    - Si el token expiró, lo refresca.
    - Si no hay token, abre navegador para autorizar.
    Devuelve las credenciales autenticadas.
    """
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"ERROR: No se encuentra {CREDENTIALS_PATH}")
        print("Descarga el archivo de credenciales OAuth desde Google Cloud Console")
        print("y guárdalo como .gmail_credentials.json en la raíz del proyecto.")
        sys.exit(1)

    creds = None

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Token expirado, refrescando...")
            creds.refresh(Request())
        else:
            print("Abriendo navegador para autorizar Gmail API...")
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())
        print(f"Token guardado en {TOKEN_PATH}")

    return creds


def get_gmail_service():
    """Devuelve un servicio de Gmail API autenticado."""
    creds = authenticate()
    return build("gmail", "v1", credentials=creds)


def _self_test():
    """Verifica que la autenticación funciona y muestra perfil."""
    service = get_gmail_service()
    profile = service.users().getProfile(userId="me").execute()
    print(f"Autenticado como: {profile['emailAddress']}")
    print(f"Total mensajes: {profile['messagesTotal']}")
    print("gmail_auth: setup completo OK")


if __name__ == "__main__":
    _self_test()
