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
class Teacher_Course_list(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username

        response = requests.get("http://127.0.0.1:8000/api/teacher/course_list", params={"username": username})
        print(response)
        course_names = []
        course_codes = []

        if response.status_code == 200:
                data = response.json()
                course_names_dict = data.get("course_names", {})
                course_names = list(course_names_dict.values())
                course_codes = list(course_names_dict.keys())

        self.course = course_names
        self.course_codes = course_codes
        self.course_buttons = []
        self.index = 0
        
        self.edit_buttons = {}
        
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
            button.setObjectName(f"course_{self.index + 1}")
            button.setText(self.course[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.course_buttons.append(button)
            
            edit = QPushButton(self.scrollAreaWidgetContents)
            edit.setObjectName(f"edit_{self.index + 1}")
            edit.setText('Edit')
            self.gridLayout.addWidget(edit, self.index, 1, 1, 1)
            self.edit_buttons[edit] = self.index
            
            delete = QPushButton(self.scrollAreaWidgetContents)
            delete.setObjectName(f"delete_{self.index + 1}")
            delete.setText('Delete')
            self.delete_buttons[delete]  = self.index
            
            # delete.clicked.connect(lambda i = i: self.delete_course(i))
            delete.clicked.connect(self.delete_course)
            
            self.gridLayout.addWidget(delete, self.index, 2, 1, 1)
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
        self.enroll_btn.setText('Add Course')

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def delete_course(self):
        sender_button = self.sender()                    
        position = None
        if sender_button in self.delete_buttons:
            position = self.delete_buttons[sender_button]
        print(position)
        if position != None:
            response = requests.delete(f"http://127.0.0.1:8000/course/{self.course_codes[position]}/{self.username}")

            if response.status_code == 200:
                data = response.json()
                success = data["success"]
                print(f"Deletion success: {success}")
                # code to remove from UI            
                if position != None:
                    for j in range(self.gridLayout.columnCount()):
                        item = self.gridLayout.itemAtPosition(position, j)
                        # item = self.gridLayout.itemAtPosition(row, j)
                        if item:
                            widget = item.widget()
                            self.gridLayout.removeWidget(widget)
                            widget.deleteLater()
                    del self.delete_buttons[sender_button]
                    # print(self.delete_buttons)
            else:
                print(f"Failed to delete course. Status code: {response.status_code}, Error: {response.text}")

    def updateAPI(self):
        response = requests.get("http://127.0.0.1:8000/api/teacher/course_list", params={"username": self.username})
        course_names = []
        course_codes= []

        if response.status_code == 200:
            data = response.json()
            course_names_dict = data.get("course_names", {})
            course_names = list(course_names_dict.values())
            course_codes = list(course_names_dict.keys())

        self.course = course_names
        self.course_codes = course_codes

    def renameCourse(self, index, newName):
        requests.put(f"http://127.0.0.1:8000/course/rename/{self.course_codes[index]}/{newName}")
