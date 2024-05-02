import os
import random
from yaml import dump, load
import shutil
from datetime import datetime
import glob
from yolov5.src import config
from ultralytics import YOLO
import cv2



class YOLO5Functions:
    def __init__(self, data_dir, 
                 params = None,
                 model_path = config.YOLO8_MODEL_PATH,
                 save_model_dir = config.SAVE_MODEL_PATH, 
                 save_predictions_dir = config.SAVE_PREDICTIONS_DIR):
        
        self.data_dir = data_dir
        self.split_ratio = config.SPLIT_RATIO

        self.model_path = model_path

        self.save_model_dir = os.path.join(save_model_dir, os.path.basename(self.data_dir))

        self.custom_yaml_file_path = config.CUSTOM_YAML_PATH

        self.save_predictions_dir = save_predictions_dir

        if not params:
            raise Exception("No parameters found.")
        else :
            self.parameters = params

        self.device = params["device"]
        if self.device == "gpu":
            self.device = "cuda"

        self.split_data_into_train_val()

        self.create_custom_yaml_file()

        self.load_model()

        


    def create_custom_yaml_file(self):
        yaml_data = dict()

        yaml_data['path'] = self.data_dir
        yaml_data['train'] = self.train_data_dir
        yaml_data['val'] = self.val_data_dir

        yaml_data['names'] = self.parameters["class_names"]

        with open(self.custom_yaml_file_path, "w") as f:
            dump(yaml_data, f)

    
    def load_model(self):
        self.model = YOLO(self.model_path)


    
    def train(self):
        self.model = self.model.to(device=self.parameters["device"])

        print(f"\nUsing parameters : \n{self.parameters}")

        t_stamp = f"{datetime.now().strftime('%d%m%Y__%H%M%S')}"

        results = self.model.train(
            data=self.custom_yaml_file_path,
            epochs=self.parameters["epochs"],
            batch=self.parameters["batch"],
            name=f"{self.save_model_dir}/{self.parameters['name']}_yolo5_{t_stamp}"
        )

        self.results = results

    
    def predict(self, img_file_path):
        os.makedirs(self.save_predictions_dir, exist_ok=True)
        prediction = self.model(img_file_path)
        save_path = os.path.join(self.save_predictions_dir, os.path.basename(img_file_path))
        prediction[0].save(filename=save_path)

        print(f"Prediction results saved to : {self.save_predictions_dir}")
        return save_path
    

    def predict_video(self, video_path):
        os.makedirs(self.save_predictions_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        # Get the video frame properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Define the codec and create a VideoWriter object
        output_video_path = os.path.join(self.save_predictions_dir, os.path.basename(video_path))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec (adjust as needed)
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))


        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 tracking on the frame, persisting tracks between frames
                results = self.model.track(frame, persist=True)

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
    yolo = YOLO5Functions(data_dir=None)

    yolo.train()

