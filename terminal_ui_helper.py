import terminaltables
from time_helper import *


class TerminalUIHelper:
    def __init__(self, timekeeper):
        self.timekeeper = timekeeper

    def print_task_table(self, lines=30):
        table_data = [self.get_print_header()]
        table_content = self.get_print_content(lines=lines)
        for array in table_content:
            table_data.append(array)
        table = terminaltables.DoubleTable(table_data)
        print(table.table)

    def get_print_header(self):
        return ["START_TIME", "END_TIME", "PROJECT_NAME", "TASK_NAME", "DURATION"]

    def get_print_content(self, lines=30):
        i = 1
        print_data = []
        all_tasks = self.timekeeper.get_all_tasks(reverse=True)
        for task in all_tasks:
            i += 1
            print_data_point = [TimeHelper.get_time_string(task.start_time), TimeHelper.get_time_string(task.end_time), task.project_name, task.name, TimeHelper.get_stopwatch_time_string(task.duration)]
            print_data.append(print_data_point)
            if i > lines or i == len(all_tasks):
                return print_data

    def print_project_table(self):
        print("Projects")
        print("--------")
        for project in self.timekeeper.get_all_projects():
            print(project)