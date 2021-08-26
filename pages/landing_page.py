from settings import urls, locators
from pages.base_page import BasePage
from elements.locator import Locator
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By


class LandingPage(BasePage):

    url = urls.LANDING_PAGE


    @property
    def login_link(self):
        locator = Locator(by=By.XPATH, value=locators.LOGIN_LINK)
        return BaseElement(self.driver, locator)

