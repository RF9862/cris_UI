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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: 12px;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
    
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:checked {{	
	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #cd18ee, stop: 0.5 #cd18ee,
                                      stop: 0.8 #1886ee, stop:1 #1886ee);
}}
'''


class ToggleButton(QPushButton):
    def __init__(
    self, 
    text,
    radius,
    color,
    bg_color,
    bg_color_hover,
    bg_color_pressed,
    parent = None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        self.custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed
        )

        self.setStyleSheet(self.custom_style)
        self.setCheckable(True)
        self.setChecked(False)
        
        self.clicked.connect(self.toggle_state)

    def toggle_state(self):
        self.uncheck_other_buttons()
        if not self.isChecked():
            self.setChecked(False)
            
        else:
            self.setChecked(True)


    def uncheck_other_buttons(self):
        for button in self.parent().findChildren(ToggleButton):
            if button != self:
                button.setChecked(False)