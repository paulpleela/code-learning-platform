from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QSpacerItem, QSizePolicy

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)

        self.back_button = QPushButton("<< Go Back")
        self.back_button.setFixedSize(100, 30)
        layout.addWidget(self.back_button)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.send_button = QPushButton("Send >>")
        self.send_button.setFixedSize(100, 30)
        layout.addWidget(self.send_button)
