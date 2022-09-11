from selenium.webdriver.common.by import By

class Locators_Login_Page:

    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'button[class="visible-password-btn"]')
    LOGIN_BUTTON = (By.XPATH, '//form[1]/button[1]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'a[class="sc-gsDKAQ cOqGzW"]')
    LOGIN_VALIDATION_MESSAGE = (By.XPATH, "//h1[contains(text(),'YOUR INFORMATION')]")
    ERROR_MESSAGE1 = (By.XPATH, "//h2[contains(text(),'password or email incorrect')]")
    ERROR_MESSAGE2 = (By.XPATH, "//h2[contains(text(),'no user found')]")
    UI = (By.XPATH, '//div[1]/div[1]')
