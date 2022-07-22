import allure
from Web.Locators.locators_aboutus_page import Locators_AboutUs
from selenium.webdriver.common.by import By
from Web.Utils.utils import Utils

class AboutUs_Page:
    def __init__(self, driver):
        self.driver = driver
        self.MapLink = Locators_AboutUs.MAP_LINK
        self.UI = Locators_AboutUs.UI
        self.aboutUs = Locators_AboutUs.ABOUT_US

    @allure.step
    @allure.description('Navigate to about-us page')
    def about_us_page(self):
        url = 'https://trip-yoetz.herokuapp.com/about'
        self.driver.get(url)
        Utils(self.driver).assertion(url, self.driver.current_url)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Validation - returns all the text in the page')
    def ui(self):
        return self.driver.find_element(By.XPATH, self.UI).get_attribute('innerText')



