import requests
import allure

class Test_Search:
    URL = "https://trip-yoetz.herokuapp.com/api/cities/"

    @allure.description('Search Correctly In The Website')
    def test_search_correctly(self):
        value = 'Miami'
        url = Test_Search.URL
        res = requests.get(url+value)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == True
        assert res_data["data"]['name'] == value

    @allure.description('Search Incorrectly - City Not Exist')
    def test_search_incorrectly_when_city_not_exist(self):
        value = 'Tel Aviv'
        url = Test_Search.URL
        res = requests.get(url+value)
        res_data = res.json()
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "no city found"

    @allure.description('Search Incorrectly When City Name Invalid')
    def test_search_incorrectly_with_invalid_value(self):
        value = '1111'
        url = Test_Search.URL
        res = requests.get(url+value)
        res_data = res.json()
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "no city found"

