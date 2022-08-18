import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.locators_user_profile import User_Profile_Locators
from Web.Utils.utils import Utils

class User_Profile_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.editButton = User_Profile_Locators.EDIT_PROFILE_BUTTON
        self.validationForEditButton = User_Profile_Locators.VALIDATION_FOR_EDIT_BUTTON
        self.firstNameInput = User_Profile_Locators.NAME_INPUT
        self.lastNameInput = User_Profile_Locators.LAST_NAME_INPUT
        self.emailInput = User_Profile_Locators.EMAIL_INPUT
        self.birthDateInput = User_Profile_Locators.BIRTH_DATE_INPUT
        self.imageInput = User_Profile_Locators.IMAGE_INPUT
        self.updateButton = User_Profile_Locators.UPDATE_BUTTON
        self.logOutButton = User_Profile_Locators.LOG_OUT_BUTTON
        self.validationForLogOutButton = User_Profile_Locators.VALIDATION_FOR_LOG_BUTTON
        self.fullName = User_Profile_Locators.FULL_NAME
        self.age = User_Profile_Locators.AGE

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
        return first_name_input

    @allure.step
    @allure.description('Insert last name value to the last name input')
    def enter_last_name(self, last_name: str):
        last_name_input = self.driver.find_element(By.CSS_SELECTOR, self.lastNameInput)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        Utils(self.driver).assertion(last_name, last_name_input.get_attribute('value'))
        return last_name_input

    @allure.step
    @allure.description('Insert email value to the email input')
    def enter_email(self, email: str):
        email_input = self.driver.find_element(By.CSS_SELECTOR, self.emailInput)
        email_input.clear()
        email_input.send_keys(email)
        Utils(self.driver).assertion(email, email_input.get_attribute('value'))
        return email_input

    @allure.step
    @allure.description('Insert image value to the image input')
    def enter_image_name(self, image: str):
        image_input = self.driver.find_element(By.CSS_SELECTOR, self.imageInput)
        image_input.clear()
        image_input.send_keys(image)
        Utils(self.driver).assertion(image, image_input.get_attribute('value'))
        return image_input

    @allure.step
    @allure.description('Insert birth date value to the birth date input, using in execute_script')
    def enter_date(self, date: str):
        birth_date_input = self.driver.find_element(By.CSS_SELECTOR, self.birthDateInput)
        self.driver.execute_script(f"document.getElementsByName('birthDate')[0].value = '{date}'")
        Utils(self.driver).assertion(date, birth_date_input.get_attribute('value'))
        return birth_date_input

    @allure.step
    @allure.description('Click on log out button and exit from account')
    def click_on_log_out_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.logOutButton).click()
        alert = self.driver.switch_to.alert
        for i in range(2):
            alert.accept()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.validationForLogOutButton)))

    @allure.step
    @allure.description('Click on update button after sending values to the inputs')
    def click_on_update_button(self):
        self.driver.find_element(By.XPATH, self.updateButton).click()

    @allure.step
    @allure.description('Update profile - insert values and click update button')
    def update_profile(self, first_name, last_name, email, date, image):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_date(date)
        self.enter_image_name(image)
        self.click_on_update_button()

    @allure.step
    @allure.description('Validation- full name value')
    def full_name_value(self):
        return self.driver.find_element(By.XPATH, self.fullName).get_attribute('innerText')

    @allure.step
    @allure.description('Validation- age value')
    def age_value(self):
        return self.driver.find_element(By.XPATH, self.age).get_attribute('innerText')

    @allure.step
    @allure.description('Validation- take th input and choose attribute(innerText, validationMessage)')
    def error_message(self, field: WebElement, attribute):
        return field.get_attribute(attribute)




