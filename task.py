import time
import uuid


class Task:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.uuid = None

    def start(self):
        self.start_time = int(time.time())
        self.uuid = uuid.UUID

    def stop(self):
        self.end_time = int(time.time())
        self.duration = self.end_time - self.start_time
