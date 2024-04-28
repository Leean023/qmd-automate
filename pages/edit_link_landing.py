from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class EditLanding(BasePage):
    #Locators
    EDITLINK1 = (By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[6]/a')
    EMPLOYEENME = (By.XPATH, '//*[@id="page-wrapper"]/div[2]/h1/strong')
    EMPLOYEERLE = (By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div[1]/p[1]/strong')
    EMPLOYEESTRT = (By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div[2]/p[1]/strong')
    EMPLOYEEST = (By.ID, 'employment-status-label')
    EMPLOYEETEAM = (By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div[1]/p[2]/strong')
    EMPLOYEETENURE = (By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div[2]/p[2]/strong')

    LCSTARTDATE = (By.NAME, 'start_date')
    LCVACATIONLV = (By.XPATH, '//*[@id="saveForm"]/div/div[2]/div/div/div[2]/input[1]')
    LCSICKLV = (By.XPATH, '//*[@id="saveForm"]/div/div[2]/div/div/div[2]/input[2]')
    LCOTHERLV = (By.XPATH, '//*[@id="saveForm"]/div/div[2]/div/div/div[2]/input[3]')
    LCAMOUNTPP = (By.NAME, 'periodical_amount')
    EDITBTN = (By.XPATH, '//*[@id="page-wrapper"]/div[5]/div[2]/div/div/div[4]/div/button')
    SVEEDITED = (By.XPATH, '//*[@id="saveForm"]/div/div[2]/div/div/div[4]/div/button[1]')

    LCPOINTS = (By.XPATH, '//*[@id="page-wrapper"]/div[5]/div[2]/div/div/div[3]/p[2]')
    SAVEEDITED = (By.XPATH, '//*[@id="saveForm"]/div/div[2]/div/div/div[4]/div/button[1]')






    def ClickEdit1(self):
        try:
            iteration_through_page = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.EDITLINK1)
            )
            iteration_through_page.click()
            return True 
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False
        
    def EmployeeName(self):
        try:
            employee_name_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEENME)
            )
            return employee_name_element
        except Exception as e:
            print(f"Employee name element not visible: {e}")
            return None

        
    
    def EmployeeRole(self):
        try:
            employee_role_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEERLE)
            )
            return employee_role_element 
        except Exception as e:
            print(f"Empoloyee Role Not Visible {e}")
            return None
        
        
    def EmployeeStart(self):
        try:
            employee_start_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEESTRT)
            )
            return employee_start_element
        except Exception as e:
            print(f"Empoloyee Role Not Visible {e}")
            return None
    
    def EmployeeStat(self):
        try:
            employee_stat_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEEST)
            )
            return employee_stat_element
        except Exception as e:
            print(f"Empoloyee Role Not Visible {e}")
            return None
        
    def EmployeeTeam(self):
        try:
            employee_team_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEETEAM)
            )
            return employee_team_element
        except Exception as e:
            print(f"Empoloyee Team Not Visible {e}")
            return None
        
    def EmployeeTenure(self):
        try:
            employee_tenure_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMPLOYEETENURE)
            )
            return employee_tenure_element
        except Exception as e:
            print(f"Empoloyee Tenure Not Visible {e}")
            return None
        
        
    def EditTexFields(self):
        try:
            edit_textfields = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.EDITBTN)
            )
            edit_textfields.click()
            return True
        except Exception as e:
            print(f"Employee Tenure Not Visible {e}")
            return False
        

    def LeaveCreditStartDate(self):
        try:
            leave_credit_start = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LCSTARTDATE)
            )

            extracted_text = leave_credit_start.get_attribute("value")
            return extracted_text  # Return the extracted text directly
        except Exception as e:
            print(f"leave credit start date is not visible {e}")
            return False
        

    def LeaveCreditVacationLeave(self):
        try:
            leave_credit_vc = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LCVACATIONLV)
            )

            extracted_text = leave_credit_vc.get_attribute("value")
            return extracted_text  # Return the extracted text directly
        except Exception as e:
            print(f"leave credit vacation leave is not visible {e}")
            return False
        


    def LeaveCreditSickLeave(self):
        try:
            leave_credit_sl = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LCSICKLV)
            )

            extracted_text = leave_credit_sl.get_attribute("value")
            return extracted_text  # Return the extracted text directly
        except Exception as e:
            print(f"leave credit sick leave is not visible {e}")
            return False
    
    def LeaveCreditOtherLeave(self):
        try:
            leave_credit_ol = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LCOTHERLV)
            )

            extracted_text = leave_credit_ol.get_attribute("value")
            return extracted_text  # Return the extracted text directly
        except Exception as e:
            print(f"leave credit other leave is not visible {e}")
            return False

    def LeaveCreditAmountPerPeriod(self):
        try:
            leave_credit_ampp = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LCAMOUNTPP)
            )

            extracted_text = leave_credit_ampp.get_attribute("value")
            return extracted_text  # Return the extracted text directly
        except Exception as e:
            print(f"leave credit amount per period is not visible {e}")
            return False
        
    def LeaveCreditLeavePoints(self):
        try:
            leave_credit_lp = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LCPOINTS)
            )
            return leave_credit_lp
        except Exception as e:
            print(f"leave credit amount per period is not visible {e}")
            return False



   # def editAllFields(self, vl):
      
        #  self.driver.find_element(*self.LCVACATIONLV).clear()
        #  self.driver.find_element(*self.LCVACATIONLV).send_keys(vl)

         # self.driver.find_element(self.LCSICKLV + Keys.BACK_SPACE).send_keys(sl)
         #self.driver.find_element(self.LCOTHERLV + Keys.BACK_SPACE).send_keys(ol)
          #self.driver.find_element(self.LCAMOUNTPP + Keys.BACK_SPACE).send_keys(app)
 
  
         # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SVEEDITED)).click()

    def enter_vl(self, vl):
        self.driver.implicitly_wait(10)  # Setting implicit wait to 10 seconds
        self.driver.find_element(*self.LCVACATIONLV).clear()
        self.driver.find_element(*self.LCVACATIONLV).send_keys(vl)

    def enter_sl(self, sl):
        self.driver.implicitly_wait(10)  # Setting implicit wait to 10 seconds
        self.driver.find_element(*self.LCSICKLV).clear()
        self.driver.find_element(*self.LCSICKLV).send_keys(sl)

    def enter_ol(self, ol):
        self.driver.implicitly_wait(10)  # Setting implicit wait to 10 seconds
        self.driver.find_element(*self.LCOTHERLV).clear()
        self.driver.find_element(*self.LCOTHERLV).send_keys(ol)

    def ClickEdit4(self):
        try:
            click_save_edit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SAVEEDITED)
            )
            click_save_edit.click()
            return True 
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False

        











                

        
            


