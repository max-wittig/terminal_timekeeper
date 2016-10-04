from json_helper import *


class TimeKeeper:
    def __init__(self):
        self.json = []
        self.projects = []
        self.save_objects = []
        self.filename = "timekeeper.json"
        self.json_helper = JsonHelper(self.filename)
        self.load_json()

    def load_json(self):
        self.json = self.json_helper.get_json()

    def load_projects(self):
        self.projects = self.json["saveProjectArray"]
        print(self.projects)