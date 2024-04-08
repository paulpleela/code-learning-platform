import persistent

class Course(persistent.Persistent):
      def __init__(self, courseName, courseCreatedDate, courseCode, courseTeacherName, studentList, moduleList, studentStatusList):
            self.Name = courseName
            self.CreatedDate = courseCreatedDate
            self.courseCode = courseCode
            self.courseTeacherName = courseTeacherName

            self.moduleList = moduleList                # List of modules objects
            self.studentList = studentList              # List of students by userName
            self.studentStatusList =  studentStatusList # [username1, username2, username3]
 
      def edit_details(self, Name, courseCode, courseTeacherName):
            self.Name = Name
            self.courseCode = courseCode
            self.courseTeacherName = courseTeacherName

      def checkStudent_ByUserName(self, userName):
            if userName in self.studentList:
                  
                  return True
            else:
                  return False
      
      def checkModule_ByIndex(self, index):
            # [Module1, Module2, Module3]
            print("Index from module", index)
            print(len(self.moduleList))
            if int(index) < len(self.moduleList):
                  print("checkmodule", int(index))
                  return True
            else:
                  return False
            
      

      def checkEveryModuleFinished_And_add_studentName(self, studentDatabase, teacherDatabase):
            # if student name is in the module.students_completed, then the student has completed the module and add the student name to the studentStatusList
            try:
                  for module in self.moduleList:
                        for studentName in module.students_completed:
                              if studentName not in self.studentStatusList:
                                    self.studentStatusList.append(studentName)
                                    teacherObject = teacherDatabase[str(self.courseTeacherName)]
                                    studentDatabase[str(studentName)].add_certification(self.Name, teacherObject.name, studentName)
                                    print("Student Status List", self.studentStatusList)
                  return True
            except Exception as e:
                  print("Error in checkEveryModuleFinished_And_add_studentName", str(e))
                  return False
      '''Module'''
      def add_module(self, module):
            self.moduleList.append(module)
      
      def remove_module(self, module):
            self.moduleList.remove(module)

      '''Student'''
      def add_student(self, student):
            self.studentList.append(student)
      
      def remove_student(self, student):
            self.studentList.remove(student)

      def print_details(self):
            print("Course Name: ", self.courseName)
            print("Course Code: ", self.courseCode)
            print("Course Teacher Name: ", self.courseTeacherName)
            print("Student List: ", self.studentList)
            print("Module List: ", self.moduleList)
      