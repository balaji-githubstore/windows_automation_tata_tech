import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    "platformName": "windows",
    "app": r"root"
}

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
wait = WebDriverWait(driver, 20)


wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//*[contains(@Name,'Skip this')]"))).click()

wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//Edit[@Name='Name']"))).clear()

wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//Edit[@Name='Name']"))).send_keys("welcome123")

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Cancel']"))).click()



time.sleep(2)

driver.quit()
