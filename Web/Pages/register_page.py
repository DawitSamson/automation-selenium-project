import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Utils.utils import Utils
from Web.Pages.user_profile_page import User_Profile_Page

class Register_Page(User_Profile_Page):
    def __init__(self, driver: WebDriver):
        User_Profile_Page.__init__(self, driver)
    pass

    @allure.step
    @allure.description('Navigate to register page')
    def register_page(self):
        url = 'https://trip-yoetz.herokuapp.com/register'
        self.driver.get(url)
        Utils(self.driver).assertion(url, self.driver.current_url)
        self.driver.implicitly_wait(25)


