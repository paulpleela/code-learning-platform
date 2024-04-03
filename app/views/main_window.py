from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
from .sidebar import Sidebar
from PySide6.QtCore import QObject, Signal

class MainWindow(QMainWindow):

    calendarResizeSignal = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Sidebar()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dashboard_btn_2.setChecked(True)
        
        self.ui.dashboard_btn_1.clicked.connect(self.on_dashboard_btn_toggled)
        self.ui.dashboard_btn_2.clicked.connect(self.on_dashboard_btn_toggled)
        
        self.ui.calendar_btn_1.clicked.connect(self.on_calendar_btn_toggled)
        self.ui.calendar_btn_2.clicked.connect(self.on_calendar_btn_toggled)
        
        self.ui.mycourses_btn_1.clicked.connect(self.on_mycourses_btn_toggled)
        self.ui.mycourses_btn_2.clicked.connect(self.on_mycourses_btn_toggled)
        
        self.ui.certificates_btn_1.clicked.connect(self.on_certificates_btn_toggled)
        self.ui.certificates_btn_2.clicked.connect(self.on_certificates_btn_toggled)
        
    #     self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)

    # ## Function for changing page to user page
    # def on_user_btn_clicked(self):
    #     self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [0, 1, 2,3 , 4, 5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_dashboard_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_calendar_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.calendarResizeSignal.emit()

    def on_mycourses_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_certificates_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    # def on_customers_btn_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)
