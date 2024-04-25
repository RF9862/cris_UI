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
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

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

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

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
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

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

        
        
        ############# YOLO 5 BUTTON ##########
        self.btn_yolo5 = ToggleButton(
            text="YOLO 5",
            radius=10,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )

        self.ui.load_pages.btn_layout_1.addWidget(self.btn_yolo5)
        
        """def print_check():
            if self.btn_yolo5.isChecked():
                print("Checked ....")
        self.btn_yolo5.clicked.connect(print_check)"""
        

        
        ############# YOLO 8 BUTTON ##########
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
            text="Save/Name model",
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


        ###########################

        self.btn_back= ToggleButton(
            text="Back",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )

        self.ui.load_pages.btn_layout_4.addWidget(self.btn_back)

        self.btn_next = ToggleButton(
            text="Next",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )


        self.ui.load_pages.btn_layout_4.addWidget(self.btn_next)


        ##################################################################

        self.btn_back_train = ToggleButton(
            text="Back",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )


        self.ui.load_pages.btn_layout_7.addWidget(self.btn_back_train)


        self.btn_train = ToggleButton(
            text="Train",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )


        self.ui.load_pages.btn_layout_7.addWidget(self.btn_train)





        ##################################################################

        self.btn_save = ToggleButton(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_title"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
        )


        self.ui.load_pages.btn_layout_8.addWidget(self.btn_save)


        ##################################################################






        ##################################################################

        #############################


        #################################################
        self.circular_bar_load_img = PyCircularProgress(
            value=40, is_rounded=False
        )
        self.ui.load_pages.circular_layout.addWidget(self.circular_bar_load_img)

        ##################################################

        self.circular_bar_train_model= PyCircularProgress(
            value=40, is_rounded=False
        )
        self.ui.load_pages.circular_layout_3.addWidget(self.circular_bar_train_model)

        ##################################################

        self.circular_bar_save_model= PyCircularProgress(
            value=100, is_rounded=False, custom_text="SUCCESS",
            font_size=20, progress_color="#00ff7f"
        )
        self.ui.load_pages.circular_layout_4.addWidget(self.circular_bar_save_model)


        
        
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