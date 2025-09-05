import re
from playwright.sync_api import Page, expect

class AddProductPage:

    def add_product_to_cart(self,page: Page):
        page.get_by_role("button",name="Add to cart").nth(4).click()

    def check_product_added(self,page: Page):
        page.locator(".shopping_cart_link").click()
        page.locator(".cart_item").is_visible()

    def proceed_to_info_page(self,page: Page):
        page.get_by_role("button",name="Checkout").click()
        page.get_by_text("Checkout: Your Information").is_visible()