import persistent

class Module(persistent.Persistent):
      def __init__(self, Name, LessonList, QuizzList, DueDate, students_completed):
            self.name = Name
            self.lessonList = LessonList        # List of lesson objects
            self.quizzList = QuizzList  # List of quizz objects
            self.dueDate = DueDate              # Deadline for the module
            self.students_completed = students_completed    # [username1, username2, username3]


      def checkLesson_ByIndex(self, lessonIndex):
            if int(lessonIndex) < len(self.lessonList):
                  return True
            else:
                  return False
            
      def checkQuizz_ByIndex(self, quizzIndex):
            if int(quizzIndex) < len(self.quizzList):
                  return True
            else:
                  return False

      def checkEveryQuizzCompleted_byWhichStudent_And_add_studentName(self):
            # if student name is in the quiz.which_student_finsished_StatusList, then the student has completed the quiz and add the student name to the students_completed list
            for quizz in self.quizzList:
                  for studentName in quizz.which_student_finsished_StatusList:
                        if studentName not in self.students_completed:
                              self.students_completed.append(studentName)
      
      def edit_details(self, moduleName, moduleDescription, moduleDueDate):
            self.Name = moduleName
            self.Description = moduleDescription
            self.DueDate = moduleDueDate

      def add_lesson(self, lesson):
            self.lessonList.append(lesson)

      def remove_lesson(self, lesson):
            self.lessonList.remove(lesson)
      
      def add_question(self, question):
            self.QuestionsList.append(question)
      
      def remove_question(self, question):
            self.QuestionsList.remove(question)

      

            
      
      