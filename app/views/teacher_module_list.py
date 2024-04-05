# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'module_list.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QStackedWidget, QMainWindow, QLineEdit)

from PySide6 import QtCore, QtGui, QtWidgets
import requests
class Teacher_Module_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.module = []
        self.cID = ""
        self.module_buttons = []
        self.index = 0
        
        self.edit_buttons = {}
        
        self.delete_buttons = {}   
        
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 489))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.courseID = QLabel(Form)
        self.courseID.setText(f"courseID : {self.cID}")
        self.courseID.setGeometry(QRect(200, 520, 300, 24))
        
        # for loop making pushButton and Label
        for _ in range(len(self.module)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"module_{self.index + 1}")
            button.setText(self.module[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.module_buttons.append(button)
            
            edit = QPushButton(self.scrollAreaWidgetContents)
            edit.setObjectName(f"edit_{self.index + 1}")
            edit.setText('Edit')
            self.gridLayout.addWidget(edit, self.index, 1, 1, 1)
            self.edit_buttons[edit] = self.index
            
            delete = QPushButton(self.scrollAreaWidgetContents)
            delete.setObjectName(f"delete_{self.index + 1}")
            delete.setText('Delete')
            self.delete_buttons[delete]  = self.index
            
            # delete.clicked.connect(lambda i = i: self.delete_module(i))
            delete.clicked.connect(self.delete_module)
            
            self.gridLayout.addWidget(delete, self.index, 2, 1, 1)
            self.index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        ############################################

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.enroll_btn = QPushButton(Form)
        self.enroll_btn.setObjectName(u"enroll_btn")
        self.enroll_btn.setGeometry(QRect(600, 510, 181, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(375, 510, 200, 31))
        
        # self.enroll_btn.clicked.connect(self.enroll_module)
        self.enroll_btn.setText('Add Module')
        
        self.return_2 = QPushButton(Form)
        self.return_2.setObjectName(u"return_2")
        self.return_2.setGeometry(QRect(30, 510, 131, 24))
        self.return_2.setText('Return to ...')

        QMetaObject.connectSlotsByName(Form)
        self.update_ui_with_modules()
    # setupUi
    
    def delete_module(self):
        sender_button = self.sender()
                
        position = None
        if sender_button in self.delete_buttons:
            position = self.delete_buttons[sender_button]
        
        if position is not None:
            response = requests.delete(f"http://127.0.0.1:8000/module/{self.cID}/{position}")
            print("del res", response)
            if response:
                # Remove widgets in the same row as the delete button
                for j in range(self.gridLayout.columnCount()):
                    for widget_position in range(len(self.delete_buttons)):
                        item = self.gridLayout.itemAtPosition(widget_position, j)
                        if item is not None:
                            widget = item.widget()
                            if widget is not None:
                                self.gridLayout.removeWidget(widget)
                                widget.deleteLater()
                # Clear references to deleted buttons
                self.delete_buttons.clear()
                self.edit_buttons.clear()
                self.module_buttons.clear()
                self.index = 0
                # Fetch and update modules to reflect the changes
                self.set_courseCode(self.cID)


    def set_courseCode(self, courseCode):
        self.cID = courseCode
        
        # Fetch modules data from the backend
        response = requests.get(f"http://127.0.0.1:8000/modules/{courseCode}")

        if response.status_code == 200:
            # Clear existing modules
            self.clear_modules()

            # Parse the response and add modules to the UI
            data = response.json()
            print(data)
            for module_obj in data["modules"]:
                print(module_obj)
                self.module.append(module_obj["name"])
                
            # Update the UI with new modules
            self.update_ui_with_modules()

    def clear_modules(self):
        self.module.clear()

    def update_ui_with_modules(self):
        # Clear the layout
        for i in reversed(range(self.gridLayout.count())):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Reinitialize index
        self.index = 0

        # Add new modules to the layout
        for module_name in self.module:
            # Add module button
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"module_{self.index + 1}")
            button.setText(module_name)
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.module_buttons.append(button)

            # Add edit button
            edit = QPushButton(self.scrollAreaWidgetContents)
            edit.setObjectName(f"edit_{self.index + 1}")
            edit.setText('Edit')
            self.gridLayout.addWidget(edit, self.index, 1, 1, 1)
            self.edit_buttons[edit] = self.index

            # Add delete button
            delete = QPushButton(self.scrollAreaWidgetContents)
            delete.setObjectName(f"delete_{self.index + 1}")
            delete.setText('Delete')
            self.gridLayout.addWidget(delete, self.index, 2, 1, 1)
            self.delete_buttons[delete] = self.index
            delete.clicked.connect(self.delete_module)

            self.index += 1

        # Update course ID label
        self.courseID.setText(f"courseID : {self.cID}")

        # Update the scroll area widget
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
