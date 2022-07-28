from Web.coftest import Fixtures
import pytest
from Web.Pages.user_profile_page import User_Profile_Page

@pytest.mark.usefixtures('login_successfully')
@pytest.mark.parametrize('browser', ['chrome'])
class Test_User_Profile(Fixtures):
    def test_update1(self):
        pass

    def test_update2(self):
        pass

    def test_update3(self):
        driver = self.driver
        user = User_Profile_Page(driver)
        user.click_on_edit_profile_button()
        user.enter_date("1996-11-26"
                        "")