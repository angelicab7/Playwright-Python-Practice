import re
from playwright.sync_api import Page, expect

class ConfirmationPage:
        def verify_confirmation_page(self,page: Page):
            expect(page.get_by_text("Thank you for your order!")).to_be_visible()
            page.get_by_role("button",name="Back Home").click()
            expect(page.get_by_text("Products")).to_be_visible()