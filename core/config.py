import json


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.settings = self.load_config()

    def load_config(self):
        with open(self.filename, "r") as cfg_file:
            settings = json.load(cfg_file)

        return settings
