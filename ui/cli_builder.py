import questionary
from pyfiglet import figlet_format
from rich.console import Console
from rich.padding import Padding


class CLIBuilder:
    def __init__(self):
        self.title = "celeste"
        self.desc = "Heavenly downloads, no divine intervention required."
        self.console = Console()

    def cli_banner(self):
        banner = figlet_format(self.title, font="sblood")
        # fonts: banner3-D , banner4, poison, larry3d,contrast, cosmic, roman, rowancap, sblood
        self.console.print(Padding(f"[#173024]{banner}[/]", (0, 2)))
        self.console.print(Padding(f"[dim]{self.desc}", (0, 2)))

    def url_input(self, fn_validate):
        url = questionary.text(
            "url:",
            validate=fn_validate,
            validate_while_typing=False,
            erase_when_done=True,
        ).ask()

        return url
