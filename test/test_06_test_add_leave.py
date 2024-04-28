import pytest
from selenium import webdriver
from pages.filing_leave import FileLeave
from utils.config import COLOR_GREEN
from utils.config import COLOR_RESET
import time

#Add a 1 day leave (Whole Day)

pytest.mark.usefixtures("browser")
def test_data_click_file_leave_btn(browser):
    file_of_leave = FileLeave(browser)

    click_file_leave_button1 = file_of_leave.click_file_leave_btn()

    if click_file_leave_button1:
        print(COLOR_GREEN + "\nClicking 'File Leave' button worked" + COLOR_RESET)

    assert click_file_leave_button1, "File Leave button not existing or interactable"

@pytest.mark.usefixtures("browser")
def test_data_click_leave_drpdwn(browser):
    leave_dropdown = FileLeave(browser)

    click_leave_dropdown = leave_dropdown.click_file_leave_drpdwn()

    if click_leave_dropdown:
        print(COLOR_GREEN + "\nClicking 'Leave Type Dropdown' button worked" + COLOR_RESET)

    assert click_leave_dropdown, "Leave Type Dropdown not existing or interactable"

@pytest.mark.usefixtures("browser")
def test_data_leave_type_vl(browser):
    select_options = FileLeave(browser)
    click_vacation_leave = select_options.select_leave_option("Vacation Leave")
    
    if click_vacation_leave:
        print(COLOR_GREEN + "\nClicking 'Leave Type (Vacation)' option worked" + COLOR_RESET)

    assert click_vacation_leave, "Vacation Leave not available"


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
    date_end = "22/10/2024"
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

@pytest.mark.usefixtures("browser")
def test_data_submission(browser):
    submit_leave = FileLeave(browser)

    leave_submission = submit_leave.click_file_submit()

    time.sleep(5)

    if leave_submission:
        print(COLOR_GREEN + "\nsubmission button works" + COLOR_RESET)

    assert leave_submission, "End Date not existing or interactable"


@pytest.mark.usefixtures("browser")
def test_click_next(browser):
    next_button = FileLeave(browser)    

    while True:
        month_identifier = next_button.presence_of_oct_2024()
        if month_identifier == "October 2024":
            print(COLOR_GREEN + "\nOctober 2024 found" + COLOR_RESET)
            break
        next_button.click_next_calendar_modal()

    assert month_identifier == "October 2024", 'error finding the text "October 2024'

 
@pytest.mark.usefixtures("browser")
def test_extract_oct_22(browser):
    day_presence = FileLeave(browser)    

    day_identifier = day_presence.presence_of_oct_22_exact_date()
    
    if day_identifier == "Vacation Leave":
           print(COLOR_GREEN + "\nVcation Leavr on October 22 found" + COLOR_RESET)

        
    assert day_identifier == "Vacation Leave", 'error finding the text "Vacation Leave" on October 22'


#Add a 5 day leave (Half Day)


    




