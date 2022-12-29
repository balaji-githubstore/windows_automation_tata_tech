import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# desired_caps = {
#     "platformName": "android",
#     "app": r"C:\Components\khan-academy-7-3-2.apk"
# }

desired_caps = {
    "platformName": "windows",
    "app": r"C:\Windows\system32\notepad.exe"
}

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
# wait=WebDriverWait(driver,30,poll_frequency=0.5,ignored_exceptions=[NoSuchElementException])
wait = WebDriverWait(driver, 20)

# print(driver.page_source)
wait.until(
    expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Edit[@Name='Text Editor']"))).send_keys(
    "hello !!!")

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//MenuItem[@Name='File']"))).click()
wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//MenuItem[contains(@Name,'Save As')]"))).click()

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Edit[@Name='File name:']"))).clear()
wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Edit[@Name='File name:']"))).send_keys(
    r"C:\mine\demo.txt")

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Save']"))).click()

time.sleep(5)
