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
from demo1_basics import demo5_notepad

desired_caps = {
    "platformName": "windows",
    "app": r"C:\Windows\system32\notepad.exe"
}

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
# wait=WebDriverWait(driver,30,poll_frequency=0.5,ignored_exceptions=[NoSuchElementException])
wait = WebDriverWait(driver, 20)

# print(driver.page_source)
elements = wait.until(
    expected_conditions.presence_of_all_elements_located((AppiumBy.XPATH, "//MenuItem")))

for ele in elements:
    print(ele.text)
    print(ele.get_attribute("Name"))
    print(15 * "-")

demo5_notepad.click_menu_item(driver, "Help")
demo5_notepad.click_menu_item(driver, "Format")
time.sleep(5)

driver.quit()
