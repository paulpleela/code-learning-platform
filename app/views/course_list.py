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

import requests

class Course_list(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username

        response = requests.get("http://127.0.0.1:8000/api/student/course_list", params={"username": username})

        course_names = []

        if response.status_code == 200:
                data = response.json()
                course_names_dict = data.get("course_names", {})
                course_names = list(course_names_dict.values())


        self.course = course_names
        self.buttons = []
        self.index = 0
        
        self.delete_buttons = {}  
        
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
        for _ in range(len(self.course)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"pushButton_{self.index + 1}")
            button.setText(self.course[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.buttons.append(button)
            
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f"label_{self.index + 1}")
            label.setText("Complete?")
            self.gridLayout.addWidget(label, self.index, 1, 1, 1)
            
            delete = QPushButton(self.scrollAreaWidgetContents)
            delete.setObjectName(f"delete_{self.index + 1}")
            delete.setText('Leave')
            self.delete_buttons[delete]  = self.index
            delete.clicked.connect(self.delete_course)
            
            self.index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        ############################################

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.enroll_btn = QPushButton(Form)
        self.enroll_btn.setObjectName(u"enroll_btn")
        self.enroll_btn.setGeometry(QRect(520, 510, 181, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 510, 391, 31))
        
        # self.enroll_btn.clicked.connect(self.enroll_course)
        self.enroll_btn.setText('Enroll Course')

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    def delete_course(self):
        sender_button = self.sender()
                
        position = None
        if sender_button in self.delete_buttons:
            position = self.delete_buttons[sender_button]
        
        if position != None:
            for j in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(position, j)
                if item:
                    widget = item.widget()
                    self.gridLayout.removeWidget(widget)
                    widget.deleteLater()
            del self.delete_buttons[sender_button]

    # def enroll_course(self):
    #     self.gridLayout.removeItem(self.verticalSpacer)
    #     button = QPushButton(self.scrollAreaWidgetContents)
    #     self.gridLayout.addWidget(button, self.index, 0, 1, 1)
    #     button.setText(self.lineEdit.text())
    #     self.buttons.append(button)
        
    #     label = QLabel(self.scrollAreaWidgetContents)
    #     label.setObjectName(f"label_{self.index+1}")
    #     label.setText(QCoreApplication.translate("Form", u"Complete?", None))

    #     self.gridLayout.addWidget(label, self.index, 1, 1, 1)
        
    #     self.index += 1

    #     self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
