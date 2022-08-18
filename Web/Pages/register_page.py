import allure
from Web.Pages.login_page import Login_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Utils.utils import Utils
from Web.Pages.user_profile_page import User_Profile_Page
from Web.Locators.locators_register import Register_Locators

class Register_Page(User_Profile_Page, Login_Page):
    def __init__(self, driver: WebDriver):

        User_Profile_Page.__init__(self, driver)
        Login_Page.__init__(self, driver)

        self.loginLink = Register_Locators.LOGIN_LINK
        self.registerButton = Register_Locators.REGISTER_BUTTON
        self.loginValidation = Register_Locators.VALIDATION_FOR_LOGIN
        self.passwordInput = Register_Locators.PASSWORD_INPUT
        self.confirmPassword = Register_Locators.CONFIRM_PASSWORD_INPUT
        self.passwordsNotMatchError = Register_Locators.PASSWORD_NOT_MATCHING
        self.userExistError = Register_Locators.USER_ALREADY_EXIST

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
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.loginValidation)))

    @allure.step
    @allure.description('insert value to "password" input')
    def enter_password(self, password):
        field = self.driver.find_element(By.XPATH, self.passwordInput)
        field.clear()
        field.send_keys(password)
        Utils(self.driver).assertion(password, field.get_attribute('value'))
        return field

    @allure.step
    @allure.description('insert value to "confirm password" input')
    def enter_confirm_password(self, password):
        field = self.driver.find_element(By.XPATH, self.confirmPassword)
        field.clear()
        field.send_keys(password)
        Utils(self.driver).assertion(password, field.get_attribute('value'))
        return field

    @allure.step
    @allure.description('clicking on register button')
    def click_on_register_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.registerButton).click()

    @allure.step
    @allure.description('Validation- error message when passwords not matching')
    def password_not_matching_error(self):
        return self.driver.find_element(By.XPATH, self.passwordsNotMatchError).get_attribute('textContent')

    @allure.step
    @allure.description('Validation- error message when user that already exist trying to register')
    def user_already_exist_error(self):
        return self.driver.find_element(By.XPATH, self.userExistError).get_attribute('textContent')
