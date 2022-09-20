from Mobile.Tests.conftest import Mobile_Fixtures
from Web.Pages.login_page import Login_Page
from Web.Test.conftest import Web_Fixtures
from Web.Utils.utils import Utils
import allure

class Test_LoginMobile(Mobile_Fixtures, Web_Fixtures):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Login to the website from mobile correctly")
    def test_login_successfully(self, pre_condition):
        pass

    def test_login_incorrectly_with_wrong_email(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email("nnn@nnn.com")
        login.enter_password("123456")
        login.login_button()
        Utils(self.driver).assertion("no user found", login.no_user_error_message())

    def test_login_incorrectly_with_wrong_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosef@gmail.com')
        login.enter_password('walla-com')
        login.login_button()
        Utils(driver).assertion('password or email incorrect', login.email_or_password_error())