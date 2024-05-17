# ///////////////////////////////////////////////////////////////
#
# BY: ///
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
import threading
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys, getpass, datetime
import os
from functools import partial
import shutil
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from PySide6.QtMultimedia import QMediaPlayer

from gui.widgets.py_video_player.py_video_player import VideoPlayer

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from gui.widgets.py_push_button.py_toggle_button import ToggleButton
from gui.widgets.py_push_button.py_upload_button import UploadButton
from gui.widgets.py_combobox.py_combobox import PyComboBox

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *
from gui.core.functions import UtilityFunctions


current_directory = os.getcwd()

sys.path.insert(0, current_directory)
from constants import *

uploading_ongoing = [False]
training_ongoing = [False]



# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        }
    ]
     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        # self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        
        ###############################################33
        # yolo buttons

        ## YOLO 5 BUTTON 
        self.btn_yolo5 = ToggleButton(
            text="YOLO 5",
            radius=10,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.ui.load_pages.btn_layout_1.addWidget(self.btn_yolo5)
        
        ## YOLO 8 BUTTON 
        self.btn_yolo8 = ToggleButton(
            text="YOLO 8",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )

        self.ui.load_pages.btn_layout_1.addWidget(self.btn_yolo8)


        ############# SECOND PANEL BUTTONS ##########
        self.btn_load_images = ToggleButton(
            text="Load images",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_2.addWidget(self.btn_load_images)


        self.btn_start_training = ToggleButton(
            text="Start training",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_2.addWidget(self.btn_start_training)


        self.btn_save_model = ToggleButton(
            text="Save model",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_2.addWidget(self.btn_save_model)


        self.btn_test_model= ToggleButton(
            text="Test model",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_2.addWidget(self.btn_test_model)

        ############ Camera buttons ##############
        self.btn_camera_A= ToggleButton(
            text="Camera A",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_3.addWidget(self.btn_camera_A)

        self.btn_Drone_A= ToggleButton(
            text="Drone A",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_3.addWidget(self.btn_Drone_A)


        ##############################################
        # load images buttons

        self.btn_back= PyPushButton(
            text="Back",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_4.addWidget(self.btn_back)

        ## circular progress bar for uploading data
        self.circular_bar_load_img = PyCircularProgress(
            value=0, is_rounded=False, set_accuracy = False,
        )
        self.ui.load_pages.circular_layout.addWidget(self.circular_bar_load_img)

        # upload button
        self.btn_next = UploadButton(
            text="Upload",
            radius=8,
            type="folder",
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            circular_progress_bar=self.circular_bar_load_img
        )
        self.ui.load_pages.btn_layout_4.addWidget(self.btn_next)

        def uploadThread():
            self.ui.load_pages.label_3.hide()
            self.ui.load_pages.verticalLayoutWidget.show()
            
            up_1 = threading.Thread(target=Functions.upload_folder, args=(self,))
            up_1.start()
        self.btn_next.clicked.connect(
            # uploadThread
            partial(Functions.upload_folder, self)
            )


        ##################################################################
        # train model buttons

        self.btn_back_train = ToggleButton(
            text="Stop training",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            deactive=True,
        )
        self.ui.load_pages.btn_layout_7.addWidget(self.btn_back_train)


        self.btn_train = PyPushButton(
            text="Train",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        
        self.ui.load_pages.btn_layout_7.addWidget(self.btn_train)

        
        def trainThread(improve_accuracy:bool):
            # first two conditions check if the folder is uploaded already
            if not hasattr(self.btn_next, "src_folder"):
                self.ui.load_pages.label_11.show()
                self.ui.load_pages.label_11.setText("No data folder selected")
                self.ui.load_pages.verticalLayoutWidget_3.hide()
                print("No data uploaded.") 
            elif not self.btn_next.src_folder:
                print("No data uploaded.") 
                self.ui.load_pages.label_11.show()
                self.ui.load_pages.label_11.setText("No data folder selected")   
                self.ui.load_pages.verticalLayoutWidget_3.hide()             
            elif not training_ongoing[0]:  # check if some training process is already going on
                self.ui.load_pages.label_11.hide()
                self.ui.load_pages.verticalLayoutWidget_3.show()     
                self.btn_back_train.setDisabled(False)
                
                if not self.btn_yolo8.isChecked() and not self.btn_yolo5.isChecked():
                    print(f"SELECT AT LEAST ONE MODEL.")
                    return 

                params =  Functions.validate_params(self)
                if not params:
                    print("Please specify parameters.")
                    return
                
                
                training_ongoing[0] = True


                self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_back_train)
                self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_train)
                self.btn_back_train.setEnabled(False)
                self.btn_train.setEnabled(False)
                

                # disable the current parameters frame
                self.ui.load_pages.frame_train_model_param.setEnabled(False)
                self.ui.load_pages.frame_train_model_param.setVisible(False)


                # get the number of images
                files_num = int(len(os.listdir(self.btn_next.src_folder)) / 2)
                self.ui.load_pages.label_12.setText(f"On {files_num} images")

                # enable the training frame
                self.ui.load_pages.frame_train_model.setEnabled(True)
                self.ui.load_pages.frame_train_model.setVisible(True)
                
                t1 = threading.Thread(target=Functions.start_training, 
                                      args=(self,params, training_ongoing, improve_accuracy))
                t1.start()
                self.btn_train.setEnabled(True)
            
        self.btn_train.clicked.connect(
            partial(trainThread, False)
            )
        

        self.btn_improve_accuracy = PyPushButton(
            text="Improve Accuracy",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            
        )
        self.btn_improve_accuracy.hide()
        self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_improve_accuracy)

        self.btn_improve_accuracy.clicked.connect(
            partial(trainThread, True)
        )


        ##################################################################
        # Save/Name model buttons
        self.btn_show_path = PyPushButton(
            text="Save CRIS",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )
        self.ui.load_pages.btn_layout_8.addWidget(self.btn_show_path)
        
        # def update_show_model_path():
        #     model_path = Functions.get_save_model_path()
        #     self.ui.load_pages.label_14.setText(model_path)
        def save_cris_file():
            import geocoder
            model_name = self.ui.load_pages.model_name_option.toPlainText()
            g = geocoder.ip('me')
            cris_path = os.path.join(CRISPATH_LOC, model_name+".cris")
            now = datetime.datetime.now()
            with open(cris_path, 'w') as f:
                f.write(f"Model Name: {model_name}\n")
                f.write(f"Location: [{str(g.latlng[0]), str(g.latlng[1])}]\n")
                f.write(f"Time: {str(now)}\n")
            self.ui.load_pages.label_13.setText(f"Your AI model {model_name} is created and ready to use.")
            print(cris_path)
            print(g.latlng)
        def save_new_model():
            if self.ui.load_pages.label_13.text() != '<html><head/><body><p>Your AI model is not created to use yet</p></body></html>':
                import geocoder
                model_path = Functions.get_save_model_path()
                shutil.copyfile(model_path, os.path.join(CRIS_MODEL, "best.cris"))
                model_name = self.ui.load_pages.model_name_option.toPlainText()
                g = geocoder.ip('me')
                cris_loc = f"Location: {str(g.latlng[0]), str(g.latlng[1])}"
                if self.btn_yolo8.isChecked(): model_yolo = "Model YOLO8\n"
                else: model_yolo = "Model YOLO5\n"
                label13_txt = model_yolo  + f"Name {model_name}\n" + f"Location {cris_loc}"
                self.ui.load_pages.label_13.setText(f"Your AI model {model_name} is created and ready to use.\n\n"+label13_txt)
        self.btn_show_path.clicked.connect(save_new_model)
        ##################################################################

        self.circular_bar_test_model= PyCircularProgress(
            value=100, is_rounded=False, custom_text="SUCCESS",
            font_size=20, progress_color="#00ff7f"
        )
        #self.ui.load_pages.circular_layout_4.addWidget(self.circular_bar_save_model)

        ##################################################

        
        # self.btn_refresh_models = PyPushButton(
        #     text="Refresh",
        #     radius=8,
        #     color=self.themes["app_color"]["text_title"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_two"],
        #     bg_color_pressed=self.themes["app_color"]["dark_three"]
        # )
        # self.ui.load_pages.btn_layout_20.addWidget(self.btn_refresh_models)
        # def refresh_models():
        #     models = UtilityFunctions.get_available_models()
        #     self.ui.load_pages.select_models_list.addItems(models)
        # self.btn_refresh_models.clicked.connect(refresh_models)

        trained_models = UtilityFunctions.get_available_models()
        # self.combo_list = PyComboBox(
        #     radius=8,
        #     color=self.themes["app_color"]["text_title"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_two"],
        #     Items = trained_models,
        # )
        # self.ui.load_pages.btn_layout_20.addWidget(self.combo_list)

        ##################################################


        # Test model
        self.btn_upload_test = UploadButton(
            text="Upload",
            radius=8,
            type="file",
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            circular_progress_bar=self.circular_bar_test_model
        )
        self.ui.load_pages.btn_layout_9.addWidget(self.btn_upload_test)

        def show_image(show_file):

            self.ui.load_pages.video_frame.setVisible(False)
            self.ui.load_pages.video_frame.setEnabled(False)

            self.ui.load_pages.output_video_frame.setVisible(False)
            self.ui.load_pages.output_video_frame.setEnabled(False)

            self.ui.load_pages.graphicsView4.setVisible(False)
            self.ui.load_pages.graphicsView4.setEnabled(False)
            
            pixmap = QPixmap(show_file)
            # pixmap.scaled(128, 128, Qt.KeepAspectRatio)
            self.ui.load_pages.graphicsView1.setPixmap(pixmap)
            self.ui.load_pages.graphicsView1.show()       
        
        def show_video(show_file):
            self.ui.load_pages.graphicsView1.setVisible(False)
            self.ui.load_pages.graphicsView1.setEnabled(False)

            self.ui.load_pages.graphicsView4.setVisible(False)
            self.ui.load_pages.graphicsView4.setEnabled(False)

            self.ui.load_pages.output_video_frame.setVisible(False)
            self.ui.load_pages.output_video_frame.setEnabled(False)

            self.ui.load_pages.video_frame.setVisible(True)
            self.ui.load_pages.video_frame.setEnabled(True)


            videoplayer = VideoPlayer(show_file, parent=self.ui.load_pages.video_frame)
            videoplayer.resize(self.ui.load_pages.video_frame.frameSize())
            videoplayer.show()

        def show_input():
            show_file = self.btn_upload_test.files[0]
            if UtilityFunctions.is_image_file(show_file):
                show_image(show_file)
            elif UtilityFunctions.is_video_file(show_file):
                show_video(show_file)
            else:
                print(f"File format is not supported:{show_file}")


        self.btn_upload_test.clicked.connect(show_input) 

        #### predict button

        self.btn_test_submit = PyPushButton(
            text="Test",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.ui.load_pages.btn_layout_9.addWidget(self.btn_test_submit)

        def predict_image(save_file, selected_model):
            #self.ui.load_pages.graphicsView1_video.setEnabled(False)
            #self.ui.load_pages.graphicsView1_video.setVisible(False)
            self.ui.load_pages.output_video_frame.setVisible(False)
            self.ui.load_pages.output_video_frame.setEnabled(False)
            
            self.ui.load_pages.graphicsView4.setEnabled(True)
            self.ui.load_pages.graphicsView4.setVisible(True)

                        
            save_file = Functions.predict_image_yolo(self, save_file, selected_model)   
            print(save_file)
            if save_file != -1:       
                # save_file = Functions.detect_yolo5(save_file, selected_model)
                pixmap = QPixmap(save_file)
                self.ui.load_pages.graphicsView4.setPixmap(pixmap)
                self.ui.load_pages.graphicsView4.show()


        def predict_video_stream(save_file, selected_model):

            self.ui.load_pages.graphicsView4.setEnabled(False)
            self.ui.load_pages.graphicsView4.setVisible(False)

            self.ui.load_pages.output_video_frame.setVisible(True)
            self.ui.load_pages.output_video_frame.setEnabled(True)

            save_file = Functions.predict_video(save_file, selected_model)
            print(save_file)

            videoplayer = VideoPlayer(save_file, parent=self.ui.load_pages.output_video_frame)
            videoplayer.resize(self.ui.load_pages.output_video_frame.frameSize())
            videoplayer.show()

        def predict_file():
            try:
                files = self.btn_upload_test.files
            except:
                files = []
                self.ui.load_pages.label_17.setText("Upload test image first")
            if len(files) > 0:
                # selected_model = self.combo_list.currentText()
                #selected_model = os.path.join(CRIS_MODEL, self.combo_list.currentText())
                # selected_model =  self.combo_list.currentText()
                # selected_model = Functions.get_save_model_path()
                selcted_model_temp = os.path.join(CRIS_MODEL, "best.cris")
                selected_model = os.path.join(CRIS_MODEL, "best.pt")
                shutil.copyfile(selcted_model_temp, selected_model)
                # print(selected_model)
                
                file_path = files[0]
                if UtilityFunctions.is_video_file(file_path):
                    predict_video_stream(file_path, selected_model)
                elif UtilityFunctions.is_image_file(file_path):
                    predict_image(file_path, selected_model)
                else:
                    print(f"File format is not supported:{file_path}")


        self.btn_test_submit.clicked.connect(predict_file)


        ##################################################################

        #############################


        #################################################
        

        ##################################################

        self.circular_bar_train_model= PyCircularProgress(
            value=0, is_rounded=False
        )
        self.ui.load_pages.circular_layout_3.addWidget(self.circular_bar_train_model)

        


        # /////////////////////////// BUTTON FUNCTIONS //////////

        def clear_frame():
            self.ui.load_pages.frame_load_images.setEnabled(False)
            self.ui.load_pages.frame_load_images.setVisible(False)

            self.ui.load_pages.frame_train_model_param.setEnabled(False)
            self.ui.load_pages.frame_train_model_param.setVisible(False)

            self.ui.load_pages.frame_save_model.setEnabled(False)
            self.ui.load_pages.frame_save_model.setVisible(False)

            self.ui.load_pages.frame_test_model.setEnabled(False)
            self.ui.load_pages.frame_test_model.setVisible(False)

            self.ui.load_pages.frame_train_model.setEnabled(False)
            self.ui.load_pages.frame_train_model.setVisible(False)



        def set_load_images_page():
            clear_frame()
            if self.btn_load_images.isChecked():
                self.ui.load_pages.frame_load_images.setEnabled(True)
                self.ui.load_pages.frame_load_images.setVisible(True)

        self.btn_load_images.clicked.connect(set_load_images_page)


        def show_training_frame():
            self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_back_train)
            self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_train)
            self.ui.load_pages.btn_layout_7_train.addWidget(self.btn_improve_accuracy)
            

            # disable the current parameters frame
            self.ui.load_pages.frame_train_model_param.setEnabled(False)
            self.ui.load_pages.frame_train_model_param.setVisible(False)


            # get the number of images
            files_num = int(len(os.listdir(self.btn_next.src_folder)) / 2)
            self.ui.load_pages.label_12.setText(f"On {files_num} images")

            # enable the training frame
            #self.ui.load_pages.frame_train_model.setEnabled(True)
            self.ui.load_pages.frame_train_model.setVisible(True)

        def set_train_model_page():
            clear_frame()
            if not training_ongoing[0]:
                if self.btn_start_training.isChecked():
                    #self.ui.load_pages.frame_train_model.setEnabled(True)
                    #self.ui.load_pages.frame_train_model.setVisible(True)
                    self.ui.load_pages.btn_layout_7.addWidget(self.btn_back_train)
                    self.ui.load_pages.btn_layout_7.addWidget(self.btn_train)
                    self.ui.load_pages.frame_train_model_param.setEnabled(True)
                    self.ui.load_pages.frame_train_model_param.setVisible(True)
            else:
                show_training_frame()

        self.btn_start_training.clicked.connect(set_train_model_page)


        def set_save_model_page():
            clear_frame()
            if self.btn_save_model.isChecked():
                self.ui.load_pages.frame_save_model.setEnabled(True)
                self.ui.load_pages.frame_save_model.setVisible(True)

        self.btn_save_model.clicked.connect(set_save_model_page)



        def set_test_model_page():
            clear_frame()
            if self.btn_test_model.isChecked():
                self.ui.load_pages.frame_test_model.setEnabled(True)
                self.ui.load_pages.frame_test_model.setVisible(True)

        self.btn_test_model.clicked.connect(set_test_model_page)



        ######################################



        # ////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)