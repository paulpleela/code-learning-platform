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

      # check if every submission.testCaseResultList has none in it, then the quiz is finished
      # and add the student userName to which_student_finsished_StatusList
      def checkEverySubmissionPassed_byWhichStudent_And_add_studentName(self):
            # return True if none not in the list
            try:
                  for submission in self.submissionDict.values():
                        if None not in submission.textcaseResultList:
                              self.which_student_finsished_StatusList.append(submission.userName)
                              print("Student Status List", self.which_student_finsished_StatusList)

                  return True
            except Exception as e:
                  print("Error in checkEverySubmissionPassed_byWhichStudent_And_add_studentName", str(e))
                  return False
            
