import questionary
from pyfiglet import figlet_format
from rich.console import Console
from rich.padding import Padding
from rich.rule import Rule
from rich.table import Table


class CLIBuilder:
    def __init__(self):
        self.title = "celeste"
        self.desc = "Heavenly downloads, no divine intervention required."
        self.console = Console()

    # prints the Celeste Banner
    def cli_banner(self):
        banner = figlet_format(self.title, font="sblood")
        # fonts: banner3-D , banner4, poison, larry3d,contrast, cosmic, roman, rowancap, sblood
        self.console.print(Padding(f"[#ffc3ff]{banner}[/]", (0, 2)))
        self.console.print(Padding(f"[dim]{self.desc}", (0, 2)))

    # Url input UI and validation
    def url_input(self, fn_validate):
        url = questionary.text(
            "url:",
            validate=fn_validate,
            validate_while_typing=False,
            erase_when_done=True,
            qmark=">",
        ).ask()

        return url

    # Display url,title,duration
    def media_info(self, info):
        video_title = info.get("title", "")
        channel = info.get("channel", "")
        duration = info.get("duration_string", "")

        T = Table(box=None, show_header=False)
        T.add_column(style="dim", width=10)
        T.add_column()

        T.add_row("Title", f"[yellow]{video_title}[/]")
        T.add_row("Channel", f"[red]{channel}[/]")
        T.add_row("Duration", f"[purple]{duration}[/]")

        self.console.print(Padding(Rule(style="dim"), (0, 2)))
        self.console.print(Padding(T, (0, 2)))
