from PySide6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets


class VerySimpleMediaPlayer(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.open_file_button = QtWidgets.QPushButton("Open file")
        self.open_file_button.clicked.connect(self.open_file)

        self.media_player = QtMultimedia.QMediaPlayer(self)
        self.media_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.media_player.setVideoOutput(self.media_widget)
        self.media_widget.show()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.media_widget)
        self.setLayout(layout)

    def open_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose video file to load")
        self.media_player.setMedia(QtCore.QUrl.fromLocalFile(filepath))
        self.media_player.setVolume(20)
        self.media_player.play()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = QtWidgets.QMainWindow()

    example_widget = VerySimpleMediaPlayer(main_window)
    main_window.setCentralWidget(example_widget)

    main_window.setVisible(True)
    app.exec()