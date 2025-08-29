import pytest
from playwright.sync_api import Page, expect
from pages.login import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage()
    login_page.test_click_username_and_password(page)