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


class ZODBConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.storage = FileStorage.FileStorage(self.db_file)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

    def close(self):
        self.connection.close()

# Helper class which has logic to interact with the ZODB database
class ZODBHelper:
    def __init__(self, zodb_connection):
        self.connection = zodb_connection

    # Student Registration and Login
    def add_student(self, student_name, student):
        if not hasattr(self.connection.root, 'students'):
            self.connection.root.students = BTrees.OOBTree.BTree()
        self.connection.root.students[str(student_name)] = student
        transaction.commit()

    def get_student(self, student_name):
        if hasattr(self.connection.root, 'students'):
            return self.connection.root.students.get(str(student_name))
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
    
    def get_teacher(self, teacher_name):
        if hasattr(self.connection.root, 'teachers'):
            return self.connection.root.teachers.get(str(teacher_name))
        return None
    
    def update_teacher(self, teacher_name, new_teacher):
        if hasattr(self.connection.root, 'teachers'):
            self.connection.root.teachers[str(teacher_name)] = new_teacher
            transaction.commit()
        
    def delete_teacher(self, teacher_name):
        if hasattr(self.connection.root, 'teachers'):
            del self.connection.root.teachers[str(teacher_name)]
            transaction.commit()

    
    ''' Course operations by each teacher'''
    def create_courseBy_teacher(self, courseCode, course):
        # "John" : Teacher object
        self.connection.root.courses[str(courseCode)] = course
        # "John" : Teacher("John", "password", "teacher", [])
        self.connection.root.teachers.get(str(course.teacherName)).ownedCourseList.append(courseCode)
        
    def fetch_OwnedCourseList(self, teacher_name):
        if hasattr(self.connection.root, 'teachers'):
            return self.connection.root.teachers.get(str(teacher_name)).ownedCourseList
        return None
    
    def update_courseBy_teacher(self, teacherName, courseCode, new_course):
        
        if hasattr(self.connection.root, 'teachers'):
            # root.teachers[TeacherName] = teacher objet
            self.connection.root.teachers.courses[str(courseCode)] = new_course
        transaction.commit()

    def delete_courseBy_teacher(self, courseCode, teacher_name):
        if hasattr(self.connection.root, 'courses'):
            del self.connection.root.courses[str(courseCode)]
            self.connection.root.teachers.get(str(teacher_name)).ownedCourseList.remove(courseCode)
            transaction.commit()

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
