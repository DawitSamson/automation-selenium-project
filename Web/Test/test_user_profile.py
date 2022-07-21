from Web.coftest import Fixtures
import pytest

@pytest.mark.usefixtures('login_successfully')
@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
class Test_User_Profile(Fixtures):
    def test_update1(self):
        pass

    def test_update2(self):
        pass

    def test_update3(self):
        pass