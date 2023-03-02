from playwright.sync_api import Playwright, sync_playwright
import time


class TalabatSearch:
    def __init__(self):
        self.url = "https://www.talabat.com/uae"

    def talabat_search(self, query):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            page.fill("//input[@id='search-box-map-first']", query)

            # Wait for the drop-down menu to appear
            page.wait_for_selector("(//div[@data-test='show-map-title'])[1]", state='visible')

            # Click on the first option in the dropdown
            page.click("(//div[@data-test='show-map-title'])[1]")


            # Wait for the page to finish loading
            page.wait_for_load_state(state='networkidle')

            # Scroll to a specific element by selector
            element = page.wait_for_selector("//div[@data-test='google-maps-component']")
            page.scroll_to(element)

            page.click("//button[@data-test='btn-deliver-here']")


if __name__ == "__main__":
    ts = TalabatSearch()
    ts.talabat_search("Dubai Internet City - Dubai - United Arab Emirates")
