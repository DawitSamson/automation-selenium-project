from selenium.webdriver.common.by import By

class Locators_Accessibility:
    MAIN_BUTTON = (By.CSS_SELECTOR, 'button[class="toggle-mode-btn"]')
    VALIDATION_MAIN_BUTTON = (By.CSS_SELECTOR, 'div[class="theme-palette active"]')
    COLORS_BUTTONS = (By.XPATH, '//header/div[2]/div[1]/button')
    VALIDATION_COLOR_BUTTON = (By.CSS_SELECTOR, 'div[class="theme-palette"]')
