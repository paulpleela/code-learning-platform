from ZODB import FileStorage, DB
import transaction
import sys
import os
import BTrees.OOBTree

model_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model'))
sys.path.append(model_dir)

from model.user import *
from databaseHelper.databaseHelper import *

from model.user import *
from model.course import *
from model.lesson import *
from model.module import *
from model.question import *
from model.submission import *
from model.testCaseResult import *
from model.testCase import *


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
