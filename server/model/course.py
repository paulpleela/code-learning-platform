import persistent

class Course(persistent.Persistent):
      def __init__(self, courseName, courseCreatedDate, courseCode, courseTeacherName, studentList, moduleList, quizzList):
            self.courseName = courseName
            self.courseCreatedDate = courseCreatedDate
            self.courseCode = courseCode
            self.courseTeacherName = courseTeacherName

            self.studentList = studentList
            self.moduleList = moduleList
            # self.studentStatus = {"username": True}
 

      def edit_details(self, courseName, courseCode, courseTeacherName):
            self.courseName = courseName
            self.courseCode = courseCode
            self.courseTeacherName = courseTeacherName

      '''Module'''
      def add_module(self, module):
            self.moduleList.append(module)
      
      def remove_module(self, module):
            self.moduleList.remove(module)

      '''Student'''
      def add_student(self, student):
            self.studentList.append(student)
      
      def remove_student(self, student):
            self.studentList.remove(student)

      '''Quizz'''
      def add_quizz(self, quizz):
            self.quizzList.append(quizz)

      def remove_quizz(self, quizz):
            self.quizzList.remove(quizz)

      def print_details(self):
            print("Course Name: ", self.courseName)
            print("Course Code: ", self.courseCode)
            print("Course Teacher Name: ", self.courseTeacherName)
            print("Student List: ", self.studentList)
            print("Module List: ", self.moduleList)
            print("Quizz List: ", self.quizzList)
      