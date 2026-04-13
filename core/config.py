import json


class Config:
    def __init__(self, filename):
        self.filename = filename

    def load_config(self):
        with open(self.filename, "r") as cfg_file:
            cfg = json.load(cfg_file)
