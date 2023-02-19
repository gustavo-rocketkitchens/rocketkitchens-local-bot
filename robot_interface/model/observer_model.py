import os
import subprocess

import watchdog.events
import watchdog.observers
import time



class Handler(watchdog.events.PatternMatchingEventHandler):

    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'], ignore_directories=True,
                                                             case_sensitive=False)
        self.process_running = False  # Add flag to keep track of whether the process is running
        self.file_processed = []  # Initialize list to keep track of processed files

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now
        ...

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)

        if event.src_path in self.file_processed:
            print("File already processed. Skipping.")
        else:
            # Add path to list of processed files
            self.file_processed.append(event.src_path)

            if not self.process_running:  # Only start the process if it's not already running
                navigation_model = "dependencies/navigation_model.py"

                dist_robot_interface = "dependencies/robot-launcher.py"
                if os.path.exists(dist_robot_interface):

                    minimize = 5
                    print("minimize = 5")

                    for i in range(minimize):
                        subprocess.Popen(['python', navigation_model])
                        time.sleep(0.1)  # Add a brief pause to prevent overloading the system

                    subprocess.Popen(['python', dist_robot_interface])
                    self.process_running = True  # Set flag to indicate that the process is running


def start_observer(src_path):
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def stop_observer():
    observer = watchdog.observers.Observer()

    observer.stop()


if __name__ == "__main__":
    home_dir = os.path.expanduser("~")
    output_dir = os.path.join(home_dir, "Downloads", "output")

    print('output_dir:', output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print("start_observer({})".format(output_dir))
    start_observer(output_dir)
