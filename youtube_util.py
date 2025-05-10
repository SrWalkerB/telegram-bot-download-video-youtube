import datetime
from pytubefix import YouTube

class YoutubeUtilService:
    def __init__(self, url: str):
        self.url = url
        self.file_name = f'{datetime.datetime.now().timestamp()}.mp4'

    def getTitle(self):
        yt = YouTube(self.url)

        return yt.title
    
    def download_video(self):
        yt = YouTube(self.url)

        video = yt.streams.get_highest_resolution()

        video.download(output_path=f'./videos', filename=self.file_name)
        
        return
    
    def download_audio(self):
        yt = YouTube(self.url)

        audio = yt.streams.get_audio_only()

        audio.download(output_path=f'./audio', filename=self.file_name)

    def get_path_video(self):
        return f'./videos/{self.file_name}'
    
    def get_path_audio(self):
        return f'./audio/{self.file_name}'