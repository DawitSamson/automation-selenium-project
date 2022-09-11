from selenium.webdriver.common.by import By
class User_Profile_Locators:
    """ need to add favorites locators - user profile """

    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, 'button[class="edit-user-btn"]')
    VALIDATION_FOR_EDIT_BUTTON = (By.CSS_SELECTOR, 'div[class="user-update-wrapper"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    BIRTH_DATE_INPUT = (By.CSS_SELECTOR, 'input[name="birthDate"]')
    IMAGE_INPUT = (By.CSS_SELECTOR, 'input[name="image"]')
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, 'button[class="logout-btn"]')
    VALIDATION_FOR_LOG_BUTTON = (By.CSS_SELECTOR, 'section[class="sc-pVTFL jQTpoc"]')
    UPDATE_BUTTON = (By.XPATH, '//form/button')
    FULL_NAME = (By.XPATH, '//div[2]/h2[1]')
    AGE = (By.XPATH, '//div[2]/h2[2]')
