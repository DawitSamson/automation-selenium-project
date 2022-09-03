from time import sleep
from Web.coftest import Fixtures
import allure
import pytest
from Web.Pages.city_page import City_Page
from Web.Utils.utils import Utils

@pytest.mark.parametrize('browser', ['chrome', 'firefox'])
@pytest.mark.usefixtures('search')
@pytest.mark.usefixtures('pre_condition')
class Test_City(Fixtures):

    @pytest.mark.parametrize('city_name', ['London'])
    def test_1(self):
        driver = self.driver
        city = City_Page(driver)
        restaurants_names = ['', '', '', '', '', '']
        city.restaurant_images()