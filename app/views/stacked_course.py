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
from views.course_list import Course_list
from views.lesson_quiz_list import Lesson_Quiz_list
from views.quiz_page import QuizPage
from views.quiz_correct_answer_list import Quiz_correct_answer_list
from views.quiz_wrong_answer_list import Quiz_wrong_answer_list
from views.quiz_answer_list import Quiz_answer_list
from views.update_lesson import EditLessonForm
from views.add_quiz_question import QuizQuestion

class Stacked_Course(QMainWindow):
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
        
        self.course_list = Course_list()   
        self.stacked.addWidget(self.course_list)
        # self.course_list.pushButton.clicked.connect(self.go_to_lesson_quiz)
        # self.course_list.pushButton_2.clicked.connect(self.go_to_lesson_quiz)
        # self.course_list.pushButton_3.clicked.connect(self.go_to_lesson_quiz)
        
        for button in self.course_list.buttons:
            button.clicked.connect(self.go_to_lesson_quiz)
        
        self.course_list.enroll_btn.clicked.connect(self.enroll_course)
        
        ##########################################
        
        self.lq_list = Lesson_Quiz_list()
        self.stacked.addWidget(self.lq_list)
        self.lq_list.return_2.clicked.connect(self.go_to_course)
        
        ########################################2
        self.quiz = QuizPage()
        self.stacked.addWidget(self.quiz)
        
        self.text_case = []
        self.answer = []
        
        self.quiz.nav_bar.back_button.clicked.connect(self.go_to_lesson_quiz)
        
        # self.quiz.nav_bar.send_button.clicked.connect(self.go_to_answer)
        
        
        QMetaObject.connectSlotsByName(Form)
    
    def go_to_course(self):
        self.stacked.setCurrentIndex(0)
    
    def go_to_lesson_quiz(self):
        self.stacked.setCurrentIndex(1)
        
    def go_to_quiz(self):
        self.stacked.setCurrentIndex(2)
    
    def go_to_lesson(self):
        pass
    
    
    def enroll_course(self):
        # if self.course_list.lineEdit.text() != '' :
            self.course_list.gridLayout.removeItem(self.course_list.verticalSpacer)
            button = QPushButton(self.course_list.scrollAreaWidgetContents)
            self.course_list.gridLayout.addWidget(button, self.course_list.index, 0, 1, 1)
            button.setText(self.course_list.lineEdit.text())
            self.course_list.buttons.append(button)
            button.clicked.connect(self.go_to_lesson_quiz)
            
            label = QLabel(self.course_list.scrollAreaWidgetContents)
            label.setObjectName(f"label_{self.course_list.index+1}")
            label.setText(QCoreApplication.translate("Form", u"Complete?", None))
            
            self.course_list.lineEdit.clear()

            self.course_list.gridLayout.addWidget(label, self.course_list.index, 1, 1, 1)
            
            self.course_list.index += 1

            self.course_list.gridLayout.addItem(self.course_list.verticalSpacer, self.course_list.index, 0, 1, 1)
            self.course_list.lineEdit.clear()
