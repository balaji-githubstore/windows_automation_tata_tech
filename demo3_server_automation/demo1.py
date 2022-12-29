from appium.webdriver.appium_service import AppiumService

service = AppiumService()
service.start(args=["--port", "7878", "--address", "127.0.0.1", "--base-path", "/wd/hub", "--relaxed-security"])

print(service.is_running)
print(service.is_listening)

service.stop()

print(service.is_running)
print(service.is_listening)