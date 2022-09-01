import random

import allure
from Web.Locators.locators_city import City_Locators
from Web.Pages.user_profile_page import User_Profile_Page
from Web.Utils.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class City_Page(User_Profile_Page):
    def __init__(self, driver):
        User_Profile_Page.__init__(self, driver)
        self.cityNavBar = City_Locators.CITY_NAV_BAR
        self.validationForCityNavBar = City_Locators.CITY_NAME_H1
        self.hotelsNavBar = City_Locators.HOTELS_NAV_BAR
        self.restaurantsNavBar = City_Locators.RESTAURANTS_NAV_BAR
        self.activitiesNavBar = City_Locators.ACTIVITIES_NAV_BAR
        self.validationForRestNavBar = City_Locators.CATEGORY_NAME

        self.restaurantsMain = City_Locators.RESTAURANTS_MAIN_DIV
        self.hotelsMain = City_Locators.HOTELS_MAIN_DIV
        self.activitiesMain = City_Locators.ACTIVITIES_MAIN_DIV

    def city_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.validationForCityNavBar).get_attribute('textContent')

    def category_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.validationForRestNavBar).get_attribute('textContent')

    def navigate_to_hotels_nav_bar(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hotelsNavBar)))
        try:
            self.driver.find_element(By.XPATH, self.hotelsNavBar).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('navbar-link')[1].click()")
        Utils(self.driver).assertion('Hotels', self.category_name())

    def navigate_to_restaurants_nav_bar(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.restaurantsNavBar)))
        try:
            self.driver.find_element(By.XPATH, self.restaurantsNavBar).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('navbar-link')[2].click()")
        Utils(self.driver).assertion('Restaurants', self.category_name())

    def navigate_to_activities_nav_bar(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.activitiesNavBar)))
        try:
            self.driver.find_element(By.XPATH, self.activitiesNavBar).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('navbar-link')[3].click()")
        Utils(self.driver).assertion('Activities', self.category_name())

    def navigate_to_city_nav_bar(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cityNavBar)))
        try:
            self.driver.find_element(By.XPATH, self.cityNavBar).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('navbar-link')[0].click()")
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationForCityNavBar)))

    def view_all_restaurants(self):
        div = self.driver.find_element(By.XPATH, self.restaurantsMain)
        link = div.find_element(By.CLASS_NAME, 'slider-link')
        try:
            link.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[0].click()")
            self.wait.until(EC.url_to_be("https://trip-yoetz.herokuapp.com/restaurants"))

    def view_all_hotels(self):
        div = self.driver.find_element(By.XPATH, self.hotelsMain)
        link = div.find_element(By.CLASS_NAME, 'slider-link')
        try:
            link.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[2].click()")
            self.wait.until(EC.url_to_be("https://trip-yoetz.herokuapp.com/hotels"))

    def view_all_activities(self):
        div = self.driver.find_element(By.XPATH, self.activitiesMain)
        link = div.find_element(By.CLASS_NAME, 'slider-link')
        try:
            link.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[4].click()")
            self.wait.until(EC.url_to_be("https://trip-yoetz.herokuapp.com/activities"))

    def click_next_image_button_restaurants(self):
        div = self.driver.find_element(By.XPATH, self.restaurantsMain)
        button = div.find_element(By.CLASS_NAME, 'next-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('next-img-btn')[0]")

    def click_prev_image_button_restaurants(self):
        div = self.driver.find_element(By.XPATH, self.restaurantsMain)
        button = div.find_element(By.CLASS_NAME, 'prev-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('prev-img-btn')[0]")

    def click_next_image_button_hotels(self):
        div = self.driver.find_element(By.XPATH, self.hotelsMain)
        button = div.find_element(By.CLASS_NAME, 'next-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('next-img-btn')[1]")

    def click_prev_image_button_hotels(self):
        div = self.driver.find_element(By.XPATH, self.hotelsMain)
        button = div.find_element(By.CLASS_NAME, 'prev-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('prev-img-btn')[1]")

    def click_next_image_button_activities(self):
        div = self.driver.find_element(By.XPATH, self.activitiesMain)
        button = div.find_element(By.CLASS_NAME, 'next-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('next-img-btn')[2]")

    def click_prev_image_button_activities(self):
        div = self.driver.find_element(By.XPATH, self.activitiesMain)
        button = div.find_element(By.CLASS_NAME, 'prev-img-btn')
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('prev-img-btn')[2]")

    def restaurant_images(self):
        div = self.driver.find_element(By.XPATH, self.restaurantsMain)
        images = div.find_elements(By.CLASS_NAME, 'slider-card')

