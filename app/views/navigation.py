from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QSpacerItem, QSizePolicy

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)

        self.previous_button = QPushButton("<")
        self.previous_button.setFixedSize(30, 30)
        layout.addWidget(self.previous_button)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.page_number = QLineEdit()
        self.page_number.setFixedSize(30, 30)
        self.page_number.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.page_number)

        self.total_pages_label = QLabel("/ X")
        layout.addWidget(self.total_pages_label)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.next_button = QPushButton(">")
        self.next_button.setFixedSize(30, 30)
        layout.addWidget(self.next_button)
