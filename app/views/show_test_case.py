# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_test_case.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,QMainWindow, QTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Show_Test_Case(QWidget):
    def __init__(self):
        super().__init__()
        self.input_info = "Hello"
        self.output_info = "Hi"
        
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(802, 552)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setGeometry(QRect(0, 0, 811, 541))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.input = QTextEdit(Form)
        self.input.setObjectName(u"input")
        self.input.setText(self.input_info)
        self.input.setReadOnly(True)

        self.verticalLayout.addWidget(self.input)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.output = QTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setText(self.output_info)
        self.output.setReadOnly(True)

        self.verticalLayout.addWidget(self.output)

        self.go_back = QPushButton(Form)
        self.go_back.setObjectName(u"pushButton")
        self.go_back.setFixedWidth(200)

        self.verticalLayout.addWidget(self.go_back)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.go_back.setText(QCoreApplication.translate("Form", u"<< Go Back", None))
    # retranslateUi

