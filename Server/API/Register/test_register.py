import random
import requests
import allure

class Test_Register:
    URL = 'https://trip-yoetz.herokuapp.com/auth/register'

    @allure.description('User Registered Correctly')
    def test_user_register_correctly(self):
        url = Test_Register.URL
        num = random.randint(1, 1500)
        data = {'birthDate': "2000-02-02",
                'email': f"yoss{num}@ss.com",
                'lastName': "Meshuulam",
                'name': "Avi",
                'password': "123456"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == True
        assert res_data['message'] == 'user added successfully'

    @allure.description('User Registered With Exist Email')
    def test_user_register_incorrectly_with_exist_email(self):
        url = Test_Register.URL
        data = {'birthDate': "2000-02-02",
                'email': "yossi111@ss.com",
                'lastName': "Meshuulam",
                'name': "Avi",
                'password': "123456"}
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data['success'] == False
        assert res_data['message'] == "user with that email already exists"


