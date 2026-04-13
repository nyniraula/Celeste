from pathlib import Path


class PathRouter:
    def __init__(self, config):
        self.output_template = config.get(
            "outtmpl", "Downloads/%(title)s - %(uploader)s_[%(height)sp].%(ext)s"
        )

    def resolve_output_path(self):

        download_path = (
            Path.home() / Path(self.output_template).parent
        )  # gets the parent directory of the outtmpl

        # Creates a new dir (both parent and children) if any missing according to the path, leaves it as it is if found (a safer way to not overwrite preexisting dir)
        download_path.mkdir(exist_ok=True, parents=True)
        # print(download_path)
