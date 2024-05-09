import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

# The setup function: Initializes the WebDriver, maximizes the browser window, and performs teardown operations.
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    def teardown():
        driver.quit()

    request.cls.driver = driver
    request.addfinalizer(teardown)

    driver.get("https://app-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80?lang=en")

# Utilizes the setup function for the test class.
@pytest.mark.usefixtures("setup")
class TestHomepage:


    def test_split_the_bill_pay_for_your_items(self):

        basepage = BasePage(self.driver)   # Creates an instance of the BasePage class.
        basepage.click_to_element(BasePage.LANDING_PAY_NOW)
        basepage.scroll_the_page()
        basepage.click_to_element(BasePage.SPLIT_BILL)
        basepage.wait_element_for_presence(BasePage.PAY_FOR_YOUR_ITEMS)
        basepage.click_to_element(BasePage.PAY_FOR_YOUR_ITEMS_SELECT)
        basepage.wait_element_for_presence(BasePage.FIRST_PLUS)
        basepage.wait_element_for_presence(BasePage.THIRD_PLUS)
        basepage.click_to_element(BasePage.FIRST_PLUS)
        basepage.click_to_element(BasePage.THIRD_PLUS)
        basepage.click_to_element(BasePage.CONFIRM)
        time.sleep(3)
        basepage.click_to_element(BasePage.CREDIT_CARD_AREA)
        basepage.switch_to_iframe(BasePage.FRAME)
        basepage.send_keys_to_element(BasePage.CREDIT_CARD_NUMBER, "4242424242424242")
        basepage.send_keys_to_element(BasePage.EXPIRATION_DATE, "02/26")
        basepage.send_keys_to_element(BasePage.CVC_NUMBER, "100")
        basepage.driver.switch_to.default_content()
        basepage.click_to_element(BasePage.PERC_FIVE_AMOUNT)
        basepage.click_to_element(BasePage.CHECKOUT_PAY_NOW)
        basepage.wait_element_for_presence(BasePage.PAYMENT_WAS_SUCCESSFUL)

    def test_split_the_bill_divide_the_bill_equally(self):
            basepage = BasePage(self.driver)   # Creates an instance of the BasePage class.
            basepage.click_to_element(BasePage.LANDING_PAY_NOW)
            basepage.scroll_the_page()
            basepage.click_to_element(BasePage.SPLIT_BILL)
            basepage.wait_element_for_presence(BasePage.DIVIDE_THE_BILL_EQUALLY)
            basepage.click_to_element(BasePage.DIVIDE_THE_BILL_EQUALLY_SELECT)
            basepage.click_to_element(BasePage.FIRST_PLUS_DIVIDE)
            basepage.click_to_element(BasePage.CONFIRM)
            time.sleep(3)
            basepage.click_to_element(BasePage.CREDIT_CARD_AREA)
            basepage.switch_to_iframe(BasePage.FRAME)
            basepage.send_keys_to_element(BasePage.CREDIT_CARD_NUMBER, "4242424242424242")
            basepage.send_keys_to_element(BasePage.EXPIRATION_DATE, "02/26")
            basepage.send_keys_to_element(BasePage.CVC_NUMBER, "100")
            basepage.driver.switch_to.default_content()
            basepage.click_to_element(BasePage.PERC_FIVE_AMOUNT)
            basepage.click_to_element(BasePage.CHECKOUT_PAY_NOW)
            basepage.wait_element_for_presence(BasePage.PAYMENT_WAS_SUCCESSFUL)
            time.sleep(2)

    def test_split_the_bill_pay_a_custom_amount(self):
            basepage = BasePage(self.driver)   # Creates an instance of the BasePage class.
            basepage.click_to_element(BasePage.LANDING_PAY_NOW)
            basepage.scroll_the_page()
            basepage.click_to_element(BasePage.SPLIT_BILL)
            basepage.wait_element_for_presence(BasePage.PAY_A_CUSTOM_AMOUNT_BUTTON)
            basepage.click_to_element(BasePage.PAY_A_CUSTOM_AMOUNT_SELECT)
            basepage.send_keys_to_element(BasePage.PAY_A_CUSTOM_AMOUNT_VALUE, "20")
            basepage.click_to_element(BasePage.CONFIRM)
            time.sleep(3)
            basepage.click_to_element(BasePage.CREDIT_CARD_AREA)
            basepage.switch_to_iframe(BasePage.FRAME)
            basepage.send_keys_to_element(BasePage.CREDIT_CARD_NUMBER, "4242424242424242")
            basepage.send_keys_to_element(BasePage.EXPIRATION_DATE, "02/26")
            basepage.send_keys_to_element(BasePage.CVC_NUMBER, "100")
            basepage.driver.switch_to.default_content()
            basepage.click_to_element(BasePage.CHECKOUT_PAY_NOW)
            basepage.wait_element_for_presence(BasePage.PAYMENT_WAS_SUCCESSFUL)
            time.sleep(2)

    def test_pay_fully(self):

        basepage = BasePage(self.driver)   # Creates an instance of the BasePage class.
        basepage.click_to_element(BasePage.LANDING_PAY_NOW)
        basepage.scroll_the_page()
        basepage.click_to_element(BasePage.PAY_FULLY)
        time.sleep(3)
        basepage.click_to_element(BasePage.CREDIT_CARD_AREA)
        basepage.switch_to_iframe(BasePage.FRAME)
        basepage.send_keys_to_element(BasePage.CREDIT_CARD_NUMBER, "4242424242424242")
        basepage.send_keys_to_element(BasePage.EXPIRATION_DATE, "02/26")
        basepage.send_keys_to_element(BasePage.CVC_NUMBER, "100")
        basepage.driver.switch_to.default_content()
        basepage.click_to_element(BasePage.CHECKOUT_PAY_NOW)
        basepage.wait_element_for_presence(BasePage.PAYMENT_WAS_SUCCESSFUL)