import pytest
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        print('\n----------------------')
        print('Initialing Chrome Driver')
        self.driver = webdriver.Chrome(executable_path='C://Users//yossi//Desktop//Python-Project'
                                                       '/SELENIUM_PROJECT/automation-selenium-project'
                                                       '/Web/Drivers/chromedriver.exe')

        print('----------------------')
        print('Test is Started')
        print('------------------------')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Test is Finished")
            self.driver.close()
            self.driver.quit()
