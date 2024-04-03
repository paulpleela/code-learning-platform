from ZODB import FileStorage, DB
import transaction
import sys
import os
import BTrees.OOBTree

model_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model'))
sys.path.append(model_dir)



'''
# ZODB database setup
storage = FileStorage.FileStorage('mydatabase.fs')
db = DB(storage)
connection = db.open()
root = connection.root

# Ensure that the 'students' key exists in the root object
if not hasattr(root, 'students'):
    root.students = BTrees.OOBTree.BTree()

# Create a new student object
# name, email, password, role, studentID, enrolledCourseList
student1 = Student("John Doe", "johndoe@gmail.com", "password", "student", 1, [])

# Add the student object to the 'students' BTree
root.students['customer-1'] = student1

# Commit the transaction
transaction.commit()

# Retrieve and print the stored student object
if hasattr(root, 'students'):
    stored_student = root.students.get('customer-1')
    if stored_student:
        print("Student ID:", stored_student.studentID)
        print("Name:", stored_student.name)
        print("Email:", stored_student.email)
        print("Enrolled Courses:", stored_student.enrolledCourseList)
    else:
        print("Student not found in the database.")
else:
    print("No students stored in the database.")

# Close the connection
connection.close()
'''
class ZODBHelper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.storage = FileStorage.FileStorage(self.db_file)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

    def close(self):
        self.connection.close()

    # Student
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
        if hasattr(self.root, 'students'):
            self.root.students[str(student_name)] = new_student
            transaction.commit()

    def delete_student(self, student_name):
        if hasattr(self.root, 'students'):
            del self.root.students[str(student_name)]
            transaction.commit()
            
    # Course
    def add_course(self, course_name, course):
        if not hasattr(self.root, 'courses'):
            self.root.courses = BTrees.OOBTree.BTree()
        self.root.courses[str(course_name)] = course
        transaction.commit()
    
    def get_course(self, course_name):
        if hasattr(self.root, 'courses'):
            return self.root.courses.get(str(course_name))
        return None
    
    def update_course(self, course_name, new_course):
        if hasattr(self.root, 'courses'):
            self.root.courses[str(course_name)] = new_course
            transaction.commit()
        
    def delete_course(self, course_name):
        if hasattr(self.root, 'courses'):
            del self.root.courses[str(course_name)]
            transaction.commit()

import random
import string

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

