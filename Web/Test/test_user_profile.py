import pytest
from Web.Base.base import Base
from Web.Pages.user_profile_page import User_Profile_Page
from Web.Test.test_login import Test_Login

@pytest.mark.usefixtures('test_login_successfully')
class Test_UserProfile(Test_Login, Base):
    def test_update_details(self):
        pass


