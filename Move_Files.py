import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/avipa/Downloads"

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.src_path} has been created!")

    def on_created(self, event):  
        print(f"Oops! Someone Deleted {event.src_path}!")  

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")
    
    def on_moved(self, event):
        print(f"Oops! Someone Moved {event.src_path} to {event.dest_path}")
        
# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()    