import allure
import pytest
from Web.Pages.register_page import Register_Page
from Web.Base.base import Base
from Web.Utils.utils import Utils
from Web.coftest import Fixtures

@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
class Test_Register(Fixtures, Base):

    @allure.description('Navigate to login page correctly')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail(reason='section class name not change')
    def test_click_on_login_link(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.click_on_login_link()

    def test_user_register_correctly(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_first_name('Yosef')
        register.enter_last_name('Alemayi')
        register.enter_date('2000-10-15')
        register.enter_email('Yosf@gmail.com')
        register.enter_image_name('no Imange')
        register.enter_password('123456')
        register.enter_confirm_password('123456')
        register.click_on_register_button()
        Utils(driver).assertion("user with that email already exists", register.user_already_exist_error())
