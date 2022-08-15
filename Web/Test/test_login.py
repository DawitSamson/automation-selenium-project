import allure
import pytest
from Web.Pages.accessibility_page import Accessibility_Page
from Web.Base.base import Base
from Web.Pages.login_page import Login_Page
from Web.Utils.utils import Utils
from Web.coftest import Fixtures
from Web.Pages.web_page import Web_Page

@pytest.mark.usefixtures('set_up')
@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
class Test_Login(Fixtures, Base):

    @allure.description('Login successfully, this is the PreCondition for user profile tests')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.usefixtures('login_successfully')
    def test_login_successfully(self):
        pass

    @allure.description('Login when the values in the fields are invalid')
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason='Email and password format messages are different on 2 browsers')
    def test_login_invalid_fields_all_the_options(self):
        emails = ['Avi', 'Yosef@', 'Miki@.com', '!!!!']
        passwords = ['5', '10', '100', '', '1115555']
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.email_and_password_combinations(emails, passwords)

    @allure.description('Login incorrectly when the email is correct and the password is incorrect')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_exist_and_incorrect_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosef@gmail.com')
        login.enter_password('walla-com')
        login.login_button()
        Utils(driver).assertion('password or email incorrect', login.email_or_password_error())

    @allure.description('Login incorrectly when the email is incorrect and the password is incorrect')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_not_exist_and_incorrect_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yossss@gmail.com')
        login.enter_password('walla-com')
        login.login_button()
        Utils(driver).assertion('no user found', login.no_user_error_message())

    @allure.description('Searching correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_search_correctly(self):
        city = 'Paris'
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        search = Web_Page(driver)
        search.searching(city)
        Utils(driver).assertion(f'Discover {city}', search.city_name_correctly())

    @allure.description('Searching incorrectly')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_search_incorrectly(self):
        city = 'Israel'
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        search = Web_Page(driver)
        search.searching(city)
        Utils(driver).assertion('No City Found', search.city_name_incorrectly())

    @allure.description('Navigate from login page to all the pages in the website')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_nav_bar_links(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        web_page = Web_Page(driver)
        web_page.click_navbar_links('Login')

    @allure.description('Verify all the text in the page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_ui(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        Utils(driver).assertion("Login\nRegister\nAbout us\nTripYoetz\nNew here ?\nTo"
                                      " register please click the link below\nRegister\nLogin\n"
                                      "LOGIN\nMarcos Bazbih\n24 years old, Ashdod\nTikva Yosef"
                                      "\n26 years old, Natanya\nAvi Admaso\n26 years old, Ashdod"
                                      "\nWho are we?\nTripYoetz\nLearn more\ncopyright © | 2022"
                                      " TripYoetz | all right reserved.", login.ui())

    @allure.description('Accessibility test on login page clicking one color after the other')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility1(self):
        driver = self.driver
        login = Login_Page(driver)
        accessibility = Accessibility_Page(driver)
        login.login_page()
        accessibility.clicking_color(2)
        accessibility.clicking_color(3)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Accessibility test on login page clicking on color and return to default color')
    @allure.severity(allure.severity_level.NORMAL)
    def test_accessibility2(self):
        driver = self.driver
        login = Login_Page(driver)
        accessibility = Accessibility_Page(driver)
        login.login_page()
        accessibility.clicking_color(2)
        accessibility.clicking_color(1)
        accessibility.clicking_color(3)
        accessibility.clicking_color(1)
        accessibility.clicking_color(4)
        accessibility.clicking_color(1)

    @allure.description('Login successfully with clicking on show password button')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason='Attribute(type) of password not change to text')
    def test_login_successfully_(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosf@gmail.com')
        login.enter_password('123456')
        login.click_show_password_button()
        login.login_button()
        login.accept_alert()
        driver.forward()
        login.click_profile_link()
        Utils(driver).assertion('YOUR INFORMATION', login.login_validation_message())
