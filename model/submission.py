class Submission:
      def __init__(self, pythonCode, textcaseResultList, score, submissionTime):
            self.pythonCode = pythonCode
            self.textcaseResultList = textcaseResultList
            self.score = score
            self.submissionTime = submissionTime

      def edit_details(self, pythonCode, textcaseResultList, score, submissionTime):
            self.pythonCode = pythonCode
            self.textcaseResultList = textcaseResultList
            self.score = score
            self.submissionTime = submissionTime

      def run_test_cases(self, pythonCode):
            pass

      def calculate_score(self, textcaseResultList):
            pass

      
          