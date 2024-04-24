# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_imagescaisvQ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from qt_core import *

class Ui_TRAIN(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(651, 478)
        self.frame_load_images = QFrame(Form)
        self.frame_load_images.setObjectName(u"frame_load_images")
        self.frame_load_images.setGeometry(QRect(100, 80, 471, 321))
        self.frame_load_images.setFrameShape(QFrame.NoFrame)
        self.frame_load_images.setFrameShadow(QFrame.Raised)
        self.frame_circular = QFrame(self.frame_load_images)
        self.frame_circular.setObjectName(u"frame_circular")
        self.frame_circular.setGeometry(QRect(170, 120, 120, 80))
        self.frame_circular.setFrameShape(QFrame.NoFrame)
        self.frame_circular.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_load_images)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 321, 61))
        self.label_2 = QLabel(self.frame_load_images)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 240, 261, 17))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"250 images are required for model YOLO5", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Drag and drop the images", None))
    # retranslateUi

