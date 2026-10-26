from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_page_title(page):
    obj_home_page =HomePage(page)
    expect(obj_home_page.page).to_have_title("Your Store")


def test_logo_check(page):
    obj_home_page =HomePage(page)
    expect(obj_home_page.check_logo()).to_be_visible()






