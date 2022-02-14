import os
import random

from PyQt5.QtCore import Qt, QUrl
from pathlib import *

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from darkstyle import change_style

app = QApplication([])
app = change_style(app)

window = QWidget()
layout = QVBoxLayout()
shuffle_button = QPushButton('Shuffle Play')
play_button = QPushButton('Play')
pause_button = QPushButton('Pause')
volume_up_button = QPushButton('Volume up')
volume_down_button = QPushButton('Volume down')
player = QMediaPlayer()

layout.addWidget(shuffle_button)
layout.addWidget(play_button)
layout.addWidget(volume_up_button)
layout.addWidget(volume_down_button)
layout.addWidget(pause_button)
window.setLayout(layout)


title_of_song = QLabel()


def VolumeUp():
    current_volume = player.volume()
    player.setVolume(current_volume + 5)


def VolumeDown():
    current_volume = player.volume()
    player.setVolume(current_volume - 5)
    print(current_volume)


def ShufflePlayAudio():
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


def PlayAudio():
    player.play()


def PauseAudio():
    player.pause()


shuffle_button.clicked.connect(ShufflePlayAudio)
play_button.clicked.connect(PlayAudio)
pause_button.clicked.connect(PauseAudio)
volume_up_button.clicked.connect(VolumeUp)
volume_down_button.clicked.connect(VolumeDown)
play_button.show()
window.show()
app.exec()
