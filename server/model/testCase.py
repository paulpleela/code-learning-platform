import persistent

class testCase(persistent.Persistent):
      def __init__(self, id, name, description, input, expectedOutput, timeOut):
            self.id = id
            self.name = name
            self.description = description
            self.input = input
            self.expectedOutput = expectedOutput
            self.timeOut = timeOut

      def edit_details(self, id, name, description, input, expectedOutput, timeOut):
            self.id = id
            self.name = name
            self.description = description
            self.input = input
            self.expectedOutput = expectedOutput
            self.timeOut = timeOut
      
      