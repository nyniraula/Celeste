from yt_dlp import YoutubeDL


class Fetcher:
    def __init__(self, url, settings):
        self.url = url
        self.settings = settings

    def fetch_info(self, console):

        with console.status("fetching data", spinner="dots"):
            with YoutubeDL(self.settings) as ydl:
                return ydl.extract_info(self.url, download=False)
