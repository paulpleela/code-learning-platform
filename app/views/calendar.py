from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QHeaderView
from PySide6.QtCore import Qt, QDate, QSize
from PySide6.QtGui import QFont, QColor  
import sys
from PySide6.QtGui import QFontMetrics
import textwrap
from PySide6.QtCore import QObject, Slot
import requests

class CalendarTable(QWidget):
    def __init__(self, username):
        super().__init__()

        self.assignments = {}
        self.current_date = QDate.currentDate()
        self.username = username

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Navigation Buttons Layout
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("<")
        self.prev_button.clicked.connect(self.prevWeek)
        self.prev_button.setFixedSize(50, 50)
        self.prev_button.setFont(QFont('Calibri', pointSize=14))
        nav_layout.addWidget(self.prev_button)

        self.title_label = QLabel("")
        self.title_label.setAlignment(Qt.AlignCenter)
        font = QFont('Calibri', pointSize=14)
        self.title_label.setFont(font)  
        self.title_label.setStyleSheet("background-color: white")
        nav_layout.addWidget(self.title_label)

        self.next_button = QPushButton(">")
        self.next_button.clicked.connect(self.nextWeek)
        self.next_button.setFixedSize(50, 50)
        self.next_button.setFont(QFont('Calibri', pointSize=14))
        nav_layout.addWidget(self.next_button)

        layout.addLayout(nav_layout)

        self.table = QTableWidget(2, 7)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.itemClicked.connect(self.handleItemClick)  
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.updateCalendar(self.username)

    def updateCalendar(self, username):

        if self.username != None:
            response = requests.get(f"http://127.0.0.1:8000/calendar/{username}")

            if response.status_code == 200:
                self.assignments = response.json()["calendar"]

        current_date = self.current_date.addDays(-self.current_date.dayOfWeek())

        start_date = current_date.toString("MMM d")
        end_date = current_date.addDays(6).toString("MMM d, yyyy")
        self.title_label.setText(f"{start_date} - {end_date}")

        print(self.assignments)
        # Clear table contents
        self.table.clearContents()

        # Remove unused rows
        while self.table.rowCount() > 2:
            self.table.removeRow(2)

        # Calculate the minimum column width based on the available space
        table_width = self.table.viewport().size().width()
        min_column_width = max(100, table_width // 7)  

        for column in range(7):
            # Set the minimum and maximum column widths
            self.table.setColumnWidth(column, min_column_width)

            day_of_week = current_date.toString("ddd")
            day_of_week_item = QTableWidgetItem(day_of_week)
            day_of_week_item.setTextAlignment(Qt.AlignCenter)
            day_of_week_item.setBackground(QColor("whitesmoke"))
            day_of_week_item.setForeground(QColor("dimgray"))
            self.table.setItem(0, column, day_of_week_item)

            day_number = current_date.day()
            day_number_item = QTableWidgetItem(str(day_number))
            font = QFont('Calibri', pointSize=14)
            day_number_item.setFont(font)
            day_number_item.setTextAlignment(Qt.AlignCenter)
            day_number_item.setBackground(QColor("whitesmoke"))
            day_number_item.setForeground(QColor("dimgray"))
            self.table.setItem(1, column, day_number_item)

            assignments = self.assignments.get(current_date.toString("yyyy-MMM-dd"), [])
            
            for row, assignment in enumerate(assignments, start=2):
                assignment_text = f"{assignment[0]}: {assignment[1]}"
                print(assignment_text)
                print(assignment_text)
                if row >= self.table.rowCount():
                    self.table.insertRow(row)
                assignment_item = QTableWidgetItem(assignment_text)
                assignment_item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, column, assignment_item)

                # Dynamically enable text wrapping if assignment text exceeds cell width
                cell_rect = self.table.visualRect(self.table.model().index(row, column))
                cell_width = cell_rect.width()
                fm = QFontMetrics(self.table.font())
                text_width = fm.boundingRect(assignment_text).width()
                if text_width > cell_width:
                    lines = textwrap.wrap(assignment, width=int(cell_width / fm.averageCharWidth()))
                    assignment_item.setText("\n".join(lines))

            if current_date == QDate.currentDate():
                for row in range(2):
                    item = self.table.item(row, column)
                    if item:
                        item.setForeground(QColor("black"))

            current_date = current_date.addDays(1)

        # Resize the table cells to fit the content after updating the calendar
        self.table.resizeRowsToContents()

    def resizeEvent(self, event):
        self.updateCalendar(self.username)

    def prevWeek(self):
        self.current_date = self.current_date.addDays(-7)  
        self.updateCalendar(self.username)

    def nextWeek(self):
        self.current_date = self.current_date.addDays(7)  
        self.updateCalendar(self.username)

    def handleItemClick(self, item):
        assignment_name = item.text()
        row = item.row()
        if row >= 2: 
            print("Clicked Assignment:", assignment_name)


class Calendar(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.calendar = CalendarTable(self.username)

        layout.addWidget(self.calendar)

        central_widget.setLayout(layout)

        self.show()

    @Slot()
    def handle_calendar_resize(self):
        # Call the resizeEvent method of the calendar widget
        self.calendar.resizeEvent(self.username)
    