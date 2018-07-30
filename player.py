from utils import threaded, pifm
from song import Song
import time

class Player:
    def __init__(self, *args, **kwargs):
        self.queue = []
        self.current = None
        self.playing = False
        self.looping = False

    @threaded
    def play(self):
        if not self.queue: return
        self.current = self.queue.pop(0)
        self.playing = True
        print(f"Playing {self.current.name}...")
        pifm(self.current.filename, bitrate="48000")
        print("Song played")
        self.playing = False

    @threaded
    def add_song(self, song):
        print(f"Downloading {song}...")
        s = Song(song)
        print("Song downloaded")
        self.queue.append(s)

    @threaded
    def start(self):
        self.looping = True
        while self.queue:
            self.play()
            time.sleep(2)
        self.looping = False
