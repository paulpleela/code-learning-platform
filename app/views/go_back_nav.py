from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QSpacerItem, QSizePolicy

class Go_Back_Nav(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.back_button = QPushButton("<< Go Back")
        self.back_button.setFixedSize(100, 30)
        layout.addWidget(self.back_button)
