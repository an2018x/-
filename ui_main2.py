# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maindBzWaM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QImage,
    QRadialGradient)
from PySide2.QtWidgets import *
import cv2
import numpy as np


class Ui_MainWindow(object):
    def cv_imread(self,file_path):
        cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
        return cv_img
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        #self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
#         self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
# "border-radius: 10px;")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(41,45,62,255), stop:0.521368 rgba(41,45,62, 255));\n"
"border-radius: 10px;")

        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none; font-family: 等线;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(210, 231, 195);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)


        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.verticalLayoutX = QVBoxLayout(self.frame_infos)
        self.verticalLayoutX.setSpacing(10)
        self.verticalLayoutX.setObjectName(u"verticalLayoutX")
        self.verticalLayoutX.setAlignment(Qt.AlignCenter)
        self.frame_pic = QFrame(self.frame_infos)
        # self.frame_pic.setStyleSheet(u"QFrame{\n"
        # "	border: 5px solid rgb(60, 231, 195);\n"
        # "}\n"
        # "QFrame:hover {\n"
        # "	border: 5px solid rgb(105, 95, 148);\n"
        # "}")
        self.frame_pic.setObjectName(u"frame_pic")
        
        self.frame_pic.setMinimumSize(QSize(1200, 450))
        self.frame_pic.setMaximumSize(QSize(1200, 450))
        self.frame_pic.setFrameShape(QFrame.StyledPanel)
        self.frame_pic.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_6.setAlignment(Qt.AlignCenter)
        #self.verticalLayout_6.setContentsMargins(10, 50, 10, 50)

        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)




        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(8)






        self.label_picture = QLabel(self.frame_pic)
        self.label_picture.resize(self.frame_pic.width(),self.frame_pic.height())
        self.label_picture.setObjectName(u"label_picture")
        #self.label_picture.setText("图片")
        # font5 = QFont()
        # font5.setFamily(u"Roboto")
        # font5.setPointSize(10)
        # self.label_picture.setFont(font5)
        self.label_picture.setStyleSheet("color: rgb(128, 102, 168);")
        #self.label_picture.setAlignment(Qt.AlignCenter)





        #self.verticalLayout_6.addWidget(self.label_picture)



        self.verticalLayoutX.addWidget(self.frame_pic)

        self.frame_inform = QFrame(self.frame_infos)
        self.frame_inform.setObjectName(u"frame_circle_2")
        self.frame_inform.setMinimumSize(QSize(1120, 180))
        self.frame_inform.setMaximumSize(QSize(1120, 180))
        self.frame_inform.setFrameShape(QFrame.StyledPanel)
        self.frame_inform.setFrameShadow(QFrame.Raised)
        font=QFont("等线",10,60)
        
        self.horizontalLayoutInfor=QHBoxLayout(self.frame_inform)
        #self.horizontalLayoutInfor.setAlignment(Qt.AlignHCenter)
        self.label_info_1=QPlainTextEdit(self.frame_inform)
        self.label_info_1.setFont(font)
        self.label_info_1.setMaximumSize(QSize(300,120))
        self.label_info_1.setMinimumSize(QSize(300,120))
        self.label_info_1.setStyleSheet(u"color: rgb(220, 220, 220);\n"
        "font-family:等线;\n"
        "padding:15px;\n"
        "background-color: rgb(33, 33, 75);\n"
        "border-radius: 10px;")
        self.label_info_1.setPlainText("招牌：")
        self.horizontalLayoutInfor.addWidget(self.label_info_1)

        self.label_info_2=QPlainTextEdit(self.frame_inform)
        self.label_info_2.setFont(font)
        self.label_info_2.setMaximumSize(QSize(300,120))
        self.label_info_2.setMinimumSize(QSize(300,120))
        self.label_info_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
        "font-family:等线;\n"
        "padding:15px;\n"
        "background-color: rgb(33, 33, 75);\n"
        "border-radius: 10px;")
        self.label_info_2.setPlainText("电话：")

        self.horizontalLayoutInfor.addWidget(self.label_info_2)

        self.label_info_3=QPlainTextEdit(self.frame_inform)
        self.label_info_3.setFont(font)
        self.label_info_3.setMaximumSize(QSize(300,120))
        self.label_info_3.setMinimumSize(QSize(300,120))
        self.label_info_3.setStyleSheet(u"color: rgb(220, 220, 220);\n"
        "font-family:等线;\n"
        "padding:15px;\n"
        "background-color: rgb(33, 33, 75);\n"
        "border-radius: 10px;")
        self.label_info_3.setPlainText("其他：")
        self.horizontalLayoutInfor.addWidget(self.label_info_3)
        self.horizontalLayoutInfor.setContentsMargins(0,0,0,0)
        self.horizontalLayoutInfor.setAlignment(Qt.AlignHCenter)
        self.horizontalLayoutInfor.setSpacing(100)
        self.verticalLayoutX.addWidget(self.frame_inform)


        self.verticalLayout_9.addWidget(self.frame_infos)

        self.frame_texts = QFrame(self.frame_content_home)
        self.frame_texts.setObjectName(u"frame_texts")
        self.frame_texts.setMinimumSize(QSize(600, 0))
        self.frame_texts.setMaximumSize(QSize(16777215, 100))
        self.frame_texts.setFrameShape(QFrame.StyledPanel)
        self.frame_texts.setFrameShadow(QFrame.Raised)


        self.verticalLayout_9.addWidget(self.frame_texts, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setGeometry(QRect(90, 70, 120, 80))
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font7 = QFont()
        font7.setFamily(u"Roboto")
        self.label_credits.setFont(font7)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"More", None))
#if QT_CONFIG(tooltip)
        # self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
#        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")

        #self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: Wanderson M. Pimenta", None))
    # retranslateUi

