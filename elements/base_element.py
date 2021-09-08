from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.web_elements = None
        self.find()

    def find(self):
        try:
            elements = WebDriverWait(self.driver, 0).until(
                EC.visibility_of_all_elements_located(locator=self.locator)
            )
            element = elements[0]
            logging.info(f"Found Elements with text: {[element.text for element in elements]}")
            self.web_element = element
            self.web_elements = elements

        except Exception as e:
            logging.exception("Failed to find element")

        return None

    def input_text(self, txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 0).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        logging.info("Clicking " + element.tag_name)
        element.click()
        logging.info("Clicked " + str(self.locator))
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text