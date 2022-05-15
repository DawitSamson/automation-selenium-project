from Pages.login_page import Login_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators_login_page import Locators_Login_Page

class Utils:
    def __init__(self, driver):
        self.driver = driver
        self.searchField = Locators_Login_Page.SEARCH_FIELD  # This is The Search Field
        self.cityName = Locators_Login_Page.CITY_NAME  # The Text That returns In Correctly Search
        self.errorCityName = Locators_Login_Page.CITY_ERROR_MESSAGE  # The Text That returns In Incorrectly Search

    def assertion(self, expected, actual, filename):
        driver = self.driver
        try:
            assert expected == actual
        except AssertionError:
            driver.get_screenshot_as_png()
            driver.save_screenshot(filename)


    def searching(self, city_name):
        searching = self.driver.find_element(By.CLASS_NAME, self.searchField)
        searching.send_keys(city_name)
        searching.send_keys(Keys.ENTER)

    def city_name_correctly(self):
        return self.driver.find_element(By.XPATH, self.cityName).get_attribute('innerText')

    def city_name_incorrectly(self):
        return self.driver.find_element(By.XPATH, self.errorCityName).get_attribute('innerText')
















    def navbar_links(self, page_name):
        driver = self.driver
        login = Login_Page(driver)
        all_the_links = login.nav_bar_links()
        compare = Utils(driver)

        for link in range(len(all_the_links)):
            if all_the_links[link].text == page_name:
                continue
            all_the_links[link].click()

            if 'Re' in all_the_links[link].text:
                compare.assertion(all_the_links[link].text, 'Register', 'RegisterError.png')

            elif 'Ab' in all_the_links[link].text:
                compare.assertion(all_the_links[link].text, 'About us', 'AboutUsError.png')

            elif 'Tr' in all_the_links[link].text:
                compare.assertion(all_the_links[link].text, 'TripYoetz', 'LogoError.png')

            elif 'Log' in all_the_links[link].text:
                compare.assertion(all_the_links[link].text, 'Login', 'LoginError.png')

            driver.back()

