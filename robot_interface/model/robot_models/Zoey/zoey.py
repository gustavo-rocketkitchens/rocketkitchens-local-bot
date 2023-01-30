import json
import requests

# from rocket_kitchens_local_bot.robot_interface.model.robot_models import orders_execution_post as post
# from rocket_kitchens_local_bot.robot_interface.model.robot_models import orders_execution_get_request as get

# from rocket_kitchens_local_bot.robot_interface.model.robot_models.admin import TaskAutomator, HandlerSheet
from robot_models.admin import TaskAutomator, HandlerSheet
import rpa as r

# from rocket_kitchens.Admin import orders_execution_post

from robot_models import orders_execution_post

class Start():


    def __init__(self):
        self.gross_profit = None
        self.avg_comission = None
        self.sum_food_values = None
        self.sum_discount_values = None
        self.bot = TaskAutomator()
        self.handler = HandlerSheet()


    def zoey_orders(self):

        # Add Zoey Robots:
        print('start zoey_orders ')

        #---------------------------
        #Start Orders Extraction
        #---------------------------

        self.bot.enter_talabat()
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
        # self.zoey_reports()
        self.zoey_file_handler()
        # self.zoey_post()
        ...

    # zoey_post()


# if __name__ == '__main__':
#     start = Start()
#     start.zoey_orders()
