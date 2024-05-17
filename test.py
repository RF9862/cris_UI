
import torch
import pickle
# Load the pre-trained model from the .pt file
model = torch.load('best.pt')  # Replace 'yolov8_model.pt' with the actual name of your .pt file

# Extract and store the model's state_dict in the data["yolo8_data"] field
model["cris"] = "111"


# Save the updated data to a .cris file
with open('your_file_name.cris', 'wb') as file:
    pickle.dump(model, file)

print(".cris file with the YOLOv8 data loaded from the .pt file has been created.")
