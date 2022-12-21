from kivymd.app import MDApp
from kivymd.uix.screen import Screen

from kivy.lang import Builder
import requests
import watchdog.events
import watchdog.observers
import time

# Create the GUI layout using Kivy language
KIVY_LAYOUT = '''
Screen:
    MDRaisedButton:
        text: "Make POST Request"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.make_post_request()
'''


class MyApp(MDApp):
    def build(self):
        # Load the Kivy language layout
        self.root = Builder.load_string(KIVY_LAYOUT)
        return self.root

    def make_post_request(self):
        # Make the POST request
        url = 'google.com'
        response = requests.post(url, data={'key': 'Rocket Kitchens'})

        # Check the status code of the response
        print(response.status_code)

        # Print the response text
        print(response.text)


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now
        MyApp().make_post_request()

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now


if __name__ == "__main__":
    src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"
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
