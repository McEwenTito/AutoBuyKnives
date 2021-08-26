from settings import config

CLOSE_AD = "/html/body/div[2]/div/div[1]/div/button"
LOGIN_LINK = "/html/body/div[3]/div[1]/div/div/ul[2]/li[1]/a"
EMAIL_INPUT = "/html/body/main/div/div/div/div/div[2]/form/input[3]"
PASSWORD_INPUT = "/html/body/main/div/div/div/div/div[2]/form/input[4]"
SIGN_IN = "/html/body/main/div/div/div/div/div[2]/form/p[2]/input"
PRICE = "//p[@class='grid-link__meta']"
ITEM = "//a[contains(@href, '/products')]"
CHECKOUT = "/html/body/main/div/div/form/div[4]/div/div/input[2]"
FIRST_NAME = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input"
LAST_NAME = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[2]/div/input"
COMPANY = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[3]/div/input"
ADDRESS = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[4]/div/input"
APARTMENT = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[5]/div/input"
CITY = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[6]/div/input"
ZIP_CODE = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[9]/div/input"
COUNTRY = f"//option[@value='{config.COUNTRY}']"
CONTINUE_TO_SHIPPING = "/html/body/div/div/div/main/div[1]/form/div[2]/button"
CONTINUE_TO_PAYMENT = "/html/body/div/div/div/main/div[1]/form/div[2]/button"
CARD_NUMBER = "/html/body/form/input[1]"
NAME_ON_CARD = "/html/body/form/input[2]"
EXPIRATION = "/html/body/form/input[5]"
SECURITY_CODE = "/html/body/form/input[6]"
IFRAME_CARD_NUMBER = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe"
IFRAME_CARD_NAME = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[2]/div/div/iframe"
IFRAME_CARD_EXPIRATION = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[3]/div/div/iframe"
IFRAME_SECURITY_CODE = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[4]/div/div[1]/iframe"
SAME_AS_SHIPPING_ADDRESS = "/html/body/div/div/div/main/div[1]/div/form/div[2]/div[2]/fieldset/div[1]/div"
PAY_NOW = "/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button"
