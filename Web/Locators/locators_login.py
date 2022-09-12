class Locators_Login_Page:
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    SHOW_PASSWORD_BUTTON = 'button[class="visible-password-btn"]'
    LOGIN_BUTTON = '//form[1]/button[1]'
    PROFILE_BUTTON = 'a[class="sc-gsDKAQ cOqGzW"]'
    LOGIN_VALIDATION_MESSAGE = "//h1[contains(text(),'YOUR INFORMATION')]"
    ERROR_MESSAGE1 = "//h2[contains(text(),'password or email incorrect')]"
    ERROR_MESSAGE2 = "//h2[contains(text(),'no user found')]"
    UI = '//div[1]/div[1]'
