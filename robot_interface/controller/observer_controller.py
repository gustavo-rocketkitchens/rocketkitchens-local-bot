import os

import subprocess
from rocket_kitchens_local_bot.robot_interface.model import observer_model
from rocket_kitchens_local_bot.robot_interface.model.observer_model import Handler

observer_process = None
def start_controller(instance):
    global observer_process

    src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"

    # Get the current working directory
    cwd = os.getcwd()

    # Navigate to the parent directory
    os.chdir('..')

    # launcher_oberserver = observer_model.start_observer(src_path)
    observer_process = subprocess.Popen(['python', 'model/observer_model.py'])

    # Run the Python script
    print(observer_process)

    # Navigate back to the original working directory
    os.chdir(cwd)

def stop_controller(instance):
    global observer_process
    src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"

    # Get the current working directory
    cwd = os.getcwd()

    # Navigate to the parent directory
    os.chdir('..')
    # observer_model.stop_observer()
    # launcher_oberserver = observer_model.start_observer(src_path)
    # launcher_oberserver = subprocess.Popen(['python', 'model/observer_model.py'])
    # Call the stop_observer function in the observer_model script
    # subprocess.Popen(['python', '-c', 'from model.observer_model import stop_observer; stop_observer()'])
    # Run the Python script
    # Stop the observer process
    observer_process.kill()
    print("stopping observer")

    # Navigate back to the original working directory
    os.chdir(cwd)


import kivy
import subprocess

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text="Run other script")
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        print("Starting Observer")
        subprocess.Popen(['python', '../model/observer_model.py'])

if __name__ == "__main__":
    MyApp().run()