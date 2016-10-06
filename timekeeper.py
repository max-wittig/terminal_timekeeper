from json_helper import *
from task import *
from project import *
from datetime import datetime
import json
from time_helper import *


class TimeKeeper:
    def __init__(self):
        self.json = None
        self.projects = []
        self.filename = "timekeeper.json"
        self.json_helper = JsonHelper(self.filename)
        self.current_project = None
        self.load_json()

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

    def get_all_tasks(self):
        task_list = []
        for project in self.projects:
            for task in project.task_list:
                task_list.append(task)
        return task_list

    def save_json(self):
        json_project_array = []
        for project in self.projects:
            current_json_project = project.to_json()
            json_project_array.append(current_json_project)

        json_task_array = []
        for task in self.get_all_tasks():
            current_json_task = task.to_json()
            json_task_array.append(current_json_task)

        save_object = {
            "saveProjectArray": json_project_array,
            "saveObjectArray": json_task_array
        }
        self.json_helper.filename = "test.json"
        self.json_helper.save(save_object)

    def load_json(self):
        """loads objects from json into memory"""
        self.json = self.json_helper.get_json()
        projects_json = self.json["saveProjectArray"]
        """all tasks from all projects"""
        task_list_json = self.json["saveObjectArray"]
        for current_project_json in projects_json:
            project_name = current_project_json["name"]
            project = Project(project_name)
            try:
                project.frozen = current_project_json["frozen"]
                project.tags = current_project_json["tags"]
            except KeyError:
                pass
            for task_json in task_list_json:
                if task_json["projectName"] == project_name:
                    task_name = task_json["taskName"]
                    start_time = TimeHelper.get_time_in_ms(json_time=task_json["startTime"])
                    end_time = TimeHelper.get_time_in_ms(json_time=task_json["endTime"])
                    duration = task_json["durationInSec"]
                    task_uuid = task_json["UUID"]
                    task = Task(task_name, project_name)
                    task.start_time = start_time
                    task.end_time = end_time
                    task.duration = duration
                    task.uuid = task_uuid
                    project.task_list.append(task)
            self.projects.append(project)
