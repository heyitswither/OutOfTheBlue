from utils import threaded, pifm

class Player:
    def __init__(self, *args, **kwargs):
        self.queue = []
        self.current = None

    @threaded
    def play(self):
        self.current = self.queue.pop(0)
        pifm(self.current.filename, bitrate="48000")

    @threaded
    def add_song(self, song):
        s = Song(song)
        self.queue.append(song)

    @threaded
    def start(self):
        while queue:
            self.play()
