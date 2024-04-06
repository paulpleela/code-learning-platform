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
class Teacher_Lesson_Quiz_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cID = ""
        self.moduleIndex = None

        self.lessons = []
        
        self.lesson_buttons = []
        self.lesson_delete = {}
        self.lesson_edit = {}
        self.lesson_index = 0
        
        self.quizzes = ['ign', 'fed', 'cga']
        self.quiz_buttons = []
        self.quiz_edit = {}
        self.quiz_delete = {}
        self.quiz_index = 0
        
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)        
        self.lesson_scroll = QScrollArea(Form)
        self.lesson_scroll.setObjectName(u"lesson_scroll")
        self.lesson_scroll.setGeometry(QRect(10, 11, 389, 461))
        self.lesson_scroll.setWidgetResizable(True)
        self.lesson_widget = QWidget()
        self.lesson_widget.setObjectName(u"lesson_widget")
        self.lesson_widget.setGeometry(QRect(0, 0, 369, 489))
        self.lesson_gridLayout = QGridLayout(self.lesson_widget)
        self.lesson_gridLayout.setObjectName(u"gridLayoutWidget")
        self.lesson_gridLayout.setGeometry(QRect(0, 0, 371, 491))
        self.lesson_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lesson_gridLayout.setColumnStretch(0, 5)
        self.lesson_gridLayout.setColumnStretch(1, 1)
        self.lesson_scroll.setWidget(self.lesson_widget)
        
        self.return_2 = QPushButton(Form)
        self.return_2.setObjectName(u"return_2")
        self.return_2.setGeometry(QRect(30, 510, 131, 24))
        self.quiz_scroll = QScrollArea(Form)
        self.quiz_scroll.setObjectName(u"quiz_scroll")
        self.quiz_scroll.setGeometry(QRect(405, 11, 388, 461))
        self.quiz_scroll.setWidgetResizable(True)
        self.quiz_widget = QWidget()
        self.quiz_widget.setObjectName(u"quiz_widget")
        self.quiz_widget.setGeometry(QRect(0, 0, 369, 489))
        self.quiz_gridLayout = QGridLayout(self.quiz_widget)
        self.quiz_gridLayout.setObjectName(u"gridLayoutWidget_2")
        self.quiz_gridLayout.setGeometry(QRect(0, 0, 371, 491))
        self.quiz_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.quiz_gridLayout.setColumnStretch(0, 5)
        self.quiz_gridLayout.setColumnStretch(1, 1)
        self.quiz_scroll.setWidget(self.quiz_widget)
        
        self.return_2.setText('Return to ...')
        self.add_lesson_btn = QPushButton(Form)
        self.add_lesson_btn.setObjectName(u"add_Lesson")
        self.add_lesson_btn.setText("Add Lesson")
        self.add_lesson_btn.setGeometry(QRect(120, 480, 201, 24))    
        
        self.add_quiz_btn = QPushButton(Form)
        self.add_quiz_btn.setObjectName(u"add_quiz")
        self.add_quiz_btn.setText("Add Quiz")
        self.add_quiz_btn.setGeometry(QRect(510, 480, 201, 24))
        
        self.courseID = QLabel(Form)
        self.courseID.setText(f"courseID : {self.cID}")
        self.courseID.setGeometry(QRect(350, 520, 300, 24))
        
        # for loop making pushButton and Label
        # Lesson
        
                                      
        for _ in range(len(self.lessons)):
            button = QPushButton(self.lesson_widget)
            button.setObjectName(f"lesson_{self.lesson_index + 1}")
            button.setText(self.lessons[self.lesson_index])
            self.lesson_gridLayout.addWidget(button, self.lesson_index, 0, 1, 1)
            self.lesson_buttons.append(button)
            
            
            edit = QPushButton(self.lesson_widget)
            edit.setObjectName(f"edit_{self.lesson_index + 1}")
            edit.setText('Edit')
            self.lesson_gridLayout.addWidget(edit, self.lesson_index, 1, 1, 1)
            self.lesson_edit[edit] = self.lesson_index
            
            delete = QPushButton(self.lesson_widget)
            delete.setObjectName(f"delete_{self.lesson_index + 1}")
            delete.setText('Delete')
            delete.clicked.connect(self.delete_lesson)
            self.lesson_gridLayout.addWidget(delete, self.lesson_index, 2, 1, 1)
            self.lesson_delete[delete] = self.lesson_index    
                        
            self.lesson_index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.lesson_gridLayout.addItem(self.verticalSpacer, self.lesson_index, 0, 1, 1)

        # for loop making pushButton and Label
        # Quiz
        for _ in range(len(self.quizzes)):
            button = QPushButton(self.quiz_widget)
            button.setObjectName(f"lesson_{self.quiz_index + 1}")
            button.setText(self.quizzes[self.quiz_index])
            self.quiz_gridLayout.addWidget(button, self.quiz_index, 0, 1, 1)
            self.quiz_buttons.append(button)
            
            edit = QPushButton(self.quiz_widget)
            edit.setObjectName(f"edit_{self.quiz_index + 1}")
            edit.setText('Edit')
            self.quiz_gridLayout.addWidget(edit, self.quiz_index, 1, 1, 1)
            self.quiz_edit[edit] = self.quiz_index
            
            delete = QPushButton(self.quiz_widget)
            delete.setObjectName(f"delete_{self.quiz_index + 1}")
            delete.setText('Delete')
            delete.clicked.connect(self.delete_quiz)
            self.quiz_gridLayout.addWidget(delete, self.quiz_index, 2, 1, 1)
            self.quiz_delete[delete] = self.quiz_index 
            
            self.quiz_index += 1
        # makes verticleSpacer
        self.verticalSpacer_2 = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.quiz_gridLayout.addItem(self.verticalSpacer_2, self.quiz_index, 0, 1, 1)
        
        QMetaObject.connectSlotsByName(Form)
        
    # setupUi
    
    def delete_lesson(self):
        sender_button = self.sender()
                
        position = None
        if sender_button in self.lesson_delete:
            position = self.lesson_delete[sender_button]
        
        if position != None:
            for j in range(self.lesson_gridLayout.columnCount()):
                item = self.lesson_gridLayout.itemAtPosition(position, j)
                if item:
                    widget = item.widget()
                    self.lesson_gridLayout.removeWidget(widget)
                    widget.deleteLater()
            del self.lesson_delete[sender_button]
        
    def delete_quiz(self):
        sender_button = self.sender()
                    
        position = None
        if sender_button in self.quiz_delete:
            position = self.quiz_delete[sender_button]
            
        if position != None:
            for j in range(self.quiz_gridLayout.columnCount()):
                item = self.quiz_gridLayout.itemAtPosition(position, j)
                if item:
                    widget = item.widget()
                    self.quiz_gridLayout.removeWidget(widget)
                    widget.deleteLater()
            del self.quiz_delete[sender_button]

    def updateLessonsUi(self, lessons):
        # Clear existing lesson buttons
        for button in self.lesson_buttons:
            button.deleteLater()
        self.lesson_buttons = []
        self.lesson_index = 0
        
        # Add new lessons
        for lesson_name in lessons:
            button = QPushButton(self.lesson_widget)
            button.setObjectName(f"lesson_{self.lesson_index + 1}")
            button.setText(lesson_name)
            self.lesson_gridLayout.addWidget(button, self.lesson_index, 0, 1, 1)
            self.lesson_buttons.append(button)
            
            edit = QPushButton(self.lesson_widget)
            edit.setObjectName(f"edit_{self.lesson_index + 1}")
            edit.setText('Edit')
            self.lesson_gridLayout.addWidget(edit, self.lesson_index, 1, 1, 1)
            self.lesson_edit[edit] = self.lesson_index
            
            delete = QPushButton(self.lesson_widget)
            delete.setObjectName(f"delete_{self.lesson_index + 1}")
            delete.setText('Delete')
            delete.clicked.connect(self.delete_lesson)
            self.lesson_gridLayout.addWidget(delete, self.lesson_index, 2, 1, 1)
            self.lesson_delete[delete] = self.lesson_index 
            
            self.lesson_index += 1

    def set_courseCode_moduleIndex(self, courseCode, moduleIndex):
        self.cID = courseCode
        self.moduleIndex = moduleIndex
        print("cID: ", self.cID, "!!!!!!!!!!!!!!!!!")
        response = requests.get(f"http://127.0.0.1:8000/lessons/{courseCode}/{moduleIndex}")

        if response.status_code == 200:
            data = response.json()
            lessons = [lesson_obj["name"] for lesson_obj in data["lessons"]]
            self.updateLessonsUi(lessons)
            print(data)
