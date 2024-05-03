
import os
import shutil
import getpass
import sys
current_directory = os.getcwd()
sys.path.insert(0, current_directory)
from constants import CRIS_MODEL
#from gui.core.json_settings import Settings


ROOT_DIR = os.getcwd()

USER_DIR = os.getcwd()  # replace it with your path to save models

#UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
UPLOAD_DATA_DIR_NAME = "UPLOAD"
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)

SPLIT_RATIO = 0.8

CUSTOM_YAML_PATH = os.path.join(ROOT_DIR, "yolo_src", "data.yaml")

YOLO8_MODEL_PATH = os.path.join(ROOT_DIR, "yolov8", "yolov8n.pt") 

YOLO5_MODEL_PATH = os.path.join(ROOT_DIR, "yolov5", "yolov5s.pt") 

SAVE_MODEL_PATH = os.path.join(ROOT_DIR, CRIS_MODEL)

SAVE_PREDICTIONS_DIR = os.path.join(ROOT_DIR, "predictions")


