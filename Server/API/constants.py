""" all the constants in the Server tests , Values, Messages and Keys """

import random

class LoginConstants:
    url_login = 'https://trip-yoetz.herokuapp.com/auth/login'
    success_key = 'success'
    message_key = 'message'
    data_valid = {"email": "Yosef@gmail.com", "password": "123456"}
    data_invalid_password = {"email": "Yosef@gmail.com", "password": "6116161616"}
    data_invalid_email = {"email": "m@fg", "password": "123456"}
    data_invalid_password_and_email = {"email": "m@fg", "password": "1223231184"}

class RegisterConstants(LoginConstants):
    num = random.randint(1, 2500)
    url_register = 'https://trip-yoetz.herokuapp.com/auth/register'
    data_valid = {'birthDate': "2000-02-02",
                  'email': f"yoss{num}@ss.com",
                  'lastName': "Meshuulam",
                  'name': "Avi",
                  'password': "123456"}
    data_invalid = {'birthDate': "2000-02-02",
                    'email': "yossi111@ss.com",
                    'lastName': "Meshuulam",
                    'name': "Avi",
                    'password': "123456"}

class SearchConstants(LoginConstants):
    url_search = "https://trip-yoetz.herokuapp.com/api/cities/"
    value_valid = 'Miami'
    value_invalid = 'Tel-Aviv'
    value_illegal = '1111'
    data_key = 'data'
    name_key = 'name'

class RestaurantsConstants(SearchConstants):
    url_restaurants = 'https://trip-yoetz.herokuapp.com/api/restaurants/'
    value_id = '624484c18f5ad0b6581d0744'
    value_id_illegal = "ad0b65"
    value_name = "Quality Italian"
    restaurant_key = 'restaurant'