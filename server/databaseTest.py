import unittest
import os
import BTrees.OOBTree
from ZODB import FileStorage, DB
from model.user import Student
from databaseHelper.databaseHelper import ZODBHelper
from databaseHelper.databaseHelper import CourseCodeGenerator

class TestZODBHelper(unittest.TestCase):
    def setUp(self):
        # Initialize the database
        self.db_file = 'test_database.fs'
        # Create a ZODBHelper instance
        self.db_helper = ZODBHelper(self.db_file)

    def tearDown(self):
        # Close the database connection and remove the test database file
        self.db_helper.close()
        os.remove(self.db_file)

    def test_student_operations(self):
        # Define a test student
        # name, password, role,  enrolledCourseList
        test_student = Student("John Doe", "password", "student", ["Math", "Science"])

        # Add the student
        self.db_helper.add_student(test_student.name, test_student)

        # Retrieve the student
        retrieved_student = self.db_helper.get_student("John Doe")
        self.assertEqual(retrieved_student, test_student)

        # Update the student
        updated_student = Student("John Doe", "newpassword", "student", ["Math", "English"])
        self.db_helper.update_student("John Doe", updated_student)

        # Retrieve the updated student
        retrieved_updated_student = self.db_helper.get_student("John Doe")
        self.assertEqual(retrieved_updated_student, updated_student)

        # Delete the student
        self.db_helper.delete_student("John Doe")
        deleted_student = self.db_helper.get_student("John Doe")
        self.assertIsNone(deleted_student)

class TestCourseCodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = CourseCodeGenerator()

    def test_generate_course_code(self):
        # Generate a course code
        course_code = self.generator.generate_course_code()
        # Ensure the generated code is not None
        self.assertIsNotNone(course_code)
        # Ensure the length of the generated code is correct
        self.assertEqual(len(course_code), 7)  # 'C' prefix + 6 random characters

        # Generate another course code
        course_code_2 = self.generator.generate_course_code()
        # Ensure the generated code is different from the first one
        self.assertNotEqual(course_code, course_code_2)

if __name__ == '__main__':
    unittest.main()
