from input.fetcher import Fetcher
from input.url_handler import URLHandler


class InputController:
    def __init__(self, cli, settings):
        self.url_handler = URLHandler(cli)
        self.url = self.url_handler.url
        self.fetcher = Fetcher(self.url, settings)
        self.media_info = self.fetcher.fetch_info(cli.console)

        cli.media_info(self.media_info)
