from timekeeper import *
import argparse
import sys
import time
import threading


def get_args():
    parser = argparse.ArgumentParser("A timekeeper")
    parser.add_argument("-d", "--debug", help="Use Debug option", action='store_true')
    parser.add_argument("-p", "--project", help="Which project to track", required=True)
    parser.add_argument("-t", "--task", help="Which task to track", required=True)
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
    timekeeper = TimeKeeper()
    thread = threading.Thread(target=timekeeper.start, args=(arg_project_name, arg_task_name))
    thread.setDaemon(True)
    thread.start()

    input_thread = threading.Thread(target=input_thread_fkt, args=(w, ))
    input_thread.start()
    while True:
        sys.stdout.write(timekeeper.current_project.current_task.get_run_time())
        sys.stdout.flush()
        time.sleep(1)
        if w:
            input_thread.join()
            break

    timekeeper.stop()
    timekeeper.save_json()

if __name__ == '__main__':
    main()
