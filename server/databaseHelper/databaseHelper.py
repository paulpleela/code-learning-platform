from ZODB import FileStorage, DB
import transaction
import sys
import os
import BTrees.OOBTree
import random
import string
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



# Helper class which has logic to interact with the ZODB database
class ZODBHelper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.storage = FileStorage.FileStorage(self.db_file)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

    def close(self):
        self.connection.close()

    # Student Registration and Login
    def add_student(self, student_name, student):
        if not hasattr(self.root, 'students'):
            self.root.students = BTrees.OOBTree.BTree()
        self.root.students[str(student_name)] = student
        transaction.commit()

    def get_student(self, student_name):
        if hasattr(self.root, 'students'):
            return self.root.students.get(str(student_name))
        return None

    def update_student(self, student_name, new_student):
        if hasattr(self.connection.root, 'students'):
            self.connection.root.students[str(student_name)] = new_student
            transaction.commit()

    def delete_student(self, student_name):
        if hasattr(self.connection.root, 'students'):
            del self.connection.root.students[str(student_name)]
            transaction.commit()


    # Teacher Registration and Login
    def add_teacher(self, teacher_name, teacher):
        if not hasattr(self.connection.root, 'teachers'):
            self.connection.root.teachers = BTrees.OOBTree.BTree()
        self.connection.root.teachers[str(teacher_name)] = teacher
        transaction.commit()

    ''' Course operations'''
    def store_course(self, course):
        if not hasattr(self.connection.root, 'courses'):
            self.connection.root.courses = BTrees.OOBTree.BTree()
        self.connection.root.courses[str(course.courseName)] = course
        transaction.commit()

    def get_course(self, courseCode):
        if hasattr(self.connection.root, 'courses'):
            return self.connection.root.courses.get(str(courseCode))
        return None
    
    # Course Creation, Update, and Deletion by each teacher
    def create_courseBy_teacher(self, courseCode, course):
        # "John" : Teacher object
        self.connection.root.courses[str(courseCode)] = course
        # "John" : Teacher("John", "password", "teacher", [])
        self.connection.root.teachers.get(str(course.teacherName)).ownedCourseList.append(courseCode)
    
    # check if the course exists in a teacher's ownedCourseList
    def get_course(self, course_name, teacher_name):

        self.connection.root.teachers.get(str(teacher_name)).ownedCourseList

    
    def update_course(self, course_name, new_course):
        if hasattr(self.connection.root, 'courses'):
            self.connection.root.courses[str(course_name)] = new_course
            transaction.commit()
        
    def delete_course(self, course_name):
        if hasattr(self.connection.root, 'courses'):
            del self.connection.root.courses[str(course_name)]
            transaction.commit()
