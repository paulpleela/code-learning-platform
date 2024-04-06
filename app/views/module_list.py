# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course_list.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QStackedWidget, QMainWindow, QLineEdit)

from PySide6 import QtCore, QtGui, QtWidgets

class Module_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.module = ['mol1', 'mol2', 'mol3']
        self.cID = "abcdefgh"
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
        for _ in range(len(self.module)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"pushButton_{self.index + 1}")
            button.setText(self.module[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.buttons.append(button)
            
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f"label_{self.index + 1}")
            label.setText("Complete?")
            self.gridLayout.addWidget(label, self.index, 1, 1, 1)
            
            self.index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        self.return_2 = QPushButton(Form)
        self.return_2.setObjectName(u"return_2")
        self.return_2.setGeometry(QRect(30, 510, 131, 24))
        self.return_2.setText('<< Go Back')
        
        self.courseID = QLabel(Form)
        self.courseID.setText(f"courseID : {self.cID}")
        self.courseID.setGeometry(QRect(350, 520, 300, 24))
        ############################################

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

        QMetaObject.connectSlotsByName(Form)
    # setupUi
