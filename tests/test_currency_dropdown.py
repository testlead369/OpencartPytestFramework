from pages.home_page import HomePage


def test_currency_dropdown_check(page):
    obj_home_page = HomePage(page)
    obj_home_page.currency_dropdown_click()
    obj_home_page.currency_dropdown__options_click()
    page.wait_for_timeout(2000)
