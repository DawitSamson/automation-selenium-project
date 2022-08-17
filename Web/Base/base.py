import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os

class Base:

    @staticmethod
    def gh_token():
        path = 'C://Users//yossi//PycharmProjects//python_Lessons/gh_token.txt'
        token = open(path).read()
        return token

    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n----------------------')
            print('Initialing Chrome Driver')
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            print('----------------------')
            print('\n----------------------')
            print('Test is Started')
            print('------------------------')
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()
            yield self.driver
            if self.driver is not None:
                print("\n----------------------------")
                print("Test is Finished")
                print('------------------------------')
                self.driver.close()
                self.driver.quit()

        elif browser == 'firefox':
            print('\n----------------------')
            os.environ['GH_TOKEN'] = self.gh_token()
            print('Initialing FireFox Driver')
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            print('----------------------')
            print('\n----------------------')
            print('Test is Started')
            print('------------------------')
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()

            yield self.driver
            if self.driver is not None:
                print("\n----------------------------")
                print("Test is Finished")
                print('------------------------------')
                self.driver.close()
                self.driver.quit()

        else:
            raise ValueError('Please insert valid Driver.')
