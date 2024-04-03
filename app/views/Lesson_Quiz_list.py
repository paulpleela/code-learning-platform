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

class Lesson_Quiz_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lessons = ['abc', 'def', 'ghi']
        self.lesson_buttons = []
        self.lesson_index = 0
        
        self.quizzes = ['ign', 'fed', 'cga']
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
        
        self.return_2.setText('Return to ...')
        
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
        
    # setupUi



