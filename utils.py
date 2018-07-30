import threading
import subprocess
import re

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

def filename_clean(filename):
    return re.sub(r"[\(\)]", "", re.sub(r"[& ]", "_", filename).strip("_"))

def pifm(filename, freq='103.3', bitrate='22500', stereo=True, volume='4'):
    subprocess.call(['./pifm', filename, freq, bitrate, 'stereo' if stereo else 'mono', volume])
