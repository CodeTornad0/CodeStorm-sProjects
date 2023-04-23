import os

import keyboard
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        keyboard.wait("enter")
        for filename in os.listdir(folder_to_track):
            src = f"{folder_to_track}/{filename}"
            new_destination = f"{folder_destination}/{filename}"
            os.rename(src, new_destination)


folder_to_track = "/your_folder_to_track"
folder_destination = "/put_any_folder_in_that_location_here"
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
# run sudo python3 main.py
