import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import watchdog.events
import watchdog.observers
import time


class MyApp(App):


    def build(self):
        layout = BoxLayout(orientation='vertical')
        start_button = Button(text='Start')
        stop_button = Button(text='Stop')
        layout.add_widget(start_button)
        layout.add_widget(stop_button)

        # Create an instance of the watchdog event handler
        self.event_handler = Handler()
        # Create an instance of the watchdog observer
        self.observer = watchdog.observers.Observer()

        # Set up the start button to start the observer
        def start_observer(instance):
            src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"
            self.observer.schedule(self.event_handler, path=src_path, recursive=True)
            self.observer.start()
            print("Observer started")

        start_button.bind(on_press=start_observer)

        # Set up the stop button to stop the observer
        def stop_observer(instance):
            self.observer.stop()
            self.observer.join()
            print("Observer stopped")

        stop_button.bind(on_press=stop_observer)

        return layout


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now


if __name__ == '__main__':
    MyApp().run()
