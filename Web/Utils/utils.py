from Web.Utils.locatorsUtils import Utils_Locators
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys


class Utils:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.searchField = Utils_Locators.SEARCH_FIELD  # This is The Search Field
        self.cityName = Utils_Locators.CITY_NAME  # The Text That returns In Correctly Search
        self.errorCityName = Utils_Locators.CITY_ERROR_MESSAGE  # The Text That returns In Incorrectly Search
        self.navBarLinks = Utils_Locators.NAV_BAR_LINKS  # Returns The List With All The 4 Links

    @allure.step
    @allure.description('This validation method, if the assert failed screenshot is taken')
    def assertion(self, expected, actual):
        driver = self.driver
        try:
            assert expected == actual
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name='screenShot',
                          attachment_type=AttachmentType.PNG)
            raise AssertionError

    @allure.step
    @allure.description('The search method that included valid and invalid search')
    def searching(self, city_name):
        searching = self.driver.find_element(By.CLASS_NAME, self.searchField)
        searching.send_keys(city_name)
        self.assertion(city_name, searching.get_attribute('value'))
        searching.send_keys(Keys.ENTER)

    @allure.step
    @allure.description('Validation - message when search is correctly')
    def city_name_correctly(self):
        return self.driver.find_element(By.XPATH, self.cityName).get_attribute('innerText')

    @allure.step
    @allure.description('Validation - message when search is incorrectly')
    def city_name_incorrectly(self):
        return self.driver.find_element(By.XPATH, self.errorCityName).get_attribute('innerText')

    @allure.step
    @allure.description('Return all the list with links on navbar when the user doesnt connect')
    def navbar_links_list(self):
        links = self.driver.find_elements(By.XPATH, self.navBarLinks)
        self.assertion(4, len(links))
        return links

    @allure.step
    @allure.description('Clicking on all the links in the navbar and return to the current page')
    def click_navbar_links(self, page_name):
        driver = self.driver
        nav_bar_links = self.navbar_links_list()
        for link in range(len(nav_bar_links)):
            if nav_bar_links[link].text == page_name:
                continue
            nav_bar_links[link].click()
            if link == 0:
                self.assertion('Login', nav_bar_links[link].text)
                self.assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/login')
            elif link == 1:
                self.assertion('Register', nav_bar_links[link].text)
                self.assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/register')
            elif link == 2:
                self.assertion('About us', nav_bar_links[link].text)
                self.assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/about')
            elif link == 3:
                self.assertion('TripYoetz', nav_bar_links[link].text)
                self.assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/')
            driver.back()








    def practice(self, div_option: int):
        locator = f'//header/div[{div_option}]/a'
        link = self.driver.find_element(By.XPATH, locator)
        if div_option == 1:
            link.click()
            self.assertion('/profile', link.get_attribute('pathname'))
        elif div_option == 3:
            link.click()
            self.assertion('About us', link.get_attribute('innerText'))
        elif div_option == 4:
            link.click()
            self.assertion("TripYoetz", link.get_attribute('innerText'))
        else:
            raise ValueError('div_position need to be 1,3,4')
        self.driver.back()

    def practice12(self):
        self.practice(3)
        self.practice(1)
        self.practice(4)