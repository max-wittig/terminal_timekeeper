from json_helper import *
from task import *
from project import *
from datetime import datetime
import json


class TimeKeeper:
    def __init__(self):
        self.json = None
        self.projects = []
        self.filename = "timekeeper.json"
        self.json_helper = JsonHelper(self.filename)
        self.current_project = None
        self.load_json()

    def get_time_in_ms(self, json_time):
        d = datetime.strptime(json_time, '%d.%m.%Y - %H:%M:%S')
        return int(d.timestamp())

    def get_project(self, project_name):
        for project in self.projects:
            if project_name == project.name:
                return project
        return None

    def start(self, project_name, task_name):
        project = self.get_project(project_name)
        if project is None:
            project = Project(project_name)
            self.projects.append(project)
        project.start(task_name)
        self.current_project = project

    def stop(self):
        if self.current_project is not None:
            self.current_project.stop()
        self.test()

    def test(self):
        for project in self.projects:
            print(project.name)
            for task in project.task_list:
                print(task.name + " " + str(task.start_time))

    def load_json(self):
        """loads objects from json into memory"""
        self.json = self.json_helper.get_json()
        projects_json = self.json["saveProjectArray"]
        """all tasks from all projects"""
        task_list_json = self.json["saveObjectArray"]
        for project_json in projects_json:
            project_name = project_json["name"]
            project = Project(project_name)
            for task_json in task_list_json:
                if task_json["projectName"] == project_name:
                    task_name = task_json["taskName"]
                    start_time = self.get_time_in_ms(task_json["startTime"])
                    end_time = self.get_time_in_ms(task_json["endTime"])
                    duration = task_json["durationInSec"]
                    task_uuid = task_json["UUID"]
                    task = Task(task_name)
                    task.start_time = start_time
                    task.end_time = end_time
                    task.duration = duration
                    task.uuid = task_uuid
                    project.task_list.append(task)
            self.projects.append(project)
