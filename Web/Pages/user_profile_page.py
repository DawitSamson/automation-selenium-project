import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.locators_user_profile import User_Profile_Locators
from Web.Utils.utils import Utils

class User_Profile_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.editButton = User_Profile_Locators.EDIT_PROFILE_BUTTON
        self.validationForEditButton = User_Profile_Locators.VALIDATION_FOR_EDIT_BUTTON
        self.firstNameInput = User_Profile_Locators.NAME_INPUT
        self.lastNameInput = User_Profile_Locators.LAST_NAME_INPUT
        self.emailInput = User_Profile_Locators.EMAIL_INPUT
        self.birthDateInput = User_Profile_Locators.BIRTH_DATE_INPUT
        self.imageInput = User_Profile_Locators.IMAGE_INPUT
        self.logOutButton = User_Profile_Locators.LOG_OUT_BUTTON

    @allure.step
    @allure.description('Click on edit button Open the edit profile window')
    def click_on_edit_profile_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.editButton).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationForEditButton)))

    @allure.step
    @allure.description('Insert first name value to the first name input')
    def enter_first_name(self, first_name: str):
        first_name_input = self.driver.find_element(By.CSS_SELECTOR, self.firstNameInput)
        first_name_input.clear()
        first_name_input.send_keys(first_name)
        Utils(self.driver).assertion(first_name, first_name_input.get_attribute('value'))

    @allure.step
    @allure.description('Insert last name value to the last name input')
    def enter_last_name(self, last_name: str):
        last_name_input = self.driver.find_element(By.CSS_SELECTOR, self.lastNameInput)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        Utils(self.driver).assertion(last_name, last_name_input.get_attribute('value'))

    @allure.step
    @allure.description('Insert last name value to the last name input')
    def enter_email(self, email: str):
        email_input = self.driver.find_element(By.CSS_SELECTOR, self.emailInput)
        email_input.clear()
        email_input.send_keys(email)
        Utils(self.driver).assertion(email, email_input.get_attribute('value'))

    @allure.step
    @allure.description('Insert last name value to the last name input')
    def enter_image_name(self, image: str):
        image_input = self.driver.find_element(By.CSS_SELECTOR, self.imageInput)
        image_input.clear()
        image_input.send_keys(image)
        Utils(self.driver).assertion(image, image_input.get_attribute('value'))

    ''' Problam'''
    def enter_date(self, date):
        date_input = self.driver.find_element(By.CSS_SELECTOR, self.birthDateInput)
        date_input.clear()
        date_input.send_keys(date)
