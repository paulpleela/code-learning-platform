# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget, QMainWindow)

class Rename(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(803, 550)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 781, 531))
        self.rename_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.rename_gridLayout.setObjectName(u"rename_gridLayout")
        self.rename_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rename_gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.rename_gridLayout.addWidget(self.lineEdit, 0, 0, 1, 3)

        self.confirm = QPushButton(self.gridLayoutWidget)
        self.confirm.setObjectName(u"confirm")

        self.rename_gridLayout.addWidget(self.confirm, 2, 2, 1, 1)

        self.cancel = QPushButton(self.gridLayoutWidget)
        self.cancel.setObjectName(u"cancel")

        self.rename_gridLayout.addWidget(self.cancel, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.confirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

