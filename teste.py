from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate the user
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates a local web server for authentication

drive = GoogleDrive(gauth)

# Upload a file
file_path = '1213_ones.py'  # Replace with your file path
upload_file = drive.CreateFile({'title': '1213_ones.py'})  # Set the file name
upload_file.SetContentFile(file_path)
upload_file.Upload()

print(f"File uploaded with ID: {upload_file['id']}")
