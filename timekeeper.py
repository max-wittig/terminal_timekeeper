from json_helper import *
from project import *
from terminal_ui_helper import *


class TimeKeeper:
    def __init__(self):
        self.terminal_ui_helper = TerminalUIHelper(self)
        self.filename = "timekeeper.json"
        self.json_helper = JsonHelper(self.filename)
        self.projects = self.json_helper.get_projects_from_json()
        self.current_project = None

    """get project object from array_list with name x"""
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
            self.json_helper.save_json(self)
            self.terminal_ui_helper.print_task_table(lines=5)

    def get_all_tasks(self, reverse=False):
        task_list = []
        for project in self.projects:
            for task in project.task_list:
                task_list.append(task)
        """sort task_list"""
        task_list.sort(key=lambda x: x.start_time, reverse=reverse)
        return task_list

    def get_all_projects(self):
        project_name_list = []
        for project in self.projects:
            project_name_list.append(project.name)
        return project_name_list
