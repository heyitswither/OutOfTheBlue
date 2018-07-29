from utils import threaded, pifm
from song import Song
import time

class Player:
    def __init__(self, *args, **kwargs):
        self.queue = []
        self.current = None

    @threaded
    def play(self):
        if not self.queue: return
        self.current = self.queue.pop(0)
        print("Playing song...")
        pifm(self.current.filename, bitrate="48000")
        print("Song played")

    @threaded
    def add_song(self, song):
        print("Downloading song...")
        s = Song(song)
        print("Song downloaded")
        self.queue.append(s)

    @threaded
    def start(self):
        self.play()
        time.sleep(2)
