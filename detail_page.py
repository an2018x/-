################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,QImage, QRadialGradient)
from PySide2.QtWidgets import *
import cv2
# GUI FILE
from ui_main2 import Ui_MainWindow

# # IMPORT FUNCTIONS
# from ui_functions2 import *



class DetailPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
#        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            # if UIFunctions.returnStatus() == 1:
            #     UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            try:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            except:
                return
        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        #UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def setInfo(self,dic):
        cvImg=self.ui.cv_imread(dic['save_path'])
        height, width, channel = cvImg.shape
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        bytesPerLine = 3 * width
        qImg = QPixmap(QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888))
        pixsize=QSize(int(self.ui.frame_pic.width()),int(self.ui.frame_pic.height()))
        scaledPixmap = qImg.scaled(pixsize, Qt.KeepAspectRatio);
        self.ui.label_picture.setPixmap(scaledPixmap)
        self.ui.label_info_1.setPlainText("招牌：\n"+dic.get('brand','None'))
        self.ui.label_info_2.setPlainText("电话：\n"+str(dic.get('tel','None')))
        self.ui.label_info_3.setPlainText("其他：\n"+str(dic.get('more','None')))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = DetailPage()
#     sys.exit(app.exec_())
