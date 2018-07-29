import youtube as yt
import utils

class Song:
    def __init__(self, title, *args, **kwargs):
        self.name = yt.get_title(title)
        self.length = yt.get_duration(title)
        self.filename = utils.filename_clean(yt.get_filename(title)) + '.wav'
        yt.download(title, self.filename)
