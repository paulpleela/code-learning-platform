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
    - username
    - name
    - password
    - role
    - ownedCourseList

Student
    -username
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
class CodeGenerator:
    def __init__(self):
        self.used_course_codes = set()

    def generate_code(self, prefix='C', length=6):
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
            student = Student(user.username, user.name, hashed_password, user.role, [])
            self.root.students[student.username] = student
        elif user.role == "teacher":
            if not hasattr(self.root, 'teachers'):
                self.root.teachers = BTrees.OOBTree.BTree()
            teacher = Teacher(user.username, user.name, hashed_password, user.role, [])
            self.root.teachers[teacher.username] = teacher
        transaction.commit()

class UserAuthentication:
    def __init__(self, root):
        self.root = root

    def student_exists(self, student_username):
        if hasattr(self.root, 'students') and student_username in self.root.students:
            return True
        return False

    def teacher_exists(self, teacher_username):
        if hasattr(self.root, 'teachers') and teacher_username in self.root.teachers:
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
        pass

    def get_all_courseNames(self):
        if hasattr(self.root, 'courses'):
            return [course.courseName for course in self.root.courses.values()]
        return []
    
    def get_student_course_list(self, username):
        ret = {}
        if hasattr(self.root, 'students'):
            student = self.root.students[username]
            course_codes = student.enrolledCourseList
            if hasattr(self.root, 'courses'):
                for course_code in course_codes:
                    course_obj = self.root.courses[course_code]
                    ret[course_code] = course_obj.Name
        return ret
    
    def get_teacher_course_list(self, username):
        ret = {}
        if hasattr(self.root, 'teachers'):
            teacher = self.root.teachers[username]
            course_codes = teacher.ownedCourseList
            if hasattr(self.root, 'courses'):
                for course_code in course_codes:
                    course_obj = self.root.courses[course_code]
                    ret[course_code] = course_obj.Name
        return ret
    
    ''' -----------------What Student can do to the course----------------- '''
    def enroll_course(self, course_code, student_username):
        if not hasattr(self.root, 'courses') or course_code not in self.root.courses:
            # Course not found
            return False

        if not hasattr(self.root, 'students') or student_username not in self.root.students:
            # Student not found
            return False

        # Enroll the student in the course
        student = self.root.students[student_username]
        student.enrolledCourseList.append(course_code)

        # Commit the student transaction
        transaction.commit()

        # Check if the course has a student list attribute
        course = self.root.courses[course_code]
        if hasattr(course, 'studentList'):
            course.studentList.append(student_username)

            # Commit the course transaction
            transaction.commit()

        return True


    def unenroll_course(self, course_code, student_username):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:

            if hasattr(self.root, 'students') and student_username in self.root.students:
                student = self.root.students[student_username]
                student.enrolledCourseList.remove(course_code)
                transaction.commit()
            transaction.commit()
        
        # remove student from the student list of the course
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'studentList'):
                course.studentList.remove(student_username)
                transaction.commit()
    ''' -----------------What Teacher can do to the course----------------- '''

    def create_course(self, course, teacher_username):
        if not hasattr(self.root, 'courses'):
            self.root.courses = BTrees.OOBTree.BTree()
        self.root.courses[course.courseCode] = course

        if hasattr(self.root, 'teachers') and teacher_username in self.root.teachers:
            teacher = self.root.teachers[teacher_username]
            teacher.ownedCourseList.append(course.courseCode)
            transaction.commit()
            return True
        transaction.abort()  # Rollback the transaction if the teacher is not found
        return False  # Return False if the teacher is not found

        
    def get_courses_by_teacherName(self, teacher_username):
        if hasattr(self.root, 'teachers') and teacher_username in self.root.teachers:
            teacher = self.root.teachers[teacher_username]
            return teacher.ownedCourseList
        return []
    
    # update course by course code and updated course
    def rename_course(self, course_code, newName):
        
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            self.root.courses[course_code].Name = newName
            transaction.commit()

    def update_courseName_ByCourseCode(self, course_code, updated_courseName):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            course.courseName = updated_courseName
            transaction.commit()

    # delete course by course code
    def delete_course_ByCourseCode(self, course_code, teacher_username):
        try:
            # Check if all necessary roots are present
            if not hasattr(self.root, 'courses') or not hasattr(self.root, 'teachers') or not hasattr(self.root, 'students'):
                raise Exception("Some required roots are missing.")

            if course_code in self.root.courses:
                del self.root.courses[course_code]

            # remove the course from the teacher's owned course list
            if teacher_username in self.root.teachers:
                teacher = self.root.teachers[teacher_username]
                if teacher.checkCourse_ByCourseCode(course_code):
                    teacher.ownedCourseList.remove(course_code)

            # remove the course from the student's enrolled course list
            for student in self.root.students.values():
                if student.checkCourse_ByCourseCode(course_code):
                    student.enrolledCourseList.remove(course_code)

            # Commit the transaction after all changes
            transaction.commit()
            return True  # Operation succeeded

        except Exception as e:
            # Rollback transaction in case of any exception
            transaction.rollback()
            print("An error occurred:", str(e))
            return False  # Operation failed


class ModuleOperations:
    def __init__(self, root):
        self.root = root


    ''' -----------------What Both students and teachers can do to the module-----------------'''
    def getModule_ByIndex(self, course_code, moduleIndex):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            
            if course.checkModule_ByIndex(moduleIndex):
                return course.moduleList[int(moduleIndex)]
        return None
    
    def get_all_modules(self, course_code):
        res = []
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if hasattr(course, 'moduleList'):
                module_objects = course.moduleList
                for module_obj in module_objects:
                    res.append({"name": module_obj.name, "dueDate": module_obj.dueDate, "students_completed": module_obj.students_completed})
        return res
    ''' -----------------What Teacher can do to the module-----------------'''
    def create_module(self, module, course_code):
        try:
            if hasattr(self.root, 'courses') and course_code in self.root.courses:
                course = self.root.courses[course_code]
                if not hasattr(course, 'moduleList'):
                    course.moduleList = BTrees.OOBTree.BTree()
                course.add_module(module)

                transaction.commit()
                return True  # Operation succeeded
        except Exception as e:
            # Rollback transaction in case of any exception
            transaction.rollback()
            print("An error occurred:", str(e))
            return False  # Operation failed
        
    def update_module(self, course_code, moduleIndex, updated_module):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]

            self.root.courses[course_code].moduleList[moduleIndex] = updated_module

    def delete_module(self, course_code, moduleIndex):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            
            # delete the module from the course
            del course.moduleList[int(moduleIndex)]


class LessonOperations:
    def __init__(self, root):
        self.root = root

    
    ''' -----------------What Both students and teachers can do to the lesson-----------------'''
    def get_lesson_ByIndex(self, course_code, module_index, lesson_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):    # True
                    return module.lessonList[int(lesson_index)]
        return None
    
    def get_all_lessons(self, course_code, module_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[int(module_index)]
                return module.lessonList
        return []
    
    ''' -----------------What Teacher can do to the lesson-----------------'''
    def create_lesson(self, course_code, moduleIndex, lesson):
        # Check if the course exists

        try:
            if hasattr(self.root, 'courses') and course_code in self.root.courses:
                course = self.root.courses[course_code]
                if course.checkModule_ByIndex(moduleIndex):
                    module = course.moduleList[moduleIndex]
                    if not hasattr(module, 'lessonList'):
                        module.lessonList = []
                    module.lessonList.append(lesson)
                    transaction.commit()
                    return True  # Operation succeeded
        except Exception as e:
            # Rollback transaction in case of any exception
            transaction.rollback()
            print("An error occurred:", str(e))
            return False
        
 

    def update_lesson_ByIndex(self, course_code, module_index, lesson_index, updated_lesson):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):    # True
                    module.lessonList[lesson_index] = updated_lesson
                    transaction.commit()
        
    def delete_lesson_ByIndex(self, course_code, module_index, lesson_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):    # True
                module = course.moduleList[module_index]
                if module.checkLesson_ByIndex(lesson_index):    # True
                    del module.lessonList[lesson_index]
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
                    return module.quizzList[quizz_index]
        return None

    def get_all_quizzs(self, course_code, module_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                return module.quizzList
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
                    module.quizzList[quizz_index] = updated_quizz
                    transaction.commit()

    def delete_quizz_ByIndex(self, course_code, module_index, quizz_index):
        if hasattr(self.root, 'courses') and course_code in self.root.courses:
            course = self.root.courses[course_code]
            if course.checkModule_ByIndex(module_index):
                module = course.moduleList[module_index]
                if module.checkQuizz_ByIndex(quizz_index):
                    del module.quizzList[quizz_index]
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
