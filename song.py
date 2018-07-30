import youtube as yt
import utils

class Song:
    def __init__(self, title, *args, **kwargs):
        self.video = yt.get_video(title)
        self.name = self.video['title']
        self.length = self.video['duration']
        self.filename = utils.filename_clean(self.video['title']) + '.wav'
        yt.download(title, '%(title)s.%%(ext)s')
