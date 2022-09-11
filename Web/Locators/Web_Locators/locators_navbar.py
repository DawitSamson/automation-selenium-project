from selenium.webdriver.common.by import By
class NavBar_Locators:
    NAV_BAR_LINKS = (By.XPATH, '//header[1]/div/a')
    SEARCH_FIELD = (By.CLASS_NAME, 'header-search-input')
    CITY_NAME = (By.XPATH, '//section[1]/h1[1]')
    CITY_ERROR_MESSAGE = (By.XPATH, "//h2[contains(text(),'no city found')]")
