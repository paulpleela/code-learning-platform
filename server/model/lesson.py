import persistent

class Lesson(persistent.Persistent):
      def __init__(self, name, file):
            self.name = name
            self.file = file# SUPPORTS 2 Formats pdf or video mp4

      def edit_details(self, video, text, image, files):
            self.video = video
            self.text = text
            self.image = image
            self.files = files
      
      def add_video(self, video):
            self.video.append(video)
      
      def remove_video(self, video):
            self.video.remove(video)

      def add_text(self, text):
            self.text.append(text)

      def remove_text(self, text):
            self.text.remove(text)

      def add_image(self, image):
            self.image.append(image)

      def remove_image(self, image):
            self.image.remove(image)

      def add_file(self, file):
            self.files.append(file)

      def remove_file(self, file):
            self.files.remove(file)

      

# The Lesson class is a simple class that contains the details of a lesson. 
# It has a video, text, image, and files.  
# The edit_details method is used to edit the details of the lesson. 
# The add_video, remove_video, add_text, remove_text, add_image, remove_image, add_files, and remove_files methods are used to add and remove the details of the lesson.