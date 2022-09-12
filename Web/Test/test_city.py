from time import sleep
from Web.Test.conftest import Web_Fixtures
import allure
import pytest
from Web.Pages.city_page import City_Page
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('search')
@pytest.mark.usefixtures('pre_condition')
@pytest.mark.parametrize('city_name', ['London'])
class Test_City(Web_Fixtures):
    def test_1(self):
        pass

    def test_12(self):
        pass