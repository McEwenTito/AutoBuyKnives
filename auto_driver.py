import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
        shipping_page.company.input_text(config.COMPANY)
        # shipping_page.go()
        # shipping_page.first_name.input_text(config.FIRST_NAME)
        # shipping_page.last_name.input_text(config.LAST_NAME)
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
        logging.info("\n\n\n " + url + "\n" + self.driver.current_url + "\n")
        act = ActionChains(payment_method_page.driver)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_1)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_2)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_3)
        payment_method_page.card_number.input_card_text(config.CARD_NUMBER_4)
        time.sleep(2)
        act.send_keys(Keys.TAB)
        # act.send_keys(Keys.TAB)
        act.perform()
        act.send_keys(config.NAME_ON_CARD).perform()

        try:
            payment_method_page.expiration.input_card_text(config.EXPIRATION_DATE_1)
            payment_method_page.expiration.input_card_text(config.EXPIRATION_DATE_2)
            payment_method_page.security_code.input_card_text(config.SECURITY_CODE)
            payment_method_page.same_as_shipping.click()
            payment_method_page.pay_now.click()
        except Exception as e:
            print("Except")
            print(e)
            pass


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
            time.sleep(2)
            logging.info("going to complete shipping information")
            checkout_page.checkout.click()
            self.complete_shipping_info(self.driver.current_url)
            logging.info("Completed shipping information")
        except:

            logging.info("FAiled to hahah")
            return
            time.sleep(1)
            checkout_page.go()
            checkout_page.checkout.click()
            self.complete_shipping_info(self.driver.current_url)


    def add_to_cart(self, url, quantity):
        add_to_cart_page = AddToCartPage(self.driver, url)
        add_to_cart_page.add_to_cart_button.click()
        time.sleep(2)
        self.checkout()


    @classmethod
    def sanitize_price(cls, price):
        return price.replace(",", "")

    @classmethod
    def hover(cls, product_page, product):
        a = ActionChains(product_page.driver)
        a.move_to_element(product).perform()


    @classmethod
    def get_product_prices(cls, product_page) -> []:
        prices = {}
        #  Mind the hover
        #  Look for $ then float hahaha you super genius you
        for product in product_page.available_items.web_elements:
            cls.hover(product_page, product)
            print(product.text)
            logging.info(product.text)
            price = product.text[product.text.rfind("$")+1:]
            try:
                prices[product] = float(cls.sanitize_price(price))
            except ValueError:
                logging.warning("Did not find price. Product could be sold out")
                continue
        logging.info(f"All prices {prices}")
        return prices



    def select_expensive_product(self, url):
        product_page = ProductPage(self.driver, url=url)
        product_page.go()
        product_prices = self.get_product_prices(product_page=product_page)
        print(f'{type(max(product_prices.values()))} {max(product_prices.values())}')
        print(product_prices.values())
        for product in product_prices:
            print(f'{type(product_prices[product])}')
            if product_prices[product] == max(product_prices.values()):
                product.click()
                self.add_to_cart(urls.CART, 1)
            else:
                logging.info("not max")



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


