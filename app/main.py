import sys
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget
from views.main_window import MainWindow
from views.login_window import LoginWindow
from views.register_window import RegisterWindow

def authenticate():
    if True:
        widget.setCurrentIndex(2)
        widget.setWindowTitle("PyQuizT")

def go_to_register():
    widget.setCurrentIndex(1)
    widget.setWindowTitle("Register | PyQuizT")

def go_to_login():
    widget.setCurrentIndex(0)
    widget.setWindowTitle("Login | PyQuizT")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
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
    login_window.register_button.clicked.connect(go_to_register)
    register_window.login_button.clicked.connect(go_to_login)

    widget.addWidget(login_window)
    widget.addWidget(register_window)
    widget.addWidget(main_window)

    widget.setFixedHeight(600)
    widget.setFixedWidth(950)
    widget.setWindowTitle("Login | PyQuizT")
    widget.show()

    sys.exit(app.exec())
