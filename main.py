from timekeeper import *
import argparse


def get_args():
    parser = argparse.ArgumentParser("A timekeeper")
    parser.add_argument("-d", "--debug", help="Use Debug option", action='store_true')
    parser.add_argument("-p", "--project", help="Which project to track", required=True)
    parser.add_argument("-t", "--task", help="Which task to track", required=True)
    options = parser.parse_args()
    return vars(options)


def main():
    options = get_args()
    debug_enabled = options.get("debug")
    arg_project_name = options.get("project")
    arg_task_name = options.get("task")
    timekeeper = TimeKeeper()
    timekeeper.start(arg_project_name, arg_task_name)
    input("Press RETURN to stop the task\n")
    timekeeper.stop()
    timekeeper.test()

if __name__ == '__main__':
    main()
