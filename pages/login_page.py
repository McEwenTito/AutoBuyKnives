from settings import urls, locators
from pages.base_page import BasePage
from elements.locator import Locator
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    url = urls.LOGIN

    @property
    def email_field(self):
        locator = Locator(by=By.XPATH, value=locators.EMAIL_INPUT)
        return BaseElement(self.driver, locator)

    @property
    def password_field(self):
        locator = Locator(by=By.XPATH, value=locators.PASSWORD_INPUT)
        return BaseElement(self.driver, locator)

    @property
    def sign_in(self):
        locator = Locator(by=By.XPATH, value=locators.SIGN_IN)
        return BaseElement(self.driver, locator)
