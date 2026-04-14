import questionary
from pyfiglet import figlet_format
from rich.console import Console
from rich.padding import Padding
from rich.rule import Rule
from rich.table import Table, box


class CLIBuilder:
    def __init__(self):
        self.title = "celeste"
        self.desc = "Heavenly downloads, no divine intervention required."
        self.console = Console()

    # prints the Celeste Banner
    def cli_banner(self):
        banner = figlet_format(self.title, font="contrast")
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
        _type = info.get("_type", "single")

        T = Table(box=None, show_header=False)
        T.add_column(style="dim", width=10)
        T.add_column()

        media_title = info.get("title", "")
        channel = info.get("channel", "")

        if _type == "playlist":
            T.add_row("Playlist", f"[white]{media_title}[/]")
            T.add_row("Channel", f"[white]{channel}[/]")
            T.add_row("Items", f"[magenta]{info.get('playlist_count', '')}[/]")
        else:
            T.add_row("Title", f"[white]{media_title}[/]")
            T.add_row("Channel", f"[white]{channel}[/]")
            T.add_row("Duration", f"[magenta]{info.get('duration_string', '')}[/]")

        self.console.print(Padding(Rule(style="dim"), (0, 2)))
        self.console.print(Padding(T, (0, 2)))

    def download_formats(self, fmts):
        T = Table(box=box.SIMPLE, padding=(0, 2), pad_edge=True)

        T.add_column("[dim]#", width=3)
        T.add_column("[dim]quality")
        T.add_column("[dim]resolution")
        T.add_column("[dim]est. size")

        for i, f in enumerate(fmts):
            format_note = f.get("format_note")
            resolution = f.get("resolution")
            filesize_bytes = f.get("filesize_approx")

            est_size_mb = (
                f"{round(filesize_bytes / (1024 * 1024))} MB"
                if filesize_bytes
                else "N/A"
            )
            T.add_row(f"{i + 1}", f"{format_note}", f"{resolution}", f"{est_size_mb}")

        self.console.print(Padding(T, (0, 2)))

        format_choice = questionary.select(
            "Select a quality",
            choices=[
                (questionary.Choice(title=f"{f.get('format_note')}", value=f))
                for f in fmts
            ],
            instruction="(Arrow keys + Enter)",
        ).ask()

        return format_choice
