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
from views.quiz_answer_list import Quiz_answer_list
from views.update_lesson import EditLessonForm
from views.add_quiz_question import QuizQuestion
from views.rename import Rename
from views.teacher_module_list import Teacher_Module_list
from views.module_rename import Module_Rename
from views.lesson_pdf import LessonPDF
from views.lesson_video import LessonVideo

import requests

class Teacher_Stacked_Course(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setupUi(self)
        self.courseCode = ""
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        font1 = QFont()
        font1.setPointSize(20)
        self.stacked = QStackedWidget(Form)
        self.stacked.setObjectName(u"stackedWidget")
        self.stacked.setGeometry(QRect(0, 0, 811, 541))
        
        ##################### 0 
        self.course_list = Teacher_Course_list(self.username)   
        self.stacked.addWidget(self.course_list)
                
        for idx, button in enumerate(self.course_list.course_buttons):
            def callback(index=idx):
                return lambda: self.go_to_module(index)
            button.clicked.connect(callback())


        for button in self.course_list.edit_buttons:
            button.clicked.connect(self.go_to_course_edit)
        
        self.course_list.enroll_btn.clicked.connect(self.add_course)
        
        ###################################### 1 
        self.lq_list = Teacher_Lesson_Quiz_list()
        self.stacked.addWidget(self.lq_list)
        self.lq_list.return_2.clicked.connect(self.go_to_module)
        
        self.lq_list.add_lesson_btn.clicked.connect(self.add_lesson)
        self.lq_list.add_quiz_btn.clicked.connect(self.add_quiz)
        
        for index, button in enumerate(self.lq_list.quiz_buttons):
            def callback(idx=index):
                return lambda: self.go_to_quiz_index(idx)
            button.clicked.connect(callback())

        # for button in self.lq_list.quiz_buttons:
        #     button.clicked.connect(self.go_to_quiz)
        
        for button in self.lq_list.lesson_edit:
            button.clicked.connect(self.go_to_lesson_edit)
        
        for button in self.lq_list.quiz_edit:
            button.clicked.connect(self.go_to_quiz_edit)
            
        ##################################### 2
        self.quiz = QuizPage()
        self.stacked.addWidget(self.quiz)
        
        self.text_case = []
        self.answer = []
        
        self.quiz.nav_bar.back_button.clicked.connect(self.go_to_lesson_quiz)
        self.quiz.nav_bar.send_button.clicked.connect(self.go_to_answer)
        
        #################################### 3
        self.show_ans = Quiz_answer_list()
        self.stacked.addWidget(self.show_ans)
        
        self.show_ans.next.clicked.connect(self.go_to_lesson_quiz)
        self.show_ans.go_back.clicked.connect(self.go_to_quiz)
        
        ################################## 4
        self.update_lesson = EditLessonForm()
        self.stacked.addWidget(self.update_lesson)
        
        self.update_lesson.back_button.clicked.connect(self.back_from_edit)
        
        #################################### 5
        self.add_quiz_question = QuizQuestion()
        self.stacked.addWidget(self.add_quiz_question)
        
        self.add_quiz_question.go_back.clicked.connect(self.back_from_quiz)
        #################################### 6
        self.course_rename = Rename()
        self.stacked.addWidget(self.course_rename)
        
        self.course_rename.cancel.clicked.connect(self.back_from_rename2course)
        
        ##################################### 7
        self.module_list = Teacher_Module_list()
        self.stacked.addWidget(self.module_list)
        
        
        self.module_list.return_2.clicked.connect(self.go_to_course)
        self.module_list.enroll_btn.clicked.connect(self.add_module)
        
        # index = 0
        # for button in self.module_list.module_buttons:
        #     print("BUTTON", button)
        #     button.clicked.connect(lambda idx=index: self.go_to_lesson_quiz_index(idx))
        #     index += 1
        ##################################### 8
        self.lesson_pdf = LessonPDF()
        self.stacked.addWidget(self.lesson_pdf)
        
        self.lesson_pdf.nav_bar.back_button.clicked.connect(self.go_to_lesson_quiz)
        ##################################### 9
        self.lesson_video = LessonVideo()
        self.stacked.addWidget(self.lesson_video)

        for button in self.module_list.edit_buttons:
            button.clicked.connect(self.go_to_module_edit)
        
        self.lesson_video.go_back.clicked.connect(self.go_to_lesson_quiz)
        
        ################################# 10
        self.module_rename = Module_Rename()
        self.stacked.addWidget(self.module_rename)
        
        self.module_rename.cancel.clicked.connect(self.back_from_rename2module)

        
     
    def go_to_course(self):
        self.stacked.setCurrentIndex(0)
    
    def go_to_lesson_quiz_index(self, index):
        course_code = self.module_list.cID
        self.course_code = course_code
        self.lq_list.set_courseCode_moduleIndex(course_code, index)
        for button in self.lq_list.lesson_edit:
            button.clicked.connect(self.go_to_lesson_edit)
        for button in self.lq_list.lesson_buttons:
            button.clicked.connect(self.go_to_lesson)
        for index, button in enumerate(self.lq_list.lesson_buttons):
            def callback(idx=index):
                return lambda: self.go_to_lesson(idx)
            button.clicked.connect(callback())
        
        print("Button clicked with index:", index)
        self.stacked.setCurrentIndex(1)

    def go_to_lesson_quiz(self):
        self.stacked.setCurrentIndex(1)

    def go_to_quiz(self):
        self.stacked.setCurrentIndex(2)
        
    def go_to_quiz_index(self, index):
        self.quiz.selectQuiz(index)
        self.stacked.setCurrentIndex(2)
    
    def go_to_answer(self):
        self.stacked.setCurrentIndex(3)
    
    def go_to_lesson(self, lessonIndex):
        courseCode = self.lq_list.cID
        moduleIndex = self.lq_list.moduleIndex
        print("cc", courseCode)
        print("moduleIndex", moduleIndex)
        response = requests.get(f"http://127.0.0.1:8000/lesson/{courseCode}/{moduleIndex}/{lessonIndex}")

        if response.status_code == 200:
            data = response.json()
            file_path = "server/static/" + data
            dot_index = file_path.rfind('.')
            file_type = file_path[dot_index + 1:]
            if file_type == "pdf":
                self.lesson_pdf.setFilePath(file_path)
                self.stacked.setCurrentIndex(8)
            else:
                self.lesson_video.setFilePath(file_path)
                self.stacked.setCurrentIndex(9)
        

    
    def go_to_module(self, index):
        course_code = self.course_list.get_courseCode(index)
        self.course_code = course_code
        self.module_list.set_courseCode(course_code)

        for index, button in enumerate(self.module_list.module_buttons):
            def callback(idx=index):
                return lambda: self.go_to_lesson_quiz_index(idx)
            button.clicked.connect(callback())

        for button in self.module_list.edit_buttons:
            button.clicked.connect(self.go_to_module_edit)
        self.stacked.setCurrentIndex(7)

        

    def go_to_course_edit(self):
        self.stacked.setCurrentIndex(6)
        
        sender_button = self.sender()
        
        if sender_button in self.course_list.edit_buttons:
            position = self.course_list.edit_buttons[sender_button]
            self.course_rename.confirm.clicked.connect(lambda: self.submit_course_rename(position))
    
    def go_to_module_edit(self):
        self.stacked.setCurrentIndex(10)
        
        sender_button = self.sender()
        
        if sender_button in self.module_list.edit_buttons:
            position = self.module_list.edit_buttons[sender_button]
            self.module_rename.confirm.clicked.connect(lambda: self.submit_module_rename(position))
    
    def back_from_rename2course(self):
        self.stacked.setCurrentIndex(0)
        self.course_rename.lineEdit.clear()
        self.course_rename.confirm.clicked.disconnect()
        
    def back_from_rename2module(self):
        self.stacked.setCurrentIndex(7)
        self.module_rename.lineEdit.clear()
        
        self.module_rename.deadline_edit.clear()
        self.module_rename.confirm.clicked.disconnect()
    
#########################################
    def submit_course_rename(self, index):
        if self.course_rename.lineEdit.text():
            self.course_list.renameCourse(index, self.course_rename.lineEdit.text())
            item = self.course_list.gridLayout.itemAtPosition(index , 0).widget()
            item.setText(self.course_rename.lineEdit.text())
            self.back_from_rename2course()
            
    def submit_module_rename(self, index):
        if self.module_rename.lineEdit.text():
            item = self.module_list.gridLayout.itemAtPosition(index , 0).widget()
            item.setText(self.module_rename.lineEdit.text())
            self.back_from_rename2module()
       
#########################################
    def add_course(self):
        if self.course_list.lineEdit.text() != '' :
            response = requests.post("http://127.0.0.1:8000/api/teacher/course", json={"name": self.course_list.lineEdit.text(), "teacherName": self.username})

            # Check if the request was successful
            if response.status_code == 200:
                # Print the response message
                if response.json()["success"]:
                    self.course_list.gridLayout.removeItem(self.course_list.verticalSpacer)
                    
                    button = QPushButton(self.course_list.scrollAreaWidgetContents)
                    self.course_list.gridLayout.addWidget(button, self.course_list.index, 0, 1, 1)
                    button.setText(self.course_list.lineEdit.text())
                    self.course_list.course_buttons.append(button)
                    button.clicked.connect(self.go_to_module)
                    
                    edit = QPushButton(self.course_list.scrollAreaWidgetContents)
                    edit.setObjectName(f"edit_{self.course_list.index + 1}")
                    edit.setText('Edit')
                    self.course_list.gridLayout.addWidget(edit, self.course_list.index, 1, 1, 1)
                    self.course_list.edit_buttons[edit] = self.course_list.index
                    edit.clicked.connect(self.go_to_course_edit)
                        
                    delete = QPushButton(self.course_list.scrollAreaWidgetContents)
                    delete.setObjectName(f"delete_{self.course_list.index + 1}")
                    delete.setText('Delete')
                    self.course_list.gridLayout.addWidget(delete, self.course_list.index, 2, 1, 1)
                    self.course_list.delete_buttons[delete] = self.course_list.index
                    delete.clicked.connect(self.course_list.delete_course)
                    
                    self.course_list.index += 1

                    self.course_list.gridLayout.addItem(self.course_list.verticalSpacer, self.course_list.index, 0, 1, 1)
                    self.course_list.updateAPI()
                    for idx, button in enumerate(self.course_list.course_buttons):
                        def callback(index=idx):
                            return lambda: self.go_to_module(index)
                        button.clicked.connect(callback())

            else:
                # Print an error message if the request failed
                print("Error:", response.text)

            self.course_list.lineEdit.clear()
            
    def add_module(self):
        if self.module_list.lineEdit.text() != '' :
            response = requests.post("http://127.0.0.1:8000/module/{}/{}".format(self.module_list.lineEdit.text(), self.module_list.cID))

            # Check if the request was successful
            if response:
                self.module_list.gridLayout.removeItem(self.module_list.verticalSpacer)
                
                button = QPushButton(self.module_list.scrollAreaWidgetContents)
                self.module_list.gridLayout.addWidget(button, self.module_list.index, 0, 1, 1)
                button.setText(self.module_list.lineEdit.text())
                self.module_list.module_buttons.append(button)
                button.clicked.connect(self.go_to_lesson_quiz_index(len(self.module_list.module_buttons)-1))
                
                edit = QPushButton(self.module_list.scrollAreaWidgetContents)
                edit.setObjectName(f"edit_{self.module_list.index + 1}")
                edit.setText('Edit')
                self.module_list.gridLayout.addWidget(edit, self.module_list.index, 1, 1, 1)
                self.module_list.edit_buttons[edit] = self.module_list.index
                edit.clicked.connect(self.go_to_module_edit)
                    
                delete = QPushButton(self.module_list.scrollAreaWidgetContents)
                delete.setObjectName(f"delete_{self.module_list.index + 1}")
                delete.setText('Delete')
                self.module_list.gridLayout.addWidget(delete, self.module_list.index, 2, 1, 1)
                self.module_list.delete_buttons[delete] = self.module_list.index
                delete.clicked.connect(self.module_list.delete_module)
                
                self.module_list.index += 1

                self.module_list.gridLayout.addItem(self.module_list.verticalSpacer, self.module_list.index, 0, 1, 1)
            
            self.module_list.lineEdit.clear()

##########################################
    def edit_lesson(self, index):
        lesson_name = self.update_lesson.lesson_name_edit.text()
        lesson_file_path = self.update_lesson.lesson_file_edit.toPlainText()
        
        if not lesson_name and not lesson_file_path:
            self.update_lesson.error_message.setText("Please enter a lesson name and attach a file")
        elif not lesson_name:
            self.update_lesson.error_message.setText("Please enter a lesson name")
        elif not lesson_file_path:
            self.update_lesson.error_message.setText("Please attach a lesson file")
        else:
            
            print("Lesson Name:", lesson_name)
            print("Lesson File Path:", lesson_file_path)
            print(index)
            item = self.lq_list.lesson_gridLayout.itemAtPosition(index, 0).widget()
            # print(item.text())
            item.setText(self.update_lesson.lesson_name_edit.text())
            self.back_from_edit()
               
    def back_from_edit(self):
        self.update_lesson.lesson_name_edit.clear()
        self.update_lesson.remove_file()
        self.update_lesson.error_message.clear()
        self.go_to_lesson_quiz()        
        self.update_lesson.add_button.clicked.disconnect()
             
    def go_to_lesson_edit(self):
        self.stacked.setCurrentIndex(4)
        sender_button = self.sender()
        
        if sender_button in self.lq_list.lesson_edit:
            position = self.lq_list.lesson_edit[sender_button]
            self.update_lesson.add_button.clicked.connect(lambda: self.edit_lesson(position))   
            
    def update_from_edit(self):
        lesson_name = self.update_lesson.lesson_name_edit.text()
        lesson_file_path = self.update_lesson.lesson_file_edit.toPlainText()
        
        if not lesson_name and not lesson_file_path:
            self.update_lesson.error_message.setText("Please enter a lesson name and attach a file")
        elif not lesson_name:
            self.update_lesson.error_message.setText("Please enter a lesson name")
        elif not lesson_file_path:
            self.update_lesson.error_message.setText("Please attach a lesson file")
        else:
            print("Lesson Name:", lesson_name)
            print("Lesson File Path:", lesson_file_path)
            self.add_lesson_from_update()
            self.back_from_edit()
                   
    def add_lesson_from_update(self):
        file_path = self.update_lesson.lesson_file_edit.toPlainText()
        files = {'file': open(file_path, 'rb')}

        last_dot_index = file_path.rfind('.')
        if last_dot_index != -1:
            file_extension = file_path[last_dot_index:]

        response = requests.post(f"http://127.0.0.1:8000/lesson/{self.lq_list.cID}/{self.lq_list.moduleIndex}/{self.update_lesson.lesson_name_edit.text()}/{file_extension}", files=files)

        if response:
                self.lq_list.lesson_gridLayout.removeItem(self.lq_list.verticalSpacer)
                
                button = QPushButton(self.lq_list.lesson_widget)
                self.lq_list.lesson_gridLayout.addWidget(button, self.lq_list.lesson_index, 0, 1, 1)
                button.setText(self.update_lesson.lesson_name_edit.text())
                self.lq_list.lesson_buttons.append(button)
                button.clicked.connect(lambda: self.go_to_lesson(self.lq_list.lesson_index-1))
                
                edit = QPushButton(self.lq_list.lesson_widget)
                edit.setObjectName(f"edit_{self.lq_list.lesson_index + 1}")
                edit.setText('Edit')
                self.lq_list.lesson_gridLayout.addWidget(edit, self.lq_list.lesson_index, 1, 1, 1)
                self.lq_list.lesson_edit[edit] = self.lq_list.lesson_index
                edit.clicked.connect(self.go_to_lesson_edit)
                    
                delete = QPushButton(self.lq_list.lesson_widget)
                delete.setObjectName(f"delete_{self.lq_list.lesson_index + 1}")
                delete.setText('Delete')
                self.lq_list.lesson_gridLayout.addWidget(delete, self.lq_list.lesson_index, 2, 1, 1)
                self.lq_list.lesson_delete[delete] = self.lq_list.lesson_index
                delete.clicked.connect(self.lq_list.delete_lesson)
                
                self.lq_list.lesson_index += 1

                self.lq_list.lesson_gridLayout.addItem(self.lq_list.verticalSpacer, self.lq_list.lesson_index, 0, 1, 1)

                print(response.status_code)
                print(response.text)
            
            
    def add_lesson(self):
        self.stacked.setCurrentIndex(4)
        self.update_lesson.add_button.clicked.connect(self.update_from_edit)
    
#######################################################
    def go_to_quiz_edit(self):
        self.stacked.setCurrentIndex(5)
        sender_button = self.sender()
        
        if sender_button in self.lq_list.quiz_edit:
            position = self.lq_list.quiz_edit[sender_button]
            self.add_quiz_question.add_question_button.clicked.connect(lambda: self.edit_quiz(position)) 
    
    def edit_quiz(self, index):
        self.add_quiz_question.update_error_message()

        # Check if there are no errors and at least one test case row is added
        if self.add_quiz_question.error_message.isHidden() and self.add_quiz_question.row_counter > 0:
            item = self.lq_list.quiz_gridLayout.itemAtPosition(index, 0).widget()
            item.setText(self.add_quiz_question.question_name_edit.text())
            print("Quiz question added3.")
            self.back_from_quiz()
            
        elif self.add_quiz_question.row_counter == 0:
            # Show error message if no test cases are added
            self.add_quiz_question.error_message.setText("Add at least 1 test case.")
            self.add_quiz_question.error_message.show()
        
    def back_from_quiz(self):
        self.add_quiz_question.clear_fields()
        self.go_to_lesson_quiz()
        self.add_quiz_question.add_question_button.clicked.disconnect()
    
    def update_from_quiz(self):
        # Update error message if necessary
        self.add_quiz_question.update_error_message()

        # Check if there are no errors and at least one test case row is added
        if self.add_quiz_question.error_message.isHidden() and self.add_quiz_question.row_counter > 0:
            # This method would be responsible for adding the quiz question to your application
            # You can implement the functionality here, such as saving the question and test cases, etc.
            # For demonstration purposes, let's just print a message
            self.add_quiz_from_update()
            
            self.back_from_quiz()
            
        elif self.add_quiz_question.row_counter == 0:
            # Show error message if no test cases are added
            self.add_quiz_question.error_message.setText("Add at least 1 test case.")
            self.add_quiz_question.error_message.show()
    def add_quiz_from_update(self):
        # if self.course_list.lineEdit.text() != '' :
            self.lq_list.quiz_gridLayout.removeItem(self.lq_list.verticalSpacer_2)
            
            button = QPushButton(self.lq_list.quiz_widget)
            self.lq_list.quiz_gridLayout.addWidget(button, self.lq_list.quiz_index, 0, 1, 1)
            button.setText(self.add_quiz_question.question_name_edit.text())
            self.lq_list.quiz_buttons.append(button)
            button.clicked.connect(self.go_to_quiz)
            
            edit = QPushButton(self.lq_list.quiz_widget)
            edit.setObjectName(f"edit_{self.lq_list.quiz_index + 1}")
            edit.setText('Edit')
            self.lq_list.quiz_gridLayout.addWidget(edit, self.lq_list.quiz_index, 1, 1, 1)
            self.lq_list.quiz_edit[edit] = self.lq_list.quiz_index
            edit.clicked.connect(self.edit_lesson)
                
            delete = QPushButton(self.lq_list.quiz_widget)
            delete.setObjectName(f"delete_{self.lq_list.quiz_index + 1}")
            delete.setText('Delete')
            self.lq_list.quiz_gridLayout.addWidget(delete, self.lq_list.quiz_index, 2, 1, 1)
            self.lq_list.quiz_delete[delete] = self.lq_list.quiz_index
            delete.clicked.connect(self.lq_list.delete_quiz)
            
            self.lq_list.quiz_index += 1

            self.lq_list.quiz_gridLayout.addItem(self.lq_list.verticalSpacer_2, self.lq_list.quiz_index, 0, 1, 1)

    def add_quiz_outside(self, courseCode, moduleIndex):
        self.add_quiz_question.add_quiz_question(courseCode, moduleIndex)
        self.go_to_lesson_quiz_index(moduleIndex)
    def add_quiz(self):
        self.stacked.setCurrentIndex(5) 
        print(self.lq_list.cID, self.lq_list.moduleIndex)
        self.add_quiz_question.add_question_button.clicked.connect(lambda: self.add_quiz_outside(self.lq_list.cID, self.lq_list.moduleIndex))
        print('exit')

        
    # def add_lesson(self):
    #     # if self.course_list.lineEdit.text() != '' :            
    #         self.lq_list.lesson_gridLayout.removeItem(self.lq_list.verticalSpacer)
            
    #         button = QPushButton(self.lq_list.lesson_widget)
    #         self.lq_list.lesson_gridLayout.addWidget(button, self.lq_list.lesson_index, 0, 1, 1)
    #         button.setText('Lesson')
    #         self.lq_list.lesson_buttons.append(button)
    #         button.clicked.connect(self.go_to_lesson)
            
    #         edit = QPushButton(self.lq_list.lesson_widget)
    #         edit.setObjectName(f"edit_{self.lq_list.lesson_index + 1}")
    #         edit.setText('Edit')
    #         self.lq_list.lesson_gridLayout.addWidget(edit, self.lq_list.lesson_index, 1, 1, 1)
    #         self.lq_list.lesson_edit[edit] = self.lq_list.lesson_index
    #         edit.clicked.connect(self.edit_lesson)
                
    #         delete = QPushButton(self.lq_list.lesson_widget)
    #         delete.setObjectName(f"delete_{self.lq_list.lesson_index + 1}")
    #         delete.setText('Delete')
    #         self.lq_list.lesson_gridLayout.addWidget(delete, self.lq_list.lesson_index, 2, 1, 1)
    #         self.lq_list.lesson_delete[delete] = self.lq_list.lesson_index
    #         delete.clicked.connect(self.lq_list.delete_lesson)
            
    #         self.lq_list.lesson_index += 1

    #         self.lq_list.lesson_gridLayout.addItem(self.lq_list.verticalSpacer, self.lq_list.lesson_index, 0, 1, 1)  
            
    # def add_quiz(self):
    #     # if self.course_list.lineEdit.text() != '' :
    #         self.lq_list.quiz_gridLayout.removeItem(self.lq_list.verticalSpacer_2)
            
    #         button = QPushButton(self.lq_list.quiz_widget)
    #         self.lq_list.quiz_gridLayout.addWidget(button, self.lq_list.quiz_index, 0, 1, 1)
    #         button.setText('Quiz')
    #         self.lq_list.quiz_buttons.append(button)
    #         button.clicked.connect(self.go_to_quiz)
            
    #         edit = QPushButton(self.lq_list.quiz_widget)
    #         edit.setObjectName(f"edit_{self.lq_list.quiz_index + 1}")
    #         edit.setText('Edit')
    #         self.lq_list.quiz_gridLayout.addWidget(edit, self.lq_list.quiz_index, 1, 1, 1)
    #         self.lq_list.quiz_edit[edit] = self.lq_list.quiz_index
    #         edit.clicked.connect(self.edit_lesson)
                
    #         delete = QPushButton(self.lq_list.quiz_widget)
    #         delete.setObjectName(f"delete_{self.lq_list.quiz_index + 1}")
    #         delete.setText('Delete')
    #         self.lq_list.quiz_gridLayout.addWidget(delete, self.lq_list.quiz_index, 2, 1, 1)
    #         self.lq_list.quiz_delete[delete] = self.lq_list.quiz_index
    #         delete.clicked.connect(self.lq_list.delete_quiz)
            
    #         self.lq_list.quiz_index += 1

    #         self.lq_list.quiz_gridLayout.addItem(self.lq_list.verticalSpacer_2, self.lq_list.quiz_index, 0, 1, 1)       
    
    
        