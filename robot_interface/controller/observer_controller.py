import os

import subprocess
from rocket_kitchens_local_bot.robot_interface.model import observer_model
from rocket_kitchens_local_bot.robot_interface.model.observer_model import Handler

observer_process = None
def start_controller(instance):

    global observer_process

    # Get the current working directory
    cwd = os.getcwd()
    print("I am here: ")
    print(cwd)

    # launcher_oberserver = observer_model.start_observer(src_path)

    dist_robot_interface = "dependencies/observer_model.py"

    # RUN WITH SCRIPT
    # observer_process = subprocess.Popen(['python', 'model/observer_model.py'])

    # RUN WITH PYSINTALLER
    observer_process = subprocess.Popen(['python', dist_robot_interface])

    # Run the Python script
    print('observer_process = ', observer_process)

def stop_controller(instance):
    global observer_process
    src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"

    # Get the current working directory
    cwd = os.getcwd()

    # Navigate to the parent directory
    os.chdir('..')

    observer_process.kill()
    print("stopping observer")

    # Navigate back to the original working directory
    os.chdir(cwd)


def start_bot_controller(instance):
    bot_process = subprocess.Popen(['python', 'model/robot-launcher.py'])
    print(bot_process)

