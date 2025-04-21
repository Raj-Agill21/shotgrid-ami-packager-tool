import sys
from PySide2.QtWidgets import QApplication, QFileDialog

def select_folder():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    folder = QFileDialog.getExistingDirectory(None, "Select Destination Folder")
    return folder
