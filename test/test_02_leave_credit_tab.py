import pytest
from pages.leave_credit_tab import LeaveCreditTab
from utils.config import COLOR_GREEN
from utils.config import COLOR_RESET

@pytest.mark.usefixtures("browser")
def test_leave_tab_presence(browser):
    leaveCreditTab = LeaveCreditTab(browser)
    assert leaveCreditTab.access_leave_credit(), "Leave Credit Tab is Not Present"
    if (leaveCreditTab.access_leave_credit()):
        print(COLOR_GREEN + "\nLeave Credit Tab is Present: Passed" + COLOR_RESET)

@pytest.mark.usefixtures("browser")
def test_text_presence(browser):
    leaveCreditTab = LeaveCreditTab(browser)
    assert leaveCreditTab.leave_credit_text_exs(), "Leave Credit Text is Not Present"
    if (leaveCreditTab.leave_credit_text_exs):
        print(COLOR_GREEN + "Leave Credit Text is Present: Passed" + COLOR_RESET)
    leaveCreditTab.go_to_leave_credit()
    
