import persistent

class Quiz(persistent.Persistent):
      def __init__(self, questionText, maxScore, testCasesList, TimeLimit, submissionDict, which_student_finsished_StatusDict):
            self.questionText = questionText
            self.maxScore = maxScore
            self.testCasesList = testCasesList
            self.timeLimit = TimeLimit

            self.submissionDict = submissionDict
            self.which_student_finsished_StatusDict = which_student_finsished_StatusDict # self.studentStatus = {"username": True}
      


      def edit_details(self, questionText, maxScore, TimeLimit):
            self.questionText = questionText
            self.maxScore = maxScore
            self.TimeLimit = TimeLimit

      def add_test_case(self, testCase):
            self.testCasesList.append(testCase)

      def remove_test_case(self, testCase):
            self.testCasesList.remove(testCase)
      
      def add_submission(self, submission):
            self.submissionDict.append(submission)

      def remove_submission(self, submission):
            self.submissionDict.remove(submission)
      
