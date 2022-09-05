from selenium.webdriver.common.by import By

class City_Locators:
    CITY_NAV_BAR = (By.XPATH, '//ul/li[1]/a')
    HOTELS_NAV_BAR = (By.XPATH, '//ul/li[2]/a')
    RESTAURANTS_NAV_BAR = (By.XPATH, '//ul/li[3]/a')
    ACTIVITIES_NAV_BAR = (By.XPATH, '//ul/li[4]/a')

    RESTAURANTS_MAIN_DIV = (By.XPATH, '//section[1]/div[1]')
    HOTELS_MAIN_DIV = (By.XPATH, '//section[1]/div[2]')
    ACTIVITIES_MAIN_DIV = (By.XPATH, '//section[1]/div[3]')

    """ Validations: """
    CITY_NAME_H1 = (By.CSS_SELECTOR, 'h1[class="city-name-h1"]')
    CATEGORY_NAME = (By.CSS_SELECTOR, 'h1[class="category-name-h1"]')