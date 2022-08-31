import time

from Web.coftest import Fixtures
import allure
import pytest
from Web.Pages.city_page import City_Page
from Web.Utils.utils import Utils

@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
@pytest.mark.usefixtures('search')
@pytest.mark.usefixtures('pre_condition')
class Test_City(Fixtures):

    @allure.description('Navigate to hotels section')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['London'])
    def test_navigate_to_hotels(self):
        driver = self.driver
        city = City_Page(driver)
        city.click_on_option_from_navbar_list('hotels')
        Utils(driver).assertion('Hotels', city.category_name())

    @allure.description('Navigate to restaurants section')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['Barcelona'])
    def test_navigate_to_restaurants(self):
        driver = self.driver
        city = City_Page(driver)
        city.click_on_option_from_navbar_list('restaurants')
        Utils(driver).assertion('Restaurants', city.category_name())

    @allure.description('Navigate to activities section')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['London'])
    def test_navigate_to_activities(self):
        driver = self.driver
        city = City_Page(driver)
        city.click_on_option_from_navbar_list('activities')
        Utils(driver).assertion('Activities', city.category_name())

    @allure.description('Navigate to on of the sections and back to city section')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['Jerusalem'])
    def test_navigate_to_city_from_another_option(self, search):
        driver = self.driver
        city = City_Page(driver)
        self.test_navigate_to_restaurants(search)
        city.click_on_option_from_navbar_list('city')
        Utils(driver).assertion("Discover Jerusalem", city.city_name())

    @allure.description('Navigate to restaurants page from city slider')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['London'])
    def test_view_all_restaurants(self):
        driver = self.driver
        user = City_Page(driver)
        user.click_restaurants_slider()
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/restaurants', driver.current_url)

    @allure.description('Navigate to hotels page from city slider')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['London'])
    def test_view_all_hotels(self):
        driver = self.driver
        user = City_Page(driver)
        user.click_hotels_slider()
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/hotels', driver.current_url)

    @allure.description('Navigate to activities page from city slider')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('city_name', ['London'])
    def test_view_all_activities(self):
        driver = self.driver
        user = City_Page(driver)
        user.click_activities_slider()
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/activities', driver.current_url)

    ''' work on buttons tests '''
    @pytest.mark.parametrize('city_name', ['London'])
    def test_click_on_next_image(self):
        driver = self.driver
        city = City_Page(driver)
        city.click_next_image_button_eat()
        assert city.click_prev_image_button_eat() == 'false'

