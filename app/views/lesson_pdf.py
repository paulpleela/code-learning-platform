from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

from views.go_back_nav import Go_Back_Nav

class LessonPDF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 550)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.layout.addWidget(self.webView)

        self.nav_bar = Go_Back_Nav()
        self.layout.addWidget(self.nav_bar, alignment=Qt.AlignBottom)

        # Specify the path to the PDF file here
        pdf_path = r"path\to\file.pdf"
        if pdf_path:
            self.webView.setUrl(QUrl("file:///" + pdf_path.replace('\\', '/')))

        # self.nav_bar.previous_button.clicked.connect(self.previous_page)
        # self.nav_bar.next_button.clicked.connect(self.next_page)
        

    # def previous_page(self):
    #     print("Go to previous page")

    # def next_page(self):
    #     print("Go to next page")
