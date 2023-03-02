from request_app import GetMenuItem
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

    def input_food(self):
        ...

if __name__ == '__main__':
    mkt = MarketingAnalysis()
    # input_area = mkt.input_area('Al Hamidiya 2')
    input_area = mkt.input_area('Al Abar')
    print(f"Restaurants in {input_area} for delivery")
    # print(input_area)
