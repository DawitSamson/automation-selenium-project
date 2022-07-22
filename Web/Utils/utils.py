from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.whoAreWeButton = Utils_Locators.WHO_ARE_WE_BUTTON  # The button That open The who are we Section
        self.whoAreWeLinks = Utils_Locators.WHO_ARE_WE_LINKS  # All The Contacts Links & Pages Links
        self.accessibilityButton = Utils_Locators.ACCESSIBILITY_BUTTON  # Button That Open the Section
        self.accessibilityColors = Utils_Locators.ACCESSIBILITY_COLORS  # List with 4 Values (Colors)

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
    @allure.description('Return all the list with links on navbar')
    def navbar_links_list(self):
        links = self.driver.find_elements(By.XPATH, self.navBarLinks)
        self.assertion(4, len(links))
        return links

    @allure.step
    @allure.description('Clicking on all the links in the navbar without the current page')
    def click_navbar_links(self, page_name):
        driver = self.driver
        nav_bar_links = self.navbar_links_list()

        for link in range(len(nav_bar_links)):
            if nav_bar_links[link].text == page_name:
                continue
            nav_bar_links[link].click()

            if 'Re' in nav_bar_links[link].text:
                self.assertion('Register', nav_bar_links[link].text)

            elif 'Ab' in nav_bar_links[link].text:
                self.assertion('About us', nav_bar_links[link].text)

            elif 'Tr' in nav_bar_links[link].text:
                self.assertion('TripYoetz', nav_bar_links[link].text)

            elif 'Log' in nav_bar_links[link].text:
                self.assertion('Login', nav_bar_links[link].text)

            driver.back()

    @allure.step
    @allure.description('The button that open the ruler with all the colors')
    def click_accessibility_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.accessibilityButton).click()

    @allure.step
    @allure.description('Getting the list with all the colors and start clicking them')
    def click_colors(self):
        wait = WebDriverWait(self.driver, 20)
        colors = self.driver.find_elements(By.XPATH, self.accessibilityColors)
        for color in range(len(colors)):
            if color != 0:
                self.driver.implicitly_wait(10)
                self.click_accessibility_button()
                wait.until(EC.presence_of_all_elements_located((By.XPATH, self.accessibilityColors)))
                wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.accessibilityColors)))
                colors[color].click()
                self.driver.implicitly_wait(10)

        """ verify the background is change to the correct color """
        self.assertion(colors[0].value_of_css_property('background-image'),
                       'linear-gradient(120deg, rgb(0, 0, 0) 40%, rgb(245, 222, 179) 60%)')
        self.assertion(colors[1].value_of_css_property('background-image'),
                       'linear-gradient(120deg, rgb(245, 203, 92) 40%, rgb(36, 36, 35) 60%)')
        self.assertion(colors[2].value_of_css_property('background-image'),
                       'linear-gradient(120deg, rgb(20, 33, 61) 40%, rgb(152, 193, 217) 60%)')
        self.assertion(colors[3].value_of_css_property('background-image'),
                       'linear-gradient(120deg, rgb(0, 0, 0) 40%, rgb(152, 150, 241) 60%)')