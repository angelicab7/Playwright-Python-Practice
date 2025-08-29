import pytest
import re
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

@pytest.fixture(scope="session", autouse=True)
def before_each(page: Page):
    print("before the test runs")
    
    # Use the 'page' instance, not the 'Page' class
    page.goto("https://www.saucedemo.com/")
    
    # Assert on the 'page' instance with the correct URL and title
    expect(page).to_have_title(re.compile("Swag Labs"))

@pytest.fixture(scope="session")
def page(browser):
   page = browser.new_page()
   yield page
   page.close()