from task import *
import json


class Project:
    def __init__(self, name):
        self.name = name
        self.task_list = []
        self.frozen = False
        self.tags = None
        self.current_task = None

    def start(self, task_name):
        self.current_task = Task(task_name, self.name)
        self.current_task.start()

    def stop(self):
        if self.current_task is not None:
            self.current_task.stop()
            self.task_list.append(self.current_task)

    def get_task_names(self):
        task_names = []
        for task in self.task_list:
            if not task_names.__contains__(task.name):
                task_names.append(task.name)
        task_names.sort()
        return task_names

    def to_json(self):
        project = {
            "name": self.name,
            "frozen": self.frozen,
            "tags": self.tags,
            "taskList": self.get_task_names()
        }
        return project
