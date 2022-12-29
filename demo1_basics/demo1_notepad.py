import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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

driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

driver.implicitly_wait(30)
# print(driver.page_source)
driver.find_element(AppiumBy.XPATH,"//Edit[@Name='Text Editor']").send_keys("hello !!!")

driver.find_element(AppiumBy.XPATH,"//MenuItem[@Name='File']").click()
driver.find_element(AppiumBy.XPATH,"//MenuItem[contains(@Name,'Save As')]").click()

driver.find_element(AppiumBy.XPATH,"//Edit[@Name='File name:']").clear()
driver.find_element(AppiumBy.XPATH,"//Edit[@Name='File name:']").send_keys(r"C:\mine\demo.txt")

driver.find_element(AppiumBy.XPATH,"//Button[@Name='Save']").click()
time.sleep(5)