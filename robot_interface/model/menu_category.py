import logging
import csv
import time
from playwright.sync_api import Playwright, sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

#
# def get_menu_categories(self, restaurants, cuisine, quantity=None):
#     self.menu_items = {}
#     num = 0
#
#     for restaurant in restaurants.values():
#         # Title: Url
#         logger.info(f"Entering {restaurant['URL']}")
#         url = "https://www.talabat.com" + restaurant['URL']
#         self.menu_items = menu_category.scrape_menu_items(url, cuisine)
#         logger.info(f"Menu Items Extracted for {cuisine} in {restaurant['URL']}")
#         logger.info(f"{self.menu_items}")
#         num += 1
#         if quantity and num == quantity:
#             break
#
#     return self.menu_items



# def save_menu_categories_to_xlsx(self, restaurants, filename, quantity=None):
#     all_menu_items = self.get_menu_categories(restaurants, quantity)
#     fieldnames = ['restaurant_name', 'price', 'name']  # use list comprehension to simplify
#
#     import openpyxl as excel
#
#     # Crete a Workbook
#     excel.Workbook.create_sheet(restaurant['restaurant_title'])
#     # For each iteration (url) create a sheet with the restaurant name and
#     # in each restaurant sheet insert their contents like
#     # restaurant_name,price,name, also add the description if available
#
#
#
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         rows = []
#         for restaurant_name, menu_items in all_menu_items.items():
#             for menu_item in menu_items:
#                 menu_item['restaurant_name'] = restaurant_name
#                 rows.append(menu_item)
#         writer.writerows(rows)


def scrape_menu_items(url: str, cuisine: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # Filter the Cuisines menu:
        page.fill("//input[@placeholder='Search menu item']", cuisine)

        time.sleep(.1)
        # Get a list of all menu category elements
        menu_categories = page.query_selector_all("[data-test='menu-category']")
        logging.info(f"Found {len(menu_categories)} menu categories")

        menu_items = {}

        for category_index in range(1, len(menu_categories)+1):
            # Get the menu category name
            category_name = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]", timeout=60000)
            logging.info(f"Scraping category {category_name}")

            # Get the list of menu item names, descriptions, and prices
            item_names = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]//div[@class='item-name']//div[@class='f-15']")
            item_descriptions = page.inner_html(f"(//div[@data-test='menu-category'])[{category_index}]//div[@class='item-name']//div[@class='f-12 description']")
            item_prices = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]//div[@class='text-right price-rating']")

            # Split the list of names, descriptions, and prices into individual items
            item_names = item_names.split('\n')
            item_descriptions = item_descriptions.split('\n')
            item_prices = item_prices.split('\n')

            # Create a list of menu items for this category
            category_items = []

            for i in range(len(item_names)):
                # If the number of names, descriptions, and prices are not equal, use an empty string for the missing value
                category_items.append({
                    'name': item_names[i].strip() if i < len(item_prices) else '',
                    'description': item_descriptions[i].strip() if i < len(item_prices) else '',
                    'price': item_prices[i].strip() if i < len(item_prices) else ''
                })

            # Add the category items to the menu_items dictionary
            menu_items[category_index] = category_items


            # Delay to avoid overcharging
            time.sleep(0.1)

        browser.close()

        return menu_items



def write_menu_items_to_csv(menu_items: dict, filename: str):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Item', 'Price'])
        for category_name, category_items in menu_items.items():
            for item_name, item_price in category_items.items():
                writer.writerow([category_name, item_name, item_price])

#
# if __name__ == '__main__':
#     url = "https://www.talabat.com/uae/restaurant/619284/manzo-sushi-and-sliders-khalifa-city-madinat-khalifa--a?aid=2060"
#
#     menu_items = scrape_menu_items(url, 'Sushi')
#     print(menu_items)
#     logging.info(f"Scraped {len(menu_items)} categories:")
#     for category, items in menu_items.items():
#         logging.info(f"{category}: {len(items)} items")
#     logging.info("Done scraping menu items")
#
