from task import *


class Project:
    def __init__(self, name):
        self.name = name
        self.task_list = []
        self.current_task = None

    def start(self, task_name):
        self.current_task = Task(task_name)
        self.current_task.start()

    def stop(self):
        if self.current_task is not None:
            self.current_task.stop()
            self.task_list.append(self.current_task)
