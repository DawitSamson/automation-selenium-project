import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.locators_user_profile import User_Profile_Locators

class User_Profile_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.editButton = User_Profile_Locators.EDIT_PROFILE_BUTTON
        self.userUpdateDiv = User_Profile_Locators.VALIDATION_FOR_EDIT_BUTTON
        self.nameInput = User_Profile_Locators.NAME_INPUT
        self.lastNameInput = User_Profile_Locators.LAST_NAME_INPUT
        self.emailInput = User_Profile_Locators.EMAIL_INPUT
        self.birthDateInput = User_Profile_Locators.BIRTH_DATE_INPUT
        self.imageInput = User_Profile_Locators.IMAGE_INPUT
        self.logOutButton = User_Profile_Locators.LOG_OUT_BUTTON

    @allure.step
    @allure.description('Click on edit button Open the edit profile window')
    def click_on_edit_profile_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.editButton).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.userUpdateDiv)))


