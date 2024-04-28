import os
import random
from yaml import dump, load
import shutil
import glob
from yolov8.src import config
from ultralytics import YOLO



class YOLO8Functions:
    def __init__(self, data_dir, 
                 model_path = config.YOLO8_MODEL_PATH,
                 save_model_dir = config.SAVE_MODEL_PATH,
                 save_predictions_dir = config.SAVE_PREDICTIONS_DIR):
        
        self.data_dir = data_dir
        self.split_ratio = config.SPLIT_RATIO

        self.model_path = model_path

        self.save_model_dir = os.path.join(save_model_dir, os.path.basename(self.data_dir))

        self.custom_yaml_file_path = config.CUSTOM_YAML_PATH

        self.save_predictions_dir = save_predictions_dir

        self.split_data_into_train_val()

        self.create_custom_yaml_file()

        self.load_model()
        self.define_parameters()

    def create_custom_yaml_file(self):
        yaml_data = dict()

        yaml_data['path'] = self.data_dir
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

 


    def predict(self, img_file_path):
        os.makedirs(self.save_predictions_dir, exist_ok=True)
        prediction = self.model(img_file_path)
        save_path = os.path.join(self.save_predictions_dir, os.path.basename(img_file_path))
        prediction[0].save(filename=save_path)

        print(f"Prediction results saved to : {self.save_predictions_dir}")
        return save_path
    

    
    
    def split_data_into_train_val(self):
        
        train_dir = os.path.join(self.data_dir, "train")
        val_dir = os.path.join(self.data_dir, "val")


        file_names = [os.path.basename(fname).split(".")[0] for fname in os.listdir(self.data_dir)]
        file_names = list(set(file_names))
        random.shuffle(file_names)

        split_index = int(len(file_names) * self.split_ratio)

        # Split files into train and val sets
        train_file_names = file_names[:split_index]
        val_file_names = file_names[split_index:]

        train_files, val_files = list(), list()
        for file in train_file_names:
            train_files.append(f"{file}.jpg")
            train_files.append(f"{file}.txt")
        for file in val_file_names:
            val_files.append(f"{file}.jpg")
            val_files.append(f"{file}.txt")

        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(val_dir, exist_ok=True)

        # Move train files to train directory
        for file in train_files:
            src_path = os.path.join(self.data_dir, file)
            dest_path = os.path.join(train_dir, file)
            shutil.move(src_path, dest_path)

        # Move val files to val directory
        for file in val_files:
            src_path = os.path.join(self.data_dir, file)
            dest_path = os.path.join(val_dir, file)
            shutil.move(src_path, dest_path)

        self.train_data_dir = train_dir
        self.val_data_dir = val_dir

        print(f"Data split and moved successfully. Train: {len(train_files)}, Validation: {len(val_files)}")


    
    def check_status(self, progress_bar=None):
        try:
            current_epoch = find_current_epoch(self.model.trainer.pbar.desc)
            prev_progress = (current_epoch-1) / self.parameters["epochs"] * 100
            current_progress = (self.model.trainer.pbar.n / self.model.trainer.pbar.total *100) / self.parameters['epochs']
            progress = prev_progress+current_progress
            #print(f"\n\n\n{prev_progress+current_progress}")
            if progress_bar:
                progress_bar.set_value(int(progress))
            
        except Exception as e:
            pass

    
    def get_custom_model_path(self):
        return self.results.save_dir if self.results.save_dir else None
    

       
    def get_available_models(save_models_dir = config.SAVE_MODEL_PATH):
        pattern = os.path.join(save_models_dir, "**", "best.pt")
        pt_files  = glob.glob(pattern, recursive=True)
        return pt_files





import re
def find_current_epoch(description):
    pattern = r"\b\d+/\d+\b"
    x = re.findall(pattern, description)[0]
    current_epoch = int(x.split("/")[0])
    return current_epoch




if __name__ == "__main__":
    yolo = YOLO8Functions()

    yolo.train()

