import time

import pytest
from Web.Pages.register_page import Register_Page
from Web.Base.base import Base
from Web.coftest import Fixtures

@pytest.mark.parametrize('browser', ['chrome'])
class Test_Register(Fixtures, Base):
    def test_1(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_first_name('Yosef')
        register.enter_last_name('ALemayi')
        register.enter_date('2001-10-30')
