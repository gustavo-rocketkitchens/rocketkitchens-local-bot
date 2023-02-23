import os
import rpa as r
import json
import requests

# from zoey_core import TaskAutomator, HandlerSheet

# from rocket_kitchens.Admin import orders_execution_post


# Local Bot

from robot_models.Zoey.zoey_core import TaskAutomator, HandlerSheet
from robot_models import orders_execution_post as post
from parameters import Parameters

#=======================================================================================================================

# Felicidade PC
# from rocket_kitchens_local_bot.robot_interface.model.robot_models.Zoey.zoey_core import TaskAutomator, HandlerSheet
# from rocket_kitchens_local_bot.robot_interface.model.robot_models import orders_execution_post as post
# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters
# from rocket_kitchens_local_bot.robot_interface.model.robot_models import orders_execution_get_request as get

#=======================================================================================================================

# Notebook
# from robot_interface.model.robot_models import orders_execution_post as post
# from robot_interface.model.parameters import Parameters

#=======================================================================================================================


class Start:

    def __init__(self):

        self.gross_profit = None
        self.avg_comission = None
        self.sum_food_values = None
        self.sum_discount_values = None
        print("Initializers in Zoey")
        print("Task Automator Class in Zoey")
        self.bot = TaskAutomator()
        self.handler = HandlerSheet()


    def get_parameters(self):
        # src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens_local_bot\robot_interface\model\robot_models\output"
        # Notebook
        # src_path = r"C:\Users\123\PycharmProjects\rocketkitchens-local-bot\robot_interface\model\robot_models\output"
        src_path = os.path.join(os.path.expanduser("~"), "Downloads", "output")

        filename = 'File.csv'
        filepath = os.path.join(src_path, filename)
        params = Parameters(filepath)

        # Get the first row of the dataframe
        row = params.df.iloc[0]

        # Extract the first value in the first cell of the row
        parameter = row.iloc[0]

        # Get the row for the extracted parameter
        self.variable_name, values = params.get_row(parameter)

        # Print the variable name and values to verify that they have been assigned correctly
        print(f'robot-launcher function name: {self.variable_name} \n in zoey.py')
        print(f'Variable name: {self.variable_name}')
        print(f'Values: {values}')

        self.username, self.password = params.get_pass(self.variable_name)

        # Print the username and password to verify that they have been assigned correctly
        print(f'Username: {self.username}')
        print(f'Password: {self.password}')
        return self.username, self.password

    def zoey_orders(self):

        # Add Zoey Robots:
        print('start zoey_orders ')

        #---------------------------
        #Start Orders Extraction
        #---------------------------
        print("instance: self.username, self.password = self.get_parameters() ")
        self.username, self.password = self.get_parameters()
        self.bot.enter_talabat(username=self.username, password=self.password)



        r.wait(12)
        self.bot.last_week_orders()
        r.wait(4)
        self.bot.exit_talabat()
        r.wait(2)
        self.bot.talabat_close_page()
        self.bot.tab_time()
        r.wait(2)

        ...

    def zoey_reports(self):

        print('start zoey_reports')

        # =======================================
        #      Zoey execution: Reports
        # =======================================

        self.bot.enter_talabat()
        r.wait(15)  # Extract 7 last days reports
        self.bot.tabalat_extract_reports()
        r.wait(4)
        self.bot.exit_talabat()
        r.wait(2)
        self.bot.talabat_close_page()
        self.bot.tab_time()
        ...

    def zoey_file_handler(self):

        print('start zoey_file_handler')

        # ---------------------------
        # Start File Handler
        # ---------------------------

        print("starting talabat read orders")
        self.handler.talabat_read_orders()
        r.wait(4)
        print("successfully talabat read orders")
        #

        print("starting talabat average food")
        self.handler.tabalat_average_food()
        r.wait(4)
        print("successfully talabat average food")


        print("starting talabat average discount")
        self.handler.tabalat_average_discount()
        r.wait(4)
        print("successfully talabat average discount")


        print("starting talabat average comission")
        self.handler.tabalat_average_comission()
        r.wait(4)
        print("successfully talabat average comission")

        print("starting talabat gross profit")
        # The last OP. gross profit function also return 4 output values
        self.sum_discount_values, self.sum_food_values, self.avg_comission, self.gross_profit = self.handler.tabalat_gross_profit()
        r.wait(4)
        print("successfully talabat gross profit - \n also return 4 output values")
        r.wait(2)
        self.handler.delete_output_file("File.csv")
        print("successfully delete output file")
        ...

    def zoey_post(self):

        print('start zoey_post')

        # ---------------------------
        # POST with orders_execution_post
        # ---------------------------

        print('sum_discount_values,sum_food_values,avg_comission,gross_profit:')
        print(self.sum_discount_values, self.sum_food_values, self.avg_comission, self.gross_profit)

        # Now we post request the robots output values
        post.post_request(sum_discount_values=self.sum_discount_values,
                          sum_food_values=self.sum_food_values,
                          avg_comission=self.avg_comission,
                          gross_profit=self.gross_profit)
        ...

    def zoey_process(self):

        self.zoey_orders()
        print('successfully zoey orders')
        # self.zoey_reports()
        self.zoey_file_handler()
        print('successfully zoey file handler')
        # self.zoey_post()
        # print('successfully zoey post')
        # print('successfully finished Zoey process')

        ...

    # zoey_post()


# if __name__ == '__main__':
#     start = Start()
#     start.zoey_orders()
