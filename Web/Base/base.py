import pytest
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n----------------------')
            print('Initialing Chrome Driver')
            self.driver = webdriver.Chrome('..//Drivers/chromedriver.exe')
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

        elif browser == 'edge':
            print('\n----------------------')
            print('Initialing Edge Driver')
            self.driver = webdriver.Edge('..//Drivers/msedgedriver.exe')

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
            print('Initialing FireFox Driver')
            self.driver = webdriver.Firefox(executable_path='..//Drivers/geckodriver.exe')

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
