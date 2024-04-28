from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LeaveCreditTab(BasePage):

    def access_leave_credit(self):
      return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[9]/a')))
    
    def leave_credit_text_exs(self):
     return WebDriverWait(self.driver, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="side-menu"]/li[9]/a/span'), "Leave Credit Management"))
    
    def go_to_leave_credit(self):
        leave = self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[9]/a')
        leave.click()

        