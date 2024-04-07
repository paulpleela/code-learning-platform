import persistent

class Submission(persistent.Persistent):
      def __init__(self, pythonCode, textcaseResultList):
            self.pythonCode = pythonCode
            self.textcaseResultList = textcaseResultList    # [none, none, fail]

