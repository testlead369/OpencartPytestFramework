from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import general_testdata_reader

def test_login_page_confirmation(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()
    obj_home_page.login_link_click()
    obj_login_page = LoginPage(page)
    expect(obj_login_page.login_page_text_check()).to_have_text("Returning Customer")

def test_successful_login_check(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()
    obj_home_page.login_link_click()
    obj_login_page = LoginPage(page)
    obj_login_page.successful_login(general_testdata_reader.test_data['credentials_valid']['username'],general_testdata_reader.test_data['credentials_valid']['password'])
    page.wait_for_timeout(4000)  # Wait for 2 seconds to allow the page to load