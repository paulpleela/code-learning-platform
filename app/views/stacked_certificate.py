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

from views.list_item import ListItem
from views.lesson_pdf import LessonPDF

class Stacked_Certificate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        font1 = QFont()
        font1.setPointSize(20)
        
        self.stacked = QStackedWidget(Form)
        self.stacked.setObjectName(u"stackedWidget")
        self.stacked.setGeometry(QRect(0, 0, 811, 541))
        
        ############################## 0
        self.certificate_list = ListItem()
        self.stacked.addWidget(self.certificate_list)
        
        for button in self.certificate_list.buttons:
            button.clicked.connect(self.go_to_show_pdf)
        
        ############################## 1
        
        self.show_pdf = LessonPDF()
        self.stacked.addWidget(self.show_pdf)
        
        self.show_pdf.nav_bar.back_button.clicked.connect(self.go_to_certificate_list)
        
        #############################
        
        QMetaObject.connectSlotsByName(Form)
    
    def go_to_certificate_list(self):
        self.stacked.setCurrentIndex(0)
        
    def go_to_show_pdf(self):
        self.stacked.setCurrentIndex(1)