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
        if self.projects is not None:
            for project in self.projects:
                if project_name == project.name:
                    return project
        return None

    def start(self, project_name, task_name):
        project = self.get_project(project_name)
        if project is None:
            project = Project(project_name)
            if self.projects is None:
                self.projects = []
            self.projects.append(project)
        project.start(task_name)
        self.current_project = project

    def stop(self):
        if self.current_project is not None:
            self.current_project.stop()
            self.projects.sort(key=lambda x: str(x.name).upper())
            self.save()

    def save(self):
        self.json_helper.save_json(self)
        self.terminal_ui_helper.print_task_table(lines=5)

    def get_all_tasks(self, reverse=False):
        task_list = []
        if self.projects is not None:
            for project in self.projects:
                for task in project.task_list:
                    task_list.append(task)
        """sort task_list"""
        task_list.sort(key=lambda x: x.start_time, reverse=reverse)
        return task_list

    def remove(self, project_name, task_name=None):
        if project_name is not None:
            selected_project = self.get_project(project_name)
            if selected_project is not None:
                if task_name is None:
                    """remove whole project with all tasks"""
                    self.projects.remove(selected_project)
                    print("removed " + project_name)
                else:
                    """taskName is something, do not remove whole project--> only selected task"""
                    selected_project.remove_task(task_name)
                    print("removed " + task_name + " from " + project_name)
            self.save()
