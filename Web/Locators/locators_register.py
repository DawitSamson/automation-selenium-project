from selenium.webdriver.common.by import By
class Register_Locators:
    LOGIN_LINK = (By.CSS_SELECTOR, 'button[class="navigate-btn"]')
    VALIDATION_FOR_LOGIN = (By.CSS_SELECTOR, 'section[class="sc-bqiRlB bvtOUu"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[class="register-btn"]')
    PASSWORD_INPUT = (By.XPATH, '//div[6]/input[1]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//div[7]/input[1]')
    PASSWORD_NOT_MATCHING = (By.XPATH, "//h2[contains(text(),'passwords not matching')]")
    USER_ALREADY_EXIST = (By.XPATH, "//h2[contains(text(),'user with that email already exists')]")