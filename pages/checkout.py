from selenium.webdriver.common.by import By
from pages.base_page import  BasePage
from elements.locator import  Locator
from settings import locators
from elements.base_element import BaseElement


class CheckoutPage(BasePage):

    @property
    def checkout(self):
        locator = Locator(by=By.XPATH, value=locators.CHECKOUT)
        return BaseElement(driver=self.driver, locator=locator)

    