import re
from playwright.sync_api import Page

class YourInfoPage:
    def fill_your_info(self,page: Page):
        page.get_by_placeholder("First Name").fill("Taylor")
        page.get_by_placeholder("Last Name").fill("Swift")
        page.get_by_placeholder("Zip/Postal Code").fill("12345")

    def proceed_to_overview_page(self,page: Page):
        page.locator("#continue").click()
        page.get_by_text("Checkout: Overview").is_visible()