
import time, os
from typing import Optional, Union
from PySide6.QtWidgets import QPushButton, QFileDialog
from PySide6.QtCore import QThread, Signal

from gui.core.functions import Functions
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
        type,
        parent = None,
    ):
        super().__init__()

        if type=="folder":
            self.clicked.connect(self.upload_folder)
        elif type=="file":
            self.clicked.connect(self.upload_files)
        else:
            raise Exception("Type must be one of : ['folder' or 'file']")

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
            self.files = file_dialog.selectedFiles()
            #print(f"Selected files : {self.files}")


    def upload_folder(self):
        options = QFileDialog.Options()
        self.src_folder = QFileDialog.getExistingDirectory(self, "Select folder",
                                                      options=options)
        







