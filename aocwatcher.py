import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import re
import sys


class Watcher:
    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Started...")
        try:
            # animation = "* "
            while True:
                # for i in range(2):
                #     sys.stdout.write("\r\r\r " + animation[i] + " ")
                #     sys.stdout.flush()
                #     time.sleep(1)
                time.sleep(10)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated.")


class MyHandler(FileSystemEventHandler):

    # def on_any_event(self, event):
    #     print(event) # Your code here

    def on_modified(self, event):
        fname = event.src_path
        if fname.endswith(".py") and "aocwatcher" not in fname:
            path = "/".join(fname.split("/")[:-1])
            # print(f"path = {path}")
            found = re.findall(r"\d+", fname)
            if found:
                week = found[-1]
                os.system(f"sh aoc.sh {fname} {path}/test{week}.txt {path}/input{week}.txt")
                


if __name__ == "__main__":
    w = Watcher(".", MyHandler())
    w.run()
