import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QFile, QTextStream

from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        
        self.ui.customers_btn_1.clicked.connect(self.on_customers_btn_toggled)
        self.ui.customers_btn_2.clicked.connect(self.on_customers_btn_toggled)
        
        self.ui.home_btn_1.clicked.connect(self.on_home_btn_toggled)
        self.ui.home_btn_2.clicked.connect(self.on_home_btn_toggled)
        
        self.ui.dashborad_btn_1.clicked.connect(self.on_dashborad_btn_toggled)
        self.ui.dashborad_btn_2.clicked.connect(self.on_dashborad_btn_toggled)
        
        self.ui.orders_btn_1.clicked.connect(self.on_orders_btn_toggled)
        self.ui.orders_btn_2.clicked.connect(self.on_orders_btn_toggled)
        
        self.ui.products_btn_1.clicked.connect(self.on_products_btn_toggled)
        self.ui.products_btn_2.clicked.connect(self.on_products_btn_toggled)
        
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


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


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



