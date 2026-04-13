from yt_dlp import YoutubeDL


class Fetcher:
    def __init__(self, url, settings):
        self.url = url
        self.settings = settings
        self.info = self.fetch_info()

    def fetch_info(self):

        with YoutubeDL(self.settings) as ydl:
            return ydl.extract_info(self.url, download=False)
