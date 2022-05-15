import pytest
from selenium import webdriver

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print('\n----------------------')
        print('Initialing Chrome Driver')
        self.driver = webdriver.Chrome(executable_path='C://Users//yossi//PycharmProjects//'
                                                       'python_Lessons//OOP//Drivers//chromedriver.exe')
        print('\n----------------------')
        print('Test is Started')
        print('------------------------')
        self.driver.implicitly_wait(15)
        self.driver.get('https://trip-yoetz.herokuapp.com/login')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
