import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def go_to_root_window():
    desired_caps = {
        "platformName": "windows",
        "app": r"root"
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    return driver


def click_menu_item(driver, text):
    wait = WebDriverWait(driver, 20)
    elements = wait.until(
        expected_conditions.presence_of_all_elements_located((AppiumBy.XPATH, "//MenuItem")))
    for ele in elements:
        if ele.text == text:
            ele.click()
            break
