import os
import random

from PyQt5.QtCore import Qt, QUrl
from pathlib import *

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from darkstyle import change_style

class Utils:
    def __init__(self):
        pass

    def VolumeUp(self, player):
        current_volume = player.volume()
        player.setVolume(current_volume + 5)

    def VolumeDown(self, player):
        current_volume = player.volume()
        player.setVolume(current_volume - 5)
        print(current_volume)

    def ShufflePlayAudio(self, player):
        print("Playing random song")
        folder = Path.cwd() / 'music'
        songs = []
        for song in folder.iterdir():
            songs.append(song)
        file = random.choice(songs)
        print(songs)
        url = QUrl.fromLocalFile(str(file))
        content = QMediaContent(url)
        player.setMedia(content)
        player.play()

    def PlayAudio(self, player):
        player.play()

    def PauseAudio(self, player):
        player.pause()

    def SearchSong():
        print("searching")

class CreateApp:
    def __init__(self):
        pass

    def main(self):
        app = QApplication([])
        app = change_style(app)

        window = QWidget()
        window.setFixedHeight(300)
        window.setFixedWidth(300)

        layout = QVBoxLayout()

        search_box = QLineEdit()
        search_box.move(20, 20)
        search_box.resize(280, 40)

        shuffle_button = QPushButton('Shuffle Play')
        play_button = QPushButton('Play')
        pause_button = QPushButton('Pause')
        volume_up_button = QPushButton('Volume up')
        volume_down_button = QPushButton('Volume down')

        player = QMediaPlayer()

        layout.addWidget(search_box)
        layout.addWidget(shuffle_button)
        layout.addWidget(play_button)
        layout.addWidget(volume_up_button)
        layout.addWidget(volume_down_button)
        layout.addWidget(pause_button)

        window.setLayout(layout)

        title_of_song = QLabel()
        utils = Utils

        shuffle_button.clicked.connect(utils.ShufflePlayAudio(self, player))
        play_button.clicked.connect(utils.PlayAudio(self, player))
        pause_button.clicked.connect(utils.PauseAudio(self, player))
        volume_up_button.clicked.connect(utils.VolumeUp(self,player))
        volume_down_button.clicked.connect(utils.VolumeDown(self, player))
        play_button.show()
        window.show()
        app.exec()

if __name__ == "__main__":
    CreateApp.main(self)



