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

    # Get the URL of the Area
    def input_area(self, area):
        logger.info(f"Getting the URL for {area}")
        self.menu = GetMenuItem()
        self.dict_area = self.menu.urls_per_area
        url = self.dict_area[area]
        url = 'https://www.talabat.com/' + url
        logger.info(f"The URL for {area} is: {url}")
        return url

    # Get the restaurants by Cuisine
    def output_restaurants_url(self, cuisine, url):
        logger.info(f"Searching for restaurants URL'S in {url}")
        self.menu = GetMenuItem()
        self.all_cuisine = self.menu.all_cuisine
        restaurants = {}

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)
            time.sleep(.2)
            logger.info(f"Opened the browser and navigated to {url}")
            search_input = page.query_selector("//input[@placeholder='Search Restaurants']")
            search_input.fill(cuisine)
            time.sleep(.1)  # Wait for 2 seconds to ensure page is loaded
            logger.info(f"Filled in the cuisine search input with {cuisine}")

            restaurant_urls = page.query_selector_all(".px-2.py-3.restuarant-item.d-block.b-t")
            if restaurant_urls:
                for restaurant_url in restaurant_urls:
                    restaurant_title = restaurant_url.query_selector(".restaurant-title.pb-1")
                    url = restaurant_url.get_attribute("href")
                    restaurant_details = {
                        "Title": restaurant_title.inner_text(),
                        "URL": url
                    }
                    restaurants[restaurant_title.inner_text()] = restaurant_details

        logger.info(f"List of Restaurants URL's: {restaurants}")

        return restaurants

    # Write the Menu Items to the CSV file
    def output_menu_item(self, cuisine, url):
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

    # mkt.input_cuisine(cuisine, url)
    # logger.info(f"Finished retrieving restaurant details for {cuisine} cuisine in {url}")
    mkt.output_restaurants_url(cuisine, url)
    logger.info(f"Finished retrieving restaurant URL's for {cuisine}")
    # mkt.output_menu_item(url)
    # logger.info("Completed scraping menu items and writing to CSV file.")

