from shotgun_api3 import Shotgun
from pyside_ui import select_folder
import os, zipfile

SG_URL = "https://samit.shotgunstudio.com"
SCRIPT_NAME = "raj_script"
SCRIPT_KEY = "jzkqws?quzhsBntgr0bjudnke"


def run_packager(shot_id, folder):
    sg = Shotgun(SG_URL, SCRIPT_NAME, SCRIPT_KEY)

    # Get tasks
    tasks = sg.find("Task", [["entity", "is", {"type": "Shot", "id": shot_id}]], ["content"])

    latest_files = []
    for task in tasks:
        files = sg.find("PublishedFile", [
            ["task", "is", task],
            ["entity", "is", {"type": "Shot", "id": shot_id}]
        ], ["path", "created_at"], order=[{'field_name': 'created_at', 'direction': 'desc'}], limit=1)

        if files and files[0]["path"]:
            latest_files.append(files[0]["path"]["local_path"])

    if not latest_files:
        return "No files found."

    folder = select_folder()
    if not folder:
        return "No folder selected."
    print(f"Processing Shot {shot_id} and saving to {folder}")
    zip_path = os.path.join(folder, f"Shot_{shot_id}_package.zip")
    with zipfile.ZipFile(zip_path, 'w') as z:
        for file_path in latest_files:
            if os.path.exists(file_path):
                z.write(file_path, os.path.basename(file_path))

    return f"Packaged {len(latest_files)} files to {zip_path}"
