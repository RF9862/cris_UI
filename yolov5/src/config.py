
import os
import shutil

#from gui.core.json_settings import Settings


ROOT_DIR = os.getcwd()

#UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
UPLOAD_DATA_DIR_NAME = "UPLOAD"
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)


SPLIT_RATIO = 0.8

CUSTOM_YAML_PATH = os.path.join(ROOT_DIR, "yolov5", "data.yaml")

YOLO8_MODEL_PATH = os.path.join(ROOT_DIR, "yolov5", "yolov5s.pt") # yolov8/yolov8n.pt

SAVE_MODEL_PATH = os.path.join(ROOT_DIR, "yolov5", "runs")

SAVE_PREDICTIONS_DIR = os.path.join(ROOT_DIR, "yolov5", "predictions")

CLASS_NAMES = ["pothole"]


