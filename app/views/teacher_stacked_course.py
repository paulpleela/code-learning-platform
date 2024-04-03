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
from views.teacher_course_list import Teacher_Course_list
from views.teacher_lesson_quiz_list import Teacher_Lesson_Quiz_list

class Teacher_Stacked_Course(QMainWindow):
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
        
        self.course_list = Teacher_Course_list()   
        self.stacked.addWidget(self.course_list)
        
        for button in self.course_list.course_buttons:
            button.clicked.connect(self.go_to_lesson_quiz)
        
        self.course_list.enroll_btn.clicked.connect(self.add_course)
        
        self.lq_list = Teacher_Lesson_Quiz_list()
        self.stacked.addWidget(self.lq_list)
        self.lq_list.return_2.clicked.connect(self.go_to_course)
        
        
        QMetaObject.connectSlotsByName(Form)
    
    def go_to_course(self):
        self.stacked.setCurrentIndex(0)
    
    def go_to_lesson_quiz(self):
        self.stacked.setCurrentIndex(1)
        
    def go_to_quiz(self):
        pass
    
    def go_to_lesson(self):
        pass
    
    
    def add_course(self):
        self.course_list.gridLayout.removeItem(self.course_list.verticalSpacer)
        
        button = QPushButton(self.course_list.scrollAreaWidgetContents)
        self.course_list.gridLayout.addWidget(button, self.course_list.index, 0, 1, 1)
        button.setText(self.course_list.lineEdit.text())
        self.course_list.buttons.append(button)
        button.clicked.connect(self.go_to_lesson_quiz)
        
        edit = QPushButton(self.course_list.scrollAreaWidgetContents)
        edit.setObjectName(f"edit_{self.course_list.index + 1}")
        edit.setText('Edit')
        self.course_list.gridLayout.addWidget(edit, self.course_list.index, 1, 1, 1)
        self.course_list.edit_buttons.append(edit)
            
        delete = QPushButton(self.course_list.scrollAreaWidgetContents)
        delete.setObjectName(f"delete_{self.course_list.index + 1}")
        delete.setText('Delete')
        self.course_list.gridLayout.addWidget(delete, self.course_list.index, 2, 1, 1)
        self.course_list.delete_buttons.append(delete)
        
        self.course_list.index += 1

        self.course_list.gridLayout.addItem(self.course_list.verticalSpacer, self.course_list.index, 0, 1, 1)
