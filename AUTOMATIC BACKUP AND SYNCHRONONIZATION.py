import os 
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive']

creds = None

# Check if token.json exists and load the credentials
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

# If no valid credentials, refresh or get new ones
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        # Authenticate and create new credentials
        flow = InstalledAppFlow.from_client_secrets_file(r"D:\AUTOMATIC BACKUP\Credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for next time
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    # Build the Google Drive service
    service = build("drive", "v3", credentials=creds)

    # Search for the folder "BackupFolder2024"
    response = service.files().list(q="name='BackupFolder2024' and mimeType='application/vnd.google-apps.folder'", spaces='drive').execute()

    if not response['files']:
        # If folder doesn't exist, create it
        file_metadata = {"name": "BackupFolder2024", "mimeType": "application/vnd.google-apps.folder"}

        file = service.files().create(body=file_metadata, fields="id").execute()

        folder_id = file['id']

    else:
        # Get the folder ID if it already exists
        folder_id = response['files'][0]['id']

    # Upload files to the folder
    for file in os.listdir('D:/AUTOMATIC BACKUP/backup_folder'):
        file_metadata = {
            "name": file,
            "parents": [folder_id]
        }

        media = MediaFileUpload(f"backup_folder/{file}")
        upload_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()

        print(f"BACKING UP FILE: {file}")


except HttpError as e:
    print(f"Error: {str(e)}")

print("YAAAAY!!! BACKUP SUCCESSFUL")