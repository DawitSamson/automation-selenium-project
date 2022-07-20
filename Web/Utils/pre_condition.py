import pytest
from Web.Base.base import Base
from Web.Pages.login_page import Login_Page
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('set_up')
@pytest.mark.parametrize('browser', ['chrome'])
class PreCondition_UserProfile(Base):

    @pytest.fixture(autouse=True)
    def test_login_successfully(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosef@gmail.com')
        login.enter_password('123456')
        login.login_button()
        login.accept_alert()
        driver.forward()
        login.click_profile_link()
        Utils(driver).assertion('YOUR INFORMATION', login.login_validation_message())


