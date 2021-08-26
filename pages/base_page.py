import logging

from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.locator import Locator
from settings import locators

logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        logging.info(f"On page: {self.url}")

    @property
    def close_ad(self):
        locator = Locator(by=By.XPATH, value=locators.CLOSE_AD)
        return BaseElement(self.driver, locator)

    def go(self):
        self.driver.get(self.url)
        try:
            self.close_ad.click()
        except Exception as e:
            logging.warning(e)

