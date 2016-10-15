import terminaltables
from time_helper import *
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
        print_data = [["PROJECT_NAME", "TOTAL_TIME"]]
        project_time_dict = self.get_project_time_dict()
        for current_project_name in project_time_dict.keys():
            project_data = [current_project_name, TimeHelper.get_stopwatch_time_string(project_time_dict[current_project_name])]
            print_data.append(project_data)
        table = terminaltables.DoubleTable(print_data)
        print(table.table)

    def get_project_time_dict(self):
        project_data_time = dict()
        for current_project_name in self.get_all_project_names():
            current_project = self.timekeeper.get_project(current_project_name)
            project_data_time[current_project_name] = current_project.get_total_project_time()
        return project_data_time

    def get_all_project_names(self):
        project_name_list = []
        if self.timekeeper.projects is not None:
            for project in self.timekeeper.projects:
                if self.show_frozen or not project.frozen:
                    project_name_list.append(project.name)
        return project_name_list
