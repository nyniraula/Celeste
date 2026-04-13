from input.fetcher import Fetcher
from input.url_handler import URLHandler


class InputController:
    def __init__(self, cli, settings):
        self.url_handler = URLHandler(cli)

        self.fetcher = Fetcher(self.url_handler.url, settings)

        cli.media_info(self.fetcher.info)
