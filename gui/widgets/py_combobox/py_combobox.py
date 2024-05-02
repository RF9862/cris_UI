# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};   
    border-radius: {_radius};    
    background-color: {_bg_color};
}}
QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: center right;
    width: 15px;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: {_radius};
    border-bottom-right-radius: {_radius};
}}
QComboBox:hover {{
    background-color: {_bg_color_hover};
}}
QComboBox::down-arrow {{
    image: url(down_arrow.png);
}}
'''

# PY COMBO BOX
# ///////////////////////////////////////////////////////////////
class PyComboBox(QComboBox):
    def __init__(
        self, 
        radius,
        color,
        bg_color,
        bg_color_hover,
        parent=None,
        Items=[]
    ):
        super().__init__()

        # SET PARAMETERS
        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover
        )
        self.setStyleSheet(custom_style)
        # self.setFixedWidth(width)
        self.addItems(Items)
    # def toggle_state(self):
    #     self.uncheck_other_buttons()
    #     if not self.isChecked():
    #         self.setChecked(False)
            
    #     else:
    #         self.setChecked(True)