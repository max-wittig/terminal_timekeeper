import uuid
import time

from helper.time_helper import TimeHelper


class Task:
    def __init__(self, name, project_name):
        """model class for a task"""
        self.name = name
        self.project_name = project_name
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.uuid = None

    def generate_uuid(self):
        self.uuid = str(uuid.uuid4())

    def start(self):
        self.start_time = int(time.time())
        self.generate_uuid()

    def stop(self):
        self.end_time = int(time.time())
        self.duration = self.end_time - self.start_time

    def get_run_time(self):
        return "\r{0} : {1} - {2}".format(self.project_name, self.name,
                                          TimeHelper.get_stopwatch_time_string(int(time.time()) - self.start_time))

    def to_json(self):
        task = {
            "projectName": self.project_name,
            "taskName": self.name,
            "startTime": TimeHelper.get_time_string(self.start_time),
            "endTime": TimeHelper.get_time_string(self.end_time),
            "durationInSec": self.duration,
            "UUID": self.uuid,
        }
        return task
