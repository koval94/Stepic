from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_and_send_keys(browser, element, value, time_out=30):
    wait = WebDriverWait(browser, time_out)
    return wait.until(EC.element_to_be_clickable(element)).send_keys(value)


def wait_for_element_and_click(browser, element, time_out=30):
    wait = WebDriverWait(browser, time_out)
    return wait.until(EC.element_to_be_clickable(element)).click()


def wait_until_element_is_visible(browser, element, time_out=30):
    wait = WebDriverWait(browser, time_out)
    return wait.until(EC.visibility_of_element_located(element))


def wait_until_element_is_present(browser, element, time_out=30):
    wait = WebDriverWait(browser, time_out)
    return wait.until(EC.presence_of_element_located(element))
