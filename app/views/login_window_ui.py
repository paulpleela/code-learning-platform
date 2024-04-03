# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(950, 600)
        LoginWindow.setInputMethodHints(Qt.ImhNone)
        self.register_button = QPushButton(LoginWindow)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(350, 390, 271, 24))
        self.verticalLayoutWidget = QWidget(LoginWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 130, 271, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(14)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignHCenter)

        self.frame_1 = QFrame(self.verticalLayoutWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.username_label = QLabel(self.frame_1)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(0, 0, 111, 16))
        self.username_input = QLineEdit(self.frame_1)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setEnabled(True)
        self.username_input.setGeometry(QRect(0, 20, 271, 21))
        self.username_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame_1)

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
        self.password_input.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.frame_2)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.register_button.setText(QCoreApplication.translate("LoginWindow", u"Don't have an account? Register", None))
        self.title.setText(QCoreApplication.translate("LoginWindow", u"Welcome", None))
        self.username_label.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_input.setText("")
        self.login_button.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
    # retranslateUi

