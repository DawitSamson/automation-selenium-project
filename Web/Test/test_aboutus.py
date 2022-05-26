import allure
import pytest
from Web.Utils.utils import Utils
from Web.Pages.aboutus_page import AboutUs_Page
from Web.Base.base import Base

@pytest.mark.usefixtures('set_up')
class Test_AboutUs(Base):

    @allure.description('Verify All The Text In The page ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_ui(self):
        driver = self.driver
        about_us = AboutUs_Page(driver)
        compare = Utils(driver)
        about_us.about_us_page()
        about_us.ui()
        compare.assertion(about_us.ui(), "Login\nRegister\nAbout us\nTripYoetz\nwelcome to tripYoetz"
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
                                         "| 2022 TripYoetz | all right reserved.")

    @allure.description('Searching Correctly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_correctly(self):
        city_name = 'London'
        driver = self.driver
        about_us = AboutUs_Page(driver)
        search = Utils(driver)
        about_us.about_us_page()
        search.searching(city_name)
        search.assertion(search.city_name_correctly(), f'Discover {city_name}')

    @allure.description('Searching Incorrectly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_incorrectly(self):
        city_name = '567'
        driver = self.driver
        about_us = AboutUs_Page(driver)
        search = Utils(driver)
        about_us.about_us_page()
        search.searching(city_name)
        search.assertion(search.city_name_incorrectly(), 'No City Found')

    @allure.description('Navigate From About Us Page To All The Pages In The Website')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navbar_links(self):
        driver = self.driver
        links = Utils(driver)
        about_us = AboutUs_Page(driver)
        about_us.about_us_page()
        links.click_navbar_links('About us')
