@echo off
REM Strip protocol and pass the rest to the Python script
set url=%1
set args=%url:packager://=%

REM Run Python with the args
"C:\Shotgrid_scripts\shotgrid_ami_packager\venv\Scripts\python.exe" "C:\Shotgrid_scripts\shotgrid_ami_packager\launcher.py" %args%

pause
