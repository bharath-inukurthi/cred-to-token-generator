import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    """add scopes which you want to aquire"""
]


def generate_token():
    """Generates a token.json file using credentials.json"""

    # Check if credentials.json exists in the current directory
    if not os.path.exists('credentials.json'):
        print("Error: credentials.json not found in the current directory")
        return

    # Create the flow using the client secrets file (credentials.json)
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)

    # Run the OAuth flow which will open a browser window for authentication
    # If you're running this on a server without a UI, use run_console() instead
    credentials = flow.run_local_server(port=8000)#specify your port

    # Save the credentials to token.json
    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

    print("Successfully generated token.json")

    # Optional: Test the credentials by making a simple API call
    try:
        service = build('gmail', 'v1', credentials=credentials)
        results = service.users().labels().list(userId='me').execute()
        print("Verified token works by retrieving Gmail labels")
    except Exception as e:
        print(f"Token generated but verification failed: {str(e)}")


if __name__ == '__main__':
    generate_token()