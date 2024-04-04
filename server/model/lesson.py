import persistent

class Lesson(persistent.Persistent):
      def __init__(self, name, filePath):
            self.name = name
            self.filePath = filePath      # file path name SUPPORTS 2 Formats pdf or video mp4      

      def edit_details(self, name, filePath):
            self.name = name
            self.filePath = filePath

# The Lesson class is a simple class that contains the details of a lesson. 
# It has a video, text, image, and files.  
# The edit_details method is used to edit the details of the lesson. 
# The add_video, remove_video, add_text, remove_text, add_image, remove_image, add_files, and remove_files methods are used to add and remove the details of the lesson.