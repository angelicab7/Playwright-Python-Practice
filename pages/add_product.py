import re
from playwright.sync_api import Page, expect

class AddProductPage:

    def test_add_product_to_cart(self,page: Page):
        page.get_by_role("button",name="Add to cart").nth(4).click()

