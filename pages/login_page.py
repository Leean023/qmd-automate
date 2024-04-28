from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')


    # Methods
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password + Keys.RETURN) 

   
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
       
