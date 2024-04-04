import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QFrame, QTextEdit


class EditLessonForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout(self)

        # Centering the frame
        frame_layout = QVBoxLayout()
        frame_layout.setAlignment(Qt.AlignCenter)

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.NoFrame)
        frame.setMaximumSize(400, 300) 

        layout = QVBoxLayout(frame)

        self.lesson_name_label = QLabel("Lesson Name:")
        layout.addWidget(self.lesson_name_label)

        self.lesson_name_edit = QLineEdit()
        layout.addWidget(self.lesson_name_edit)

        # Increase vertical spacing between widgets
        layout.addSpacing(20)

        self.lesson_file_label = QLabel("Lesson File:")
        layout.addWidget(self.lesson_file_label)

        self.file_path_layout = QHBoxLayout() 
        self.lesson_file_edit = QTextEdit()
        self.lesson_file_edit.setReadOnly(True)
        self.file_path_layout.addWidget(self.lesson_file_edit)

        self.remove_button = QPushButton("Remove")
        self.remove_button.setFixedSize(50, 50)
        self.remove_button.clicked.connect(self.remove_file)
        self.file_path_layout.addWidget(self.remove_button)

        layout.addLayout(self.file_path_layout)
        layout.addSpacing(20)

        self.browse_button = QPushButton("Browse Files")
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        layout.addSpacing(20)

        self.error_message = QLabel()
        self.error_message.setStyleSheet("color: red")
        layout.addWidget(self.error_message)

        layout.addSpacing(20)

        self.add_button = QPushButton("Update Lesson")
        self.add_button.clicked.connect(self.add_lesson)
        layout.addWidget(self.add_button)

        frame.setLayout(layout)

        frame_layout.addWidget(frame)
        main_layout.addLayout(frame_layout)

        self.back_button = QPushButton("Back")
        main_layout.addWidget(self.back_button, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.setLayout(main_layout)

        self.file_size_limit = 500 * 1024 * 1024  # 500MB

    def browse_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf);;MP4 Files (*.mp4)")
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                file_size = os.path.getsize(file_path)
                if file_size > self.file_size_limit:
                    self.error_message.setText("Selected file must be smaller than 500MB")
                    return
                else:
                    self.error_message.clear()
                self.lesson_file_edit.setPlainText(file_path)

    def remove_file(self):
        self.lesson_file_edit.clear()

    def add_lesson(self):
        lesson_name = self.lesson_name_edit.text()
        lesson_file_path = self.lesson_file_edit.toPlainText()

        if not lesson_name and not lesson_file_path:
            self.error_message.setText("Please enter a lesson name and attach a file")
        elif not lesson_name:
            self.error_message.setText("Please enter a lesson name")
        elif not lesson_file_path:
            self.error_message.setText("Please attach a lesson file")
        else:
            print("Lesson Name:", lesson_name)
            print("Lesson File Path:", lesson_file_path)
            self.error_message.clear()
