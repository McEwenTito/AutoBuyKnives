from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.locator import Locator
from pages.base_page import BasePage


class AddToCartPage(BasePage):

    @property
    def quantity(self):
        locator = Locator(by=By.ID, value="Quantity")
        return BaseElement(self.driver, locator)

    @property
    def add_to_cart_button(self):
        locator = Locator(by=By.ID, value="AddToCart")
        return BaseElement(self.driver, locator)

