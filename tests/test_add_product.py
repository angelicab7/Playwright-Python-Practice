import pytest
from playwright.sync_api import Page, expect
from pages.add_product import AddProductPage

def test_add_product_to_cart(page: Page, login):
    add_product = AddProductPage()
    add_product.test_add_product_to_cart(page)