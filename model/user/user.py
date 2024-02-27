
# abstract class User and two clases, student and teacher, inherit from it
class User:
      def __init__(self, name, email, password, role):
            self.name = name
            self.email = email
            self.password = password
            self.role = role

      def edit_details(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password

class Student(User):
      def __init__(self, name, email, password, role, studentID, enrolledCourseList):
            super().__init__(name, email, password, role)
            self.studentID = studentID
            self.enrolledCourseList = enrolledCourseList

      def enroll_course(self, course):
            self.enrolledCourseList.append(course)

      def unenroll_course(self, course):
            self.enrolledCourseList.remove(course)

      

class Teacher(User):
      def __init__(self, name, email, password, role, teacherID, ownedCourseList):
            super().__init__(name, email, password, role)
            self.teacherID = teacherID
            self.ownedCourseList = ownedCourseList

      def own_course(self, course):
            self.ownedCourseList.append(course)

      def unown_course(self, course):
            self.ownedCourseList.remove(course)

      