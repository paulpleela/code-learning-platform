import sys
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget
from views.main_window import MainWindow
from views.login_window import LoginWindow
from views.register_window import RegisterWindow
import requests

url = "http://127.0.0.1:8000"

def authenticate():
    # widget.setCurrentIndex(2)
    data = {
        "username": login_window.username_input.text(),
        "password": login_window.password_input.text()
    }

    if len(login_window.username_input.text()) == 0:
        login_window.set_error_message("Please enter your username")
        return 
    elif len(login_window.password_input.text()) == 0:
        login_window.set_error_message("Please enter your password")
        return 
    
    response = requests.post(url + "/api/user/login", json=data)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        widget.setCurrentIndex(2)
        widget.setWindowTitle("PyQuizT")
    else:
        try:
            response_data = response.json()
            error_detail = response_data.get('detail', 'An error occured')
            login_window.set_error_message(error_detail)
        except ValueError:
            error_detail = 'Error parsing response JSON'
            login_window.set_error_message('An error occured')
        print("Error:", error_detail)



def register():
    data = {
        "username": register_window.username_input.text(),
        "password": register_window.password_input.text(),
        "role": register_window.role_selector.currentData()
    }
    
    if len(register_window.username_input.text()) == 0:
        register_window.set_error_message("Please enter a username")
        return 
    elif len(register_window.password_input.text()) == 0:
        register_window.set_error_message("Please enter a password")
        return 
    elif register_window.password_input.text() != register_window.confirm_input.text():
        register_window.set_error_message("Passwords to not match")
        return
    
    response = requests.post(url + "/api/user/register", json=data)
    print(response)
    if response.status_code == 200:
        response_data = response.json()
        go_to_login()
    else:
        try:
            response_data = response.json()
            error_detail = response_data.get('detail', 'An error occured')
            register_window.set_error_message(error_detail)
        except ValueError:
            error_detail = 'Error parsing response JSON'
            register_window.set_error_message('An error occured')
        print("Error:", error_detail)



def go_to_register():
    widget.setCurrentIndex(1)
    widget.setWindowTitle("Register | PyQuizT")

def go_to_login():
    widget.setCurrentIndex(0)
    widget.setWindowTitle("Login | PyQuizT")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("app/views/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    widget = QStackedWidget()
    login_window = LoginWindow()
    register_window = RegisterWindow()
    main_window = MainWindow()
    
    main_window.ui.exit_btn_1.clicked.connect(go_to_login)
    main_window.ui.exit_btn_2.clicked.connect(go_to_login)

    login_window.login_button.clicked.connect(authenticate)
    login_window.goto_register_button.clicked.connect(go_to_register)
    register_window.register_button.clicked.connect(register)
    register_window.goto_login_button.clicked.connect(go_to_login)

    widget.addWidget(login_window)
    widget.addWidget(register_window)
    widget.addWidget(main_window)

    widget.resize(950, 600)
    widget.setWindowTitle("Login | PyQuizT")
    widget.show()

    sys.exit(app.exec())
