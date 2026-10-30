from playwright.sync_api import expect
from utils import general_testdata_reader
from pages.home_page import HomePage

def test_logo_check(page):
    obj_home_page =HomePage(page)
    expect(obj_home_page.check_logo()).to_be_visible()

def test_page_title(page):
    obj_home_page =HomePage(page)
    expect(obj_home_page.page).to_have_title("Your Store")

def test_phone_number_display(page):
    obj_home_page = HomePage(page)
    phone_number = obj_home_page.Phone_number_display()
    expect (phone_number).to_have_text(general_testdata_reader.test_data['phone_number']['phone_number_display'])

def test_currency_dropdown_check(page):
    obj_home_page = HomePage(page)
    obj_home_page.currency_dropdown__options_click()


def test_my_account_click(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()

def test_login_link_click(page):
    obj_home_page = HomePage(page)
    obj_home_page.my_account_click()
    obj_home_page.login_link_click()
    page.wait_for_timeout(2000)  # Wait for 2 seconds to allow the page to load



