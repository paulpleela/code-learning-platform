from pydantic import BaseModel
from typing import Optional, Dict

# abstract class User and two clases, student and teacher, inherit from it
class User:
      def __init__(self, name, password, role):
            self.name = name

            self.password = password
            self.role = role

      def edit_details(self, name, password):
            self.name = name

            self.password = password

class Student(User):
      def __init__(self, name, password, role,  enrolledCourseList):
            super().__init__(name, password, role)
  
            self.enrolledCourseList = enrolledCourseList

      def enroll_course(self, course):
            self.enrolledCourseList.append(course)

      def unenroll_course(self, course):
            self.enrolledCourseList.remove(course)

      

class Teacher(User):
      def __init__(self, name, password, role,  ownedCourseList):
            super().__init__(name, password, role)

            self.ownedCourseList = ownedCourseList

      def own_course(self, course):
            self.ownedCourseList.append(course)

      def unown_course(self, course):
            self.ownedCourseList.remove(course)

      # check course by course name
      def getCourse(self, courseName):
            for course in self.ownedCourseList:
                  if course.courseName == courseName:
                        return course
            return None
