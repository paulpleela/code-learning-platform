from ZODB import FileStorage, DB
import transaction
import sys
import os
import BTrees.OOBTree
import random
import string
from model.user import *
import bcrypt

'''
Database stored in ZODB

Teacher
    - name
    - password
    - role
    - ownedCourseList

Student
    - name
    - password
    - role
    - enrolledCourseList

Course
    - name
    - teacherName
    - courseCode
    - lessonList
    - studentList
    - moduleList
    - quizzList

Lesson
    - name
    - lessonContent
    - lessonType
    - lessonDate

Module
    - name
    - lessonList

Quizz
    - name
    - questionList

Question
    - question
    - answerList

Answer
    - answer
    - isCorrect

Submission
    - studentName
    - quizzName
    - answerList

TestCase
    - input
    - output

TestCaseResult
    - studentName
    - quizzName
    - testCaseList
    - result

'''
class CourseCodeGenerator:
    def __init__(self):
        self.used_course_codes = set()

    def generate_course_code(self, prefix='C', length=6):
        while True:
            # Generate a random portion for the course code
            random_portion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            # Combine the prefix with the random portion
            course_code = f'{prefix}{random_portion}'
            # Check if the generated course code is unique
            if course_code not in self.used_course_codes:
                self.used_course_codes.add(course_code)
                return course_code


class UserRegistration:
    def __init__(self, root):
        self.root = root

    def register_user(self, user):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        if user.role == "student":
            if not hasattr(self.root, 'students'):
                self.root.students = BTrees.OOBTree.BTree()
            student = Student(user.username, hashed_password, user.role, [])
            self.root.students[student.name] = student
        elif user.role == "teacher":
            if not hasattr(self.root, 'teachers'):
                self.root.teachers = BTrees.OOBTree.BTree()
            teacher = Teacher(user.username, hashed_password, user.role, [])
            self.root.teachers[teacher.name] = teacher
        transaction.commit()

class UserAuthentication:
    def __init__(self, root):
        self.root = root

    def student_exists(self, student_name):
        if hasattr(self.root, 'students') and student_name in self.root.students:
            return True
        return False

    def teacher_exists(self, teacher_name):
        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            return True
        return False

    def login_user(self, username, password):
        if hasattr(self.root, 'students') and username in self.root.students:
            user = self.root.students[username]
            if bcrypt.checkpw(password.encode('utf-8'), user.password):
                return user
        elif hasattr(self.root, 'teachers') and username in self.root.teachers:
            user = self.root.teachers[username]
            if bcrypt.checkpw(password.encode('utf-8'), user.password):
                return user
        return None

    def get_user_details(self):
        if hasattr(self.root, 'students'):
            for student in self.root.students.values():
                student.print_details()
        if hasattr(self.root, 'teachers'):
            for teacher in self.root.teachers.values():
                teacher.print_details()

class CourseOperations:
    def __init__(self, root):
        self.root = root

    def get_course_by_code(self, course_code):
        if hasattr(self.root, 'courses'):
            return self.root.courses.get(course_code)
        return None
    
    def get_all_courses(self):
        if hasattr(self.root, 'courses'):
            return self.root.courses.values()
        return []

    ''' -----------------What Student can do to the course----------------- '''
    def enroll_course(self, course_code, student_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:

            if hasattr(self.root, 'students') and student_name in self.root.students:
                student = self.root.students[student_name]
                student.enrolledCourseList.append(course_code)
                transaction.commit()
            transaction.commit()
        
        # add student to the student list of the course
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'studentList'):
                course.studentList.append(student_name)
                transaction.commit()

    def unenroll_course(self, course_code, student_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:

            if hasattr(self.root, 'students') and student_name in self.root.students:
                student = self.root.students[student_name]
                student.enrolledCourseList.remove(course_code)
                transaction.commit()
            transaction.commit()
        
        # remove student from the student list of the course
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'studentList'):
                course.studentList.remove(student_name)
                transaction.commit()
    ''' -----------------What Teacher can do to the course----------------- '''

    def create_course(self, course, teacher_name):
        if not hasattr(self.root, 'courses'):
            self.root.courses = BTrees.OOBTree.BTree()
        self.root.courses[course.courseCode] = course

        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            teacher = self.root.teachers[teacher_name]
            teacher.ownedCourseList.append(course)
            transaction.commit()
        transaction.commit()

        
    def get_courses_by_teacherName(self, teacher_name):
        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            teacher = self.root.teachers[teacher_name]
            return teacher.ownedCourseList
        return []
    
    # update course by course code and updated course
    def update_course(self, course_code, updated_course):
        
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            self.root.courses[course_code] = updated_course
            transaction.commit()

    def update_courseName_ByCourseCode(self, course_code, updated_courseName):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            course.courseName = updated_courseName
            transaction.commit()

    # delete course by course code
    def delete_course_ByCourseCode(self, course_code, teacher_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            del self.root.courses[course_code]
            transaction.commit()

        # remove the course from the teacher's owned course list
        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            teacher = self.root.teachers[teacher_name]
            if teacher.checkCourse_ByCourseCode(course_code):
                teacher.ownedCourseList.remove(course_code)
                transaction.commit()

        # remove the course from the student's enrolled course list
        if hasattr(self.root, 'students'):
            for student in self.root.students.values():
                if student.checkCourse_ByCourseCode(course_code): # -> True
                    student.enrolledCourseList.remove(course_code)
                    transaction.commit()  
        transaction.commit()

class ModuleOperations:
    def __init__(self, root):
        self.root = root

    ''' -----------------What Both students and teachers can do to the module-----------------'''
    def getModule_ByIndex(self, course_code, moduleIndex):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and moduleIndex in course.moduleList:
                return course.moduleList.get(moduleIndex)
        return None
    
    def get_all_modules(self, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList'):
                return course.moduleList.values()
        return []
    ''' -----------------What Teacher can do to the module-----------------'''
    def create_module(self, module, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if not hasattr(course, 'moduleList'):
                course.moduleList = BTrees.OOBTree.BTree()
            course.add_module(module)

            transaction.commit()

    def update_module(self, course_code, moduleIndex, updated_module):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and moduleIndex in course.moduleList:
                course.moduleList[moduleIndex] = updated_module
                transaction.commit()

    def delete_module(self, course_code, moduleIndex):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and moduleIndex in course.moduleList:
                del course.moduleList[moduleIndex]
                transaction.commit()


class LessonOperations:
    def __init__(self, root):
        self.root = root

    ''' -----------------What Both students and teachers can do to the lesson-----------------'''
    def get_lesson_ByIndex(self, course_code, module_index, lesson_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):
                    return module.moduleLessonList[lesson_index]
        return None

    def get_all_lessons(self, course_code, module_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                return module.LessonList
        return []
    
    ''' -----------------What Teacher can do to the lesson-----------------'''
    def create_lesson(self, course_code, lesson):
        # Check if the course exists

        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            
            # first go to the module list of the course
            if hasattr(course, 'moduleList'):
                for module in course.moduleList.values():
                    if hasattr(module, 'lessonList'):
                        module.lessonList.append(lesson)
                        transaction.commit()
 

    def update_lesson_ByIndex(self, course_code, module_index, lesson_index, updated_lesson):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):    # True
                    module.moduleLessonList[lesson_index] = updated_lesson
                    transaction.commit()
        
    def delete_lesson_ByIndex(self, course_code, module_index, lesson_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):    # True
                    del module.moduleLessonList[lesson_index]
                    transaction.commit()

class QuizzOperations:
    def __init__(self, root):
        self.root = root

    ''' -----------------What Both students and teachers can do to the quizz-----------------'''
    def get_quizz_ByIndex(self, course_code, module_index, quizz_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                if module.checkQuizz_ByIndex(quizz_index):
                    return module.QuizzList[quizz_index]
        return None

    def get_all_quizzs(self, course_code, module_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                return module.QuizzList
        return []

    ''' -----------------What Teacher can do to the quizz-----------------'''
    def create_quizz(self, course_code, quizz):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            
            # first go to the module list of the course
            if hasattr(course, 'moduleList'):
                for module in course.moduleList.values():
                    if hasattr(module, 'quizzList'):
                        module.quizzList.append(quizz)
                        transaction.commit()


    def update_quizz_ByIndex(self, course_code, module_index, quizz_index, updated_quizz):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                if module.checkQuizz_ByIndex(quizz_index):
                    module.QuizzList[quizz_index] = updated_quizz
                    transaction.commit()

    def delete_quizz_ByIndex(self, course_code, module_index, quizz_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                if module.checkQuizz_ByIndex(quizz_index):
                    del module.QuizzList[quizz_index]
                    transaction.commit()
class TestCaseOperations:
    def __init__(self, root):
        self.root = root

    

class ZODBHelper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.storage = FileStorage.FileStorage(self.db_file)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

        self.user_registration = UserRegistration(self.root)
        self.user_authentication = UserAuthentication(self.root)

        self.course_operations = CourseOperations(self.root)

        self.module_operations = ModuleOperations(self.root) 

        self.lesson_operations = LessonOperations(self.root)
        self.quizz_operations = QuizzOperations(self.root)   

    def close(self):
        self.connection.close()
