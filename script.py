import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
def convert_token_format():
    """Converts existing token.json to the format expected by google.auth.load_credentials_from_file()"""

    token_path = 'etc/secrets/token.json'

    # Read the existing token
    with open(token_path, 'r') as f:
        token_data = json.load(f)

    # Create the properly formatted token data
    formatted_token = {
        "type": "authorized_user",
        "client_id": token_data.get("client_id"),
        "client_secret": token_data.get("client_secret"),
        "refresh_token": token_data.get("refresh_token")
    }

    # Save the formatted token
    with open(token_path, 'w') as f:
        json.dump(formatted_token, f)

    print(f"Converted token.json to the proper format")

# Define the scopes your application needs
# For Gmail API, common scopes include:
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    # Add other scopes as needed
]


def generate_token():
    #Generates a token.json file using credentials.json
    
    # Check if credentials.json exists in the current directory
    if not os.path.exists('credentials.json'):
        print("Error: credentials.json not found in the current directory")
        return
    
    # Create the flow using the client secrets file (credentials.json)
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    
    # Run the OAuth flow which will open a browser window for authentication
    # If you're running this on a server without a UI, use run_console() instead
    credentials = flow.run_local_server(port=54767)
    
    # Save the credentials to token.json
    with open('etc/secrets/token.json', 'w') as token:
        token.write(credentials.to_json())
    
    print("Successfully generated token.json")
    
    # Optional: Test the credentials by making a simple API call
    try:
        service = build('gmail', 'v1', credentials=credentials)
        results = service.users().labels().list(userId='me').execute()
        print("Verified token works by retrieving Gmail labels")
        convert_token_format()
    except Exception as e:
        print(f"Token generated but verification failed: {str(e)}")
    

if __name__ == '__main__':
    generate_token()

