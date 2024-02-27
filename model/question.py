class Question:
      def __init__(self, questionText, maxScore, testCasesList, TimeLimit, submissionDict):
            self.questionText = questionText
            self.maxScore = maxScore
            self.testCasesList = testCasesList
            self.TimeLimit = TimeLimit
            self.submissionDict = submissionDict
      
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
      
