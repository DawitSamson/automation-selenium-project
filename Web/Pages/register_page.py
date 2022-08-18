import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Utils.utils import Utils
from Web.Pages.user_profile_page import User_Profile_Page
from Web.Locators.locators_register import Register_Locators

class Register_Page(User_Profile_Page):
    def __init__(self, driver: WebDriver):
        User_Profile_Page.__init__(self, driver)
        self.loginLink = Register_Locators.LOGIN_LINK
        self.registerButton = Register_Locators.REGISTER_BUTTON
        self.loginValidation = Register_Locators.VALIDATION_FOR_LOGIN

    @allure.step
    @allure.description('Navigate to register page')
    def register_page(self):
        url = 'https://trip-yoetz.herokuapp.com/register'
        self.driver.get(url)
        Utils(self.driver).assertion(url, self.driver.current_url)
        self.driver.implicitly_wait(25)

    @allure.step
    @allure.description('clicking on login button - should navigate to login page')
    def click_on_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.loginLink).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.loginValidation)))