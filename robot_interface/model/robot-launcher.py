import os

from rocket_kitchens.Admin import admin as ad
from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters
class RobotLauncher:
    def __init__(self):
        bot = ad.TaskAutomator()
        print("HandlerSheet Class")
        handler = ad.HandlerSheet()

        self.enter_talabat = 'Enter Talabat'
        self.extract_orders = 'Extract Orders'
        self.extract_reports = ''
        self.exit_talabat = ''


        # self.bot_extract_orders =  bot.tabalat_extract_orders()
        self.bot_extract_orders =  bot.enter_talabat()



    def get_parameters(self):
        src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"
        filename = 'File (5).csv'
        filepath = os.path.join(src_path, filename)
        params = Parameters(filepath)

        self.variable_name, values = params.get_row(1)

        # Print the variable name and values to verify that they have been assigned correctly
        print(f'Variable name: {self.variable_name}')
        print(f'Values: {values}')

    def start_robots(self):
        if self.variable_name == self.extract_orders:
            self.bot_extract_orders()

        ...

if __name__ == "__main__":
    rl = RobotLauncher()
    rl.get_parameters()

    rl.start_robots()