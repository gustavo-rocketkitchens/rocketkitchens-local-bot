import os

import json
import requests

from leo_core import TaskAutomator, HandlerSheet
import rpa as r

# from rocket_kitchens.Admin import orders_execution_post

from robot_models import orders_execution_post as post

# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters
from parameters import Parameters

class Start():


    def __init__(self):
        self.username, self.password = self.get_parameters('Leo')
        self.gross_profit = None
        self.avg_comission = None
        self.sum_food_values = None
        self.sum_discount_values = None
        self.bot = TaskAutomator()
        self.handler = HandlerSheet()


    def get_parameters(self, robot="Zoey"):
        src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens_local_bot\robot_interface\model\robot_models\output"
        filename = 'File.csv'
        filepath = os.path.join(src_path, filename)
        params = Parameters(filepath)

        self.username, self.password = params.get_pass(robot)

        # Print the username and password to verify that they have been assigned correctly
        print(f'Username: {self.username}')
        print(f'Password: {self.password}')
        return self.username, self.password

