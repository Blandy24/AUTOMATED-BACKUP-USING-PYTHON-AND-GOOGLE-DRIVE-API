
This Python script automates the process of backing up files from a local directory to a Google Drive folder. It utilizes the Google Drive API for seamless integration with Google Drive. The script checks for valid credentials, authenticates the user if necessary, and creates a dedicated folder (if not already existing) on Google Drive to store the backup files.

Key Features:
Authentication: Uses OAuth 2.0 credentials for secure access to Google Drive.
Folder Management: Checks for an existing backup folder on Google Drive and creates one if it doesn’t exist.
File Upload: Automatically uploads files from a specified local folder to the Google Drive folder.
Error Handling: Catches and prints any errors related to the Google Drive API.
Requirements:
Google Cloud project with Google Drive API enabled.
OAuth 2.0 credentials (Credentials.json).
Python libraries: google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client.
Setup Instructions:
Create a project on Google Cloud Console.
Enable the Google Drive API for the project.
Download the Credentials.json file and place it in the project directory.
Install required libraries using pip install -r requirements.txt.
Run the script to authenticate and upload your backup files to Google Drive.
