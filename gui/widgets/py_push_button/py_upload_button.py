from PySide6.QtWidgets import QPushButton, QFileDialog
from PySide6.QtCore import QThread, Signal
import time, os


class FileUploader(QThread):
    progress_changed = Signal(int)

    def __init__(self, files, parent=None):
        super().__init__(parent)
        self.files = files

    def run(self):
        total_size = sum(os.path.getsize(file) for file in self.files)
        uploaded_size = 0

        for file in self.files:
            #file_size = os.path.getsize(file)
            with open(file, 'rb') as f:
                while True:
                    chunk = f.read(3000)  # Read a chunk of data
                    if not chunk:
                        break
                    uploaded_size += len(chunk)
                    progress = uploaded_size * 100 // total_size
                    self.progress_changed.emit(progress)
                    time.sleep(0.1)  # Simulate upload delay

from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #cd18ee, stop: 0.5 #cd18ee,
                                      stop: 0.8 #1886ee, stop:1 #1886ee);
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////


class UploadButton(QPushButton):
    def __init__(
        self, 
        text,
        radius,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        circular_progress_bar,
        parent = None,
    ):
        super().__init__()

        self.clicked.connect(self.upload_files)
        self.file_uploader = FileUploader([])
        self.file_uploader.progress_changed.connect(self.update_progress)

        self.circular_progress_bar = circular_progress_bar

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed
        )
        self.setStyleSheet(custom_style)

    
    def upload_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            self.file_uploader.files = files
            self.file_uploader.start()

    def update_progress(self, progress):
        # Assuming you have a reference to the circular progress bar widget
        # Replace circular_progress_bar with the variable name of your circular progress bar widget
        self.circular_progress_bar.set_value(progress)





