import pytest
from pages.login_page import LoginPage
from utils.config import COLOR_RESET
from utils.config import COLOR_GREEN

@pytest.mark.usefixtures("browser", "base_url")
def test_valid_login(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_url(base_url)
    login_page.login("admin@qstrike.com", "secret")
    if (browser.current_url == "http://127.0.0.1:8000/administration" ):
        print(COLOR_GREEN + "You have accessed the admin side: Passed" + COLOR_RESET)
    assert browser.current_url == "http://127.0.0.1:8000/administration"





