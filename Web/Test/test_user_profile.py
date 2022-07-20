import pytest
from Web.Utils.pre_condition import PreCondition_UserProfile

@pytest.mark.usefixtures('test_login_successfully')
class Test_User_Profile(PreCondition_UserProfile):

    def test_update(self):
        pass

    def test_update1(self):
        pass

    def test_update2(self):
        pass

    def test_update3(self):
        pass

    def test_update4(self):
        pass
