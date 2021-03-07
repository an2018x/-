from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,QThread)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os


class SignalInfo(QtCore.QObject):
    sinInfo=QtCore.Signal(dict)

class ProgressInfo(QtCore.QObject):
    proInfo=QtCore.Signal(int)

class MyThread(QThread):
    def __init__(self,d,dir,config):
        self.signalInfo=SignalInfo()
        self.progressInfo=ProgressInfo()
        self.d=d
        self.config=config
        self.dir=dir
        super(MyThread,self).__init__()


    def run(self):
        if os.path.isdir(self.dir):
            self.d.detectDir(self.dir,self.config,self.signalInfo,self.progressInfo)
        else:

            return self.d.detectFile(self.dir,self.config,self.signalInfo,self.progressInfo)

