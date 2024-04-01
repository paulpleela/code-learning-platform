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
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QStackedWidget, QMainWindow)

from PySide6 import QtCore, QtGui, QtWidgets

class Course_list(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 781, 491))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.pushButton.clicked.connect(self.get_into_course)
        self.pushButton_2.clicked.connect(self.get_into_course)
        self.pushButton_3.clicked.connect(self.get_into_course)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    def get_into_course(self):
        print('get into course')
        pass
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Course", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Course", None))
        self.label.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Course", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Complete?", None))
        
        
    # retranslateUi
    

