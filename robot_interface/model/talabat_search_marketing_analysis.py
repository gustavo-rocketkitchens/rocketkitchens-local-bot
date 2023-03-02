from request_app import GetMenuItem
import menu_category
import logging
from playwright.sync_api import sync_playwright
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class MarketingAnalysis(GetMenuItem):

    def __init__(self):
        super().__init__()
        self.menu = None
        self.dict_area = None

    def input_area(self, area):
        logger.info(f"Getting the URL for {area}")
        self.menu = GetMenuItem()
        self.dict_area = self.menu.urls_per_area
        url = self.dict_area[area]
        url = 'https://www.talabat.com/' + url
        logger.info(f"The URL for {area} is: {url}")
        return url


    def input_cuisine(self, cuisine, url):
        logger.info(f"Searching for {cuisine} in {url}")
        self.menu = GetMenuItem()
        self.all_cuisine = self.menu.all_cuisine
        restaurants = {}

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)
            time.sleep(5)
            logger.info(f"Opened the browser and navigated to {url}")
            search_input = page.query_selector("//input[@placeholder='Search Restaurants']")
            search_input.fill(cuisine)
            time.sleep(2)  # Wait for 2 seconds to ensure page is loaded
            logger.info(f"Filled in the cuisine search input with {cuisine}")


            restaurant_list = page.query_selector_all("//div[@class='d-flex']")
            for index, restaurant in enumerate(restaurant_list):
                restaurant_title = restaurant.query_selector(".restaurant-title.pb-1")
                cuisines_section = restaurant.query_selector(".cuisines-section.pb-1.truncate")
                ratings_section = restaurant.query_selector(".ratings-and-new-section.pb-1.d-flex")
                info_section = restaurant.query_selector(".info-section.pb-1.f-14.delivery-info.d-flex")
                tlb_badge_section = restaurant.query_selector(
                    ".tlb-badge-section.d-flex.align-items-center.flex-wrap")
                logger.info(f"Details for restaurant {index + 1}:")
                logger.info(f"Title: {restaurant_title.inner_text()}")
                logger.info(f"Cuisine: {cuisines_section.inner_text()}")
                logger.info(f"Ratings and new section: {ratings_section.inner_text()}")
                logger.info(f"Info section: {info_section.inner_text()}")
                logger.info(f"TLB badge section: {tlb_badge_section.inner_text()}")
                restaurant_details = {
                    "Title": restaurant_title.inner_text(),
                    "Cuisine": cuisines_section.inner_text(),
                    "Ratings and new section": ratings_section.inner_text(),
                    "Info section": info_section.inner_text(),
                    "TLB badge section": tlb_badge_section.inner_text()
                }
                restaurants[restaurant_title.inner_text()] = restaurant_details


        return restaurants

    def output_menu_item(self, url):
        logger.info(f"Scraping menu items for {url}")
        menu_items = menu_category.scrape_menu_items(url)
        logger.info(f"Scraped {len(menu_items)} menu items")
        menu_category.write_menu_items_to_csv(menu_items, 'menu_items.csv')


if __name__ == '__main__':
    mkt = MarketingAnalysis()
    area = 'Business Bay'
    cuisine = 'Sushi'
    logger.info(f"Getting details for restaurants in {area} serving {cuisine} cuisine")
    url = mkt.input_area(area)

    mkt.input_cuisine(cuisine, url)
    logger.info(f"Finished retrieving restaurant details for {cuisine} cuisine in {url}")
    # mkt.output_menu_item(url)
    # logger.info("Completed scraping menu items and writing to CSV file.")
