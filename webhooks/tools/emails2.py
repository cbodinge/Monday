from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send():
    """Shows basic usage of the Gmail API.
       Send a mail using gmail API
    """
    scope = 'https://www.googleapis.com/auth/gmail.send'

    credentials = Credentials.from_authorized_user_file('C:\\Coding Projects\\Monday\\client_secret.json', [scope])
    service = build('gmail', 'v1', credentials=credentials)

    send_message = service.users().messages().send(userId="me", body={'raw': get_message()}).execute()
    print('Message Id: %s' % send_message['id'])
# Load credentials (ensure OAuth2 is properly authenticated)

def get_message():
    message = MIMEMultipart()
    message['to'] = "carter.bodinger@pinpointtesting.com"
    message['from'] = "pinpoint.requisitions@gmail.com"
    message['subject'] = "Test Email"
    msg = MIMEText('This is a test email.')
    message.attach(msg)

    return base64.urlsafe_b64encode(message.as_bytes()).decode()

