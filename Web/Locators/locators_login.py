class Locators_Login_Page:

    EMAIL_FIELD = 'email'  # Email Field
    PASSWORD_FIELD = 'password'  # Password Field
    SHOW_PASSWORD_BUTTON = 'button[class="visible-password-btn"]'
    LOGIN_BUTTON = '//form[1]/button[1]'  # Login Button
    PROFILE_BUTTON = 'a[class="sc-gsDKAQ cOqGzW"]'
    LOGIN_VALIDATION_MESSAGE = "//h1[contains(text(),'YOUR INFORMATION')]"  # Successfully Login:
    ERROR_MESSAGE1 = "//h2[contains(text(),'password or email incorrect')]"  # When Email is Correct
    ERROR_MESSAGE2 = "//h2[contains(text(),'no user found')]"  # When Email is InCorrect
    UI = '//div[1]/div[1]'
