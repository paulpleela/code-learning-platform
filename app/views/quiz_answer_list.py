# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quiz_wrong_answer_list.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QWidget , QMainWindow)

from PySide6 import QtCore, QtGui, QtWidgets

class Quiz_answer_list(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.index = 0
        self.results = []
        self.test_case = []
        self.answer = []
        
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
        
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        self.gridLayout.setColumnStretch(5, 0)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.go_back = QPushButton(Form)
        self.go_back.setObjectName(u"go_back")
        self.go_back.setGeometry(QRect(30, 510, 131, 24))
        self.go_back.setText("<< Go Back")
        
        self.next = QPushButton(Form)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(650, 510, 131, 24))
        self.next.setText("Exit Quiz")
        self.next.setVisible(False)
        
        QMetaObject.connectSlotsByName(Form)

    def setResults(self, results):
        self.results = results
        
        # Clearing previous buttons and labels
        for button in self.buttons:
            button.deleteLater()
        self.buttons = []
        
        # Clearing previous labels
        for i in range(self.gridLayout.count()):
            item = self.gridLayout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        self.index = 0
        all_passed = True
        # Adding buttons and labels based on results data
        for result in self.results:
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"pushButton_{self.index + 1}")
            button.setText(f"Test_case_{self.index + 1}")
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.buttons.append(button)
            
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f"label_{self.index + 1}")
            if result == "Passed":
                label.setText(result)
            else:
                label.setText("Error")
                all_passed = False
            self.gridLayout.addWidget(label, self.index, 1, 1, 1)
            
            self.index += 1
        
        # Adding vertical spacer
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        # Checking if all test cases are correct
        if all_passed:
            self.next.setVisible(True)
