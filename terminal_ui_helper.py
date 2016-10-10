import terminaltables
from time_helper import *


class TerminalUIHelper:
    def __init__(self, timekeeper):
        self.timekeeper = timekeeper
        self.show_frozen = False

    def print_task_table(self, lines=30):
        table_data = [self.get_print_header()]
        table_content = self.get_print_content(lines=lines)
        if table_content is not None:
            for array in table_content:
                table_data.append(array)
            table = terminaltables.DoubleTable(table_data)
            print(table.table)

    def get_print_header(self):
        return ["WEEKDAY", "START_TIME", "END_TIME", "PROJECT_NAME", "TASK_NAME", "DURATION"]

    def get_print_content(self, lines=30):
        i = 0
        print_data = []
        all_tasks = self.timekeeper.get_all_tasks(reverse=True)
        for task in all_tasks:
            i += 1
            print_data_point = [TimeHelper.get_weekday(task.start_time), TimeHelper.get_time_string(task.start_time), TimeHelper.get_time_string(task.end_time), task.project_name, task.name, TimeHelper.get_stopwatch_time_string(task.duration)]
            print_data.append(print_data_point)
            if i > lines or i == len(all_tasks):
                return print_data

    def print_project_table(self):
        print("Projects")
        print("--------")
        for project in self.get_all_project_names():
            print(project)

    def get_all_project_names(self):
        project_name_list = []
        if self.timekeeper.projects is not None:
            for project in self.timekeeper.projects:
                if self.show_frozen or not project.frozen:
                    project_name_list.append(project.name)
        return project_name_list
