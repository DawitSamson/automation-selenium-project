import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.locators_login_page import Locators_Login_Page
from selenium.webdriver.common.by import By
from Web.Utils.utils import Utils
from selenium.webdriver.support.wait import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC

class Login_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.emailBox = Locators_Login_Page.EMAIL_FIELD
        self.passwordBox = Locators_Login_Page.PASSWORD_FIELD
        self.loginButton = Locators_Login_Page.LOGIN_BUTTON
        self.loginValidationMessage = Locators_Login_Page.LOGIN_VALIDATION_MESSAGE
        self.email_Password_error = Locators_Login_Page.ERROR_MESSAGE1
        self.userError = Locators_Login_Page.ERROR_MESSAGE2
        self.UI = Locators_Login_Page.UI

    # Pre Condition:
    @allure.step
    def login_page(self):
        url = 'https://trip-yoetz.herokuapp.com/login'
        self.driver.get(url)
        Utils(self.driver).assertion(self.driver.current_url, url)

    # Actions:
    @allure.step
    def enter_email(self, email):
        email_input = self.driver.find_element(By.NAME, self.emailBox)
        email_input.clear()
        email_input.send_keys(email)
        Utils(self.driver).assertion(email_input.get_attribute('value'), email)

    @allure.step
    def enter_password(self, password):
        password_input = self.driver.find_element(By.NAME, self.passwordBox)
        password_input.clear()
        password_input.send_keys(password)
        Utils(self.driver).assertion(password_input.get_attribute('value'), password)

    @allure.step
    def login_button(self):
        self.driver.find_element(By.XPATH, self.loginButton).click()

    @allure.step
    def accept_alert(self):
        WAIT(self.driver, 20).until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()

    # Messages:
    @allure.step
    def login_validation_message(self):
        WAIT(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, self.loginValidationMessage)))
        return self.driver.find_element(By.XPATH, self.loginValidationMessage).get_attribute('innerText')

    @allure.step
    def js_email(self):
        return self.driver.find_element(By.NAME, self.emailBox).get_attribute('validationMessage')

    @allure.step
    def js_password(self):
        return self.driver.find_element(By.NAME, self.passwordBox).get_attribute('validationMessage')

    @allure.step
    def email_or_password_error(self):
        return self.driver.find_element(By.XPATH, self.email_Password_error).get_attribute('innerText')

    @allure.step
    def no_user_error_message(self):
        return self.driver.find_element(By.XPATH, self.userError).get_attribute('innerText')

    @allure.step
    def ui(self):
        return self.driver.find_element(By.XPATH, self.UI).get_attribute('innerText')
