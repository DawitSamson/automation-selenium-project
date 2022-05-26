class Locators_Login_Page:
    # Name:
    EMAIL_FIELD = 'email'  # Email Field
    PASSWORD_FIELD = 'password'  # Password Field

    # XPath:
    LOGIN_BUTTON = '//form[1]/button[1]'  # Login Button

    LOGIN_VALIDATION_MESSAGE = '//div[1]/h1[1]'  # Successfully Login:
    ERROR_MESSAGE1 = "//h2[contains(text(),'password or email incorrect')]"  # When Email is Correct
    ERROR_MESSAGE2 = "//h2[contains(text(),'no user found')]"  # When Email is InCorrect

    UI = '//div[1]/div[1]'
