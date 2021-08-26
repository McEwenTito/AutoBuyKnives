from pages.base_page import BasePage
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from elements.locator import Locator
from settings import locators

class ShippingMethodPage(BasePage):

    @property
    def continue_to_payment(self):
        locator = Locator(by=By.XPATH, value=locators.CONTINUE_TO_PAYMENT)
        return BaseElement(self.driver, locator)

class ShippingPage(BasePage):

    @property
    def first_name(self):
        locator = Locator(by=By.XPATH, value=locators.FIRST_NAME)
        return BaseElement(self.driver, locator)

    @property
    def last_name(self):
        locator = Locator(by=By.XPATH, value=locators.LAST_NAME)
        return BaseElement(self.driver, locator)

    @property
    def company(self):
        locator = Locator(by=By.XPATH, value=locators.COMPANY)
        return BaseElement(self.driver, locator)

    @property
    def address(self):
        locator = Locator(by=By.XPATH, value=locators.ADDRESS)
        return BaseElement(self.driver, locator)

    @property
    def apartment(self):
        locator = Locator(by=By.XPATH, value=locators.APARTMENT)
        return BaseElement(self.driver, locator)

    @property
    def city(self):
        locator = Locator(by=By.XPATH, value=locators.CITY)
        return BaseElement(self.driver, locator)

    @property
    def zip_code(self):
        locator = Locator(by=By.XPATH, value=locators.ZIP_CODE)
        return BaseElement(self.driver, locator)

    @property
    def country(self):
        locator = Locator(by=By.XPATH, value=locators.COUNTRY)
        return BaseElement(self.driver, locator)

    @property
    def continue_to_shipping(self):
        locator = Locator(by=By.XPATH, value=locators.CONTINUE_TO_SHIPPING)
        return BaseElement(self.driver, locator)