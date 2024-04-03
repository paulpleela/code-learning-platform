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
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.lesson_gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.lesson_gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.lesson_gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.lesson_gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.lesson_gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.lesson_gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.lesson_gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

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
        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.quiz_gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.quiz_gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.quiz_gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.quiz_gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.quiz_gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.quiz_gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.quiz_gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.quiz_gridLayout.setColumnStretch(0, 5)
        self.quiz_gridLayout.setColumnStretch(1, 1)
        self.quiz_scroll.setWidget(self.quiz_widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.return_2.setText(QCoreApplication.translate("Form", u"Return to ...", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Complete?", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Complete?", None))
    # retranslateUi

