# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 Multimedia player example"""

import sys
from PySide6.QtCore import Qt, Slot, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QStyle, QPushButton, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget

MP4 = 'video/mp4'


class LessonVideo(QMainWindow):

    def __init__(self):
        super().__init__()

        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)

        tool_bar = self.addToolBar("Controls")
        
        self.bottom_left_toolbar = QToolBar()
        self.addToolBar(Qt.BottomToolBarArea, self.bottom_left_toolbar)

        style = self.style()

        self._play_pause_action = QAction(style.standardIcon(QStyle.SP_MediaPlay), "Play", self)
        self._play_pause_action.setCheckable(True)
        self._play_pause_action.toggled.connect(self.toggle_play_pause)
        tool_bar.addAction(self._play_pause_action)

        self._browse_slider = QSlider()
        self._browse_slider.setOrientation(Qt.Horizontal)
        self._browse_slider.sliderMoved.connect(self.seek_position)
        tool_bar.addWidget(self._browse_slider)

        self._video_widget = QVideoWidget()
        self.setCentralWidget(self._video_widget)
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.positionChanged.connect(self.update_slider_position)
        self._player.setVideoOutput(self._video_widget)

        self.go_back = QPushButton("<< Go Back")
        self.bottom_left_toolbar.addWidget(self.go_back)
        
        self.update_buttons(self._player.playbackState())

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot()
    def toggle_play_pause(self, checked):
        if checked:
            self._player.play()
            self._play_pause_action.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self._player.pause()
            self._play_pause_action.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        self._play_pause_action.setEnabled(media_count > 0)
        self._play_pause_action.setChecked(state == QMediaPlayer.PlayingState)

        if state == QMediaPlayer.PlayingState:
            self._browse_slider.setMaximum(self._player.duration())
            self._browse_slider.setEnabled(True)
        else:
            self._browse_slider.setEnabled(False)

    @Slot(int)
    def seek_position(self, position):
        self._player.setPosition(position)

    @Slot(int)
    def update_slider_position(self, position):
        self._browse_slider.setValue(position)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    def setFilePath(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self._playlist.append(url)
        self._playlist_index = len(self._playlist) - 1
        self._player.setSource(url)
        self._player.play()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     available_geometry = main_win.screen().availableGeometry()
#     main_win.resize(available_geometry.width() / 3,
#                     available_geometry.height() / 2)

#     # Set the fixed path to file
#     file_path = "path/to/mp4/file"
#     url = QUrl.fromLocalFile(file_path)
#     main_win._playlist.append(url)
#     main_win._playlist_index = len(main_win._playlist) - 1
#     main_win._player.setSource(url)
#     main_win._player.play()

#     main_win.show()
#     sys.exit(app.exec())
