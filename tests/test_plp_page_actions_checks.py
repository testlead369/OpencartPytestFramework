
from playwright.sync_api import expect

import utils
from pages.home_page import HomePage
from pages.plp_page import PLPPage
from utils import general_testdata_reader

def test_collect_dropdown_values(page):
    obj_home_page = HomePage(page)
    obj_home_page.desktop_mouse_hover_click()
    obj_plp_page=PLPPage(page)
    assert obj_plp_page.get_sortby_dropdown_values()==utils.general_testdata_reader.test_data['sort_by']['sort_options']

def test_listed_products_name(page):
    obj_home_page = HomePage(page)
    obj_home_page.desktop_mouse_hover_click()
    obj_plp_page = PLPPage(page)
    obj_plp_page.select_name_sort_option()
    mylist=obj_plp_page.get_listed_products()
    #mylist.sort(key=str.lower) #key=str.lower tells .sort() to use that lowercase version to decide the order.
    # since we have 'iphone' and 'ipod' in lower case, it converts all to lower,then sort but doesn't change in the list. That sorting is temporary
    assert mylist==utils.general_testdata_reader.test_data['listed products']['listed_products_sorted']

