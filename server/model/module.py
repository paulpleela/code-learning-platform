import persistent

class Module(persistent.Persistent):
      def __init__(self, Name, LessonList, QuizzList, DueDate, which_student_finsished_StatusDict):
            self.name = Name
            self.lessonList = LessonList        # List of lesson objects
            self.quizzList = QuizzList  # List of question objects
            self.dueDate = DueDate              # Deadline for the module
            self.which_student_finsished_StatusDict = which_student_finsished_StatusDict # {"username": True}


      def checkLesson_ByIndex(self, lessonIndex):
            if lessonIndex < len(self.LessonList):
                  return True
            else:
                  return False
            
      def checkQuizz_ByIndex(self, quizzIndex):
            if quizzIndex < len(self.quizzList):
                  return True
            else:
                  return False
            
      
      def edit_details(self, moduleName, moduleDescription, moduleDueDate):
            self.Name = moduleName
            self.Description = moduleDescription
            self.DueDate = moduleDueDate

      def add_lesson(self, lesson):
            self.LessonList.append(lesson)

      def remove_lesson(self, lesson):
            self.LessonList.remove(lesson)
      
      def add_question(self, question):
            self.QuestionsList.append(question)
      
      def remove_question(self, question):
            self.QuestionsList.remove(question)

      

            
      
      