# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import shutil
import time
import glob
from datetime import datetime
import threading
import random

from ultralytics import YOLO
from yolov8.src.yolo_utils import YOLO8Functions
from yolov5.src.yolo_utils import YOLO5Functions
from yolov8.src.config import SAVE_MODEL_PATH

from gui.core.json_settings import Settings

UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)

SAVE_PREDICTIONS_DIR = os.path.join(os.getcwd(), "predictions")


class UtilityFunctions:
    

    def copy_dir(source_folder , progress_bar=None, destination_folder=DESTINATION_DIR):
        
        DIR_NAME = f"{datetime.now().strftime('%d%m%Y__%H%M%S')}"
        DIR_path = os.path.join(destination_folder, DIR_NAME)
        os.makedirs(DIR_path, exist_ok=True)

        Functions.current_destination_dir = DIR_path
        try:

            file_names = os.listdir(source_folder)

            total_size = len(file_names)

            for i, file_name in enumerate(file_names):
                src_file = os.path.join(source_folder, file_name)
                dst_file = os.path.join(Functions.current_destination_dir, file_name)
                # Copy the entire folder recursively
                shutil.copyfile(src_file, dst_file)

                if progress_bar:
                    current_progress = (i+1)/total_size * 100
                    progress_bar.set_value(int(current_progress))

            print(f"Folder '{source_folder}' copied to '{Functions.current_destination_dir}' successfully.")

        except Exception as e:
            print(f"Error: {e}")




# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:

    current_destination_dir = None
    save_model_path = None
    yolo = None
    save_predictions_dir = SAVE_PREDICTIONS_DIR

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image
    

    def remove_uploaded_files(setup_window):
        pass


    def upload_folder(setup_window):
        UtilityFunctions.copy_dir(
            source_folder=setup_window.btn_next.src_folder,
            progress_bar=setup_window.circular_bar_load_img
        )

    
    def start_training_yolo8(progress_bar):
        yolo = YOLO8Functions(data_dir=Functions.current_destination_dir)
        Functions.yolo = yolo
        t1 = threading.Thread(target=yolo.train)
        t1.start()
        while t1.is_alive():
            yolo.check_status(progress_bar)
            time.sleep(1)
        Functions.save_model_path = yolo.get_custom_model_path()

    
    def start_training_yolo5(progress_bar):
        yolo = YOLO5Functions(data_dir=Functions.current_destination_dir)

        Functions.yolo = yolo

        t1 = threading.Thread(target=yolo.train)
        t1.start()
        while t1.is_alive():
            yolo.check_status(progress_bar)
            time.sleep(1)
        Functions.save_model_path = yolo.get_custom_model_path()


    def start_training(setup_window, status):
        # first two conditions check if the data is uploaded
        if hasattr(setup_window.btn_next, "src_folder"):
            if setup_window.btn_next.src_folder:
                if setup_window.btn_yolo8.isChecked():
                    Functions.start_training_yolo8(setup_window.circular_bar_train_model)
                elif setup_window.btn_yolo5.isChecked():
                    Functions.start_training_yolo5(setup_window.circular_bar_train_model)
                else:
                    print(f"SELECT AT LEAST ONE MODEL.")
            
        else:
            print("No data folder selected.")
        status[0] = False
        


    def get_save_model_path():
        if Functions.save_model_path:
            return str(Functions.save_model_path)
        else:
            return "No current model found."
        
    
    def predict_image_yolo(img_file_path, selected_model_path):

        model = YOLO(selected_model_path)
        os.makedirs(Functions.save_predictions_dir, exist_ok=True)
        prediction = model(img_file_path)
        save_path = os.path.join(Functions.save_predictions_dir, os.path.basename(img_file_path))
        prediction[0].save(filename=save_path)

        print(f"Prediction results saved to : {Functions.save_predictions_dir}")
        return save_path
    

    def get_available_models():
        models = list()
        models5 = YOLO5Functions.get_available_models()
        models8 = YOLO8Functions.get_available_models()
        models = models5 + models8
        return models






