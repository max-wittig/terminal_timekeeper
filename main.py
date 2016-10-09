#!/usr/bin/python3.5


from timekeeper import *
import argparse
import sys
import time
import threading


def get_args():
    parser = argparse.ArgumentParser("A timekeeper")
    parser.add_argument("-d", "--debug", help="Use Debug option", action='store_true')
    parser.add_argument("-p", "--project", help="Which project to track")
    parser.add_argument("-t", "--task", help="Which task to track")
    parser.add_argument("-l", "--list", help="Show list of tasks", action="store_true")
    parser.add_argument("-c", "--count", help="Count of lines", type=int)
    options = parser.parse_args()
    return vars(options)


def input_thread_fkt(w):
    input()
    w.append(None)


def main():
    w = []
    options = get_args()
    debug_enabled = options.get("debug")
    arg_project_name = options.get("project")
    arg_task_name = options.get("task")
    show_list = options.get("list")
    count = options.get("count")
    timekeeper = TimeKeeper()

    if show_list:
        if arg_project_name is not None:
            pass
        if count is None:
            count = 30
        timekeeper.terminal_ui_helper.print_task_table(lines=count)
        #timekeeper.terminal_ui_helper.print_project_table()
    else:
        if arg_task_name is None or arg_project_name is None:
            exit("Project and taskname are required")
        thread = threading.Thread(target=timekeeper.start, args=(arg_project_name, arg_task_name))
        thread.setDaemon(True)
        thread.start()

        input_thread = threading.Thread(target=input_thread_fkt, args=(w, ))
        input_thread.start()
        while True:
            if timekeeper.current_project is not None:
                sys.stdout.write(timekeeper.current_project.current_task.get_run_time())
                sys.stdout.flush()
                time.sleep(1)
                if w:
                    input_thread.join()
                    break
        timekeeper.stop()

if __name__ == '__main__':
    main()
