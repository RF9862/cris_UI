# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesKkIsfL.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLayout, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1106, 591)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 621, 531))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_options = QFrame(self.frame_2)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setGeometry(QRect(60, 190, 521, 251))
        self.frame_options.setFrameShape(QFrame.NoFrame)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_options)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 10, 311, 41))
        self.verticalLayoutWidget = QWidget(self.frame_options)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 110, 160, 80))
        self.circular_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.circular_layout.setObjectName(u"circular_layout")
        self.circular_layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 121, 20))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 470, 131, 20))
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(180, 30, 372, 30))
        self.btn_layout_1 = QHBoxLayout(self.widget)
        self.btn_layout_1.setObjectName(u"btn_layout_1")
        self.btn_layout_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_layout_1.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(160, 460, 363, 30))
        self.btn_layout_3 = QHBoxLayout(self.widget1)
        self.btn_layout_3.setObjectName(u"btn_layout_3")
        self.btn_layout_3.setContentsMargins(0, 0, 0, 0)
        self.widget2 = QWidget(self.frame_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 110, 596, 30))
        self.btn_layout_2 = QHBoxLayout(self.widget2)
        self.btn_layout_2.setObjectName(u"btn_layout_2")
        self.btn_layout_2.setContentsMargins(0, 0, 0, 0)
        self.graphicsView1 = QGraphicsView(self.frame)
        self.graphicsView1.setObjectName(u"graphicsView1")
        self.graphicsView1.setGeometry(QRect(640, 100, 256, 192))
        self.graphicsView1.setFrameShape(QFrame.NoFrame)
        self.graphicsView2 = QGraphicsView(self.frame)
        self.graphicsView2.setObjectName(u"graphicsView2")
        self.graphicsView2.setGeometry(QRect(940, 380, 256, 192))
        self.graphicsView2.setFrameShape(QFrame.NoFrame)
        self.graphicsView3 = QGraphicsView(self.frame)
        self.graphicsView3.setObjectName(u"graphicsView3")
        self.graphicsView3.setGeometry(QRect(640, 380, 256, 192))
        self.graphicsView3.setFrameShape(QFrame.NoFrame)
        self.graphicsView4 = QGraphicsView(self.frame)
        self.graphicsView4.setObjectName(u"graphicsView4")
        self.graphicsView4.setGeometry(QRect(930, 100, 256, 192))
        self.graphicsView4.setFrameShape(QFrame.NoFrame)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(680, 70, 151, 17))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(950, 70, 151, 17))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(680, 350, 151, 17))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(970, 350, 151, 17))

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"250 images are required", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Select Model", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Select stream", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Stream Name A", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
    # retranslateUi

