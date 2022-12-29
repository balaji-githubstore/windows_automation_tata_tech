from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = AppiumService()
# start the server
service.start(args=["--port", "7878", "--address", "127.0.0.1", "--base-path", "/wd/hub", "--relaxed-security"])

print(service.is_running)
print(service.is_listening)

desired_caps = {
    "platformName": "windows",
    "app": r"C:\Users\JiDi\AppData\Roaming\Zoom\bin\Zoom.exe"
}

driver = webdriver.Remote(command_executor="http://127.0.0.1:7878/wd/hub", desired_capabilities=desired_caps)
wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Sign In']"))).click()

wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//Edit[contains(@Name,'your email')]"))).send_keys("demo@gmail.com")

wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//Edit[contains(@Name,'your password')]"))).click()

wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//Edit[contains(@Name,'your password')]"))).send_keys("welcome123")

wait.until(expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Sign In']"))).click()

actual_error = wait.until(expected_conditions.visibility_of_element_located(
    (AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]"))).text

print(actual_error)

driver.quit()

# stop the server
service.stop()
