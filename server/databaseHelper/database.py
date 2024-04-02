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

    def add_student(self, student_id, student):
        if not hasattr(self.root, 'students'):
            self.root.students = BTrees.OOBTree.BTree()
        self.root.students[str(student_id)] = student
        transaction.commit()

    def get_student(self, student_id):
        if hasattr(self.root, 'students'):
            return self.root.students.get(str(student_id))
        return None

    def update_student(self, student_id, new_student):
        if hasattr(self.root, 'students'):
            self.root.students[str(student_id)] = new_student
            transaction.commit()

    def delete_student(self, student_id):
        if hasattr(self.root, 'students'):
            del self.root.students[str(student_id)]
            transaction.commit()

# Example usage:
if __name__ == "__main__":
      # Create an instance of the helper class
      db_helper = ZODBHelper('mydatabase.fs')

      # Add a student to the database
      student1 = {"name": "John Doe", "email": "johndoe@gmail.com", "password": "password", "role": "student", "studentID": 1, "enrolledCourseList": []}
      db_helper.add_student(student1["studentID"], student1)

      # Retrieve and print the stored student object
      retrieved_student = db_helper.get_student(student1["studentID"])
      print("Retrieved Student:", retrieved_student)

      # Update the student object
      student1_updated = {"name": "John Doe", "email": "johndoe@gmail.com", "password": "newpassword", "role": "student", "studentID": 1, "enrolledCourseList": ["Math", "English"]}
      db_helper.update_student(student1_updated["studentID"], student1_updated)

      # Retrieve and print the updated student object
      retrieved_student_updated = db_helper.get_student(student1_updated["studentID"])
      print("Updated Student:", retrieved_student_updated)

      # Delete the student object
      db_helper.delete_student(student1_updated["studentID"])
      
      
      # Close the database connection
      db_helper.close()
