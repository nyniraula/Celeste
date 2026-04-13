from input.url_handler import URLHandler


class InputController:
    def __init__(self, cli):
        self.cli = cli

        self.url_handler = URLHandler(cli)
