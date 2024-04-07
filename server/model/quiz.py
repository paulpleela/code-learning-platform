import persistent

class Quiz(persistent.Persistent):
      def __init__(self, questionName, questionInstruction,inputVarNameList, testCaseDict, submissionDict, which_student_finsished_StatusList):
            self.questionName = questionName
            self.questionInstruction = questionInstruction
            self.inputVarNameList = inputVarNameList

            self.testCaseDict = testCaseDict                # {(1,2,3): "", }
            self.submissionDict = submissionDict            # {"username": submission}
            self.which_student_finsished_StatusList = which_student_finsished_StatusList # [username, username, username]
      


      def edit_details(self, questionText, maxScore, TimeLimit):
            self.questionText = questionText
            self.maxScore = maxScore
            self.TimeLimit = TimeLimit


      
