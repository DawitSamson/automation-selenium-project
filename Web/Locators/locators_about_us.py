from selenium.webdriver.common.by import By
class Locators_AboutUs:
    MAP_IFRAME = (By.CSS_SELECTOR, 'iframe[class="location-map"]')
    GOOGLE_MAPS_LINK = (By.CSS_SELECTOR, 'a[class="google-maps-link"]')
    UI = (By.XPATH, '//body[1]/div[1]/div[1]')
