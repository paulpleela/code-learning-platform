# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_item.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QGridLayout, QLabel)

from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui, QtWidgets

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name = ['list1', 'list2', 'list3']
        self.complete = [2 , 5 , 3]
        self.number_of_module = [3, 5 , 8]
        self.buttons = []
        self.index = 0
        
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 489))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        
        # for loop making pushButton and Label
        for _ in range(len(self.name)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"pushButton_{self.index + 1}")
            button.setText(self.name[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.buttons.append(button)
            
            bar = QProgressBar(self.scrollAreaWidgetContents)
            bar.setValue(self.complete[self.index]/self.number_of_module * 100)
            bar.setStyleSheet('''   QProgressBar {
                                    border: solid grey;
                                    border-radius: 15px;
                                    color: black;
                                    }
                                    QProgressBar::chunk 
                                    {
                                    background-color: #05B8CC;
                                    border-radius :15px;
                                    }      ''')
            self.gridLayout.addWidget(bar , self.index , 1 ,  1, 1)
            
            self.index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        ############################################

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        QMetaObject.connectSlotsByName(Form)
    # setupUi


