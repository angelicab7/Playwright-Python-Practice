import pytest
import re
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from pages.login import LoginPage

"""
    Fixture to create a browser instance and a session-level scope.
"""
@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

"""
    Fixture to create a new page within the browser instance.
"""
@pytest.fixture(scope="session")
def page(browser):
   page = browser.new_page()
   yield page
   page.close()
   
"""
    Fixture to navigate to the webpage before each test.
"""
@pytest.fixture(scope="session", autouse=True)
def before_each(page: Page):
    print("before the test runs")
    
    # Use the 'page' instance, not the 'Page' class
    page.goto("https://www.saucedemo.com/")
    
    # Assert on the 'page' instance with the correct URL and title
    expect(page).to_have_title(re.compile("Swag Labs"))

"""
    Fixture to perform a successful login before each test.
"""
@pytest.fixture
def login(page: Page):
    login_page = LoginPage()
    login_page.test_click_username_and_password(page)
    yield
