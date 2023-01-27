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


        self.handler.talabat_read_orders()
        r.wait(4)
        #

        self.handler.tabalat_average_food()
        r.wait(4)


        self.handler.tabalat_average_discount()
        r.wait(4)


        self.handler.tabalat_average_comission()
        r.wait(4)

        # The last OP. gross profit function also return 4 output values
        self.sum_discount_values, self.sum_food_values, self.avg_comission, self.gross_profit = self.handler.tabalat_gross_profit()
        r.wait(4)

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

    # =======================================
    #      Start Zoey Process
    # =======================================



    # zoey_post()


# if __name__ == '__main__':
#     start = Start()
#     start.zoey_orders()
#
#
#

# if __name__ == '__main__':
    ...
    # =======================================
    #      Initializers
    # =======================================
    # print("Initializers")
    # # print("Accesses Class")
    # # go = Accesses()
    # print("Task Automator Class")
    # bot = TaskAutomator()
    # print("HandlerSheet Class")
    # handler = HandlerSheet()


    #=======================================
    #      Zoey execution: Reports
    #=======================================
    #
    # bot.enter_talabat()
    # r.wait(15)  # Extract 7 last days reports
    # bot.tabalat_extract_reports()
    # r.wait(4)
    # bot.exit_talabat()
    # r.wait(2)
    # bot.talabat_close_page()
    # bot.tab_time()


    # =======================================
    #      Orders execution
    # =======================================


    #---------------------------
    # Start Orders Extraction
    #---------------------------
    # bot.enter_talabat()
    # r.wait(12)
    # bot.last_week_orders()
    # r.wait(4)
    # bot.exit_talabat()
    # r.wait(2)
    # bot.talabat_close_page()
    # bot.tab_time()
    # r.wait(2)


    #---------------------------
    # Start File Handler
    #---------------------------

    #
    # handler.talabat_read_orders()
    # r.wait(4)
    # #
    #
    # handler.tabalat_average_food()
    # r.wait(4)
    #
    #
    # handler.tabalat_average_discount()
    # r.wait(4)
    #
    #
    # handler.tabalat_average_comission()
    # r.wait(4)

    # The last OP. gross profit function also return 4 output values
    # sum_discount_values, sum_food_values, avg_comission, gross_profit = handler.tabalat_gross_profit()
    # r.wait(4)
    #

    # =======================================
    # CRUD: Work with json to do Requests
    # =======================================


    #---------------------------
    # POST with orders_execution_post
    #---------------------------



    # print('sum_discount_values,sum_food_values,avg_comission,gross_profit:')
    # print(sum_discount_values,sum_food_values,avg_comission,gross_profit)
    #
    # # Now we post request the robots output values
    # post.post_request(sum_discount_values=sum_discount_values,
    #                   sum_food_values=sum_food_values,
    #                   avg_comission=avg_comission,
    #                   gross_profit=gross_profit)
    #
    #
    # # ---------------------------
    # # GET with orders_execution_get_request
    # # ---------------------------
    #
    # #
    # # Last Uncategorized Bin
    # url = 'https://api.jsonbin.io/v3/c/uncategorized/bins/'
    #
    # headers = {
    #     'Content-Type': 'application/json',
    #     'X-Master-Key': '$2b$10$MSqfpi3TaFfyy45aXt9VRunVcgUmS2o8ckmJvDRy1Ztd72SMZUiU6',
    #     'X-Access-Key': '$2b$10$I/J3Ic0JvtvK8z9yiaNseeZfnxfiyESI4fI7yNf6v.Dlzw.iRFOI.',
    #     'X-Sort-Order': 'ascending'
    # }
    #
    # data = {}
    # req = requests.get(url, json=data, headers=headers)
    # '''collect_records:: return a dict with the uncategorized bins'''
    # records, last_record = get.collect_records(req)
    # # print('records')
    # # print(records)
    # # print('last_record')
    # # print(last_record)
    # url = 'https://api.jsonbin.io/v3/b/' + last_record
    # req = requests.get(url, json=None, headers=headers)
    # print('printing the dict of the last bin:')
    # print(last_record)
    #
    # # print('printing the message of the last bin:')
    # last_record = get.collect_last_record(req)
    # print(last_record)
    # print(last_record.values())