import json


class Config:
    def __init__(self):
        try:
            with open("config.json", "r") as f:
                self.config = json.loads(f.read())
        except (FileExistsError, FileNotFoundError):
            with open("config.json", "w") as f:
                f.write("{}")
                self.config = {}

    def restart(self):
        self.__init__()

    def __getitem__(self, key: str):
        return self.config[key]

    def __setitem__(self, key, value):
        self.config[key] = value

    def save(self):
        with open("config.json", "w") as f:
            f.write(json.dumps(self.config))
