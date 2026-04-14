from pathlib import Path


class PathRouter:
    def __init__(self, config):
        try:
            self.download_path = config["paths"]["home"]
        except KeyError:
            self.download_path = "Downloads/Celeste"

        try:
            self.temp_download_path = config["paths"]["temp"]
        except KeyError:
            self.temp_download_path = "Downloads/Celeste/.tmp"

    def resolve_output_path(self):

        whole_download_path = Path.home() / self.download_path
        whole_temp_download_path = Path.home() / self.temp_download_path

        # Checks if dir and sub dir exists and creates missing one's, doesnt touch if already exist
        whole_temp_download_path.mkdir(exist_ok=True, parents=True)

        return {
            "home": whole_download_path,
            "temp": whole_temp_download_path,
        }  # returns the whole path to update the config for all os-es
