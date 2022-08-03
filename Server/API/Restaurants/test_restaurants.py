import allure
import requests


class Test_Restaurants:
    URL = 'https://trip-yoetz.herokuapp.com/api/restaurants/'

    @allure.description('Get single Restaurant with Correctly data')
    def test_get_single_restaurant_correctly(self):
        value_id = '624484c18f5ad0b6581d0744'
        value_name = "Quality Italian"
        url = Test_Restaurants.URL
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 15
        assert res_data['success'] == True
        assert res_data['restaurant']['name'] == value_name

    @allure.description('Get single Restaurant with Incorrectly Data')
    def test_get_restaurant_data_incorrectly(self):
        value_id = "ad0b65"
        url = Test_Restaurants.URL
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 500
        assert res_data['success'] == False
        assert res_data['message'] == f'Cast to ObjectId failed for value "{value_id}" ' \
                                      '(type string) at path "_id" for model "Restaurant"'

    @allure.description('Get All the Data from restaurants')
    def test_get_all_the_restaurants(self):
        res = requests.get(Test_Restaurants.URL)
        res_data = res.json()
        number_of_records = len(res_data['data'])
        assert res.status_code == 200
        assert res_data['success'] == True
        assert number_of_records == 67

    @allure.description
    def test_add_comment_on_restaurant(self):
        value_id = '62446e465228abc755a013d9'
        res = requests.get(Test_Restaurants.URL+value_id)
        print(res.status_code)
        res_data = res.json()
        a = res_data['restaurant']['comments']
        print(a[0]['body'])