from time import sleep
from Web.Utils.utils import Utils
from Web.Pages.login_page import Login_Page
from Web.Base.base import Base
import pytest

class Fixtures(Base):
    @pytest.fixture()
    def login_successfully(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosf@gmail.com')
        login.enter_password('123456')
        login.login_button()
        login.accept_alert()
        sleep(0.5)
        driver.forward()
        login.click_profile_link()
        Utils(driver).assertion('YOUR INFORMATION', login.login_validation_message())
