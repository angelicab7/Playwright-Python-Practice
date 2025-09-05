import re
from playwright.sync_api import Page, expect

class OverviewPage:
    def verify_payment_information_and_finish(self,page: Page):
        expect(page.get_by_text("Payment Information:")).to_be_visible()
        expect(page.get_by_text("Shipping Information:")).to_be_visible()
        expect(page.get_by_text("Price Total")).to_be_visible()
        page.get_by_role("button",name="Finish").click()