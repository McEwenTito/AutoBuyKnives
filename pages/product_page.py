from selenium.webdriver.common.by import By

from elements.locator import Locator
from pages.base_page import BasePage
from settings import urls, locators
from elements.base_element import BaseElement

class ProductPage(BasePage):

    # url = urls.APPAREL

    @property
    def available_items(self):
        locator = Locator(by=By.XPATH, value=locators.ITEM)
        return BaseElement(self.driver, locator)


    @property
    def descriptions(self):
        locator = Locator(by=By.XPATH, value=locators.PRICE)
        return BaseElement(self.driver, locator)

