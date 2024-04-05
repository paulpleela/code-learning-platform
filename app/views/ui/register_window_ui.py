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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(950, 600)
        RegisterWindow.setInputMethodHints(Qt.ImhNone)
        self.gridLayout_2 = QGridLayout(RegisterWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(RegisterWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 271, 261))
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

        self.frame_4 = QFrame(self.verticalLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.name_label = QLabel(self.frame_4)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(0, 0, 261, 16))
        self.name_label.setFont(font1)
        self.name_input = QLineEdit(self.frame_4)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(0, 20, 271, 21))
        self.name_input.setFont(font2)

        self.verticalLayout.addWidget(self.frame_4)

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

        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.confirm_label = QLabel(self.frame_3)
        self.confirm_label.setObjectName(u"confirm_label")
        self.confirm_label.setGeometry(QRect(0, 0, 269, 24))
        self.confirm_label.setMinimumSize(QSize(269, 24))
        self.confirm_label.setFont(font1)
        self.confirm_input = QLineEdit(self.frame_3)
        self.confirm_input.setObjectName(u"confirm_input")
        self.confirm_input.setGeometry(QRect(0, 20, 271, 24))
        self.confirm_input.setMinimumSize(QSize(269, 24))
        self.confirm_input.setFont(font2)
        self.confirm_input.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.confirm_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.frame_3)

        self.role_selector = QComboBox(self.verticalLayoutWidget)
        self.role_selector.addItem("")
        self.role_selector.addItem("")
        self.role_selector.setObjectName(u"role_selector")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.role_selector.setFont(font3)
        self.role_selector.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.role_selector)

        self.goto_login_button = QPushButton(self.frame)
        self.goto_login_button.setObjectName(u"goto_login_button")
        self.goto_login_button.setGeometry(QRect(20, 360, 271, 24))
        self.goto_login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_button = QPushButton(self.frame)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(20, 300, 269, 26))
        self.register_button.setMinimumSize(QSize(269, 24))
        self.register_button.setFont(font2)
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.error_message = QLabel(self.frame)
        self.error_message.setObjectName(u"error_message")
        self.error_message.setGeometry(QRect(28, 280, 261, 20))
        self.error_message.setStyleSheet(u"#error_message{color: rgb(255, 0, 0)}")

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"Login", None))
        self.title.setText(QCoreApplication.translate("RegisterWindow", u"Create an account", None))
        self.username_label.setText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.name_label.setText(QCoreApplication.translate("RegisterWindow", u"Full Name (for certificates)", None))
        self.password_label.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.password_input.setText("")
        self.confirm_label.setText(QCoreApplication.translate("RegisterWindow", u"Confirm Password", None))
        self.confirm_input.setText("")
        self.role_selector.setItemText(0, QCoreApplication.translate("RegisterWindow", u"I'm a Student", None))
        self.role_selector.setItemText(1, QCoreApplication.translate("RegisterWindow", u"I'm a Teacher", None))

        self.goto_login_button.setText(QCoreApplication.translate("RegisterWindow", u"Already have an account? Login", None))
        self.register_button.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
        self.error_message.setText("")
    # retranslateUi

