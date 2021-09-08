import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.add_to_cart import AddToCartPage
from pages.payment_method import PaymentMethodPage
from pages.product_page import ProductPage
from pages.checkout import CheckoutPage
from pages.shipping import ShippingPage, ShippingMethodPage
from settings import config, locators
from settings import urls


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized");
# chrome_options.add_argument("headless");


class AutoDriver:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_page_load_timeout(60)
        except Exception as e:
            logging.exception(e)


    def complete_shipping_info(self, url):
        shipping_page = ShippingPage(self.driver, url)
        # shipping_page.go()
        shipping_page.first_name.input_text(config.FIRST_NAME)
        shipping_page.last_name.input_text(config.LAST_NAME)
        shipping_page.company.input_text(config.COMPANY)
        shipping_page.address.input_text(config.ADDRESS)
        shipping_page.apartment.input_text(config.APARTMENT)
        shipping_page.city.input_text(config.CITY)
        shipping_page.zip_code.input_text(config.ZIP_CODE)
        shipping_page.country.click()
        shipping_page.continue_to_shipping.click()
        self.choose_shipping_method(self.driver.current_url)
        logging.info("This is the url :" + self.driver.current_url)


    def complete_payment_info(self, url):
        payment_method_page = PaymentMethodPage(self.driver, url)
        # payment_method_page.go()
        logging.info("\n\n\n " + url + "\n" + self.driver.current_url + "\n")
        iframe = self.driver.find_element_by_xpath(locators.IFRAME_CARD_NUMBER)
        self.driver.switch_to.frame(iframe)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_1)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_2)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_3)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_4)
        self.driver.switch_to.parent_frame()
        iframe = self.driver.find_element_by_xpath(locators.IFRAME_CARD_NAME)
        self.driver.switch_to.frame(iframe)
        payment_method_page.name_on_card.input_text(config.NAME_ON_CARD)
        self.driver.switch_to.parent_frame()
        iframe = self.driver.find_element_by_xpath(locators.IFRAME_CARD_EXPIRATION)
        self.driver.switch_to.frame(iframe)
        payment_method_page.expiration.input_card_text(config.EXPIRATION_DATE_1)
        payment_method_page.expiration.input_card_text(config.EXPIRATION_DATE_2)
        self.driver.switch_to.parent_frame()
        iframe = self.driver.find_element_by_xpath(locators.IFRAME_SECURITY_CODE)
        self.driver.switch_to.frame(iframe)
        payment_method_page.security_code().input_text(config.SECURITY_CODE)
        self.driver.switch_to.parent_frame()
        payment_method_page.same_as_shipping.click()
        payment_method_page.pay_now.click()


    def choose_shipping_method(self, url):
        shipping_method_page = ShippingMethodPage(self.driver, url=url)
        # shipping_method_page.go()
        logging.info("On url 444:" + self.driver.current_url)
        time.sleep(1)
        shipping_method_page.continue_to_payment.click()
        logging.info("This is the url :" + self.driver.current_url)
        self.complete_payment_info(self.driver.current_url)
        logging.info("Clinked something")




    def checkout(self):
        checkout_page = CheckoutPage(self.driver, urls.CART)
        checkout_page.go()
        try:
            logging.info("going to complete shipping information")
            checkout_page.checkout.click()
            self.complete_shipping_info(self.driver.current_url)
            logging.info("Completed shipping information")
        except:
            logging.info("FAiled to hahah")
            time.sleep(1)
            checkout_page.go()
            checkout_page.checkout.click()
            self.complete_shipping_info(self.driver.current_url)


    def add_to_cart(self, url, quantity):
        add_to_cart_page = AddToCartPage(self.driver, url)
        add_to_cart_page.quantity.web_element.clear()
        add_to_cart_page.quantity.input_text(quantity)
        add_to_cart_page.add_to_cart_button.click()
        try:
            logging.info("Inside error handler")
            time.sleep(1)
            stock_error = self.driver.find_element_by_xpath("//p[contains(@class, 'errors')]")
            stock_error = stock_error.text
            logging.info("Stock Error: " + stock_error)
            add_to_cart_page.go()
            add_to_cart_page.quantity.web_element.clear()
            add_to_cart_page.quantity.input_text(stock_error[17:18])
            add_to_cart_page.add_to_cart_button.click()
            self.checkout()
        except Exception as e:
            logging.exception(e)
            self.checkout()


    @classmethod
    def get_product_prices(cls, product_page) -> []:
        prices = []
        ###  Look for $ then float hahaha you super genius you
        for description in product_page.descriptions.web_elements:
            logging.info(description.text)
            price = description.text[description.text.rfind("$")+1:]
            prices.append(float(price))
        logging.info(f"All prices {prices}")
        return prices


    def sold_out(self, item, prices) -> bool:
        try:
            badge = item.find_element_by_xpath(".//span[@class='badge__text']")
            logging.info("Badge : " + badge.text)
            if "SOLD" in badge.text:
                logging.info("This item is sold out")
                prices.remove(max(prices))
                return True
            else:
                return False
        except:
            return False


    def select_expensive_product(self, url):
        product_page = ProductPage(self.driver, url=url)
        product_page.go()
        prices = self.get_product_prices(product_page=product_page)
        for description in product_page.descriptions.web_elements:
            price = description.text[description.text.rfind("$")+1:]
            item = description.find_element_by_xpath("..")
            if not self.sold_out(item, prices) and (float(price)) == max(prices):
                logging.info(description.text + " " + item.text)
                item.click()
                self.add_to_cart(self.driver.current_url, config.QUANTITY)
                break
            else:
                continue




    def start(self):
        landing_page = LandingPage(self.driver, url=urls.LANDING_PAGE)
        landing_page.go()
        landing_page.login_link.click()

    def login(self):
        login_page = LoginPage(self.driver, url=urls.LOGIN)
        login_page.go()
        time.sleep(1)
        login_page.email_field.input_text(config.EMAIL)
        login_page.password_field.input_text(config.PASSWORD)
        login_page.sign_in.click()


