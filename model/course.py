class course:
      def __init__(self, courseName, courseCreatedDate, courseCode, courseTeacher, studentList, moduleList, quizzList):
            self.courseName = courseName
            self.courseCreatedDate = courseCreatedDate
            self.courseCode = courseCode
            self.courseTeacher = courseTeacher

            self.studentList = studentList
            self.moduleList = moduleList
            self.quizzList = quizzList
            
            

      def edit_details(self, courseName, courseCode, courseTeacher):
            self.courseName = courseName
            self.courseCode = courseCode
            self.courseTeacher = courseTeacher

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

      