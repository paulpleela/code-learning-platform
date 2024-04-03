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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(950, 600)
        LoginWindow.setInputMethodHints(Qt.ImhNone)
        self.gridLayout_2 = QGridLayout(LoginWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(LoginWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 271, 231))
        self.verticalLayoutWidget.setMinimumSize(QSize(269, 24))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(269, 24))
        self.title.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(17)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title)

        self.frame_1 = QFrame(self.verticalLayoutWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(269, 24))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.username_label = QLabel(self.frame_1)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(0, 0, 269, 24))
        self.username_label.setMinimumSize(QSize(269, 24))
        font1 = QFont()
        font1.setPointSize(11)
        self.username_label.setFont(font1)
        self.username_input = QLineEdit(self.frame_1)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setEnabled(True)
        self.username_input.setGeometry(QRect(0, 20, 271, 24))
        self.username_input.setMinimumSize(QSize(269, 24))
        font2 = QFont()
        font2.setPointSize(10)
        self.username_input.setFont(font2)
        self.username_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(269, 24))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.password_label = QLabel(self.frame_2)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(0, 0, 269, 24))
        self.password_label.setMinimumSize(QSize(269, 24))
        self.password_label.setFont(font1)
        self.password_input = QLineEdit(self.frame_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(0, 20, 271, 24))
        self.password_input.setMinimumSize(QSize(269, 24))
        self.password_input.setFont(font2)
        self.password_input.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.frame_2)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(269, 24))
        self.login_button.setFont(font2)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.login_button)

        self.goto_register_button = QPushButton(self.frame)
        self.goto_register_button.setObjectName(u"goto_register_button")
        self.goto_register_button.setGeometry(QRect(20, 250, 271, 24))
        self.goto_register_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.title.setText(QCoreApplication.translate("LoginWindow", u"Welcome", None))
        self.username_label.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_input.setText("")
        self.login_button.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.goto_register_button.setText(QCoreApplication.translate("LoginWindow", u"Don't have an account? Register", None))
    # retranslateUi

