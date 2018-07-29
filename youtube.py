import subprocess

class VideoNotFound(Exception):
    pass

def get_url(value, search=True):
    key = 'ytsearch:' + value if search else value
    p = subprocess.Popen('youtube-dl -g ' + key, shell=True, stdout=PIPE, stderr=PIPE)
    if p.returncode != 0:
        return "", ""
    return p.stdout.splitlines()

def get_title(value, search=True):
    key = 'ytsearch:' + value if search else value
    p = subprocess.Popen('youtube-dl -e ' + key, shell=True, stdout=PIPE, stderr=PIPE)
    if p.returncode != 0:
        return ""
    return p.stdout

def get_duration(value, search=True):
    key = 'ytsearch:' + value if search else value
    p = subprocess.Popen('youtube-dl --get-duration ' + key, shell=True, stdout=PIPE, stderr=PIPE)
    if p.returncode != 0:
        return ""
    return p.stdout

def get_filename(value, search=True):
    key = 'ytsearch:' + value if search else value
    p = subprocess.Popen('youtube-dl -o "%%(title)s" --get-filename ' + key, shell=True, stdout=PIPE, stderr=PIPE)
    if p.returncode != 0:
        return ""
    return p.stdout

def download(value, filename, search=True):
    key = 'ytsearch:' + value if search else value
    p = subprocess.Popen(f'youtube-dl -o "{filename}" -x --audio-format wav --audio-quality 48K ' + key, shell=True, stdout=PIPE, stderr=PIPE)
    if p.returncode != 0:
        raise VideoNotFound()

