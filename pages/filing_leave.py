from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Locators

class FileLeave(BasePage):
    
    FILELEAVE = (By.XPATH, '//*[@id="side-menu"]/li[11]/a')
    ADDLEAVEBTN = (By.XPATH, '//*[@id="calendar"]/div[1]/div[3]/button[1]')
    LEAVETYPEDRPDN = (By.NAME, 'leave_type_id')
    VCNLV = (By.ID, 'leave-type-option-1')
    TOGGLESWITCH = (By.XPATH, '//*[@id="add-leave-form"]/div/div/div[2]/div[2]/span')
    TOGGLELABEL = (By.XPATH, '//*[@id="day-switch-label"]')

    CALENDARSTART = (By.ID, 'start_date')
    CALENDAREND = (By.ID, 'end_date')
    REASON = (By.NAME, 'reason')
    ATTACHFILE = (By.NAME, 'leave-attach-file')
    CLOSEMODAL = (By.XPATH, '//*[@id="closeModal"]')
    SUBMITBTN = (By.XPATH, '//*[@id="add-leave-form"]/div/div/div[2]/div[4]/button[2]')

    #CALENDAR UI

    NEXTCAL = (By.XPATH, '//*[@id="calendar"]/div[1]/div[1]/div/button[3]/span')
    OCT2024 = (By.XPATH, '//*[@id="fc-dom-1"]')
    OCT22 = (By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/a/div/div/div/div')

 
    def click_file_leave(self):
        try:
            click_file_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.FILELEAVE)
            )
            click_file_leave.click()
            return True 
        except Exception as e:
            print(f"Error clicking file leave tab: {e}")
            return False
    
    def click_file_leave_btn(self):
        try:
            click_file_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ADDLEAVEBTN)
            )
            click_file_leave.click()
            return True 
        except Exception as e:
            print(f"Error clicking file leave button: {e}")
            return False
    
    def click_file_leave_drpdwn(self):
        try:
            click_file_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LEAVETYPEDRPDN)
            )
            click_file_leave.click()
            return True 
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False
        
        
    def select_leave_option(self, option_text):
        try:
            click_vacation_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LEAVETYPEDRPDN)
            )
            
            select = Select(click_vacation_leave)
            select.select_by_visible_text(option_text)
            
            return True
        except Exception as e:
            print(f"Error clicking {option_text}: {e}")
            return False

    def click_leave_vacation(self):
        return self.select_leave_option("Vacation Leave")

    def click_leave_sick(self):
        return self.select_leave_option("Sick Leave")

    def click_leave_other(self):
        return self.select_leave_option("Other Leave")
    
    def click_toggle_switch(self):
        try:
            click_file_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.TOGGLESWITCH)
            )
            click_file_leave.click()
            return True 
        except Exception as e:
            print(f"Error clicking toggle switch: {e}")
            return False
        
    def toggle_label(self):
        try:
            toggle_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TOGGLELABEL)
            )
            toggle_label_text = toggle_element.text
            return toggle_label_text
        except Exception as e:
            print(f"Error displaying toggle label: {e}")
            return False
        
    def input_start(self, startVal):
        try:
            start_date = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CALENDARSTART)
            )
            start_date.clear()
            start_date.send_keys(startVal)
            return True
        except Exception as e:
            print(f"Error inputting start date: {e}")
            return False
    
    def input_end(self, endVal):
        try:
            end_date = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CALENDAREND)
            )
            end_date.clear()
            end_date.send_keys(endVal)
            return True
        except Exception as e:
            print(f"Error inputting end date ehe: {e}")
            return False

    
        
    def input_reason(self, Reason):
        try:
            end_date = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REASON)
            )
 
            end_date.send_keys(Reason)
            return True
        except Exception as e:
            print(f"Error inputting reason: {e}")
            return False
        
    def input_file_attach(self, file_path):
        try:
            file_path = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ATTACHFILE)
            )
 
            file_path.send_keys(file_path)
            return True
        except Exception as e:
            print(f"Error attaching file: {e}")
            return False
        
    def refresh_browser(self):
        try:
            self.driver.refresh()
        except Exception as e:
            print(f"Error refreshing browser: {e}")
            return False
        
         
    def close_modal(self):
        try:
            close_file_leave_modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CLOSEMODAL)
            )
            close_file_leave_modal.click()
            return True
        except Exception as e:
            print(f"Error refreshing browser: {e}")
            return False
    
    def click_file_submit(self):
        try:
            click_file_leave = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SUBMITBTN)
            )
            click_file_leave.click()
            return True 
        except Exception as e:
            print(f"Error clicking submit button: {e}")
            return False
        
    #calendar
    def click_next_calendar_modal(self):
        try:
            click_next_cal= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.NEXTCAL)
            )
            click_next_cal.click()
            return True
        except Exception as e:
            print(f"Error clicking next for calendar ui browser: {e}")
            return False
        
    def presence_of_oct_2024(self):
        try:
            month_presence = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.OCT2024)
            )
            return month_presence.text
        except Exception as e:
            print(f"Error fetching the month text in year 2024: {e}")
            return None
        
    
    def presence_of_oct_22_exact_date(self):
        try:
            date_presence = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.OCT22)
            )
            return date_presence.text
        except Exception as e:
            print(f"Error fetching the october 22 text: {e}")
            return None
            
    


    
                
        
        
    

    


            