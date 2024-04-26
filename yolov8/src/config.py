
import os
import shutil

#from gui.core.json_settings import Settings


ROOT_DIR = os.getcwd()

#UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
UPLOAD_DATA_DIR_NAME = "UPLOAD"
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)


TRAIN_DATA = DESTINATION_DIR
VAL_DATA = os.path.join(os.getcwd(), "val")

CUSTOM_YAML_PATH = os.path.join(ROOT_DIR, "yolov8", "data.yaml")

YOLO8_MODEL_PATH = os.path.join(ROOT_DIR, "yolov8", "yolov8n.pt") # yolov8/yolov8n.pt

SAVE_MODEL_PATH = os.path.join(ROOT_DIR, "yolov8", "runs")

CLASS_NAMES = ["pothole"]


