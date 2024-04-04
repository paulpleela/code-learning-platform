import persistent

class Module(persistent.Persistent):
      def __init__(self, moduleName, moduleDescription, moduleLessonList, moduleQuestionsList, moduleDueDate, moduleType, moduleStatus):
            self.moduleName = moduleName
            self.moduleDescription = moduleDescription
            self.moduleLessonList = moduleLessonList
            self.moduleQuestionsList = moduleQuestionsList
            self.moduleDueDate = moduleDueDate              # Deadline for the module
            self.moduleStatus = moduleStatus
            # self.studentStatus = {"username": True}

      def edit_details(self, moduleName, moduleDescription, moduleDueDate):
            self.moduleName = moduleName
            self.moduleDescription = moduleDescription
            self.moduleDueDate = moduleDueDate

      def add_lesson(self, lesson):
            self.moduleLessonList.append(lesson)

      def remove_lesson(self, lesson):
            self.moduleLessonList.remove(lesson)
      
      def add_question(self, question):
            self.moduleQuestionsList.append(question)
      
      def remove_question(self, question):
            self.moduleQuestionsList.remove(question)

      

            
      
      