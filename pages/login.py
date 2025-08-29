import re
from playwright.sync_api import Page, expect

class LoginPage:

    def test_click_username_and_password(self,page: Page):
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        # Click the login button.
        page.locator("#login-button").click()

        # Expects successful login by seeing the home page with Products title.
        expect(page.get_by_text("Products")).to_be_visible()