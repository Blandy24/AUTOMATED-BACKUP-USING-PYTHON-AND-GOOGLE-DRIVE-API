
This Python script automates the process of backing up files from a local directory to a Google Drive folder. It utilizes the Google Drive API for seamless integration with Google Drive. The script checks for valid credentials, authenticates the user if necessary, and creates a dedicated folder (if not already existing) on Google Drive to store the backup files.

Key Features:
1.Authentication: Uses OAuth 2.0 credentials for secure access to Google Drive.
2.Folder Management: Checks for an existing backup folder on Google Drive and creates one if it doesn’t exist.
3.File Upload: Automatically uploads files from a specified local folder to the Google Drive folder.
4.Error Handling: Catches and prints any errors related to the Google Drive API.

Requirements:
1.Google Cloud project with Google Drive API enabled.
2.OAuth 2.0 credentials (Credentials.json).
3.Python libraries: google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client.

Setup Instructions:
1.Create a project on Google Cloud Console.
2.Enable the Google Drive API for the project.
3.Download the Credentials.json file and place it in the project directory.
4.Install required libraries using pip install -r requirements.txt.
5.Run the script to authenticate and upload your backup files to Google Drive.
