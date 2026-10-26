
from playwright.sync_api import Page
from utils import general_testdata_reader


import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True
    }

@pytest.fixture()
def page(page:Page):
    page.goto(general_testdata_reader.test_data["application"]["application URL"])
    yield page