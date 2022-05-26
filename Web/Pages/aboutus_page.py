import allure
from Web.Locators.locators_aboutus_page import Locators_AboutUs
from selenium.webdriver.common.by import By

class AboutUs_Page:
    def __init__(self, driver):
        self.driver = driver
        self.MapLink = Locators_AboutUs.MAP_LINK
        self.UI = Locators_AboutUs.UI
        self.aboutUs = Locators_AboutUs.ABOUT_US

    @allure.step
    def about_us_page(self):
        self.driver.get('https://trip-yoetz.herokuapp.com/about')
        self.driver.implicitly_wait(20)

    @allure.step
    def ui(self):
        return self.driver.find_element(By.XPATH, self.UI).get_attribute('innerText')



