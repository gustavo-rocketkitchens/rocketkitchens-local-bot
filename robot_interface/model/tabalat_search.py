import os
import rpa as r
import json
import requests
import logging
import time
# from leo_core import TaskAutomator, HandlerSheet
from robot_models.Leo.leo_core import TaskAutomator, HandlerSheet

# from rocket_kitchens.Admin import orders_execution_post

# =======================================================================================================================

# Local Bot
from robot_models import orders_execution_post as post
from parameters import Parameters

# =======================================================================================================================
from foreground_model import get_page_title, activate_window


class TalabatSearch:


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tab_log = float()
        ...

    def talabat_search(self):

        url = r"https://www.talabat.com/uae"

        # Configure logging
        logger = logging.getLogger(__name__)

        # get the start time
        st = time.time()

        r.init(visual_automation=True)
        # title = get_page_title(url)

        # focus = "focus(title='{}')".format(title)
        # maximize = "maximize (title='{}')".format(title)
        # r.run(focus)
        # r.run(maximize)
        r.url(url)
        r.wait(1)
        #
        # r.run(focus)
        # r.run(maximize)
        # activate_window(title)
        # r.wait(1)
        # r.run(maximize)
        # logger.info("Maximizing")
        r.keyboard("[alt][space]")
        r.keyboard("x")
        r.wait(1)
        logger.info("Maximizing Con")
        r.keyboard("[alt][space]")
        r.keyboard("x")

        # Search
        r.wait(2)
        # r.type("//input[@id='search-box-map-first']", "Sushi")
        r.type("//input[@id='search-box-map-first']", "[clear]" + "Business Bay, Marasi Drive")

        r.wait(.2)
        r.click("//button[@data-testid='letsgo-btn']")
        r.wait(2)


        r.type("//input[@placeholder='Search Restaurants']", "Sushi[enter]")
        r.wait(.2)
        # r.type("//input[@id='placeSearch']", "Business Bay - Dubai")
        # r.wait(.2)
        r.click("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a[1]/div[1]")

        # get the end time
        et = time.time()

        # get the execution time
        elapsed_time = et - st
        logger.info('Log in Tabalat execution time: %s seconds', elapsed_time)

        self.tab_log = elapsed_time


if __name__ == '__main__':
    TS = TalabatSearch()
    TS.talabat_search()










