import pytest
from selenium import webdriver
from pages.edit_link_landing import EditLanding
from utils.config import COLOR_GREEN
from utils.config import COLOR_RESET
import random
import time


@pytest.mark.usefixtures("browser")
def test_data_edit_link(browser):
    editlanding = EditLanding(browser)

    click_edit_link = editlanding.ClickEdit1()

    if click_edit_link:
        print(COLOR_GREEN + "\nClicking 'Edit Link' worked" + COLOR_RESET)

    assert click_edit_link, "edit link navigation not existing"

    

@pytest.mark.usefixtures("browser")
def test_data_employee_name(browser):
    editlanding = EditLanding(browser)

    edit_link_name = editlanding.EmployeeName()

    text_presence = edit_link_name.text

    if text_presence == "Taguibao, Jester Dela Cruz":
        print(COLOR_GREEN + "Visible Name is : Taguibao, Jester Dela Cruz" + COLOR_RESET)

    assert text_presence == "Taguibao, Jester Dela Cruz.", "Name: 'Taguibao, Jester Dela Cruz.' is not visible"



@pytest.mark.usefixtures("browser")
def test_data_employee_role(browser):
    editlanding_role = EditLanding(browser)

    edit_link_role = editlanding_role.EmployeeRole()

    text_presence = edit_link_role.text

    if text_presence == "Software Engineer":
        print(COLOR_GREEN + "Visible Role is : Software Engineer " + COLOR_RESET)

    assert text_presence == "Software Engineer", "Role: 'Software Engineer.' is not visible"


@pytest.mark.usefixtures("browser")
def test_data_employee_start(browser):
    editlanding_start = EditLanding(browser)

    edit_link_start = editlanding_start.EmployeeStart()

    text_presence = edit_link_start.text

    if text_presence == "2024-01-01":
        print(COLOR_GREEN + "Visible Start date is: 2024-01-01" + COLOR_RESET)

    assert text_presence == "2024-01-01", "Start date is empty or not visible"


@pytest.mark.usefixtures("browser")
def test_data_employee_stat(browser):
    editlanding_statt = EditLanding(browser)

    edit_link_stat = editlanding_statt.EmployeeStat()

    text_presence = edit_link_stat.text

    if text_presence == "Probationary":
        print(COLOR_GREEN + "Status is: Probationary" + COLOR_RESET)

    assert text_presence == "Probationary", "Stat field is empty or not visible"

@pytest.mark.usefixtures("browser")
def test_data_employee_team(browser):
    editlanding_statt = EditLanding(browser)

    edit_link_stat = editlanding_statt.EmployeeTeam()

    text_presence = edit_link_stat.text

    if text_presence == "Web Team":
        print(COLOR_GREEN + "Current selected employee is part of: Web Team" + COLOR_RESET)

    assert text_presence == "Web Team", "Stat field is empty or not visible" #//*[@id="page-wrapper"]/div[3]/div/div[2]/p[2]/strong

@pytest.mark.usefixtures("browser")
def test_data_employee_tenure(browser):
    editlanding_tenure = EditLanding(browser)

    edit_link_tenure = editlanding_tenure.EmployeeTenure()

    text_presence = edit_link_tenure.text

    assert text_presence != "", "Tenure is not displayed" #//*[@id="page-wrapper"]/div[3]/div/div[2]/p[2]/strong



@pytest.mark.usefixtures("browser")
def test_data_leave_credit_start(browser):
    editlanding_textfields = EditLanding(browser)

    leave_credit_start_date = editlanding_textfields.LeaveCreditStartDate()
    
    if (leave_credit_start_date != ""):
        print(COLOR_GREEN + "Start Date Field is not empty" + COLOR_RESET) 
    assert leave_credit_start_date != "", "Start date field is empty"



@pytest.mark.usefixtures("browser")
def test_data_leave_credit_vl(browser):
    editlanding_vl_field = EditLanding(browser)

    leave_credit_vl_txt = editlanding_vl_field.LeaveCreditVacationLeave()

    leave_credit_vl = float(leave_credit_vl_txt)
    
    if (leave_credit_vl != ""):
        print(COLOR_GREEN + "Vacation Leave Field is not empty: {}".format(leave_credit_vl) + COLOR_RESET) 
    assert leave_credit_vl != "", "Start date field is empty"



@pytest.mark.usefixtures("browser")
def test_data_leave_credit_sl(browser):
    editlanding_sl_field = EditLanding(browser)

    leave_credit_sl_txt = editlanding_sl_field.LeaveCreditSickLeave()

    leave_credit_sl = float(leave_credit_sl_txt)
    
    if (leave_credit_sl != ""):
        print(COLOR_GREEN + "Sick Leave Field is not empty: {}".format(leave_credit_sl) + COLOR_RESET) 
    assert leave_credit_sl != "", "Start date field is empty"



@pytest.mark.usefixtures("browser")
def test_data_leave_credit_ol(browser):
    editlanding_sl_field = EditLanding(browser)

    leave_credit_ol_txt = editlanding_sl_field.LeaveCreditOtherLeave()

    leave_credit_ol = float(leave_credit_ol_txt)
    
    if (leave_credit_ol != ""):
        print(COLOR_GREEN + "OtherLeave Field is not empty: {}".format(leave_credit_ol) + COLOR_RESET) 
    assert leave_credit_ol != "", "other date field is empty"


@pytest.mark.usefixtures("browser")
def test_data_leave_credit_ampp(browser):
    editlanding_ampp_field = EditLanding(browser)

    leave_credit_ampp = editlanding_ampp_field.LeaveCreditAmountPerPeriod()
    
    if (leave_credit_ampp != ""):
        print(COLOR_GREEN + " Amount Per Period Field is not empty: {}".format(leave_credit_ampp) + COLOR_RESET) 
    assert leave_credit_ampp != "", "Amount Per Period field is empty"


@pytest.mark.usefixtures("browser")
def test_data_leave_credit_lp(browser):
    editlanding_lp_field = EditLanding(browser)

    leave_credit_lp = editlanding_lp_field.LeaveCreditLeavePoints().text

    number = float(leave_credit_lp.split(":")[-1].strip())
    
    
    if (number != ""):
        print(COLOR_GREEN + "No Leave Points is not empty" + COLOR_RESET) 
    assert number != "", "Leave points field is empty"



@pytest.mark.usefixtures("browser")
def test_data_total_leave_validation(browser):
    edit_link_leaves = EditLanding(browser)

    vacation_leave = edit_link_leaves.LeaveCreditVacationLeave()
    sick_leave = edit_link_leaves.LeaveCreditSickLeave()
    other_leave = edit_link_leaves.LeaveCreditOtherLeave()

    leave_points = edit_link_leaves.LeaveCreditLeavePoints().text

    leave_points_vl = float(vacation_leave)
    leave_points_sl = float(sick_leave)
    leave_points_ol = float(other_leave)

    leave_points_ttl = float(leave_points.split(":")[-1].strip())
  

    total_value_pts = leave_points_vl + leave_points_sl + leave_points_ol
    rounded_total_value_pts = round(total_value_pts) 

    float_rounded_total_value = float(rounded_total_value_pts)
   
    if (float_rounded_total_value == leave_points_ttl):
        print(COLOR_GREEN + "Sum of leave pts: {} and total leaves pts: {} are equal".format(float_rounded_total_value, leave_points_ttl) + COLOR_RESET)
   
    assert float_rounded_total_value == leave_points_ttl, "total leave points is not equal to the sum of vl, ol, and sl"
    time.sleep(2)



@pytest.mark.usefixtures("browser")
def test_data_click_edit(browser):
    editlanding_textfields = EditLanding(browser)

    clicked_edit = editlanding_textfields.EditTexFields()
    
    if (clicked_edit):
        print(COLOR_GREEN + "The Edit button for edit textfields has been successfuly clicked" + COLOR_RESET) 
    assert clicked_edit, "The button was not clicked or the button is not existing"
    
  

@pytest.mark.usefixtures("browser")
def test_data_save_vl(browser):
    lcvl = EditLanding(browser)

    random_value = random.randint(1, 1000)

    edit_fields = lcvl.enter_vl(random_value)
    
    if (edit_fields):
        print(COLOR_GREEN + "Vacationn Leave field has been edited" + COLOR_RESET) 


@pytest.mark.usefixtures("browser")
def test_data_edit_sl(browser):
    lcsl = EditLanding(browser)
    random_value = random.randint(1, 1000)

    edit_fields = lcsl.enter_sl(random_value)
    
    if (edit_fields):
        print(COLOR_GREEN + "Sick Leave field has been edited" + COLOR_RESET) 

    

@pytest.mark.usefixtures("browser")
def test_data_edit_ol(browser):
    lcol = EditLanding(browser)
    random_value = random.randint(1, 1000)

    edit_fields = lcol.enter_ol(random_value)
    
    if (edit_fields):
        print(COLOR_GREEN + "Sick Leave field has been edited" + COLOR_RESET) 



@pytest.mark.usefixtures("browser")
def test_save_edit_fields(browser):
    lcsl = EditLanding(browser)

    save_fields = lcsl.ClickEdit4()
    
    if (save_fields):
        print(COLOR_GREEN + "Saving edited fields worked!" + COLOR_RESET) 
    time.sleep(2)


@pytest.mark.usefixtures("browser")
def test_data_total_leave_validation_after_recalc(browser):
    edit_link_leaves = EditLanding(browser)

    vacation_leave = edit_link_leaves.LeaveCreditVacationLeave()
    sick_leave = edit_link_leaves.LeaveCreditSickLeave()
    other_leave = edit_link_leaves.LeaveCreditOtherLeave()

    leave_points = edit_link_leaves.LeaveCreditLeavePoints().text

    leave_points_vl = float(vacation_leave)
    leave_points_sl = float(sick_leave)
    leave_points_ol = float(other_leave)

    leave_points_ttl = float(leave_points.split(":")[-1].strip())
  

    total_value_pts = leave_points_vl + leave_points_sl + leave_points_ol
    rounded_total_value_pts = round(total_value_pts) 

    float_rounded_total_value = float(rounded_total_value_pts)
   
    if (float_rounded_total_value == leave_points_ttl):
        print(COLOR_GREEN + "Sum of leave pts: {} and total leaves pts: {} are equal are edits".format(float_rounded_total_value, leave_points_ttl) + COLOR_RESET)
   
    assert float_rounded_total_value == leave_points_ttl, "total leave points is not equal to the sum of vl, ol, and sl"
    time.sleep(2)












