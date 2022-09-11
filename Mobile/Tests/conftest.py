from appium import webdriver
import pytest

class Mobile_Fixtures:
    desire_caps = {"platformName": "Android",
                   "appium:platformVersion": "10.0",
                   "appium:deviceName": "Samsung Galaxy A71 API 29",
                   "appium:automationName": "UiAutomator1",
                   "appium:browserName": "Chrome"}
    url = "http://localhost:4723/wd/hub"

    @pytest.fixture(name='set_up_mobile', autouse=True)
    def set_up(self):
        print('\n----------------------------------')
        print('Initialing Device -> Samsung Galaxy A71')
        print('------------------------------------')
        self.driver = webdriver.Remote(command_executor=Mobile_Fixtures.url,
                                       desired_capabilities=Mobile_Fixtures.desire_caps)
        print('\n----------------------------------')
        print('Test is Started')
        print('------------------------------------')
        self.driver.implicitly_wait(30)
        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Test is Finished")
            print('------------------------------')
            self.driver.quit()