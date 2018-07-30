import youtube as yt
import utils
import os

class Song:
    def __init__(self, title, *args, **kwargs):
        self.video = yt.get_video(title)
        self.name = self.video['title']
        self.length = self.video['duration']
        self.filename = utils.filename_clean(self.video['title']) + '.wav'
        if os.path.isfile(self.filename): return
        yt.download(title, '%(title)s.%%(ext)s')
