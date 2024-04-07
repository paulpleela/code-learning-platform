import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QGridLayout, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QRect

import requests

class QuizQuestion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Quiz Question")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Widgets for entering question name and text
        self.question_name_label = QLabel("Question Name:")
        self.question_name_edit = QLineEdit()
        self.question_instructions_label = QLabel("Question Instructions:")
        self.question_instructions_edit = QTextEdit()

        # Layout for question name and text
        question_layout = QVBoxLayout()
        question_layout.addWidget(self.question_name_label)
        question_layout.addWidget(self.question_name_edit)
        question_layout.addWidget(self.question_instructions_label)
        question_layout.addWidget(self.question_instructions_edit)

        # Widgets for entering test cases
        self.num_variables_label = QLabel("Number of Test Case Input Variables:")
        self.num_variables_edit = QLineEdit()
        self.num_variables_edit.textChanged.connect(self.clear_test_cases)  # Connect to clear test cases when text changes
        self.error_message = QLabel()
        self.error_message.setStyleSheet("color: red")
        self.error_message.hide()
        self.add_test_case_button = QPushButton("Add Test Case")
        self.add_test_case_button.clicked.connect(self.add_test_case)

        # Layout for test cases
        test_cases_layout = QVBoxLayout()
        num_variables_layout = QHBoxLayout()  # New layout for number of variables label and line edit
        num_variables_layout.addWidget(self.num_variables_label)
        num_variables_layout.addWidget(self.num_variables_edit)
        test_cases_layout.addLayout(num_variables_layout)
        test_cases_layout.addWidget(self.add_test_case_button)
        # Grid layout for test case inputs
        self.test_cases_grid_layout = QGridLayout()

        # Add layouts to main layout
        main_layout.addLayout(question_layout)
        main_layout.addLayout(test_cases_layout)
        main_layout.addLayout(self.test_cases_grid_layout)

        # Flag to track whether header has been added
        self.header_added = False

        # Counter for row headings
        self.row_counter = 0

        main_layout.addWidget(self.error_message)
        # Button to add quiz question
        self.add_question_button = QPushButton("Add Quiz Question")
        self.add_question_button.clicked.connect(self.add_quiz_question)
        main_layout.addWidget(self.add_question_button)
        
        self.go_back = QPushButton("<< Go Back")
        self.go_back.setFixedWidth(100)
        main_layout.addWidget(self.go_back)

    def clear_test_cases(self):
        # Clear all test cases from the grid layout
        while self.test_cases_grid_layout.count():
            item = self.test_cases_grid_layout.takeAt(0)
            layout_item = item.layout()
            if layout_item:
                # If the item is a layout, recursively clear its content
                self.clear_layout(layout_item)
            else:
                widget = item.widget()
                if widget:
                    # Remove the widget from its parent
                    widget.setParent(None)

        # Hide error label when text is changed
        self.error_message.hide()

        # Reset header flag
        self.header_added = False

        # Reset row counter
        self.row_counter = 0

        # Reset column stretch factors
        self.update_column_stretch_factors()

    def clear_layout(self, layout):
        # Recursively clear layout contents
        while layout.count():
            item = layout.takeAt(0)
            layout_item = item.layout()
            if layout_item:
                # If the item is a layout, recursively clear its content
                self.clear_layout(layout_item)
            else:
                widget = item.widget()
                if widget:
                    # Remove the widget from its parent
                    widget.setParent(None)

    def add_test_case(self):
        # Check if the current number of test cases exceeds the limit of 9
        if self.row_counter >= 9:
            # Show error message if the limit is reached
            self.error_message.setText("Maximum of 9 test cases allowed")
            self.error_message.show()
            return
    
        # Check if the input value is between 0 and 7
        try:
            num_variables = int(self.num_variables_edit.text())
            if num_variables < 0 or num_variables > 7:
                self.error_message.setText("Number of input variables must be between 0 and 7")
                self.error_message.show()
                return
        except ValueError:
            # Show error message if input is not valid
            self.error_message.setText("Number of test cases must be an integer")
            self.error_message.show()
            return

        # If no input variables, there can only be 1 output
        if num_variables == 0 and self.row_counter > 0:
            # Show error message if a test case row already exists
            self.error_message.setText("Only 1 expected output allowed when there are no input variables")
            self.error_message.show()
            return
        
        # Add header row if not already added
        if not self.header_added:
            header_label = QLabel("#")
            header_label.setFont(QFont("Arial", 10, QFont.Bold))
            self.test_cases_grid_layout.addWidget(header_label, 0, 0)

            if num_variables > 0:
                for col in range(num_variables):
                    label = QLineEdit(f"var_{col+1}")
                    label.setFont(QFont("Arial", 10, QFont.Bold))
                    self.test_cases_grid_layout.addWidget(label, 0, col + 1)
                output_label = QLabel("Output")
                output_label.setFont(QFont("Arial", 10, QFont.Bold))
                self.test_cases_grid_layout.addWidget(output_label, 0, num_variables + 1)
            else:
                output_label = QLabel("Output")
                output_label.setFont(QFont("Arial", 10, QFont.Bold))
                self.test_cases_grid_layout.addWidget(output_label, 0, 1)  # Only one column for output

            self.header_added = True

        # Increment row counter
        self.row_counter += 1

        # Add row number
        row_label = QLabel(str(self.row_counter))
        row_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Align text to the right and center vertically
        self.test_cases_grid_layout.addWidget(row_label, self.row_counter, 0)

        # Add input boxes for each variable and expected output
        if num_variables > 0:
            for col in range(num_variables):
                input_edit = QLineEdit()
                self.test_cases_grid_layout.addWidget(input_edit, self.row_counter, col + 1)

            # Add output box
            output_edit = QLineEdit()
            self.test_cases_grid_layout.addWidget(output_edit, self.row_counter, num_variables + 1)
        else:
            # Only one column for output
            output_edit = QLineEdit()
            self.test_cases_grid_layout.addWidget(output_edit, self.row_counter, 1)

        # Update column stretch factors
        self.update_column_stretch_factors()

    def update_column_stretch_factors(self):
        # Count the number of columns
        num_columns = self.test_cases_grid_layout.columnCount()

        # Calculate the stretch factor for each column
        stretch_factor = 1.0 / max(1, num_columns - 1)

        # Set stretch for all columns except the first one
        for col in range(1, num_columns):
            self.test_cases_grid_layout.setColumnStretch(col, stretch_factor)

    def update_error_message(self):
        # Update error label based on current state
        question_name = self.question_name_edit.text().strip()
        question_instructions = self.question_instructions_edit.toPlainText().strip()
        num_variables = int(self.num_variables_edit.text()) if self.num_variables_edit.text() else 0

        if not question_name:
            self.error_message.setText("Please enter a question name")
            self.error_message.show()
        elif not question_instructions:
            self.error_message.setText("Please enter question instructions")
            self.error_message.show()
        elif num_variables == 0 and self.row_counter == 0:
            self.error_message.setText("Add at least 1 test case")
            self.error_message.show()
        else:
            # Check if any test case input or output is empty
            empty_input_or_output = False
            for row in range(1, self.row_counter + 1):
                for col in range(1, num_variables + 2):
                    widget = self.test_cases_grid_layout.itemAtPosition(row, col).widget()
                    if isinstance(widget, QLineEdit) and widget.text().strip() == "":
                        empty_input_or_output = True
                        break
                if empty_input_or_output:
                    break

            if empty_input_or_output:
                self.error_message.setText("Enter all test cases' input and expected output")
                self.error_message.show()
            else:
                self.error_message.hide()

    def add_quiz_question(self, courseCode, moduleIndex):
        self.update_error_message()
        
        # Check if there are no errors and at least one test case row is added
        if self.error_message.isHidden() and self.row_counter > 0:
            input_var_names = []
            test_cases = {}

            for row in range(1, self.row_counter + 1):
                input_values = []
                output_value = None

                for col in range(1, self.test_cases_grid_layout.columnCount()):
                    widget = self.test_cases_grid_layout.itemAtPosition(row, col).widget()
                    if isinstance(widget, QLineEdit):
                        # Convert the text to the appropriate type
                        value = self.convert_to_python_type(widget.text().strip())
                        # If it's the last column, it's the output value
                        if col == self.test_cases_grid_layout.columnCount() - 1:
                            output_value = value
                        else:
                            input_values.append(value)

                # If there are input values and an output value, add them to test_cases dictionary
                if input_values and output_value is not None:
                    # Convert input values to a tuple and add to test_cases
                    test_cases[str(tuple(input_values))] = output_value

            # Gather input variable names from the first row
            for col in range(1, self.test_cases_grid_layout.columnCount() - 1):
                widget = self.test_cases_grid_layout.itemAtPosition(0, col).widget()
                if isinstance(widget, QLineEdit):
                    input_var_names.append(widget.text().strip())

            # Get question name and question instructions
            question_name = self.question_name_edit.text().strip()
            question_instructions = self.question_instructions_edit.toPlainText().strip()

            data = {
                "questionName": question_name,
                "questionInstruction": question_instructions,
                "inputVarNameList": input_var_names,
                "testCaseDict": test_cases
            }

            print("????", input_var_names)
            print(test_cases)

            response = requests.post(f"http://127.0.0.1:8000/quizz/{courseCode}/{moduleIndex}", json=data)

            # Check if the request was successful
            if response.status_code == 200:
                self.clear_fields()
                print("added quiz")
            else:
                print(response.text)

        elif self.row_counter == 0:
            # Show error message if no test cases are added
            self.error_message.setText("Add at least 1 test case")
            self.error_message.show()

    def convert_to_python_type(self, value):
        try:
            # Try evaluating the expression
            return eval(value)
        except Exception as e:
            # If evaluation fails, return the value as is
            return value
            
    def clear_fields(self):
        # Clear question name and instructions
        self.question_name_edit.clear()
        self.question_instructions_edit.clear()

        # Clear number of variables and test case grid
        self.num_variables_edit.clear()
        self.clear_test_cases()

        # Clear error message
        self.error_message.clear()
        self.error_message.hide()
