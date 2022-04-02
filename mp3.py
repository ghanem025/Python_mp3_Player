import random
from PyQt5.QtCore import Qt, QUrl
from pathlib import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from darkstyle import change_style


def main():
    app = QApplication([])
    app = change_style(app)

    window = QWidget()
    window.setFixedHeight(300)
    window.setFixedWidth(200)

    layout = QVBoxLayout()

    search_box = QLineEdit()
    search_box.move(20, 20)
    search_box.resize(280, 40)
    song_title = QLabel()
    current_song = ''

    search_button = QPushButton('Search')
    shuffle_button = QPushButton('Shuffle Play')
    play_button = QPushButton('Play')
    pause_button = QPushButton('Pause')
    volume_up_button = QPushButton('Volume up')
    volume_down_button = QPushButton('Volume down')

    player = QMediaPlayer()

    layout.addWidget(search_box)
    layout.addWidget(search_button)
    layout.addWidget(shuffle_button)
    layout.addWidget(play_button)
    layout.addWidget(volume_up_button)
    layout.addWidget(volume_down_button)
    layout.addWidget(pause_button)

    window.setLayout(layout)

    def MusicList():
        folder = Path.cwd() / 'music'
        songs = []
        for song in folder.iterdir():
            songs.append(song)
        return songs

    list_of_songs = MusicList()
    current_song = random.choice(list_of_songs)

    def VolumeUp():  # helper functions for app
        current_volume = player.volume()
        player.setVolume(current_volume + 5)

    def VolumeDown():
        current_volume = player.volume()
        player.setVolume(current_volume - 5)
        print(current_volume)

    def ShuffleWrapper():
        ShufflePlayAudio(list_of_songs)

    def ShufflePlayAudio(list_of_songs):
        file = random.choice(list_of_songs)
        PlayAudio(file)

    def PlayWrapper():
        PlayAudio(current_song)

    def PlayAudio(file):
        print("the SONG NOW IS ", file)
        url = QUrl.fromLocalFile(str(file))
        content = QMediaContent(url)
        player.setMedia(content)
        player.play()

    def PauseAudio():
        player.pause()

    def SearchSong():
        search_box_text = search_box.text()
        current_song = search_box_text
        song_title.setText(search_box_text)
        print("song title is " + song_title.text())
        print("current song is " + current_song)
        if song_title.text() is current_song:
            print("PLAYING " + current_song)

        search_box.setText("")

        print("searching")

    shuffle_button.clicked.connect(ShuffleWrapper)
    play_button.clicked.connect(PlayAudio)
    pause_button.clicked.connect(PauseAudio)
    volume_up_button.clicked.connect(VolumeUp)
    volume_down_button.clicked.connect(VolumeDown)
    search_button.clicked.connect(SearchSong)
    play_button.show()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
