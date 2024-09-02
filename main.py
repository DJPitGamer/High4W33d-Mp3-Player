import os
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QSlider, QListWidget, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from pygame import mixer
from mutagen.mp3 import MP3
from youtube_search import YoutubeSearch
import requests
from PIL import Image
from io import BytesIO
import sys

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("High4W33d Mp3 Player")
        self.setGeometry(0, 0, 1920, 1080)
        self.showMaximized()

        # Set Dark Mode
        self.set_dark_mode()

        # Layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.song_title = QLabel("Song Title", self)
        self.song_title.setAlignment(Qt.AlignCenter)
        self.song_title.setStyleSheet("font-size: 24px; color: white;")
        self.layout.addWidget(self.song_title)

        self.artist_name = QLabel("Artist Name", self)
        self.artist_name.setAlignment(Qt.AlignCenter)
        self.artist_name.setStyleSheet("font-size: 18px; color: white;")
        self.layout.addWidget(self.artist_name)

        # Center Layout for Cover
        self.center_layout = QVBoxLayout()
        self.center_layout.setAlignment(Qt.AlignCenter)
        
        # Spacer at the top to help center the cover
        self.center_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Cover Label with large size and centered alignment
        self.cover_label = QLabel(self)
        self.cover_label.setFixedSize(600, 600)  # Increase size
        self.cover_label.setAlignment(Qt.AlignCenter)
        self.cover_label.setPixmap(QPixmap("no_cover.png"))
        self.center_layout.addWidget(self.cover_label)

        # Spacer at the bottom to help center the cover
        self.center_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Adding center_layout to the main layout
        self.layout.addLayout(self.center_layout)

        self.progress_bar = QSlider(Qt.Horizontal, self)
        self.layout.addWidget(self.progress_bar)

        # Time Display
        self.time_label = QLabel("00:00 / 00:00", self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 16px; color: white;")
        self.layout.addWidget(self.time_label)

        # Control Buttons
        self.controls_layout = QHBoxLayout()

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.prev_button)

        self.play_button = QPushButton("Play", self)
        self.play_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.play_button)

        self.next_button = QPushButton("Next", self)
        self.next_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.next_button)

        self.shuffle_button = QPushButton("Shuffle", self)
        self.shuffle_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.shuffle_button)

        self.repeat_button = QPushButton("Repeat", self)
        self.repeat_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.repeat_button)

        self.like_button = QPushButton("Like", self)
        self.like_button.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444; padding: 10px;")
        self.controls_layout.addWidget(self.like_button)

        self.layout.addLayout(self.controls_layout)

        # Song List
        self.song_list = QListWidget(self)
        self.song_list.setStyleSheet("font-size: 16px; color: white; background-color: #2b2b2b;")
        self.layout.addWidget(self.song_list)

        # Load Songs
        self.music_dir = "path/to/your/music/files"
        self.load_songs(self.music_dir)

        # Event Listeners
        self.play_button.clicked.connect(self.play_pause)
        self.next_button.clicked.connect(self.next_song)
        self.prev_button.clicked.connect(self.prev_song)
        self.shuffle_button.clicked.connect(self.shuffle_songs)
        self.repeat_button.clicked.connect(self.toggle_repeat)
        self.like_button.clicked.connect(self.like_song)
        self.song_list.itemDoubleClicked.connect(self.select_song)
        self.progress_bar.sliderMoved.connect(self.set_position)

        # Initialize Player
        self.is_playing = False
        self.is_paused = False
        self.current_song = None
        self.song_index = 0
        self.repeat_mode = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        mixer.init()

    def set_dark_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    def load_songs(self, music_dir):
        for root, dirs, files in os.walk(music_dir):
            for file in files:
                if file.endswith(".mp3"):
                    song_path = os.path.join(root, file)
                    song_name = os.path.splitext(file)[0]
                    self.song_list.addItem(song_name)

    def play_pause(self):
        if self.is_playing:
            if self.is_paused:
                mixer.music.unpause()
                self.play_button.setText("Pause")
                self.is_paused = False
            else:
                mixer.music.pause()
                self.play_button.setText("Play")
                self.is_paused = True
        else:
            if self.current_song is None:
                self.select_song(self.song_list.item(self.song_index))
            mixer.music.play()
            self.play_button.setText("Pause")
            self.is_playing = True
            self.is_paused = False

    def select_song(self, item):
        self.song_index = self.song_list.row(item)
        song_name = item.text()
        song_path = os.path.join(self.music_dir, f"{song_name}.mp3")

        self.load_cover(song_name)
        self.play_song(song_path)

        # Auslesen der Metadaten
        audio = MP3(song_path)
        tags = audio.tags
        artist_name = 'Unknown Artist'
    
        if tags:
            artist_name = tags.get('TPE1', ['Unknown Artist'])[0]

        self.song_title.setText(song_name)
        self.artist_name.setText(artist_name if artist_name else 'Unknown Artist')
    
        self.progress_bar.setRange(0, int(audio.info.length))
        self.timer.start(1000)

    def play_song(self, song_path):
        mixer.music.load(song_path)
        mixer.music.play()
        self.is_playing = True
        self.play_button.setText("Pause")
        self.current_song = song_path
        print(f"Playing: {os.path.basename(song_path)}")

    def next_song(self):
        if self.song_index < self.song_list.count() - 1:
            self.song_index += 1
        else:
            self.song_index = 0
        self.select_song(self.song_list.item(self.song_index))

    def prev_song(self):
        if self.song_index > 0:
            self.song_index -= 1
        else:
            self.song_index = self.song_list.count() - 1
        self.select_song(self.song_list.item(self.song_index))

    def shuffle_songs(self):
        song_count = self.song_list.count()
        order = list(range(song_count))
        random.shuffle(order)
        temp_items = []
        for i in order:
            temp_items.append(self.song_list.takeItem(i))
        for i in order:
            self.song_list.insertItem(i, temp_items.pop(0))

    def toggle_repeat(self):
        self.repeat_mode = (self.repeat_mode + 1) % 3
        modes = ["No Repeat", "Repeat One", "Repeat All"]
        self.repeat_button.setText(modes[self.repeat_mode])
        print(f"Repeat Mode: {modes[self.repeat_mode]}")

    def like_song(self):
        item = self.song_list.item(self.song_index)
        item.setBackground(Qt.yellow)

    def set_position(self, position):
        mixer.music.set_pos(position)

    def update_progress(self):
        if self.is_playing and not self.is_paused:
            position = mixer.music.get_pos() // 1000
            self.progress_bar.setValue(position)

            song_length = self.progress_bar.maximum()
            time_passed = f"{position // 60:02d}:{position % 60:02d}"
            total_time = f"{song_length // 60:02d}:{song_length % 60:02d}"
            self.time_label.setText(f"{time_passed} / {total_time}")

            # Check if the song has ended
            if not mixer.music.get_busy():
                if self.repeat_mode == 1:
                    print("End of song. Repeating current song.")
                    self.play_song(self.current_song)
                elif self.repeat_mode == 2 or self.song_index < self.song_list.count() - 1:
                    print("End of song. Playing next song.")
                    self.next_song()
                else:
                    print("End of song. No repeat mode active. Stopping playback.")
                    self.is_playing = False
                    self.play_button.setText("Play")
                    mixer.music.stop()

    def search_from_youtube(self, query):
        results = YoutubeSearch(query, max_results=1).to_dict()
        if results:
            video_info = results[0]
            return {
                "title": video_info["title"],
                "url": f"https://www.youtube.com/watch?v={video_info['id']}",
                "description": video_info["long_desc"],
                "publishedTime": video_info["publish_time"],
                "durationH": video_info["duration"],
                "viewH": video_info["views"],
                "thumbnail": video_info["thumbnails"][0]
            }
        return None

    def load_cover(self, song_name):
        search_result = self.search_from_youtube(song_name)
        if search_result:
            thumbnail_url = search_result["thumbnail"]
            response = requests.get(thumbnail_url)
            image = Image.open(BytesIO(response.content))
            # Save high-resolution cover temporarily
            image.save("temp_cover.jpg", quality=95)
            pixmap = QPixmap("temp_cover.jpg")
            pixmap = pixmap.scaled(self.cover_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.cover_label.setPixmap(pixmap)
        else:
            self.cover_label.setPixmap(QPixmap("no_cover.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
