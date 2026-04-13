from pathlib import Path


class PathRouter:
    def __init__(self, config):
        self.output_template = config.get(
            "outtmpl", "Downloads/%(title)s - %(uploader)s_[%(height)sp].%(ext)s"
        )

    def resolve_output_path(self):

        path_segments = self.output_template.split(
            "/"
        )  # splits the outtmpl into array by /
        path_segments.pop()  # removes  the %(title)s - %(uploader)s_[%(height)sp].%(ext)s part

        relative_path = "/".join(path_segments)

        download_path = Path.home() / relative_path

        # Creates a new dir (both parent and children) if any missing according to the path, leaves it as it is if found (a safer way to not overwrite preexisting dir)
        download_path.mkdir(exist_ok=True, parents=True)
        print(download_path)
