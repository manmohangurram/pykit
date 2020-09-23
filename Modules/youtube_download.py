import os
import time

class downloader:

    def __init__(self, url, resolution, location):
        self.url = url
        self.location = os.path.join(os.path.expanduser('~'),location)
        self.resolution = resolution
    
    def audio_download(self):
        link  = f"youtube-dl -i --extract-audio --audio-format {self.resolution}  --audio-quality 0 -o '{self.location}/%(title)s.%(ext)s' {self.url}"
        os.system(link)
        time.sleep(2)

    def vedio_download(self):
        #os.system("export PATH=/media/mohan/Study\ and\ Softwares/pykit-master:$PATH")
        #os.system("cd /media/mohan/Study\ and\ Softwares/pykit-master")
        print(self.resolution,self.location)
        link = f"youtube-dl -o '{self.location}/%(title)s.%(ext)s' -f 'bestvideo[height<={self.resolution}]+bestaudio/best[height<={self.resolution}]' {self.url}"
        os.system(link)
        time.sleep(2)