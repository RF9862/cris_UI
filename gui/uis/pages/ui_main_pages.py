# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesLTDyHW.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from PySide6.QtMultimediaWidgets import QVideoWidget


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        #MainPages.resize(1106, 591)


        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget(MainPages)
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

        self.frame_load_images = QFrame(self.frame_2)
        self.frame_load_images.setObjectName(u"frame_load_images")
        self.frame_load_images.setGeometry(QRect(60, 160, 521, 301))
        self.frame_load_images.setFrameShape(QFrame.NoFrame)
        self.frame_load_images.setFrameShadow(QFrame.Raised)

        self.frame_load_images.setEnabled(False)
        self.frame_load_images.setVisible(False)


        
        self.verticalLayoutWidget = QWidget(self.frame_load_images)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 
                                                    self.frame_load_images.frameSize().width(), 
                                                    self.frame_load_images.frameSize().height()))
        self.verticalLayoutWidget.hide()
        
        load_img_width = self.verticalLayoutWidget.frameSize().width() / 2
        x_pos_load_img = load_img_width / 2

        self.label_3 = QLabel(self.frame_load_images)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(x_pos_load_img, 100, load_img_width, 41))

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(x_pos_load_img, 210, load_img_width, 41))
        self.horizontalLayoutWidget = QWidget(self.frame_load_images)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(x_pos_load_img, 240, load_img_width, 49))
        self.btn_layout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.btn_layout_4.setObjectName(u"btn_layout_4")
        self.btn_layout_4.setContentsMargins(0, 0, 0, 0)

        self.circular_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.circular_layout.setObjectName(u"circular_layout")
        self.circular_layout.setContentsMargins(x_pos_load_img+30, 
                                                self.label_3.frameSize().height(), 0, 
                                                self.label_8.frameSize().height()+
                                                self.horizontalLayoutWidget.frameSize().height())


        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(x_pos_load_img, 210, load_img_width, 41))
        self.horizontalLayoutWidget = QWidget(self.frame_load_images)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 240, 321, 49))
        self.btn_layout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.btn_layout_4.setObjectName(u"btn_layout_4")
        self.btn_layout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 121, 20))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 490, 131, 20))
        self.groupBox_1 = QGroupBox(self.frame_2)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(10, 10, 571, 71))
        self.groupBox_1.setStyleSheet(u"")
        self.groupBox_1.setFlat(False)
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 99, 620, 60))
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 30, 372, 49))
        self.btn_layout_1 = QHBoxLayout(self.layoutWidget)
        self.btn_layout_1.setObjectName(u"btn_layout_1")
        self.btn_layout_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_layout_1.setContentsMargins(1, 1, 1, 1)
        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(150, 490, 363, 30))
        self.btn_layout_3 = QHBoxLayout(self.layoutWidget1)
        self.btn_layout_3.setObjectName(u"btn_layout_3")
        self.btn_layout_3.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget2 = QWidget(self.frame_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 110, 596, 40))
        self.btn_layout_2 = QHBoxLayout(self.layoutWidget2)
        self.btn_layout_2.setObjectName(u"btn_layout_2")
        self.btn_layout_2.setContentsMargins(0, 0, 0, 0)



        self.frame_train_model = QFrame(self.frame_2)
        self.frame_train_model.setObjectName(u"frame_train_model")
        self.frame_train_model.setGeometry(QRect(60, 160, 521, 301))
        self.frame_train_model.setFrameShape(QFrame.NoFrame)
        self.frame_train_model.setFrameShadow(QFrame.Raised)


        self.frame_train_model.setEnabled(False)
        self.frame_train_model.setVisible(False)


        self.verticalLayoutWidget_3 = QWidget(self.frame_train_model)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 
                                                    self.frame_train_model.frameSize().width(), 
                                                    self.frame_train_model.frameSize().height()-20))
        self.verticalLayoutWidget_3.hide()


        train_model_width = self.verticalLayoutWidget_3.frameSize().width() /2
        x_pos_train_model = train_model_width / 2

        self.label_11 = QLabel(self.frame_train_model)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(x_pos_train_model, 0, train_model_width, 41))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter) 


        self.label_12 = QLabel(self.frame_train_model)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(x_pos_train_model, 
                                        self.frame_train_model.frameSize().height() - 42, 
                                        train_model_width, 41))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        self.label_12.hide()


        self.circular_layout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.circular_layout_3.setObjectName(u"circular_layout_3")
        self.circular_layout_3.setContentsMargins(x_pos_load_img+30, 
                                                self.label_11.frameSize().height()+5, 0, 
                                                self.label_12.frameSize().height()+5)



        self.horizontalLayoutWidget_3_train = QWidget(self.frame_train_model)
        self.horizontalLayoutWidget_3_train.setObjectName(u"horizontalLayoutWidget_3_train")
        self.horizontalLayoutWidget_3_train.setGeometry(QRect(80, 240, 321, 49))

        self.btn_layout_7_train = QHBoxLayout(self.horizontalLayoutWidget_3_train)
        self.btn_layout_7_train.setObjectName(u"btn_layout_7")
        self.btn_layout_7_train.setContentsMargins(0, 0, 0, 0)


        ###############################################


        self.frame_train_model_param = QFrame(self.frame_2)
        self.frame_train_model_param.setObjectName(u"frame_train_model_param")
        self.frame_train_model_param.setGeometry(QRect(60, 160, 521, 301))
        self.frame_train_model_param.setFrameShape(QFrame.NoFrame)
        self.frame_train_model_param.setFrameShadow(QFrame.Raised)


        self.frame_train_model_param.setEnabled(False)
        self.frame_train_model_param.setVisible(False)



        self.label_param_1 = QLabel(self.frame_train_model_param)
        self.label_param_1.setObjectName(u"label_param_1")
        self.label_param_1.setGeometry(QRect(100, 0, 311, 41))
        self.verticalLayoutWidget_param_1 = QWidget(self.frame_train_model_param)
        self.verticalLayoutWidget_param_1.setObjectName(u"verticalLayoutWidget_param_1")
        self.verticalLayoutWidget_param_1.setGeometry(QRect(90, 50, 451, 161))

        self.epoch_option = QLineEdit()
        self.epoch_option.setValidator(QIntValidator())
        self.epoch_option.setText("3")

        self.batch_option = QLineEdit()
        self.batch_option.setValidator(QIntValidator())
        self.batch_option.setText("8")

        self.gpu_option = QComboBox()
        self.gpu_option.addItems(["cpu", "gpu"])

        self.model_name_option = QTextEdit()
        self.model_name_option.setText("custom_model")

        #self.class_names_option = QTextEdit()

        self.form_param = QFormLayout(self.verticalLayoutWidget_param_1)
        self.form_param.addRow("Epochs: ", self.epoch_option)
        self.form_param.addRow("Batch size:", self.batch_option)
        self.form_param.addRow("Device:", self.gpu_option)
        self.form_param.addRow("Model name:", self.model_name_option)
        #self.form_param.addRow("Class names :", self.class_names_option)

        self.horizontalLayoutWidget_param_1 = QWidget(self.frame_train_model_param)
        self.horizontalLayoutWidget_param_1.setObjectName(u"horizontalLayoutWidget_param_1")
        self.horizontalLayoutWidget_param_1.setGeometry(QRect(80, 240, 321, 49))
        self.btn_layout_7 = QHBoxLayout(self.horizontalLayoutWidget_param_1)
        self.btn_layout_7.setObjectName(u"btn_layout_7")
        self.btn_layout_7.setContentsMargins(0, 0, 0, 0)

        ################################################



        self.frame_save_model = QFrame(self.frame_2)
        self.frame_save_model.setObjectName(u"frame_save_model")
        self.frame_save_model.setGeometry(QRect(60, 160, 521, 301))
        self.frame_save_model.setFrameShape(QFrame.NoFrame)
        self.frame_save_model.setFrameShadow(QFrame.Raised)


        self.frame_save_model.setEnabled(False)
        self.frame_save_model.setVisible(False)


        self.label_13 = QLabel(self.frame_save_model)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 0, 400, 41))
        #self.verticalLayoutWidget_4 = QWidget(self.frame_save_model)
        #self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        #self.verticalLayoutWidget_4.setGeometry(QRect(120, 50, 251, 161))
        #self.circular_layout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        #self.circular_layout_4.setObjectName(u"circular_layout_4")
        #self.circular_layout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_save_model)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 60, 500, 100))
        self.label_14.setWordWrap(True)
        self.horizontalLayoutWidget_4 = QWidget(self.frame_save_model)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(80, 240, 321, 49))
        self.btn_layout_8 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.btn_layout_8.setObjectName(u"btn_layout_8")
        self.btn_layout_8.setContentsMargins(0, 0, 0, 0)




        self.frame_test_model = QFrame(self.frame_2)
        self.frame_test_model.setObjectName(u"frame_test_model")
        self.frame_test_model.setGeometry(QRect(60, 160, 521, 301))
        self.frame_test_model.setFrameShape(QFrame.NoFrame)
        self.frame_test_model.setFrameShadow(QFrame.Raised)


        self.frame_test_model.setEnabled(False)
        self.frame_test_model.setVisible(False)


        self.label_17 = QLabel(self.frame_test_model)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(100, 0, 360, 41))

        self.verticalLayoutWidget_5 = QWidget(self.frame_test_model)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(120, 50, 251, 161))
        #self.circular_layout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        #self.circular_layout_5.setObjectName(u"circular_layout_5")
        #self.circular_layout_5.setContentsMargins(0, 0, 0, 0)

        # self.select_models_list = QComboBox(self.verticalLayoutWidget_5)
        self.btn_layout_20 = QHBoxLayout(self.verticalLayoutWidget_5)
        self.btn_layout_20.setObjectName(u"btn_layout_20")
        self.btn_layout_20.setContentsMargins(0, 0, 0, 0)


        self.label_18 = QLabel(self.frame_test_model)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(90, 210, 381, 41))
        self.horizontalLayoutWidget_5 = QWidget(self.frame_test_model)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(80, 240, 321, 49))

        self.btn_layout_9 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.btn_layout_9.setObjectName(u"btn_layout_9")
        self.btn_layout_9.setContentsMargins(0, 0, 0, 0)
        


        self.label.raise_()
        self.label_2.raise_()
        self.groupBox_1.raise_()
        #self.groupBox_2.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.frame_load_images.raise_()
        self.frame_train_model.raise_()
        self.frame_save_model.raise_()
        self.frame_test_model.raise_()
        self.frame_train_model_param.raise_()



        self.graphicsView1 = QLabel(self.frame)
        self.graphicsView1.setObjectName(u"graphicsView1")
        self.graphicsView1.setGeometry(QRect(640, 100, 256, 192))
        self.graphicsView1.setFrameShape(QFrame.NoFrame)
        self.graphicsView1.setScaledContents(True)
        self.graphicsView1.setEnabled(False)
        self.graphicsView1.setVisible(False)


        self.graphicsView1_video = QVideoWidget(self.frame)
        self.graphicsView1_video.setObjectName(u"graphicsView1_video")
        self.graphicsView1_video.setGeometry(QRect(640, 100, 256, 192))
        self.graphicsView1_video.setEnabled(False)
        self.graphicsView1_video.setVisible(False)


        self.graphicsView2 = QLabel(self.frame)
        self.graphicsView2.setObjectName(u"graphicsView2")
        self.graphicsView2.setGeometry(QRect(940, 380, 256, 192))
        self.graphicsView2.setFrameShape(QFrame.NoFrame)
        self.graphicsView2.setScaledContents(True)
        self.graphicsView2.setEnabled(False)
        self.graphicsView2.setVisible(False)
        self.graphicsView3 = QLabel(self.frame)
        self.graphicsView3.setObjectName(u"graphicsView3")
        self.graphicsView3.setGeometry(QRect(640, 380, 256, 192))
        self.graphicsView3.setFrameShape(QFrame.NoFrame)
        self.graphicsView3.setScaledContents(True)
        self.graphicsView3.setEnabled(False)
        self.graphicsView3.setVisible(False)
        self.graphicsView4 = QLabel(self.frame)
        self.graphicsView4.setObjectName(u"graphicsView4")
        self.graphicsView4.setGeometry(QRect(930, 100, 256, 192))
        self.graphicsView4.setFrameShape(QFrame.NoFrame)
        self.graphicsView4.setScaledContents(True)
        self.graphicsView4.setEnabled(False)
        self.graphicsView4.setVisible(False)



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

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>250 images are required</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Drag and Drop or Select images</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Select Model", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Select stream", None))
        self.groupBox_1.setTitle("")
        self.groupBox_2.setTitle("")
        self.label_11.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Training started for YOLO</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>On 250 images</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Save trainned model and CRIS file</p></body></html>", None))
        #self.label_14.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Drag and Drop or Select images</p></body></html>", None))
        #self.label_14.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>path here.</p></body></html>", None))
        
        self.label_17.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Select model </p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Select images(.jpg) or video(.mp4)</p></body></html>", None))
        
        self.label_param_1.setText("Training parameters:")

        self.label_4.setText(QCoreApplication.translate("MainPages", u"Stream Name A", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Preview Stream", None))
    # retranslateUi

