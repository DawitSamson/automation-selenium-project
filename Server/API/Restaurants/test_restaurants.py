import allure
import requests


class Test_Restaurants:
    URL = 'https://trip-yoetz.herokuapp.com/api/restaurants/'

    @allure.description('Navigate to Restaurant Page Correctly')
    def test_navigate_restaurants_correctly(self):
        value_id = '624484c18f5ad0b6581d0744'
        value_name = "Quality Italian"
        url = Test_Restaurants.URL
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 15
        assert res_data['success'] == True
        assert res_data['restaurant']['name'] == value_name

    @allure.description('Navigate to Restaurant Page Incorrectly')
    def test_navigate_restaurants_incorrectly(self):
        value_id = "ad0b65"
        url = Test_Restaurants.URL
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 500
        assert res_data['success'] == False
        assert res_data['message'] == f'Cast to ObjectId failed for value "{value_id}" ' \
                                      '(type string) at path "_id" for model "Restaurant"'

