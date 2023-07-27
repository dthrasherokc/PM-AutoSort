import time
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(filename='auto_sorter.log', level=logging.INFO)

# Specify the source directory and destination directory
source_directory = r"PATH OF FOLDER YOU WANT TO OBSERVE FOR CHANGES. THIS IS WHERE YOU WILL DRAG/SAVE FILES TO"
destination_directory = r"PATH OF APARTMENT NUMBERS FOLDER DIRECTORY"

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Log the event
        logging.info(f"Modified: {event.src_path}")
        
        # Only move files, not directories
        if not event.is_directory:
            file_name = os.path.split(event.src_path)[-1]
            # Get the first part of the file name (the folder name)
            folder_name = file_name.split()[0]
            destination_folder = os.path.join(destination_directory, folder_name)
            
            # Log the file move
            logging.info(f"Moving file {file_name} to {destination_folder}")
            
            # Move the file to the destination folder
            shutil.move(event.src_path, os.path.join(destination_folder, file_name))

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

   