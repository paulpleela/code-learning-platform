# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Lesson_Quiz_list.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QMainWindow)

from PySide6 import QtCore, QtGui, QtWidgets
import requests
class Lesson_Quiz_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lessons = []
        self.cID = ""
        self.username = ""
        self.moduleIndex = None
        self.lesson_buttons = []
        self.lesson_index = 0
        
        self.quizzes = []
        self.quiz_status = []
        self.quiz_buttons = []
        self.quiz_index = 0
        
        self.setupUi(self)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        self.lesson_scroll = QScrollArea(Form)
        self.lesson_scroll.setObjectName(u"lesson_scroll")
        self.lesson_scroll.setGeometry(QRect(10, 10, 371, 491))
        self.lesson_scroll.setWidgetResizable(True)
        self.lesson_widget = QWidget()
        self.lesson_widget.setObjectName(u"lesson_widget")
        self.lesson_widget.setGeometry(QRect(0, 0, 369, 489))
        self.gridLayoutWidget = QWidget(self.lesson_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 371, 491))
        self.lesson_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.lesson_gridLayout.setObjectName(u"lesson_gridLayout")
        self.lesson_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lesson_gridLayout.setColumnStretch(0, 5)
        self.lesson_gridLayout.setColumnStretch(1, 1)
        self.lesson_scroll.setWidget(self.lesson_widget)
        
        self.return_2 = QPushButton(Form)
        self.return_2.setObjectName(u"return_2")
        self.return_2.setGeometry(QRect(30, 510, 131, 24))
        self.quiz_scroll = QScrollArea(Form)
        self.quiz_scroll.setObjectName(u"quiz_scroll")
        self.quiz_scroll.setGeometry(QRect(410, 10, 371, 491))
        self.quiz_scroll.setWidgetResizable(True)
        self.quiz_widget = QWidget()
        self.quiz_widget.setObjectName(u"quiz_widget")
        self.quiz_widget.setGeometry(QRect(0, 0, 369, 489))
        self.gridLayoutWidget_2 = QWidget(self.quiz_widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 371, 491))
        self.quiz_gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.quiz_gridLayout.setObjectName(u"quiz_gridLayout")
        self.quiz_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.quiz_gridLayout.setColumnStretch(0, 5)
        self.quiz_gridLayout.setColumnStretch(1, 1)
        self.quiz_scroll.setWidget(self.quiz_widget)
        
        self.return_2.setText('<< Go Back')
        
        # self.courseID = QLabel(Form)
        # self.courseID.setText(f"courseID : {self.cID}")
        # self.courseID.setGeometry(QRect(350, 520, 300, 24))
        
        # for loop making pushButton and Label
        # Lesson
        for _ in range(len(self.lessons)):
            button = QPushButton(self.gridLayoutWidget)
            button.setObjectName(f"lesson_{self.lesson_index + 1}")
            button.setText(self.lessons[self.lesson_index])
            self.lesson_gridLayout.addWidget(button, self.lesson_index, 0, 1, 1)
            self.lesson_buttons.append(button)
            
            label = QLabel(self.gridLayoutWidget)
            label.setObjectName(f"label_{self.lesson_index + 1}")
            label.setText("Complete?")
            self.lesson_gridLayout.addWidget(label, self.lesson_index, 1, 1, 1)
            
            self.lesson_index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.lesson_gridLayout.addItem(self.verticalSpacer, self.lesson_index, 0, 1, 1)

        # for loop making pushButton and Label
        # Quiz
        for _ in range(len(self.quizzes)):
            button = QPushButton(self.gridLayoutWidget)
            button.setObjectName(f"lesson_{self.quiz_index + 1}")
            button.setText(self.quizzes[self.quiz_index])
            self.quiz_gridLayout.addWidget(button, self.quiz_index, 0, 1, 1)
            self.quiz_buttons.append(button)
            
            label = QLabel(self.gridLayoutWidget)
            label.setObjectName(f"label_{self.quiz_index + 1}")
            label.setText("Complete?")
            self.quiz_gridLayout.addWidget(label, self.quiz_index, 1, 1, 1)
            
            self.quiz_index += 1
        # makes verticleSpacer
        self.verticalSpacer_2 = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.quiz_gridLayout.addItem(self.verticalSpacer_2, self.quiz_index, 0, 1, 1)
        
        QMetaObject.connectSlotsByName(Form)

    def updateLessonsUi(self, lessons):
        # Clear existing lesson buttons
        for i in reversed(range(self.lesson_gridLayout.count())):
            widget = self.lesson_gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        # for button in self.lesson_buttons:
        #     self.lesson_gridLayout.removeItem(button)
        #     # button.deleteLater()
        # for button in self.lesson_delete:
        #     self.lesson_gridLayout.removeItem(button)
        #     # button.deleteLater()
        # for button in self.lesson_edit:
        #     self.lesson_gridLayout.removeItem(button)
        #     # button.deleteLater()
        self.lesson_gridLayout.removeItem(self.verticalSpacer)
        
        self.lesson_buttons = []
        self.lesson_index = 0
        
        # Add new lessons
        for lesson_name in lessons:
            button = QPushButton(self.lesson_widget)
            button.setObjectName(f"lesson_{self.lesson_index + 1}")
            button.setText(lesson_name)
            self.lesson_gridLayout.addWidget(button, self.lesson_index, 0, 1, 1)
            self.lesson_buttons.append(button)
            
            self.lesson_index += 1
            
        self.lesson_gridLayout.addItem(self.verticalSpacer, self.lesson_index, 0, 1, 1)
            

    def updateQuizUi(self, quizzes, quiz_status):
        print('update')
        # Clear old Element
        for i in reversed(range(self.quiz_gridLayout.count())):
            widget = self.quiz_gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.quiz_gridLayout.removeItem(self.verticalSpacer_2)
        
        self.quiz_buttons = []
        self.quiz_index = 0
        
        # Add new quiz
        for i in range(len(quizzes)):
            button = QPushButton(self.quiz_widget)
            button.setObjectName(f"quiz_{self.quiz_index + 1}")
            button.setText(quizzes[i])

            label = QLabel(self.gridLayoutWidget)
            label.setObjectName(f"label_{self.quiz_index + 1}")
            label.setText("Passed" if self.username in quiz_status[i] else "Not passed")
            self.quiz_gridLayout.addWidget(label, self.quiz_index, 1, 1, 1)

            self.quiz_gridLayout.addWidget(button, self.quiz_index, 0, 1, 1)
            self.quiz_buttons.append(button)

            
            
            self.quiz_index += 1
            
        self.quiz_gridLayout.addItem(self.verticalSpacer_2, self.quiz_index, 0, 1, 1)


    # setupUi
    def set_courseCode_moduleIndex(self, username, courseCode, moduleIndex, lesson_or_quiz):
        self.username = username
        self.cID = courseCode
        self.moduleIndex = moduleIndex

        if lesson_or_quiz == "lesson":
            response = requests.get(f"http://127.0.0.1:8000/lessons/{courseCode}/{moduleIndex}")

            if response.status_code == 200:
                data = response.json()
                lessons = [lesson_obj["name"] for lesson_obj in data["lessons"]]
                self.updateLessonsUi(lessons)
                print(data)
        else:
            print('begin')
            response = requests.get(f"http://127.0.0.1:8000/quizzes/{courseCode}/{moduleIndex}")
            print("quiz reponse", response.text)
            if response.status_code == 200:
                data = response.json()
                quizzes = [quiz_obj["questionName"] for quiz_obj in data["quizzes"]]
                quiz_status = [quiz_obj["which_student_finsished_StatusList"] for quiz_obj in data["quizzes"]]
                self.updateQuizUi(quizzes, quiz_status)
                print("quizdata", data)

    def updateUi(self):
        response = requests.get(f"http://127.0.0.1:8000/quizzes/{self.cID}/{self.moduleIndex}")
        if response.status_code == 200:
            data = response.json()
            quizzes = [quiz_obj["questionName"] for quiz_obj in data["quizzes"]]
            quiz_status = [quiz_obj["which_student_finsished_StatusList"] for quiz_obj in data["quizzes"]]
            self.updateQuizUi(quizzes, quiz_status)
            