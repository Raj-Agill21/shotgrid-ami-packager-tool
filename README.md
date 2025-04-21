# ShotGrid AMI Packager Tool

A customization for Autodesk Flow Production Tracking (ShotGrid) using an Action Menu Item (AMI) that launches a local Python tool to package the latest published files from selected shots.

## 🎯 Goal

Right-click on one or more Shots in ShotGrid → Launch a local tool via `packager://` → Select a destination folder via UI → Automatically fetch & zip latest published files (Model, Rig, Texture, Anim).

## 🛠️ Features

- Triggered via AMI and a custom Windows protocol (`packager://`)
- PySide-based UI to choose the destination folder once
- Fetches latest published files from all relevant tasks
- Creates zip files per shot in the selected folder

## 📂 Files Included

| File               | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `launcher.bat`     | Launches the Python script when `packager://` is called       |
| `register_packages.reg` | Registers the `packager://` protocol on Windows              |
| `launcher.py`      | Parses arguments and launches the packager                    |
| `packager.py`      | Core logic: connects to ShotGrid, fetches files, creates zips |
| `pyside_ui.py`     | PySide UI for selecting destination folder                    |

---

## 🧰 Prerequisites

- Python 3.x
- ShotGrid Desktop App installed
- PySide2 installed:
  ```bash
  pip install PySide2

## 🚀 Setup Instructions
## ✅ 1. Clone the Repository

git clone https://github.com/yourusername/shotgrid-ami-packager-tool.git
cd shotgrid-ami-packager-tool

## 🔧 2. Register the packager:// Protocol
Edit the register_packages.reg file:

Update the path to launcher.bat (absolute path, double backslashes)

Example:

@="\"C:\\\\Users\\\\yourname\\\\shotgrid-ami-packager-tool\\\\launcher.bat\" \"%1\""
Save and double-click the .reg file to add the protocol to the registry.

## 🧷 3. Customize ShotGrid Script Credentials
Open packager.py and modify the following with your studio’s credentials:

sg = Shotgun(
    base_url="https://yourstudio.shotgrid.autodesk.com",
    script_name="your_script_name",
    api_key="your_script_key"
)

base_url → your studio’s ShotGrid site URL
script_name and api_key → credentials from ShotGrid Admin → Scripts

## 🛠️ 4. Configure the Action Menu Item (AMI)
In ShotGrid Web UI:

1. Go to Admin Menu → Site Preferences → Action Menu Items

2. Click + Add an Action Menu Item

3. Set the following values:

Field	Value
Title	Package Selected Shots
Entity Type	Shot
Multi-Entity	✅ Enabled
URL	packager://#{id}

4. Save it.

## 🧪 5. Test the Tool
1. Open ShotGrid and select one or more Shots.

2. Right-click → Choose “Package Selected Shots” (your AMI).

3. A PySide window appears to select the destination folder.

4. The tool fetches latest published files for tasks like Model, Rig, Texture, Anim.

5. Zipped files are saved to the selected location — one zip per shot.

## ⚠️ Notes
 - Works only on Windows (due to .bat + registry)

 - ShotGrid must have published files under proper task types

 - Supports multiple shots in one go with one folder prompt
