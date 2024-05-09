import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from loguru import logger  # Import the logging library 'logger' from Loguru.



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Initializes the BasePage with the WebDriver instance.
    # Locator constants for elements on the page.
    LANDING_PAY_NOW = (By.XPATH, "//button[@data-qa-id='landing-pay-now']")
    SPLIT_BILL = (By.XPATH, "//button[@data-qa-id='billing-split-bill']")
    PAY_FOR_YOUR_ITEMS = (By.XPATH, "//h3[@data-qa-id='split-modal-by-item']")
    DIVIDE_THE_BILL_EQUALLY = (By.XPATH, "//h3[@data-qa-id='split-modal-by-share']")
    PAY_A_CUSTOM_AMOUNT_BUTTON = (By.XPATH, "//h3[@data-qa-id='split-modal-custom']")
    PAY_A_CUSTOM_AMOUNT_VALUE = (By.XPATH, "//input[@id='fullWidth']")
    DIVIDE_THE_BILL_EQUALLY_SELECT = (By.XPATH, "//button[@id='select-byShare']")
    PAY_A_CUSTOM_AMOUNT_SELECT = (By.XPATH, "//button[@id='select-custom']")
    PAY_FOR_YOUR_ITEMS_SELECT = (By.XPATH, "//button[@id='select-byItem']")
    FIRST_PLUS = (By.XPATH, "//button[@id='add-item-1']")
    FIRST_PLUS_DIVIDE = (By.XPATH, "//*[@data-testid='AddRoundedIcon']")
    THIRD_PLUS = (By.XPATH, "//button[@id='add-item-3']")
    CONFIRM = (By.XPATH, "//button[@id='split-bill']/span[@class='wrapper']")
    PAY_AMOUNT_TEXT_AREA = (By.XPATH, "//div[@class='MuiBox-root css-1s9tqk4']")
    CREDIT_CARD_NUMBER = (By.XPATH, "//input[@id='Field-numberInput']")
    PAY_FULLY = (By.XPATH, "//button[@id='pay-full-bill']")
    CVC_NUMBER = (By.XPATH, "//input[@id='Field-cvcInput']")
    EXPIRATION_DATE = (By.XPATH, "//input[@id='Field-expiryInput']")
    CREDIT_CARD_AREA = (By.XPATH, "//*[@class='PayStripe_cardOverlay__VScOx']")
    EDIT_SPLIT = (By.XPATH, "//*[@class='MuiTouchRipple-root css-w0pj6f']")
    PAY_AMOUNT = (By.XPATH, "//*[@data-testid='EditRoundedIcon']")
    PERC_FIVE_AMOUNT = (By.XPATH, "//div[@class='MuiBox-root css-hk5mkc']")
    CHECKOUT_PAY_NOW = (By.XPATH, "//button[contains(@class, 'PayButtonElement_button__V8yic')]")
    PAYMENT_WAS_SUCCESSFUL = (By.XPATH, "//p[contains(@class, 'css-1dbb4wf')]")
    FRAME = ((By.XPATH, "//iframe[contains(@src, 'elements-inner-payment-edc4a3b1feea16ee9b8e9917c9780645')]"))


    # Clicks on an element identified by locator.
    def click_to_element(self, locator):
        try:
            element = self.wait_element_for_presence(locator)
            element.click()
            logger.info(f"{locator} öğesine tıklandı.")
        except NoSuchElementException as e:
            logger.error(f"Hata: {e}")

    # Waits for an element identified by locator to be clickable.
    def wait_element_for_presence(self, locator):
        try:
            element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
            logger.info(f"{locator} öğesi bulundu.")
            return element
        except NoSuchElementException as e:
            logger.error(f"Hata: {e}")

    # Sends keys to an element identified by locator.
    def send_keys_to_element(self, locator, text):
        try:
            element = self.wait_element_for_presence(locator)
            element.send_keys(text)
            logger.info(f"{text} metni {locator} öğesine gönderildi.")
        except NoSuchElementException as e:
            logger.error(f"Hata: {e}")

    # Switches to an iframe identified by frame_locator.
    def switch_to_iframe(self, frame_locator):
        try:
            iframe = self.wait_element_for_presence(frame_locator)
            self.driver.switch_to.frame(iframe)
        except NoSuchElementException:
            print("Iframe bulunamadı.")

    # Scrolls the page downwards.
    def scroll_the_page(self):
        time.sleep(2)
        self.driver.execute_script("window.scroll(0, 300);")


