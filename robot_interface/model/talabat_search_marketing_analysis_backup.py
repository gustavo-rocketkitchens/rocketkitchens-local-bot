from request_app import GetMenuItem
import menu_category
import logging


class MarketingAnalysis(GetMenuItem):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.dict_area = None

    def input_area(self, area):
        self.menu = GetMenuItem()
        self.dict_area = self.menu.urls_per_area
        # print(self.dict_area[area])
        url = self.dict_area[area]

        url = 'https://www.talabat.com/' + url

        return url

    def input_cuisine(self, cuisine, url):
        self.menu = GetMenuItem()
        self.all_cuisine = self.menu.all_cuisine

        if cuisine in self.all_cuisine:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto(url)

        return url

    def output_menu_item(self, url):
        # url = "https://www.talabat.com/uae/restaurant/619284/manzo-sushi-and-sliders-khalifa-city-madinat-khalifa--a?aid=2060"
        menu_items = menu_category.scrape_menu_items(url)
        print(menu_items)
        menu_category.write_menu_items_to_csv(menu_items, 'menu_items.csv')


if __name__ == '__main__':
    mkt = MarketingAnalysis()
    # input_area = mkt.input_area('Al Hamidiya 2')
    # input_area = mkt.input_area('Al Abar')
    # input_area = mkt.input_area('Al Bandar (Al Raha)')
    # input_area = mkt.input_area('Al Humrah - A')
    input_area = mkt.input_area('Business Bay')
    print(f"Restaurants in {input_area} for delivery")
    # print(input_area)
    mkt.input_cuisine(input_area, cuisine)

    mkt.output_menu_item(url)