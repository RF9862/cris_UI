from PySide6.QtWidgets import QPushButton, QFileDialog
from PySide6.QtCore import QThread, Signal
import time


class FileUploader(QThread):
    progress_changed = Signal(int)

    def run(self):
        # Simulate file upload process
        for i in range(101):
            time.sleep(0.1)  # Simulate upload delay
            self.progress_changed.emit(i)

class UploadButton(QPushButton):
    def __init__(self, circular_progress_bar, parent=None):
        super().__init__("Upload", parent)
        self.clicked.connect(self.upload_files)
        self.file_uploader = FileUploader()
        self.file_uploader.progress_changed.connect(self.update_progress)

        self.circular_progress_bar = circular_progress_bar

    def upload_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            self.file_uploader.start()

    def update_progress(self, progress):
        # Assuming you have a reference to the circular progress bar widget
        # Replace circular_progress_bar with the variable name of your circular progress bar widget
        self.circular_progress_bar.set_value(progress)

