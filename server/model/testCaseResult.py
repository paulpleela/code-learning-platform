import persistent

class textCaseResult(persistent.Persistent):
      def __init__(self, textCase, result, message, timeTaken, status):
            self.textCase = textCase
            self.result = result        # output of the test case
            self.message = message
            self.timeTaken = timeTaken
            self.status = status        # pass or fail

