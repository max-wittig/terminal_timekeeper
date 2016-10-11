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

    def remove(self, remove):
        try:
            """tag or task"""
            remove_type = remove[0]
            delete_project = remove[1]
            selected_project = self.get_project(delete_project)
            if selected_project is not None:
                if str(remove_type).startswith("task"):
                    try:
                        delete_task = remove[2]
                    except IndexError:
                        delete_task = None

                    if delete_task is None:
                            """remove whole project with all tasks"""
                            self.projects.remove(selected_project)
                            print("removed " + delete_project)
                    else:
                        """taskName is something, do not remove whole project--> only selected task"""
                        selected_project.remove_task(delete_task)
                        print("removed " + delete_task + " from " + delete_project)

                elif str(remove_type).startswith("tag"):
                    delete_tag = remove[2]
                    if delete_tag in selected_project.tags:
                        selected_project.tags.remove(delete_tag)
            self.save()
        except IndexError:
            print("IndexError")

    def add(self, parameter):
        try:
            add_type = parameter[0]
            project_name = parameter[1]

            if project_name is not None:
                add_project = self.get_project(project_name)
                if add_project is not None:
                    if str(add_type).startswith("tag"):
                        for tag in parameter:
                            if tag != project_name and tag != "tag":
                                if add_project.tags is None:
                                    add_project.tags = []
                                if not add_project.tags.__contains__(tag):
                                    add_project.tags.append(tag)
                    elif str(add_type).startswith("task"):
                        task_name = parameter[2]
                        start_time = parameter[3]
                        end_time = parameter[4]
                        task = Task(task_name, project_name)
                        task.start_time = int(start_time)
                        task.end_time = int(end_time)
                        task.duration = int(end_time)-int(start_time)
                        task.generate_uuid()
                        add_project.task_list.append(task)
            self.save()
        except IndexError:
            print("Missing parameters!")
