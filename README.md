
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

