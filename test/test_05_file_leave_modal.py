import pytest
from selenium import webdriver
from pages.filing_leave import FileLeave
from utils.config import COLOR_GREEN
from utils.config import COLOR_RESET
import time


#UI Test

@pytest.mark.usefixtures("browser")
def test_data_edit_link(browser):
    file_of_leave = FileLeave(browser)

    click_file_leave = file_of_leave.click_file_leave()

    if click_file_leave:
        print(COLOR_GREEN + "\nClicking 'File Leave' worked" + COLOR_RESET)

    assert click_file_leave, "File Leave navigation not existing or interactable"

@pytest.mark.usefixtures("browser")
def test_data_click_file_leave(browser):
    file_of_leave = FileLeave(browser)

    click_file_leave_button = file_of_leave.click_file_leave_btn()

    if click_file_leave_button:
        print(COLOR_GREEN + "\nClicking 'File Leave' button worked" + COLOR_RESET)

    assert click_file_leave_button, "File Leave button not existing or interactable"

@pytest.mark.usefixtures("browser")
def test_data_click_leave_drpdwn(browser):
    leave_dropdown = FileLeave(browser)

    click_leave_dropdown = leave_dropdown.click_file_leave_drpdwn()

    if click_leave_dropdown:
        print(COLOR_GREEN + "\nClicking 'Leave Type Dropdown' button worked" + COLOR_RESET)

    assert click_leave_dropdown, "Leave Type Dropdown not existing or interactable"


@pytest.mark.usefixtures("browser")
def test_data_leave_type_options(browser):
    select_options = FileLeave(browser)
    click_vacation_leave = select_options.select_leave_option("Vacation Leave")
    click_sick_leave = select_options.select_leave_option("Sick Leave")
    click_other_leave = select_options.select_leave_option("Other Leave")
    
    if click_vacation_leave and click_sick_leave and click_other_leave:
        print(COLOR_GREEN + "\nClicking 'Leave Type (Vacation)' option worked" + COLOR_RESET)

    assert click_vacation_leave and click_sick_leave and click_other_leave , "Vacation Leave, Sick Leave or Other Leave might not be interactable or present"


@pytest.mark.usefixtures("browser")
def test_data_click_leave_switch(browser):
    click_toggle_switch = FileLeave(browser)

    click_switch = click_toggle_switch.click_toggle_switch()

    if click_switch:
        print(COLOR_GREEN + "\nClicking 'Toggle Switch Worked' button worked" + COLOR_RESET)

    assert click_switch, "Toggle Switch not existing or interactable"


@pytest.mark.usefixtures("browser")
def test_data_update_toggle_label(browser):
    toggle_label = FileLeave(browser)

    toggle_lbl = toggle_label.toggle_label()

    if toggle_lbl == "Half Day":
        print(COLOR_GREEN + "\nClicking 'Toggle Switch Worked' button worked" + COLOR_RESET)

    assert toggle_lbl, "Toggle Label not existing or interactable"

@pytest.mark.usefixtures("browser")
def test_data_start_date(browser):
    start_date = FileLeave(browser)
    date_start = "22/10/2024"
    input_start_date = start_date.input_start(date_start)

    if input_start_date:
        print(COLOR_GREEN + "\nDone inputting a start date value" + COLOR_RESET)

    assert input_start_date, "Start Date not existing or interactable"
    

@pytest.mark.usefixtures("browser")
def test_data_end_date(browser):
    end_date = FileLeave(browser)
    date_end = "23/10/2024"
    input_end_date = end_date.input_end(date_end)

    if input_end_date:
        print(COLOR_GREEN + "\nDone inputting an end date value" + COLOR_RESET)

    assert input_end_date, "End Date not existing or interactable"


@pytest.mark.usefixtures("browser")
def test_data_reason(browser):
    leave_reason = FileLeave(browser)


    reason_text = "I have nothing to say"
    input_reason = leave_reason.input_reason(reason_text)

    if input_reason:
        print(COLOR_GREEN + "\nDone inputting an end date value" + COLOR_RESET)

    assert input_reason, "End Date not existing or interactable"
    leave_reason.close_modal()
    time.sleep(3)

'''
@pytest.mark.usefixtures("browser")
def test_data_file_attach(browser):
    attach_file = FileLeave(browser)

    file_path = "C:\\Users\\leand\\Downloads\\PUPGS-CD-Labels.pdf"

    input_file = attach_file.input_file_attach(file_path)

    if input_file:
        print(COLOR_GREEN + "\nDone inputting the file" + COLOR_RESET)

    assert input_file, "File Attachment not existing or interactable"
'''

  
 
    
   
  








    #FILING LEAVE TEST

