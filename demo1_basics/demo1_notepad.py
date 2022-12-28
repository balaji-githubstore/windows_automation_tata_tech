import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    "platformName": "windows",
    "app": r"C:\Windows\system32\notepad.exe"
}


driver=webdriver.Remote(command_executor="http://127.0.0.1:5050/wd/hub",desired_capabilities=desired_caps)

driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPath,"//MenuItem[@Name='File']").click()

driver.find_element(AppiumBy.XPATH,"//*[@Name='Text Editor']").send_keys("hello everyone!!")

time.sleep(5000)