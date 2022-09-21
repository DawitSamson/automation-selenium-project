import allure
import pytest
from Web.Test.conftest import Web_Fixtures
from Web.Pages.Web_Page.accessibility_page import Accessibility_Page
from Web.Pages.Web_Page.navbar_page import NavBar
from Web.Pages.user_profile_page import User_Profile_Page
from Web.Pages.city_page import City_Page
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('search')
@pytest.mark.usefixtures('pre_condition')
@pytest.mark.parametrize('city_name', ['London'])
class Test_City(Web_Fixtures):

    @allure.description('Searching correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_search_correctly(self):
        pass

    @allure.description('Searching incorrectly')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_search_incorrectly(self):
        driver = self.driver
        navbar = NavBar(driver)
        navbar.searching("tel-aviv")
        Utils(driver).assertion("No City Found", navbar.city_name_incorrectly())

    @allure.description('Accessibility test on login page clicking one color after the other')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility1(self):
        driver = self.driver
        accessibility = Accessibility_Page(driver)
        accessibility.clicking_color(2)
        accessibility.clicking_color(3)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Accessibility test on login page clicking on color and return to default color')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility2(self):
        driver = self.driver
        accessibility = Accessibility_Page(driver)
        accessibility.clicking_color(2)
        accessibility.clicking_color(1)
        accessibility.clicking_color(3)
        accessibility.clicking_color(1)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Clicking all the navbar links')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_nav_bar_links(self):
        driver = self.driver
        web_page = NavBar(driver)
        web_page.click_navbar_links_1(1)
        web_page.click_navbar_links_1(3)
        web_page.click_navbar_links_1(4)
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/cities', self.driver.current_url)

    @allure.description('User log out correctly from the user account')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_log_out(self):
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_log_out_button()
        Utils(driver).assertion("https://trip-yoetz.herokuapp.com/", driver.current_url)

    @allure.description('User navigate to hotels section in navbar')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_hotels_correctly(self):
        driver = self.driver
        city = City_Page(driver)
        city.navigate_to_hotels_nav_bar()
        Utils(driver).assertion("Hotels", city.category_name())

    @allure.description('User navigate to restaurants section in navbar')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_restaurants_correctly(self):
        driver = self.driver
        city = City_Page(driver)
        city.navigate_to_restaurants_nav_bar()
        Utils(driver).assertion("Restaurants", city.category_name())

    @allure.description('User navigate to activities section in navbar')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_activities_correctly(self):
        driver = self.driver
        city = City_Page(driver)
        city.navigate_to_activities_nav_bar()
        Utils(driver).assertion("Activities", city.category_name())

    @allure.description('User navigate to one of the sections in navbar and navigate again to city page')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_city_correctly(self):
        driver = self.driver
        city = City_Page(driver)
        city.navigate_to_activities_nav_bar()
        Utils(driver).assertion("Activities", city.category_name())
        city.navigate_to_city_nav_bar()
        Utils(driver).assertion("Discover London", city.city_name())

    @allure.description('User navigate to hotels section from view all link')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_hotels_from_view_all_link(self):
        driver = self.driver
        city = City_Page(driver)
        city.view_all_hotels()
        Utils(driver).assertion("Hotels", city.category_name())

    @allure.description('User navigate to restaurants section from view all link')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_restaurants_from_view_all_link(self):
        driver = self.driver
        city = City_Page(driver)
        city.view_all_restaurants()
        Utils(driver).assertion("Restaurants", city.category_name())

    @allure.description('User navigate to activities section from view all link')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_activities_from_view_all_link(self):
        driver = self.driver
        city = City_Page(driver)
        city.view_all_activities()
        Utils(driver).assertion("Activities", city.category_name())