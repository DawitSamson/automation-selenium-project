import allure
import pytest
from Web.Utils.utils import Utils
from Web.Pages.aboutus_page import AboutUs_Page
from Web.Base.base import Base
from Web.coftest import Fixtures
from Web.Pages.accessibility_page import Accessibility_Page

@pytest.mark.usefixtures('set_up')
@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
class Test_AboutUs(Fixtures, Base):

    @allure.description('Verify all the user interface in the page ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_ui(self):
        driver = self.driver
        about_us = AboutUs_Page(driver)
        about_us.about_us_page()
        Utils(driver).assertion("Login\nRegister\nAbout us\nTripYoetz\nwelcome to tripYoetz"
                                         "\nAbout Us\nTripYoetz, the world's largest travel guidance platform"
                                         ", helps hundreds of millions of people each month become better "
                                         "travelers, from planning to booking to taking a trip. Travelers"
                                         " across the globe use the Tripadvisor site and app to discover "
                                         "where to stay, what to do and where to eat based on guidance "
                                         "from those who have been there before. With more than 1 billion "
                                         "reviews and opinions of nearly 8 million businesses, travelers"
                                         " turn to Tripadvisor to find deals on accommodations, book"
                                         " experiences, reserve tables at delicious restaurants and "
                                         "discover great places nearby. As a travel guidance company"
                                         " available in 43 markets and 22 languages, Tripadvisor makes"
                                         " planning easy no matter the trip type.\nContact"
                                         " Us\n\n054-8789426\n\ncontact@TripYoetz.com\n\n24 / 7\n\nMeet the "
                                         "team\nMarcos Bazbih\n24 years old, Ashdod\nFull Stack"
                                         " Developer\nTikva Yosef\n26 years old, Natanya\nFull Stack "
                                         "Developer\nAvi Admaso\n26 years old, Ashdod\nFull Stack Developer"
                                         "\nFollow the links below for more info\nMarcos Bazbih\n24 years old,"
                                         " Ashdod\nTikva Yosef\n26 years old, Natanya\nAvi Admaso\n26 years"
                                         " old, Ashdod\nWho are we?\nTripYoetz\nLearn more\ncopyright © "
                                         "| 2022 TripYoetz | all right reserved.", about_us.ui())

    @allure.description('Searching correctly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_correctly(self):
        city_name = 'London'
        driver = self.driver
        about_us = AboutUs_Page(driver)
        search = Utils(driver)
        about_us.about_us_page()
        search.searching(city_name)
        search.assertion(f'Discover {city_name}', search.city_name_correctly())

    @allure.description('Searching incorrectly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_incorrectly(self):
        city_name = '567'
        driver = self.driver
        about_us = AboutUs_Page(driver)
        search = Utils(driver)
        about_us.about_us_page()
        search.searching(city_name)
        search.assertion('No City Found', search.city_name_incorrectly())

    @allure.description('Navigate from about-us page to all the pages in the website')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navbar_links(self):
        driver = self.driver
        links = Utils(driver)
        about_us = AboutUs_Page(driver)
        about_us.about_us_page()
        links.click_navbar_links('About us')

    @allure.description('Accessibility test on about-us page clicking one color after the other')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility1(self):
        driver = self.driver
        about = AboutUs_Page(driver)
        accessibility = Accessibility_Page(driver)
        about.about_us_page()
        accessibility.clicking_color(2)
        accessibility.clicking_color(3)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Accessibility test on about-us page clicking on color and return to default color')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility2(self):
        driver = self.driver
        about = AboutUs_Page(driver)
        accessibility = Accessibility_Page(driver)
        about.about_us_page()
        accessibility.clicking_color(2)
        accessibility.clicking_color(1)
        accessibility.clicking_color(3)
        accessibility.clicking_color(1)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

