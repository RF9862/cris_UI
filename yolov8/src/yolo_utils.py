import os
from yaml import dump, load
from yolov8.src import config
from ultralytics import YOLO



class YOLOFunctions:
    def __init__(self):
        self.model_path = config.YOLO8_MODEL_PATH
        self.train_data_dir = config.TRAIN_DATA
        self.val_data_dir = config.VAL_DATA
        self.save_model_dir = config.SAVE_MODEL_PATH

        self.custom_yaml_file_path = config.CUSTOM_YAML_PATH

        self.create_custom_yaml_file()

        self.load_model()
        self.define_parameters()

    def create_custom_yaml_file(self):
        yaml_data = dict()

        yaml_data['path'] = config.ROOT_DIR
        yaml_data['train'] = self.train_data_dir
        yaml_data['val'] = self.val_data_dir

        yaml_data['names'] = config.CLASS_NAMES

        with open(self.custom_yaml_file_path, "w") as f:
            dump(yaml_data, f)

    
    def load_model(self):
        self.model = YOLO(self.model_path)

    def define_parameters(self):
        param = dict()

        param["epochs"] = 1
        param["batch"] = 8
        param["name"] = "yolo8_custom"

        self.parameters = param

    
    def train(self):
        results = self.model.train(
            data=self.custom_yaml_file_path,
            epochs=self.parameters["epochs"],
            batch=self.parameters["batch"],
            name=f"{self.save_model_dir}/{self.parameters['name']}"
        )

        self.results = results




if __name__ == "__main__":
    yolo = YOLOFunctions()

    yolo.train()

