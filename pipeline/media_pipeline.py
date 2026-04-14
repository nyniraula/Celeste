from dataclasses import dataclass

from pipeline.download import Download
from pipeline.format_handler import FormatHandler


@dataclass
class Download_Constants:
    Single_Download_Type: str
    Playlist_Download_Type: str
    Playlist_Download_Cap: int


class MediaPipeline:
    def __init__(self, url, media_info, settings, cli):
        self.url = url
        self.formats = media_info["formats"]
        self._type = media_info.get("_type", "single")
        self.settings = settings
        self.cli = cli

        self.download_constants = Download_Constants(
            Single_Download_Type=self.settings.get(
                "single_download_type", "video"
            ).lower(),
            Playlist_Download_Type=self.settings.get(
                "playlist_download_type", "video"
            ).lower(),
            Playlist_Download_Cap=self.settings.get("playlist_download_cap", 1080),
        )

    def start_downloader(self):
        download = Download(self.url, self.settings, constants=self.download_constants)

        if self._type == "playlist":
            download.playlist()
        else:
            format_handler = FormatHandler(self.formats)
            format_handler.rank()
            displayable_fmts = format_handler.resolve_ranked()
            fmt_choice = self.cli.download_formats(displayable_fmts)
            download.video(fmt_choice)
