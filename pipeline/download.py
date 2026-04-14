from yt_dlp import YoutubeDL


class Download:
    def __init__(self, url, settings, constants):
        self.url = url
        self.settings = settings
        self.constants = constants

    def _download(self):
        with YoutubeDL(self.settings) as ydl:
            ydl.download(self.url)

    def audio(self):
        self.settings.update(
            {
                "format": "bestaudio[ext=m4a]",
                "writesubtitles": False,
                "writeautomaticsub": False,
                "writethumbnail": False,
                "embedthumbnail": False,
                "postprocessors": [],
            }
        )

        self._download()

    def playlist(self):
        if self.constants.Playlist_Download_Type == "audio":
            self.audio()
        else:
            self.settings.update(
                {
                    "format": "bestvideo[height<={PLAYLIST_DOWNLOAD_CAP}]+bestaudio[ext=m4a]"
                }
            )

        self._download()

    def video(self, fmt):
        if self.constants.Single_Download_Type == "audio":
            self.audio()
        else:
            self.settings.update({"format": f"{fmt['format_id']}+bestaudio[ext=m4a]"})

        self._download()
