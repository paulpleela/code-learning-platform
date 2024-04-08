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
from PySide6.QtCore import Qt

import requests 

class Dashboard(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.name = []
        self.complete = []
        self.number_of_total = []
        self.username = username
        
        response = requests.get(f"http://127.0.0.1:8000/dashboard/checkUser/{self.username}")
        print(self.username , response)
        if response.status_code == 200:
            data = response.json()
            print(data)
            if data["role"] == 'student':
                self.updateStudentAPI()
            elif data["role"] == 'teacher':
                self.updateTeacherAPI()
        print(self.name, self.complete, self.number_of_total)
        
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
            if self.number_of_total[self.index] == 0:
                bar.setValue(0)
            else:
                bar.setValue(self.complete[self.index]/self.number_of_total[self.index] * 100)
            bar.setAlignment(Qt.AlignCenter) 
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
    
    def updateStudentAPI(self):
        response = requests.get(f"http://127.0.0.1:8000/dashboard/student/{self.username}")
        course_nameList = []
        totalFinished = []
        totalModule = []
        if response.status_code == 200:
            data = response.json()
            print(data)
            course_nameList = data["dashboard"]["courseNameList"]
            totalFinished = data["dashboard"]["totalCompletedModules"]
            totalModule = data["dashboard"]["totalModules"]
        
        self.name = course_nameList
        self.complete = totalFinished
        self.number_of_total = totalModule
    
    def updateTeacherAPI(self):
        response = requests.get(f"http://127.0.0.1:8000/dashboard/teacher/{self.username}")
        course_nameList = []
        totalFinished = []
        totalModule = []
        if response.status_code == 200:
            data = response.json()
            print(data)
            course_nameList = data["dashboard"]["courseNameList"]
            totalFinished = data["dashboard"]["totalFinishedStudents"]
            totalModule = data["dashboard"]["totalStudents"]
        
        self.name = course_nameList
        self.complete = totalFinished
        self.number_of_total = totalModule
        
    def updateUI(self):
        # Clear existing course buttons
        # for button in self.course_buttons:
        #     button.deleteLater()
        for i in reversed(range(self.gridLayout.count())):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.gridLayout.removeItem(self.verticalSpacer)
        
        self.buttons = []
        self.buttons = []
        #Update API
        response = requests.get(f"http://127.0.0.1:8000/dashboard/checkUser/{self.username}")
        
        if response.status_code == 200:
            data = response.json()
            if data["role"] == 'student':
                self.updateStudentAPI()
            elif data["role"] == 'teacher':
                self.updateTeacherAPI()
                
        self.index = 0
        # Re-create course buttons
        for _ in range(len(self.name)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"pushButton_{self.index + 1}")
            button.setText(self.name[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.buttons.append(button)
            
            bar = QProgressBar(self.scrollAreaWidgetContents)
            if self.number_of_total[self.index] == 0:
                bar.setValue(0)
            else:
                bar.setValue(self.complete[self.index]/self.number_of_total[self.index] * 100)
            bar.setAlignment(Qt.AlignCenter) 
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
            # print(i)
            self.index += 1
        # makes verticleSpacer
        self.gridLayout.addItem(self.verticalSpacer, self.index, 1, 1, 1)




