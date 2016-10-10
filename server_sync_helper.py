import requests
import os
import json


class ServerSyncHelper:
    def __init__(self):
        self.url = None
        self.testing = False
        self.username = None
        self.password = None
        """PHP is weird"""
        self.complete = "true"
        self.filename = "server_info.json"
        self.parse_server_info()

    def parse_server_info(self):
        """because my server address is secret"""
        if self.testing:
            self.filename = "server_info_testing.json"
        if os.path.isfile(self.filename):
            with open(self.filename) as f:
                json_content = json.load(f)
                self.url = json_content["url"]
                self.username = json_content["username"],
                self.password = json_content["password"]

    def get_data(self, json_string):
        return {
            "username": self.username,
            "password": self.password,
            "jsonString": json_string,
            "complete": self.complete
        }

    def save(self, save_object):
        json_string = json.dumps(save_object)
        try:
            requests.post(self.url, self.get_data(json_string))
        except:
            print("Couldn't reach server!")
