from settings import config

CLOSE_AD = "/html/body/div[2]/div/div[1]/div/button"
LOGIN_LINK = "/html/body/div[3]/div[1]/div/div/ul[2]/li[1]/a"
# EMAIL_INPUT = "/html/body/main/div/div/div/div/div[2]/form/input[3]"
EMAIL_INPUT = "/html/body/div[4]/main/div/div/div[2]/form/input[3]"
# PASSWORD_INPUT = "/html/body/main/div/div/div/div/div[2]/form/input[4]"
PASSWORD_INPUT = "/html/body/div[4]/main/div/div/div[2]/form/input[4]"
# SIGN_IN = "/html/body/main/div/div/div/div/div[2]/form/p[2]/input"
SIGN_IN = "/html/body/div[4]/main/div/div/div[2]/form/p[1]/input"
# PRICE = "//p[@class='grid-link__meta']"
PRICE = "//p[@class='product-item__price-wrapper']"
ITEM = "//a[contains(@href, '/products')]"
# ITEM = "/html/body/div[4]/main/div/div/div[1]/div/a/span/span"

CHECKOUT = "/html/body/div[5]/main/div/div/form/footer/div/div/p[3]/button"
FIRST_NAME = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input"
LAST_NAME = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[2]/div/input"
COMPANY = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[3]/div/input"
ADDRESS = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[4]/div/input"
APARTMENT = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[5]/div/input"
CITY = "//input[@placeholder='City']"
ZIP_CODE = "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[9]/div/input"
COUNTRY = f"//option[@value='{config.COUNTRY}']"
CONTINUE_TO_SHIPPING = "/html/body/div/div/div/main/div[1]/form/div[2]/button"
CONTINUE_TO_PAYMENT = "/html/body/div/div/div/main/div[1]/form/div[2]/button"
CARD_NUMBER = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/div[3]/div[1]/div/div[1]/iframe"
NAME_ON_CARD = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/div[3]/div[2]"
EXPIRATION = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/div[3]/div[3]/div/div/iframe"
SECURITY_CODE = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/div[3]/div[4]/div/div[1]/iframe"
IFRAME_CARD_NUMBER = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/div[3]/div[1]/div/div[1]/iframe"
IFRAME_CARD_NAME = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[2]/div/div/iframe"
IFRAME_CARD_EXPIRATION = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[3]/div/div/iframe"
IFRAME_SECURITY_CODE = "/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[4]/div/div[1]/iframe"
SAME_AS_SHIPPING_ADDRESS = "/html/body/div/div/div/main/div[1]/div/form/div[2]/div[2]/fieldset/div[1]/div"
PAY_NOW = "/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button"

