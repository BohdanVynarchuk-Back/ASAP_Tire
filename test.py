import time

from base_data.base_page import Page
from pages.home_page import HomePage


def test_first(browser):
    a = HomePage(browser)
    a.click_on_zip_code()
    time.sleep(5)
    return a