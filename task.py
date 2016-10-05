import time
import uuid
import datetime


class Task:
    def __init__(self, name, project_name):
        self.name = name
        self.project_name = project_name
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.uuid = None

    def start(self):
        self.start_time = int(time.time())
        self.uuid = str(uuid.uuid4())

    def stop(self):
        self.end_time = int(time.time())
        self.duration = self.end_time - self.start_time

    def get_run_time(self):
        return "\r"+str(time.strftime('%H:%M:%S', time.gmtime(int(time.time()) - self.start_time)))

    def to_json(self):
        task = {
            "taskName": self.name,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "durationInSec": self.duration,
            "UUID": self.uuid,
            "projectName": self.project_name
        }
        return task
