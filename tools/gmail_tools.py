#   To install the Google client library for Python, run the following command:
#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


from __future__ import print_function
import re
import base64
import email
import json
import os.path

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

#search_for = "in:inbox subject:(verification code)"
search_for = "in:inbox is:unread"


class Message:
    def __init__(self, id=None, subject=None, body=None, status=None, report=None):
        self.id = id
        self.subject = subject
        self.body = body
        self.status = status
        self.report = report

    def __repr__(self):
        return f"Message(id={self.id}, subject='{self.subject}', body='{self.body}', status='{self.status}', report='{self.report}')"


class MockResponse:
    def __init__(self, messages_data):
        self.messages = []
        for msg_data in messages_data:
            # Using **msg_data to unpack dictionary keys as keyword arguments
            self.messages.append(Message(**msg_data))

    def __repr__(self):
        return f"MockResponse(messages={self.messages})"


def authorize(credentials_file_path, token_file_path):
    """Shows basic usage of authorization"""
    try:
        credentials = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_file_path):
            try:
                credentials = Credentials.from_authorized_user_file(token_file_path, SCOPES)
                credentials.refresh(Request())
            except google.auth.exceptions.RefreshError as error:
                # if refresh token fails, reset creds to none.
                credentials = None
                print(f'An refresh authorization error occurred: {error}')
        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file_path, SCOPES)
                credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_file_path, 'w') as token:
                token.write(credentials.to_json())
    except HttpError as error:
        # Todo handle error
        print(f'An authorization error occurred: {error}')

    return credentials

def list_messages(credentials):
    try:
        # create a gmail service object
        service = build('gmail', 'v1', credentials=credentials)

        # Call the Gmail v1 API
        results = service.users().messages().list(userId='me', q=search_for).execute()
        all_messages = []
        messages = results.get('messages', [])

        if not messages:
            print('No messages where found.')
            return
        #print('Messages:')

        cnt = 0
        for message in messages:
            if cnt > 1:
                break

            message = get_message(credentials, message['id'])
            all_messages.append(message)
            cnt = cnt + 1
        return all_messages

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


def strip_html_regex(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def get_message(credentials, message_id) -> Message:
    # get a message
    try:
        service = build('gmail', 'v1', credentials=credentials)

        # Call the Gmail v1 API, retrieve message data.
        message = service.users().messages().get(userId='me', id=message_id, format='raw').execute()

        # Parse the raw message.
        mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))

        body = ""
        # Find full message body
        message_main_type = mime_msg.get_content_maintype()
        if message_main_type == 'multipart':
            for part in mime_msg.get_payload():
                if part.get_content_maintype() == 'text':
                    body = part.get_payload()
        elif message_main_type == 'text':
            body = mime_msg.get_payload()

        return Message(id=message_id, subject=mime_msg['subject'], body=strip_html_regex(body))

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'A message get error occurred: {error}')


def get_unread_messages_from_inbox() -> dict:
    """Get a list of unread emails in inbox
    returns a list of messages"""
    creds = authorize('C:\\YouTube\\dev\\credentials.json', "token.json")
    results = list_messages(creds)
    objects_dict_v2 = {obj.id: obj.__dict__ for obj in results}
    return objects_dict_v2

def update_label(credentials, message_id, add_label_id=None, remove_label_id=None):
    try:
        # create a gmail service object
        service = build('gmail', 'v1', credentials=credentials)
        print(f"Message id to update label {message_id}")
        body = {
            "addLabelIds": [
                add_label_id
            ],
          "removeLabelIds": [
            remove_label_id
          ]
        }
        # Call the Gmail v1 API
        results = service.users().messages().modify(userId='me', id=message_id, body=body).execute()
        print(results)
        return results
    except HttpError as error:
        print(f'An error occurred: {error}')
        return -1


def update_unread_messages_to_read(message_ids: list[str]) -> dict:
    """Updates a list of messages, marking them as read by removing the 'UNREAD' label.

    Args:
        message_ids: A list of message ID strings to be updated.

    Returns:
        dict: A dictionary where keys are message IDs and values are dictionaries
              of message attributes for a set of messages fetched after the update
              operation (currently limited by the behavior of `list_messages`).
              Note: This may not directly correspond to the messages updated
              if they don't fall within the scope of `list_messages`.
    """
    creds = authorize('C:\\YouTube\\dev\\credentials.json', "token.json")
    print("Looping through message IDs:")
    for message_id in message_ids:
        print(f"Updating message {message_id} to read")
        update_label(creds, message_id, add_label_id=None, remove_label_id="UNREAD" )
    results = list_messages(creds)
    objects_dict_v2 = {obj.id: obj.__dict__ for obj in results}
    return objects_dict_v2


if __name__ == '__main__':
    creds = authorize('C:\\YouTube\\dev\\credentials.json', "token.json")
    get_unread_messages_from_inbox()
