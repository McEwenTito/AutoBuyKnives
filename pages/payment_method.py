from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.locator import Locator
from pages.base_page import BasePage
from settings import locators




class PaymentMethodPage(BasePage):

    @property
    def card_number(self):
        locator = Locator(by=By.XPATH, value=locators.CARD_NUMBER)
        return BaseElement(self.driver, locator)

    @property
    def name_on_card(self):
        locator = Locator(by=By.XPATH, value=locators.NAME_ON_CARD)
        return BaseElement(self.driver, locator)

    @property
    def expiration(self):
        locator = Locator(by=By.XPATH, value=locators.EXPIRATION)
        return BaseElement(self.driver, locator)

    @property
    def security_code(self):
        locator = Locator(by=By.XPATH, value=locators.SECURITY_CODE)
        return BaseElement(self.driver, locator)

    @property
    def same_as_shipping(self):
        locator = Locator(by=By.XPATH, value=locators.SAME_AS_SHIPPING_ADDRESS)
        return BaseElement(self.driver, locator)

    @property
    def pay_now(self):
        locator = Locator(by=By.XPATH, value=locators.PAY_NOW)
        return BaseElement(self.driver, locator)

