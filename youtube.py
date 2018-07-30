import youtube_dl

opts = {"default_search": "ytsearch",
        "quiet": True,
        "restrictfilenames": True,
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }]}
yt = youtube_dl.YoutubeDL

class VideoNotFound(Exception):
    pass

def get_video(value):
    videos = yt({'simulate':True,**opts}).extract_info(value)['entries']
    if not videos:
        raise VideoNotFound()
    return videos[0]

def download(value, filename, search=True):
    yt({'outtmpl':filename,**opts}).extract_info(value)

