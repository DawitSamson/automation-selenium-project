import allure
from OOP.Locators.locators_login_page import Locators_Login_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Page:

    def __init__(self, driver):
        self.driver = driver
        self.loginValidationMessage = Locators_Login_Page.LOGIN_VALIDATION_MESSAGE
        self.emailBox = Locators_Login_Page.EMAIL_FIELD
        self.passwordBox = Locators_Login_Page.PASSWORD_FIELD
        self.loginButton = Locators_Login_Page.LOGIN_BUTTON

        self.email_Password_error = Locators_Login_Page.ERROR_MESSAGE1
        self.userError = Locators_Login_Page.ERROR_MESSAGE2

        self.navBarLinks = Locators_Login_Page.NAV_BAR_LINKS

        self.searchField = Locators_Login_Page.SEARCH_FIELD
        self.cityName = Locators_Login_Page.CITY_NAME
        self.cityErrorMessage = Locators_Login_Page.CITY_ERROR_MESSAGE

        self.whoAreWeButton = Locators_Login_Page.WHO_ARE_WE_BUTTON

    # Actions:
    @allure.step
    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.emailBox).clear()
        self.driver.find_element(By.NAME, self.emailBox).send_keys(email)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.passwordBox).clear()
        self.driver.find_element(By.NAME, self.passwordBox).send_keys(password)

    @allure.step
    def login_button(self):
        self.driver.find_element(By.XPATH, self.loginButton).click()

    @allure.step
    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present(), 'TimeOut')
        alert = self.driver.switch_to.alert
        alert.dismiss()

    @allure.step
    def nav_bar_links(self):
        return self.driver.find_elements(By.XPATH, self.navBarLinks)

    @allure.step
    def searching(self, city):
        field = self.driver.find_element(By.CLASS_NAME, self.searchField)
        field.send_keys(city)
        field.send_keys(Keys.ENTER)

    # Messages:
    @allure.step
    def login_validation_message(self):
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
    def city_name(self):
        return self.driver.find_element(By.XPATH, self.cityName).get_attribute('innerText')

    @allure.step
    def error_city_name(self):
        return self.driver.find_element(By.XPATH, self.cityErrorMessage).get_attribute('innerText')

