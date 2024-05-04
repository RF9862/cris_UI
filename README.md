
### Installation

First clone the repo. <br>
Create virtual env. (optional) <br>
Then install necessary libraries:
```
pip install -r requirements.txt
```
## IMPORTANT
After installing the requirements.txt, run:
```
python3 customise_ultralytics/modify_trainer.py
```
<br>
Then run main.py file as usual.

### Info
- The ultralytics package is modified to run the code. 
- The trainer module in the ultralytics package is replaced with the custom module.
- This is done to get the progress bar status while training process. So that it can be displayed in the training part of the UI. 

### Training data preparation
- The folder used to train the model should contain two folders named: images/ and labels/ and also a file named "classes.txt" where class names should be specified one by one on each line.
- e.g. classes.txt can look like:
    ```
    dog
    cat
    bird
    ```
- 
### Folder Descriptions

- **images/**: This directory is for storing your image files. Place all your image data in this folder. 

- **labels/**: Store your label files or annotations in this directory. This could include text files or other formats depending on your project's requirements.

- **classes.txt**: This file contains a list of classes or categories used in your dataset. Each line represents a unique class name.

## Folder Structure for Uploading Data

```bash
├── folder_to_upload
│   ├── images
│   │   ├── (image files to upload)
│   ├── labels
│   │   ├── (corresponding labels)
│   └── classes.txt

```

## ERRORS:
1. If you get error related to CUDA even if a cuda device is available, please try:
```
sudo rmmod nvidia_uvm
sudo modprobe nvidia_uvm
```
and then try again.
