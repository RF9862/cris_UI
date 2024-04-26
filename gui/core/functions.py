# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import shutil

from gui.core.json_settings import Settings

UPLOAD_DATA_DIR_NAME = Settings().items["upload_dir_name"]
DESTINATION_DIR = os.path.join(os.getcwd(), UPLOAD_DATA_DIR_NAME)



# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image
    

    def copy_dir(source_folder , progress_bar=None, destination_folder=DESTINATION_DIR):
        # remove the folder
        shutil.rmtree(destination_folder)
        # CREATE THE DIR
        os.makedirs(DESTINATION_DIR, exist_ok=True)
        try:
            
            file_names = os.listdir(source_folder)

            total_size = len(file_names)

            for i, file_name in enumerate(file_names):
                src_file = os.path.join(source_folder, file_name)
                dst_file = os.path.join(destination_folder, file_name)
                # Copy the entire folder recursively
                shutil.copyfile(src_file, dst_file)

                if progress_bar:
                    current_progress = (i+1)/total_size * 100
                    progress_bar.set_value(int(current_progress))

            
            print(f"Folder '{source_folder}' copied to '{destination_folder}' successfully.")

        except Exception as e:
            print(f"Error: {e}")
