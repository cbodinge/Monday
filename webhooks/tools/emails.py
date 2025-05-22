from __future__ import print_function
import os
import argparse
from googleapiclient.discovery import build
from apiclient import errors
import oauth2client
from oauth2client import client, file, tools
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



SCOPES = "https://mail.google.com/"
CLIENT_SECRET_FILE = 'C:\\Coding Projects\\Monday\\client_secret.json'
APPLICATION_NAME = 'Sample Testing'

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
      Credentials, the obtained credential.
    """

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)

        print('Storing credentials to ' + credential_path)


    return credentials


# create a message
def CreateMessage(sender: str, to: str, subject: str, attachments: list):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      attachments: The text and attachments of the email message.

    Returns:
      An object containing a base64 encoded email object.
    """
    msg = MIMEMultipart()
    msg['to'] = to
    msg['from'] = sender
    msg['subject'] = subject

    for attachment in attachments:
        msg.attach(attachment)


    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()

    return {'raw': raw}


# send message
def SendMessage(service, user_id, message):
    """Send an email message.

    Args:
     service: Authorized Gmail API service instance.
     user_id: User's email address. The special value "me"
     can be used to indicate the authenticated user.
     message: Message to be sent.

    Returns:
     Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        # print 'Message Id: %s' % message['id']
        return message
    except errors.HttpError as e:
        print('An error occurred: %s' % e)


def text(msg: str):
    return MIMEText(msg, 'plain', 'utf-8')


def pdf(_file: bytes, filename: str):
    pdf_file = MIMEApplication(_file, _subtype="pdf")
    pdf_file.add_header('Content-Disposition', 'attachment', filename=filename)

    return pdf_file


def send(receiver: str, subject: str, attachments: list):
    """Shows basic usage of the Gmail API.
       Send a mail using gmail API
    """
    credentials = get_credentials()
    service = build('gmail', 'v1', credentials=credentials)

    message = CreateMessage("pinpoint.requisitions@gmail.com", receiver, subject, attachments)

    SendMessage(service, "me", message)

