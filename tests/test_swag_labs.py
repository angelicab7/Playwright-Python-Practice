import pytest
from playwright.sync_api import Page, expect
from pages.add_product_page import AddProductPage
from pages.your_info import YourInfoPage
from pages.overview_page import OverviewPage
from pages.confirmation_page import ConfirmationPage

def test_add_product_to_cart(page: Page, login):
    add_product = AddProductPage()
    add_product.add_product_to_cart(page)

def test_check_product_added(page: Page):
    check_product = AddProductPage()
    check_product.check_product_added(page)

def test_proceed_to_info_page(page: Page):
    navigate_to_product_page = AddProductPage()
    navigate_to_product_page.proceed_to_info_page(page)

def test_fill_your_info(page: Page):
    fill_info = YourInfoPage()
    fill_info.fill_your_info(page)

def test_proceed_to_overview(page: Page):
    click_continue = YourInfoPage()
    click_continue.proceed_to_overview_page(page)

def test_verify_overview(page: Page):
    overview_info = OverviewPage()
    overview_info.verify_payment_information_and_finish(page)

def test_verify_confirmation_page(page: Page):
    thank_you_message = ConfirmationPage()
    thank_you_message.verify_confirmation_page(page)
