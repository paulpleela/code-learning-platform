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

class Course_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.index = 3
        
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
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.enroll_btn = QPushButton(Form)
        self.enroll_btn.setObjectName(u"enroll_btn")
        self.enroll_btn.setGeometry(QRect(520, 510, 181, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 510, 391, 31))
        
        self.enroll_btn.clicked.connect(self.enroll_course)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Course", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Course", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Course", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.label.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.enroll_btn.setText(QCoreApplication.translate("Form", u"Enroll Course", None))
    # retranslateUi

    def enroll_course(self):
        self.gridLayout.removeItem(self.verticalSpacer)
        button = QPushButton(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(button, self.index, 0, 1, 1)
        button.setText(self.lineEdit.text())
        
        label = QLabel(self.scrollAreaWidgetContents)
        label.setObjectName(u"label_3")
        label.setText(QCoreApplication.translate("Form", u"Complete?", None))

        self.gridLayout.addWidget(label, self.index, 1, 1, 1)
        
        self.index += 1

        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
