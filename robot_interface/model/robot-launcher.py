import os

# #  To run With Script
# from rocket_kitchens.Admin import admin as ad
# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters
# from rocket_kitchens_local_bot.robot_interface.model.robot_models.Zoey import zoey

#  To run in Pyinstaller
from parameters import Parameters
from robot_models.Zoey import zoey

from robot_models import admin as ad




class RobotLauncher:


    def __init__(self):
        bot = ad.TaskAutomator()
        print("HandlerSheet Class")
        handler = ad.HandlerSheet()

        self.enter_talabat = 'Enter Talabat'
        self.extract_orders = 'Extract Orders'
        self.extract_reports = ''
        self.exit_talabat = ''
        self.zoey = 'Zoey'
        self.leo = 'Leo'
        self.sal = 'Sal'

        #===============================================================
        # Launch the following Robots:
        #===============================================================

        # self.bot_extract_orders =  bot.tabalat_extract_orders()
        self.bot_extract_orders = bot.enter_talabat

        # Zoey
        start = zoey.Start()
        self.bot_zoey = start.zoey_orders

        # Leo
        self.bot_leo = ''

        # Sal
        self.bot_sal = ''



    def get_parameters(self):
        src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens_local_bot\robot_interface\model\robot_models\output"
        filename = 'File.csv'
        filepath = os.path.join(src_path, filename)
        params = Parameters(filepath)

        # self.variable_name, values = params.get_row(1)
        self.variable_name, values = params.get_row("Zoey")

        # Print the variable name and values to verify that they have been assigned correctly
        print(f'Variable name: {self.variable_name}')
        print(f'Values: {values}')

    def start_robots(self):

        if self.variable_name == self.extract_orders:
            self.bot_extract_orders()
        if self.variable_name == self.zoey:
            self.bot_zoey()
        ...

    def start_zoey(self):
        if self.variable_name == self.zoey:
            self.bot_zoey()


        ...

if __name__ == "__main__":
    rl = RobotLauncher()
    rl.get_parameters()

    # rl.start_zoey()
    rl.start_robots()
