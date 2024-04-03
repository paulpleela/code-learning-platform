# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(950, 600)
        self.login_button = QPushButton(RegisterWindow)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(350, 420, 271, 24))
        self.verticalLayoutWidget = QWidget(RegisterWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 120, 271, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_label = QLabel(self.frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(0, 0, 111, 16))
        self.username_input = QLineEdit(self.frame)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(0, 20, 271, 21))
        self.username_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.password_label = QLabel(self.frame_2)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(0, 0, 49, 16))
        self.password_input = QLineEdit(self.frame_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(0, 20, 271, 21))
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.confirm_label = QLabel(self.frame_3)
        self.confirm_label.setObjectName(u"confirm_label")
        self.confirm_label.setGeometry(QRect(0, 0, 131, 16))
        self.confirm_input = QLineEdit(self.frame_3)
        self.confirm_input.setObjectName(u"confirm_input")
        self.confirm_input.setGeometry(QRect(0, 20, 271, 21))
        self.confirm_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.frame_3)

        self.register_button = QPushButton(self.verticalLayoutWidget)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout.addWidget(self.register_button)


        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"Register", None))
        self.login_button.setText(QCoreApplication.translate("RegisterWindow", u"Already have an account? Login", None))
        self.title.setText(QCoreApplication.translate("RegisterWindow", u"Create an account", None))
        self.username_label.setText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.confirm_label.setText(QCoreApplication.translate("RegisterWindow", u"Confirm Password", None))
        self.register_button.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
    # retranslateUi

