import questionary
from rich.console import Console


class CLIBuilder:
    def __init__(self):
        self.console = Console()

    def url_input(self, fn_validate):
        url = questionary.text(
            "url:",
            validate=fn_validate,
            validate_while_typing=False,
            erase_when_done=True,
        ).ask()

        return url
