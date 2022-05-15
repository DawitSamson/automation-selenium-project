class Locators_Login_Page:
    # Name:
    EMAIL_FIELD = 'email'  # Email Field
    PASSWORD_FIELD = 'password'  # Password Field

    # XPath:
    LOGIN_BUTTON = '//form[1]/button[1]'  # Login Button

    LOGIN_VALIDATION_MESSAGE = '//div[1]/h1[1]'  # Successfully Login:
    ERROR_MESSAGE1 = "//h2[contains(text(),'password or email incorrect')]"  # When Email is Correct
    ERROR_MESSAGE2 = "//h2[contains(text(),'no user found')]"  # When Email is InCorrect

    NAV_BAR_LINKS = '//header[1]/div/a'  # all The 4 Links in The NavBar

    SEARCH_FIELD = 'header-search-input'  # Search Field
    CITY_NAME = '//section[1]/h1[1]'  # Searching Correctly
    CITY_ERROR_MESSAGE = "//h2[contains(text(),'no city found')]"  # Searching Incorrectly

    WHO_ARE_WE_BUTTON = '//footer[1]/button[1]'  # The Button That Open The Who Are We Section
