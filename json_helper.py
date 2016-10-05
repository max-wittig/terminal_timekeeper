import json
import os


class JsonHelper:
    def __init__(self, filename):
        self.filename = filename

    def get_json(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as f:
                return json.load(f)

    def save(self, content):
        with open(self.filename, "w") as f:
            f.write(json.dumps(content))

