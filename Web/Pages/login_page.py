import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.locators_login_page import Locators_Login_Page
from selenium.webdriver.common.by import By
from Web.Utils.utils import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.emailBox = Locators_Login_Page.EMAIL_FIELD
        self.passwordBox = Locators_Login_Page.PASSWORD_FIELD
        self.loginButton = Locators_Login_Page.LOGIN_BUTTON
        self.profileLink = Locators_Login_Page.PROFILE_BUTTON
        self.loginValidationMessage = Locators_Login_Page.LOGIN_VALIDATION_MESSAGE
        self.email_Password_error = Locators_Login_Page.ERROR_MESSAGE1
        self.userError = Locators_Login_Page.ERROR_MESSAGE2
        self.showPasswordButton = Locators_Login_Page.SHOW_PASSWORD_BUTTON
        self.UI = Locators_Login_Page.UI

    @allure.step
    @allure.description('Navigate to login page')
    def login_page(self):
        url = 'https://trip-yoetz.herokuapp.com/login'
        self.driver.get(url)
        Utils(self.driver).assertion(url, self.driver.current_url)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Navigate to user profile after successfully login')
    def click_profile_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.profileLink).click()
        self.wait.until(EC.url_to_be('https://trip-yoetz.herokuapp.com/profile'))
        Utils(self.driver).assertion('https://trip-yoetz.herokuapp.com/profile', self.driver.current_url)

    @allure.step
    @allure.description('Show password button - should display text in password input')
    def click_show_password_button(self):
        value = self.driver.find_element(By.NAME, self.passwordBox).get_attribute('type')
        Utils(self.driver).assertion('password', value)
        self.driver.find_element(By.CSS_SELECTOR, self.showPasswordButton).click()
        Utils(self.driver).assertion('text', value)

    @allure.step
    @allure.description('Clear and insert data to email input')
    def enter_email(self, email):
        email_input = self.driver.find_element(By.NAME, self.emailBox)
        email_input.clear()
        email_input.send_keys(email)
        Utils(self.driver).assertion(email, email_input.get_attribute('value'))

    @allure.step
    @allure.description('Clear and insert data to password input')
    def enter_password(self, password):
        password_input = self.driver.find_element(By.NAME, self.passwordBox)
        password_input.clear()
        password_input.send_keys(password)
        Utils(self.driver).assertion(password, password_input.get_attribute('value'))

    @allure.step
    @allure.description('Login button - should return 2 error messages or alert')
    def login_button(self):
        self.driver.find_element(By.XPATH, self.loginButton).click()

    @allure.step
    @allure.description('Alert after login successfully')
    def accept_alert(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()
        # self.driver.forward()

    @allure.step
    @allure.description('Validation - all email and password format messages')
    def email_and_password_combinations(self, emails: list, passwords: list):
        for email in range(len(emails)):
            for password in range(len(passwords)):
                self.enter_email(emails[email])
                self.enter_password(passwords[password])
                self.login_button()
                if 'include' in self.js_email():
                    Utils(self.driver).assertion(f"Please include an '@' in the email address."
                                                 f" '{emails[email]}' is missing an '@'.", self.js_email(),
                                                 "Please enter an email address.")
                elif 'enter' in self.js_email():
                    Utils(self.driver).assertion(f"Please enter a part following '@'. "
                                                 f"'{emails[email]}' is incomplete.", self.js_email(),
                                                 "Please enter an email address.")
                elif 'used at' in self.js_email():
                    msg = Utils(self.driver).slicing(emails[email], '@')
                    Utils(self.driver).assertion(f"'.' is used at a wrong position in '{msg}'.", self.js_email(),
                                                 "Please enter an email address.")
                if len(passwords[password]) == 1:
                    Utils(self.driver).assertion("Please lengthen this text to 4 characters or more "
                                                 "(you are currently using 1 character).", self.js_password(),
                                                 "Please use at least 4 characters "
                                                 "(you are currently using 1 characters).")
                elif len(passwords[password]) in range(2, 4):
                    Utils(self.driver).assertion(f"Please lengthen this text to 4 characters or more"
                                                 f" (you are currently using {len(passwords[password])}"
                                                 f" characters).", self.js_password(),
                                                 "Please use at least 4 characters "
                                                 f"(you are currently using {len(passwords[password])} characters).")

    @allure.step
    @allure.description('Validation - the message from user profile page after successfully login')
    def login_validation_message(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.loginValidationMessage)))
        return self.driver.find_element(By.XPATH, self.loginValidationMessage).get_attribute('innerText')

    @allure.step
    @allure.description('Validation - error messages where email not in the email format')
    def js_email(self):
        return self.driver.find_element(By.NAME, self.emailBox).get_attribute('validationMessage')

    @allure.step
    @allure.description('Validation - error messages where password not in the password format')
    def js_password(self):
        return self.driver.find_element(By.NAME, self.passwordBox).get_attribute('validationMessage')

    @allure.step
    @allure.description('Validation - error message where password is invalid')
    def email_or_password_error(self):
        return self.driver.find_element(By.XPATH, self.email_Password_error).get_attribute('innerText')

    @allure.step
    @allure.description('Validation - error message where email is invalid')
    def no_user_error_message(self):
        return self.driver.find_element(By.XPATH, self.userError).get_attribute('innerText')

    @allure.step
    @allure.description('Validation - returns all the text in page')
    def ui(self):
        return self.driver.find_element(By.XPATH, self.UI).get_attribute('innerText')
