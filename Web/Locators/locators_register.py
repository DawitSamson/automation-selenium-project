class Register_Locators:
    LOGIN_LINK = 'button[class="navigate-btn"]'
    VALIDATION_FOR_LOGIN = 'section[class="sc-bqiRlB bvtOUu"]'
    REGISTER_BUTTON = 'button[class="register-btn"]'
    PASSWORD_INPUT = '//div[6]/input[1]'
    CONFIRM_PASSWORD_INPUT = '//div[7]/input[1]'
    PASSWORD_NOT_MATCHING = "//h2[contains(text(),'passwords not matching')]"
    USER_ALREADY_EXIST = "//h2[contains(text(),'user with that email already exists')]"