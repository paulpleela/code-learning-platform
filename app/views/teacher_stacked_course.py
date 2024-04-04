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
from views.quiz_page import QuizPage
from views.quiz_correct_answer_list import Quiz_correct_answer_list
from views.quiz_wrong_answer_list import Quiz_wrong_answer_list

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
        ##################### 0 
        self.stacked = QStackedWidget(Form)
        self.stacked.setObjectName(u"stackedWidget")
        self.stacked.setGeometry(QRect(0, 0, 811, 541))
        
        self.course_list = Teacher_Course_list()   
        self.stacked.addWidget(self.course_list)
        
        for button in self.course_list.course_buttons:
            button.clicked.connect(self.go_to_lesson_quiz)
        
        self.course_list.enroll_btn.clicked.connect(self.add_course)
        
        ###################################### 1 
        self.lq_list = Teacher_Lesson_Quiz_list()
        self.stacked.addWidget(self.lq_list)
        self.lq_list.return_2.clicked.connect(self.go_to_course)
        
        self.lq_list.add_lesson_btn.clicked.connect(self.add_lesson)
        self.lq_list.add_quiz_btn.clicked.connect(self.add_quiz)
        
        for button in self.lq_list.quiz_buttons:
            button.clicked.connect(self.go_to_quiz)
            
        ##################################### 2
        self.quiz = QuizPage()
        self.stacked.addWidget(self.quiz)
        
        self.quiz.nav_bar.back_button.clicked.connect(self.go_to_lesson_quiz)
        self.quiz.nav_bar.send_button.clicked.connect(self.go_to_wrong)
        
        #################################### 3
        self.correct = Quiz_correct_answer_list()
        self.stacked.addWidget(self.correct)
        
        #################################### 4
        self.wrong = Quiz_wrong_answer_list()
        self.stacked.addWidget(self.wrong)
        
        QMetaObject.connectSlotsByName(Form)
    
    def go_to_course(self):
        self.stacked.setCurrentIndex(0)
    
    def go_to_lesson_quiz(self):
        self.stacked.setCurrentIndex(1)
        
    def go_to_quiz(self):
        self.stacked.setCurrentIndex(2)
    
    def go_to_correct(self):
        self.stacked.setCurrentIndex(3)
    
    def go_to_wrong(self):
        self.stacked.setCurrentIndex(4)
    
    def go_to_lesson(self):
        pass
    
    
    
    def add_course(self):
        # if self.course_list.lineEdit.text() != '' :
            self.course_list.gridLayout.removeItem(self.course_list.verticalSpacer)
            
            button = QPushButton(self.course_list.scrollAreaWidgetContents)
            self.course_list.gridLayout.addWidget(button, self.course_list.index, 0, 1, 1)
            button.setText(self.course_list.lineEdit.text())
            self.course_list.course_buttons.append(button)
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
            self.course_list.delete_buttons[delete] = self.course_list.index
            delete.clicked.connect(self.course_list.delete_course)
            
            self.course_list.index += 1

            self.course_list.gridLayout.addItem(self.course_list.verticalSpacer, self.course_list.index, 0, 1, 1)

    def add_lesson(self):
        # if self.course_list.lineEdit.text() != '' :
            self.lq_list.lesson_gridLayout.removeItem(self.lq_list.verticalSpacer)
            
            button = QPushButton(self.lq_list.lesson_widget)
            self.lq_list.lesson_gridLayout.addWidget(button, self.lq_list.lesson_index, 0, 1, 1)
            button.setText('Lesson')
            self.lq_list.lesson_buttons.append(button)
            button.clicked.connect(self.go_to_lesson)
            
            edit = QPushButton(self.lq_list.lesson_widget)
            edit.setObjectName(f"edit_{self.lq_list.lesson_index + 1}")
            edit.setText('Edit')
            self.lq_list.lesson_gridLayout.addWidget(edit, self.lq_list.lesson_index, 1, 1, 1)
            self.lq_list.lesson_edit.append(edit)
                
            delete = QPushButton(self.lq_list.lesson_widget)
            delete.setObjectName(f"delete_{self.lq_list.lesson_index + 1}")
            delete.setText('Delete')
            self.lq_list.lesson_gridLayout.addWidget(delete, self.lq_list.lesson_index, 2, 1, 1)
            self.lq_list.lesson_delete[delete] = self.lq_list.lesson_index
            delete.clicked.connect(self.lq_list.delete_lesson)
            
            self.lq_list.lesson_index += 1

            self.lq_list.lesson_gridLayout.addItem(self.lq_list.verticalSpacer, self.lq_list.lesson_index, 0, 1, 1)  
            
    def add_quiz(self):
        # if self.course_list.lineEdit.text() != '' :
            self.lq_list.quiz_gridLayout.removeItem(self.lq_list.verticalSpacer_2)
            
            button = QPushButton(self.lq_list.quiz_widget)
            self.lq_list.quiz_gridLayout.addWidget(button, self.lq_list.quiz_index, 0, 1, 1)
            button.setText('Quiz')
            self.lq_list.quiz_buttons.append(button)
            button.clicked.connect(self.go_to_quiz)
            
            edit = QPushButton(self.lq_list.quiz_widget)
            edit.setObjectName(f"edit_{self.lq_list.quiz_index + 1}")
            edit.setText('Edit')
            self.lq_list.quiz_gridLayout.addWidget(edit, self.lq_list.quiz_index, 1, 1, 1)
            self.lq_list.quiz_edit.append(edit)
                
            delete = QPushButton(self.lq_list.quiz_widget)
            delete.setObjectName(f"delete_{self.lq_list.quiz_index + 1}")
            delete.setText('Delete')
            self.lq_list.quiz_gridLayout.addWidget(delete, self.lq_list.quiz_index, 2, 1, 1)
            self.lq_list.quiz_delete[delete] = self.lq_list.quiz_index
            delete.clicked.connect(self.lq_list.delete_quiz)
            
            self.lq_list.quiz_index += 1

            self.lq_list.quiz_gridLayout.addItem(self.lq_list.verticalSpacer_2, self.lq_list.quiz_index, 0, 1, 1)       
    
