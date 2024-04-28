from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  # Set an implicit wait

    def open_url(self, url):
        self.driver.get(url)

    # TO WAIT
    def wait_for_element(self, locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    # TO CLICK
    def do_click(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        if element:
            try:
                element.click()
            except Exception as e:
                print(f"Failed to click on element with locator {locator}. Error: {e}")

    # TO SEND KEYS
    def do_send_keys(self, locator, text, timeout=15):
        element = self.wait_for_element(locator, timeout)
        if element:
            try:
                element.send_keys(text)
            except Exception as e:
                print(f"Failed to send keys to element with locator {locator}. Error: {e}")

    # TO GET TEXT
    def get_element_text(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        if element:
            try:
                return element.text
            except Exception as e:
                print(f"Failed to get text from element with locator {locator}. Error: {e}")
