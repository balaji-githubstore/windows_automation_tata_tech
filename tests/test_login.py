import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that


@pytest.mark.usefixtures("setup_session")
class TestLogin:
    @pytest.fixture(scope="function", autouse=True)
    def setup_app(self):
        desired_caps = {
            "platformName": "windows",
            "app": r"C:\Users\JiDi\AppData\Roaming\Zoom\bin\Zoom.exe"
        }
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:7878/wd/hub",
                                       desired_capabilities=desired_caps)
        self.wait = WebDriverWait(self.driver, 20)
        yield
        self.driver.quit()

    def test_invalid_login(self):
        print(self.service)
        print(self.service)
        self.wait.until(
            expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Sign In']"))).click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (AppiumBy.XPATH, "//Edit[contains(@Name,'your email')]"))).send_keys("demo@gmail.com")
        self.wait.until(expected_conditions.visibility_of_element_located(
            (AppiumBy.XPATH, "//Edit[contains(@Name,'your password')]"))).click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (AppiumBy.XPATH, "//Edit[contains(@Name,'your password')]"))).send_keys("welcome123")
        self.wait.until(
            expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Sign In']"))).click()
        actual_error = self.wait.until(expected_conditions.visibility_of_element_located(
            (AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]"))).text

        assert_that(actual_error).contains("Incorrect")

    def test_Sign_In_Check(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//Button[@Name='Sign In']"))).click()
