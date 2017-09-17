import requests
import os
import json


class ServerSyncHelper:
    def __init__(self, json_helper):
        self.json_helper = json_helper
        self.url = None
        self.testing = False
        self.username = None
        self.password = None
        """PHP is weird"""
        self.complete = "true"
        self.filename = "server_info.json"
        self.file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), self.filename)
        self.parse_server_info()

    def parse_server_info(self):
        """because my server address is secret"""
        if self.testing:
            self.filename = "server_info_testing.json"
        if os.path.isfile(self.file):
            with open(self.file) as f:
                json_content = json.load(f)
                self.url = json_content["url"]
                self.username = json_content["username"],
                self.password = json_content["password"]

    def get_upload_data(self, json_string):
        return {
            "username": self.username,
            "password": self.password,
            "jsonString": json_string,
            "complete": self.complete
        }

    def get_download_data(self):
        return {
            "username": self.username,
            "password": self.password
        }

    def save(self, save_object):
        json_string = json.dumps(save_object)
        try:
            requests.post(self.url, self.get_upload_data(json_string))
        except:
            print("Couldn't reach server!")

    def download_from_server(self):
        try:
            data = requests.post(self.url, self.get_download_data())
            self.json_helper.save_raw(data.text)
        except:
            print("Couldn't reach server!")
