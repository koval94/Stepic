import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from waiter import *

link = 'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/'


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    add_to_cart_button = (By.XPATH, ".//input[@id='id_quantity']/following-sibling::button")
    result = wait_until_element_is_present(browser=browser, element=add_to_cart_button)
    assert result.is_displayed
