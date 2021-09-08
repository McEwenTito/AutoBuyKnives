from auto_driver import AutoDriver
from settings import urls

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auto_driver = AutoDriver()
    auto_driver.login()
    auto_driver.select_expensive_product(urls.APPAREL)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
