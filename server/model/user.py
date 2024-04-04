from pydantic import BaseModel
from typing import Optional, Dict
import persistent

# abstract class User and two clases, student and teacher, inherit from it
class User(persistent.Persistent):
      def __init__(self, name, password, role):
            self.name = name

            self.password = password
            self.role = role

      def edit_details(self, name, password):
            self.name = name

            self.password = password

class Student(User, persistent.Persistent):
      def __init__(self, name, password, role,  enrolledCourseList):
            super().__init__(name, password, role)
  
            self.enrolledCourseList = enrolledCourseList

      def enroll_course(self, courseCode):
            self.enrolledCourseList.append(courseCode)

      def unenroll_course(self, courseCode):
            self.enrolledCourseList.remove(courseCode)

      def checkCourse_ByCourseCode(self, courseCode):
            if courseCode in self.enrolledCourseList:
                  return True
            else:
                  return False
            
      def print_details(self):
            print("Name:", self.name)
            print("Role:", self.role)
            print("Enrolled Courses:", self.enrolledCourseList)

      

class Teacher(User, persistent.Persistent):
      def __init__(self, name, password, role,  ownedCourseList):
            super().__init__(name, password, role)

            self.ownedCourseList = ownedCourseList          # List of courses by courseCode
      # check course by courseCode
      def checkCourse_ByCourseCode(self, courseCode):
            if courseCode in self.ownedCourseList:
                  return True
            else:
                  return False

      def print_details(self):
            print("Name:", self.name)
            print("Role:", self.role)
            print("Owned Courses:", self.ownedCourseList)