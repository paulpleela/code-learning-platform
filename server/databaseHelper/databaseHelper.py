from ZODB import FileStorage, DB
import transaction
import sys
import os
import BTrees.OOBTree
import random
import string
from model.user import *
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
        if user.role == "student":
            if not hasattr(self.root, 'students'):
                self.root.students = BTrees.OOBTree.BTree()
            student = Student(user.username, user.password, user.role, [])
            self.root.students[student.name] = student
        elif user.role == "teacher":
            if not hasattr(self.root, 'teachers'):
                self.root.teachers = BTrees.OOBTree.BTree()
            teacher = Teacher(user.username, user.password, user.role, [])
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
            if user.password == password:
                return user
        elif hasattr(self.root, 'teachers') and username in self.root.teachers:
            user = self.root.teachers[username]
            if user.password == password:
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

    def create_course(self, course, teacher_name):
        if not hasattr(self.root, 'courses'):
            self.root.courses = BTrees.OOBTree.BTree()
        self.root.courses[course.courseCode] = course

        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            teacher = self.root.teachers[teacher_name]
            teacher.ownedCourseList.append(course)
            transaction.commit()
        transaction.commit()

    def get_course_by_code(self, course_code):
        if hasattr(self.root, 'courses'):
            return self.root.courses.get(course_code)
        return None
    
    def get_all_courses(self):
        if hasattr(self.root, 'courses'):
            return self.root.courses.values()
        return []
    
    def get_courses_by_teacher(self, teacher_name):
        if hasattr(self.root, 'teachers') and teacher_name in self.root.teachers:
            teacher = self.root.teachers[teacher_name]
            return teacher.ownedCourseList
        return []

    # update course by course code and updated course
    def update_course(self, course_code, updated_course):
        
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            self.root.courses[course_code] = updated_course
            transaction.commit()

        

        '''
        # also update the course in the teacher's owned course list
        if hasattr(self.root, 'teachers'):
            for teacher in self.root.teachers.values():
                if course_code in teacher.ownedCourseList:
                    teacher.ownedCourseList[course_code] = updated_course
                    transaction.commit()
        '''

    
    # delete course by course code
    def delete_course(self, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            # remove the course from the teacher's owned course list
            if hasattr(self.root, 'teachers'):
                for teacher in self.root.teachers.values():
                    if course in teacher.ownedCourseList:
                        teacher.ownedCourseList.remove(course)
                        transaction.commit()
            del self.root.courses[course_code]
            transaction.commit()

        '''
        # also remove the course from the teacher's owned course list
        if hasattr(self.root, 'teachers'):
            for teacher in self.root.teachers.values():
                if course_code in teacher.ownedCourseList:
                    teacher.ownedCourseList.remove(course_code)
                    transaction.commit()
        '''


class LessonOperations:
    def __init__(self, root):
        self.root = root

    def create_lesson(self, lesson, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if not hasattr(course, 'lessonList'):
                course.lessonList = BTrees.OOBTree.BTree()
            course.lessonList[lesson.name] = lesson
            transaction.commit()

    def get_lesson(self, course_code, lesson_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'lessonList') and lesson_name in course.lessonList:
                return course.lessonList.get(lesson_name)
        return None

    def get_all_lessons(self, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'lessonList'):
                return course.lessonList.values()
        return []

    def update_lesson(self, course_code, lesson_name, updated_lesson):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'lessonList') and lesson_name in course.lessonList:
                course.lessonList[lesson_name] = updated_lesson
                transaction.commit()

    def delete_lesson(self, course_code, lesson_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'lessonList') and lesson_name in course.lessonList:
                del course.lessonList[lesson_name]
                transaction.commit()

class ModuleOperations:
    def __init__(self, root):
        self.root = root

    def create_module(self, module, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if not hasattr(course, 'moduleList'):
                course.moduleList = BTrees.OOBTree.BTree()
            course.moduleList[module.name] = module
            transaction.commit()

    def get_module(self, course_code, module_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and module_name in course.moduleList:
                return course.moduleList.get(module_name)
        return None

    def get_all_modules(self, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList'):
                return course.moduleList.values()
        return []

    def update_module(self, course_code, module_name, updated_module):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and module_name in course.moduleList:
                course.moduleList[module_name] = updated_module
                transaction.commit()

    def delete_module(self, course_code, module_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList') and module_name in course.moduleList:
                del course.moduleList[module_name]
                transaction.commit()

class QuizzOperations:
    def __init__(self, root):
        self.root = root

    def create_quizz(self, quizz, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if not hasattr(course, 'quizzList'):
                course.quizzList = BTrees.OOBTree.BTree()
            course.quizzList[quizz.name] = quizz
            transaction.commit()

    def get_quizz(self, course_code, quizz_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'quizzList') and quizz_name in course.quizzList:
                return course.quizzList.get(quizz_name)
        return None

    def get_all_quizzes(self, course_code):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'quizzList'):
                return course.quizzList.values()
        return []

    def update_quizz(self, course_code, quizz_name, updated_quizz):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'quizzList') and quizz_name in course.quizzList:
                course.quizzList[quizz_name] = updated_quizz
                transaction.commit()

    def delete_quizz(self, course_code, quizz_name):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'quizzList') and quizz_name in course.quizzList:
                del course.quizzList[quizz_name]
                transaction.commit()

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
        self.lesson_operations = LessonOperations(self.root)
        self.module_operations = ModuleOperations(self.root) 
        self.quizz_operations = QuizzOperations(self.root)   

    def close(self):
        self.connection.close()
