
import os
import shutil


from ultralytics.engine import trainer


CUSTOMISE_ULTRALYTICS = "customise_ultralytics"
MODULES_TO_REPLACE_DIR = "modules_to_replace"

MODULES_DIR = os.path.join(os.getcwd(), CUSTOMISE_ULTRALYTICS, MODULES_TO_REPLACE_DIR)
TRAINER_FILE_NAME = "trainer.py"


def modify_ultralytics():
    try:
        src = os.path.join(MODULES_DIR, TRAINER_FILE_NAME)
        dst = trainer.__file__

        shutil.copyfile(src, dst)

        print(f"Copied : {src} to {dst}")

    except Exception as e:
        print(f"Could not customise ultralytics: {str(e)}")



if __name__ == "__main__":
    modify_ultralytics()
