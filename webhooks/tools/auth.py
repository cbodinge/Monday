import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# The scope for sending emails
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Token file (will be generated if it doesn't exist)
TOKEN_PICKLE = 'token.pickle'

# Load credentials or start the OAuth2 flow
def authenticate_gmail():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(TOKEN_PICKLE):
        with open(TOKEN_PICKLE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_PICKLE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Use the credentials to build the Gmail service
def get_gmail_service():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    return service

# Example of sending an email (you can modify as needed)
def send_email():
    service = get_gmail_service()
    message = {
        'to': 'receiver@example.com',
        'subject': 'Test Email',
        'body': 'This is a test email.'
    }
    # Convert message to a format Gmail can send and send it using the service
    # (refer to Gmail API documentation for exact implementation)
