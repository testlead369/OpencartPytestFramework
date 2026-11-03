from playwright.sync_api import expect

import utils.general_testdata_reader
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

def test_sidebar_validations(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()
    obj_home_page.login_link_click()
    obj_login_page = LoginPage(page)
    assert obj_login_page.collecting_sidebar_elements() ==utils.general_testdata_reader.test_data['Login_sidebar']['data']

def test_invalid_login_message(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()
    obj_home_page.login_link_click()
    obj_login_page = LoginPage(page)
    obj_login_page.unsuccessful_login(general_testdata_reader.test_data['credentials_invalid']['username'],general_testdata_reader.test_data['credentials_invalid']['password'])
    expect(obj_login_page.invalid_login_message()).to_have_text("Warning: No match for E-Mail Address and/or Password.")