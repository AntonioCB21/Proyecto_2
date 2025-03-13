import os
import json
import time
import datetime
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import dropbox

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def authenticate_dropbox(token):
    return dropbox.Dropbox(token)

def upload_to_google_drive(drive, file_path):
    file_name = file_path.split("/")[-1]
    file = drive.CreateFile({'title': file_name})
    file.SetContentFile(file_name)
    file.Upload()
    print(f"Uploaded {file_name} to Google Drive")

def upload_to_dropbox(dbx, file_path):
    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), f"/{os.path.basename(file_path)}", mode=dropbox.files.WriteMode("overwrite"))
    print(f"Uploaded {file_path} to Dropbox")

def clean_old_files():
    config = load_config()
    retention_days = config.get("retention_days", 7)
    now = datetime.datetime.now()
    for file in os.listdir(config["backup_folder"]):
        file_path = os.path.join(config["backup_folder"], file)
        file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if (now - file_time).days > retention_days:
            os.remove(file_path)
            print(f"Deleted old backup: {file}")

def backup():
    config = load_config()
    drive, dbx = None, None
    
    if config.get("use_google_drive", False):
        drive = authenticate_google_drive()
    if config.get("use_dropbox", False):
        dbx = dropbox.Dropbox(config["dropbox_token"])
    
    for file in config["files_to_backup"]:
        if drive:
            upload_to_google_drive(drive, file)
        if dbx:
            upload_to_dropbox(dbx, file)
    
    clean_old_files()

# Programar ejecución automática
config = load_config()
schedule.every(config.get("backup_interval", 24)).hours.do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(60)
