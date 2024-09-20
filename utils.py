
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
from email.message import EmailMessage

# Função para criar o serviço do Gmail
def Create_Service(client_secret_file, api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    cred = None
    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server(port=8000)  # Porta padrão para desenvolvimento

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        return service
    except Exception as e:
        print(f'Erro ao conectar com o serviço do Gmail: {e}')
        return None

# Função para enviar email usando Gmail
def send_email_via_gmail(subject, body, to_email):
    try:
        # Criar serviço do Gmail
        service = Create_Service('credentials.json', 'gmail', 'v1', ['https://mail.google.com/'])
        
        if service:
            # Montar a mensagem
            message = EmailMessage()
            message.set_content(body)
            message['To'] = to_email
            message['From'] = 'seuemail@gmail.com'  # Substitua pelo seu email
            message['Subject'] = subject

            # Codificar a mensagem em base64
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            raw_message = {'raw': raw_message}

            # Enviar email via Gmail API
            service.users().messages().send(userId='me', body=raw_message).execute()
            print(f'Email enviado para {to_email}')
        else:
            print("Serviço do Gmail não foi criado.")
    
    except Exception as e:
        print(f'Erro ao enviar email: {e}')