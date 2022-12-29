import pytest
from appium.webdriver.appium_service import AppiumService

""" Appium server start and stops at session level """


@pytest.fixture(scope="class")
def setup_session(request):
    service = AppiumService()
    service.start(args=["--port", "7878", "--address", "127.0.0.1", "--base-path", "/wd/hub", "--relaxed-security"])
    request.cls.service = "hello"
    yield
    service.stop()
