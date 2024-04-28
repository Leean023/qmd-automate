from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException



class EditLink(BasePage):
    # Locators
    SEARCHFIELD = (By.CSS_SELECTOR, 'input[type="search"].form-control.input-sm')
    SEARCHRESULT = (By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr/td[2][contains(text(), "Dungca, Aljim Carillo.")]/ancestor::tr')
    TABLEBODYRES = (By.XPATH, '//*[@id="DataTables_Table_0"]/tbody')
    TABLEROWS = (By.TAG_NAME, 'tr')
    TABLEDATAS = (By.TAG_NAME, 'td')

    TABLEBODYFIRST = (By.XPATH, '//*[@id="DataTables_Table_0"]/tbody')

    CLICKDESCENDING = (By.XPATH, '//*[@id="DataTables_Table_0"]/thead/tr/th[2]')

    NEXTPAGE2nd = (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul/li[3]/a')
    NEXTPAGE3rd = (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul/li[4]/a')
    NEXTPAGE4th = (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul/li[5]/a')
    NEXTPAGE5th = (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul/li[6]/a')

    NEXTPAGEDISABLED = (By.XPATH, '//*[@id="DataTables_Table_0_next"]')
    RESETPGNUM = (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul/li[2]/a')

    EMPTYSEARCHRES = (By.CLASS_NAME, 'dataTables_empty')


    def searchField(self, input):
        
      return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCHFIELD)).send_keys(input)

    def emptySearchField(self):
        search_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCHFIELD))
        search_field.clear()
        search_field.send_keys(Keys.BACKSPACE) 

         
    
    def searchResult(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCHRESULT))
        text = self.driver.find_element(*self.SEARCHRESULT).text
        return text

    def searchOrder(self):
        table_body = self.driver.find_element(*self.TABLEBODYRES)
        rows = table_body.find_elements(*self.TABLEROWS)
        return rows
    

    def dataAvailability(self):
        table_body = self.driver.find_element(*self.TABLEBODYFIRST)
        rows = table_body.find_elements(*self.TABLEROWS)
        
        # Define an empty list to store cell elements for each row
        tabledata = []
        
        # Iterate over each row and find elements within each row
        for row in rows:
            cells = row.find_elements(*self.TABLEDATAS)
            tabledata.append(cells)  # Append the list of cell elements to the tabledata list
        
        return tabledata  # Return the list containing cell elements for all rows
    

    def get_first_column_data(self):
        table_body = self.driver.find_element(*self.TABLEBODYRES)
        rows = table_body.find_elements(*self.TABLEROWS)
        
        first_column_data = []
        for row in rows:
            cells = row.find_elements(*self.TABLEDATAS)
            first_cell = cells[1]  # Get the first cell (first column) of the row
            first_column_data.append(first_cell.text)  # Extract the text from the first cell
        
        return first_column_data
    
    def click_descending_name(self):
        click_descending = self.driver.find_element(*self.CLICKDESCENDING)
        click_descending.click()


    def pagination_2nd(self):
        try:
            iteration_through_page = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXTPAGE2nd)
            )
            iteration_through_page.click()
            return True 
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False


    def pagination_3rd(self):
        try:
            iteration_through_page = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXTPAGE3rd)
            )
            iteration_through_page.click()
            return True  
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False
        
    def pagination_4th(self):
        try:
            iteration_through_page = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXTPAGE4th)
            )
            iteration_through_page.click()
            return True  
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False
    
    def pagination_5th(self):
        try:
            iteration_through_page = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXTPAGE5th)
            )
            iteration_through_page.click()
            return True  
        except Exception as e:
            print(f"Error clicking pagination button: {e}")
            return False
        
    
    def reset_page_number(self):
        page1 = self.driver.find_element(*self.RESETPGNUM).click()
        return page1
    
    def empty_result(self):
        empty = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMPTYSEARCHRES))
        return empty.text










            

        







