# ///////////////////////////////////////////////////////////////
#
# BY: ///
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
import os, sys
import shutil
import time
import glob
from datetime import datetime
import threading
import random
import cv2

import torch
import mimetypes

from ultralytics import YOLO
from yolo_src.yolo_utils import YOLOFunctions, YOLO5Functions
#from yolov8.src.config import SAVE_MODEL_PATH
from yolov5.detect import run as y5_detect

from gui.core.json_settings import Settings
current_directory = os.getcwd()

sys.path.insert(0, current_directory)
from constants import CRIS_MODEL
UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)

SAVE_PREDICTIONS_DIR = os.path.join(os.getcwd(), "predictions")


SAVE_MODEL_PATH = os.path.join(os.getcwd(), "models")

IMG_FILES_NAME = "images"
LABEL_FILES_NAME = "labels"
CLASSES_FILE_NAME = "classes.txt"


class UtilityFunctions:
    
    def extract_class_names(file_path):
        class_names = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    class_name = line.strip()
                    if class_name:  
                        class_names.append(class_name)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        return class_names



    def copy_dir(source_folder , progress_bar=None, destination_folder=DESTINATION_DIR):
        
        DIR_NAME = f"{datetime.now().strftime('%d%m%Y__%H%M%S')}"
        DIR_path = os.path.join(destination_folder, DIR_NAME)
        os.makedirs(DIR_path, exist_ok=True)

        Functions.current_destination_dir = DIR_path
        # source dir contains 2 dir : images/ and labels/ and 1 file: classes.txt
        try:

            source_img_folder = os.path.join(source_folder,IMG_FILES_NAME)
            source_label_folder = os.path.join(source_folder, LABEL_FILES_NAME)

            img_file_names = [os.path.join(source_img_folder, n) for n in os.listdir(source_img_folder)]
            label_file_names = [os.path.join(source_label_folder, n) for n in  os.listdir(source_label_folder)]

            classes_file = os.path.join(source_folder, CLASSES_FILE_NAME)

            Functions.CLASS_NAMES = UtilityFunctions.extract_class_names(classes_file)
            print(Functions.CLASS_NAMES)

            file_names = img_file_names + label_file_names

            total_size = len(file_names)

            for i, file_name in enumerate(file_names):
                src_file = os.path.join(source_folder, file_name)
                dst_file = os.path.join(Functions.current_destination_dir, os.path.basename(file_name))
                # Copy the entire folder recursively
                shutil.copyfile(src_file, dst_file)

                if progress_bar:
                    current_progress = (i+1)/total_size * 100
                    progress_bar.set_value(int(current_progress))

            print(f"Folder '{source_folder}' copied to '{Functions.current_destination_dir}' successfully.")

            return len(img_file_names)
        except Exception as e:
            raise e


    def gpu_available():
        status = torch.cuda.is_available()
        print(status)
        return status
    

    def is_video_file(path):
        return mimetypes.guess_type(path)[0].startswith("video/")

    def is_image_file(path):
        return mimetypes.guess_type(path)[0].startswith("image/")
    
    def get_available_models(save_models_dir = CRIS_MODEL):
        # CRISPATH = f"C:/Users/{getpass.getuser()}/.cris/model"
        #pt_files = [f for f in os.listdir(CRIS_MODEL) if (f.split('.')[-1].lower() in ['pt'])]       
        pattern = os.path.join(save_models_dir, "**", "best.pt")
        pt_files  = glob.glob(pattern, recursive=True)
        return pt_files





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
        setup_window.ui.load_pages.label_3.hide()
        setup_window.ui.load_pages.verticalLayoutWidget.show()          
        img_files_num = UtilityFunctions.copy_dir(
            source_folder=setup_window.btn_next.src_folder,
            progress_bar=setup_window.circular_bar_load_img
        )
        setup_window.ui.load_pages.label_3.show()
        setup_window.ui.load_pages.label_3.setText(f"Successfully Uploaded {img_files_num} images")
        setup_window.ui.load_pages.verticalLayoutWidget.hide()          


    def start_training_yolo(yolo_version, params, progress_bar):
        yolo = YOLOFunctions(data_dir=Functions.current_destination_dir,
                              yolo_version=yolo_version,
                              params=params)

        Functions.yolo = yolo

        t1 = threading.Thread(target=yolo.train)
        t1.start()
        while t1.is_alive():
            yolo.check_status(progress_bar)
            time.sleep(1)
        Functions.save_model_path = yolo.get_custom_model_path()


    def start_training_yolo5(params, progress_bar):
        yolo = YOLO5Functions(data_dir=Functions.current_destination_dir,
                              params=params)

        Functions.yolo = yolo


        t1 = threading.Thread(target=yolo.train, args=(progress_bar,))
        t1.start()



    def start_training(setup_window, params, status):
        try:
            if setup_window.btn_yolo8.isChecked():
                Functions.start_training_yolo(8, params, setup_window.circular_bar_train_model)
            elif setup_window.btn_yolo5.isChecked():
                #Functions.start_training_yolo(5,params, setup_window.circular_bar_train_model)
                Functions.start_training_yolo5(params, setup_window.circular_bar_train_model)
            else:
                print(f"SELECT AT LEAST ONE MODEL.")
                setup_window.ui.load_pages.label_11.show()
                setup_window.ui.load_pages.label_11.setText("SELECT AT LEAST ONE MODEL.")
                setup_window.ui.load_pages.verticalLayoutWidget_3.hide()              

            status[0] = False
        except Exception as e:
            status[0] = False
            raise e
        


    def get_save_model_path():
        if Functions.save_model_path:
            return str(Functions.save_model_path)
        else:
            return "No current model found."
        
    def detect_yolo5(img_file_path, selected_model_path):


        save_path = y5_detect(weights=selected_model_path, source=img_file_path, conf_thres=0.1,
                              project=Functions.save_predictions_dir, name="", exist_ok=True)
        return save_path

    def predict_image_yolo(img_file_path, selected_model_path):

        model = YOLO(selected_model_path)
        os.makedirs(Functions.save_predictions_dir, exist_ok=True)
        prediction = model(img_file_path)
        save_path = os.path.join(Functions.save_predictions_dir, os.path.basename(img_file_path))
        prediction[0].save(filename=save_path)

        print(f"Prediction results saved to : {Functions.save_predictions_dir}")
        return save_path
    

    def predict_video(video_path, selected_model_path):

        model = YOLO(selected_model_path)

        os.makedirs(Functions.save_predictions_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        # Get the video frame properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Define the codec and create a VideoWriter object
        output_video_path = os.path.join(Functions.save_predictions_dir, os.path.basename(video_path))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec (adjust as needed)
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))


        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 tracking on the frame, persisting tracks between frames
                results = model.track(frame, persist=True)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Convert annotated frame from matplotlib to OpenCV format
                annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

                # Write the annotated frame to the output video
                out.write(annotated_frame)
            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object, VideoWriter, and close the display window
        cap.release()
        out.release()

        # Print a message when video processing is complete
        print(f"Annotated video saved to: {output_video_path}")
        return output_video_path
    


    def validate_params(setup_window):
        epochs = setup_window.ui.load_pages.epoch_option.text()
        batch = setup_window.ui.load_pages.batch_option.text()
        device = setup_window.ui.load_pages.gpu_option.currentText()
        if device == "gpu":
            if not UtilityFunctions.gpu_available():
                print("No cuda device found.")
                return None
            
            device = "cuda"

        model_name = setup_window.ui.load_pages.model_name_option.toPlainText()
        class_names = Functions.CLASS_NAMES

        if not all([epochs, batch, model_name, class_names]):
            print([epochs, batch, model_name, class_names])
            return None
        

        params = dict()
        params["epochs"] = int(epochs)
        params["batch"] = int(batch)
        params["device"] = device
        params["name"] = model_name
        params["class_names"] = class_names
        return params




