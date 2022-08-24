import allure
from Web.Pages.Web_Page.navbar_page import NavBar
from Web.Utils.utils import Utils
from Web.Pages.Web_Page.accessibility_page import Accessibility_Page
from Web.coftest import Fixtures
import pytest
from Web.Pages.user_profile_page import User_Profile_Page

@pytest.mark.usefixtures('pre_condition')
@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
class Test_User_Profile(Fixtures):

    @allure.description('Accessibility test on about-us page clicking one color after the other')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility1(self):
        driver = self.driver
        accessibility = Accessibility_Page(driver)
        accessibility.clicking_color(2)
        accessibility.clicking_color(3)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Accessibility test on about-us page clicking on color and return to default color')
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

    @allure.description('Searching correctly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_correctly(self):
        city_name = 'Barcelona'
        driver = self.driver
        search = NavBar(driver)
        search.searching(city_name)
        Utils(driver).assertion(f'Discover {city_name}', search.city_name_correctly())

    @allure.description('Searching incorrectly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_incorrectly(self):
        city_name = '!!!'
        driver = self.driver
        search = NavBar(driver)
        search.searching(city_name)
        Utils(driver).assertion('No City Found', search.city_name_incorrectly())

    @allure.description('Clicking all the navbar links')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_nav_bar_links(self):
        driver = self.driver
        web_page = NavBar(driver)
        web_page.click_navbar_links_1(3)
        web_page.click_navbar_links_1(4)
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/profile', self.driver.current_url)

    @allure.description('User log out correctly from the user account')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_log_out_correctly(self):
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_log_out_button()

    @allure.description('Update user full name correctly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_fullname(self):
        driver = self.driver
        f_name = 'Avi'
        l_name = 'Saba'
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_first_name(f_name)
        user.enter_last_name(l_name)
        user.click_on_update_button()
        Utils(driver).assertion(f"Name: {f_name} {l_name}", user.full_name_value())

    @allure.description('Update user first name Incorrectly when the length of first name lower than 2')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_first_name_incorrectly1(self):
        driver = self.driver
        f_name = 'a'
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_first_name(f_name)
        user.click_on_update_button()
        Utils(driver).assertion('עליך להאריך את הטקסט ל-2 תווים או יותר (כרגע יש תו אחד).',
                                user.error_message(user.enter_first_name(f_name), 'validationMessage'),
                                'Please use at least 2 characters (you are currently using 1 characters).')

    @allure.description('Update user last name Incorrectly when the length of first name lower than 2')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_last_name_incorrectly1(self):
        driver = self.driver
        l_name = 'a'
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_last_name(l_name)
        user.click_on_update_button()
        Utils(driver).assertion('עליך להאריך את הטקסט ל-2 תווים או יותר (כרגע יש תו אחד).',
                                user.error_message(user.enter_last_name(l_name), 'validationMessage'),
                                'Please use at least 2 characters (you are currently using 1 characters).')

    @allure.description('Update user last name Incorrectly when the length of first name greater than 10')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.xfail(reason='first name value with length (11) and actual value send with length (10),test is passed')
    def test_update_user_first_name_incorrectly2(self):
        f_name = 'abcdefgijkl'
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_first_name(f_name)
        user.click_on_update_button()

    @allure.description('Update user birth date correctly')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_birth_date(self):
        year, month, day = '1995', '10', '09'
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_date('{}-{}-{}'.format(year, month, day))
        user.click_on_update_button()
        Utils(driver).assertion(f"Age: {2022-int(year)}", user.age_value())

    @allure.description('Update user birth date incorrectly when birth greater than 01-01-2004')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_birth_date_incorrectly1(self):
        year, month, day = '2005', '01', '01'
        date = '{}-{}-{}'.format(year, month, day)
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_date(date)
        user.click_on_update_button()
        Utils(driver).assertion('על הערך להיות 01/01/2004 או מוקדם יותר.',
                                user.error_message(user.enter_date(date), 'validationMessage'),
                                'Please select a value that is no later than 2004-01-01.')

    @allure.description('Update user birth date incorrectly when birth lower than 01-01-1902')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_birth_date_incorrectly2(self):
        year, month, day = '1901', '01', '01'
        date = '{}-{}-{}'.format(year, month, day)
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_date(date)
        user.click_on_update_button()
        Utils(driver).assertion('על הערך להיות 01/01/1902 ומעלה.',
                                user.error_message(user.enter_date(date), 'validationMessage'),
                                'Please select a value that is no earlier than 1902-01-01.')
