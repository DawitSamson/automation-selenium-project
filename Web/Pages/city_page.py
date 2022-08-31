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
        self.cityOption = City_Locators.CITY_OPTION
        self.hotelsOption = City_Locators.HOTELS_OPTION
        self.restaurantsOption = City_Locators.RESTAURANTS_OPTION
        self.activitiesOption = City_Locators.ACTIVITIES_OPTION
        self.validationForNavBarList = City_Locators.VALIDATION_FOR_NAVBAR_LIST_OPTION
        self.validationForCityOption = City_Locators.VALIDATION_FOR_CITY_OPTION
        self.hotelsSlider = City_Locators.HOTELS_SLIDER
        self.restaurantsSlider = City_Locators.RESTAURANTS_SLIDER
        self.activitiesSlider = City_Locators.ACTIVITIES_SLIDER
        self.nextImageButtonEat = City_Locators.NEXT_IMAGE_BUTTON_EAT
        self.prevImageButtonEat = City_Locators.PREV_IMAGE_BUTTON_EAT

    @allure.step
    @allure.description('Clicking on option from navbar list and handle element interrupted error')
    def click_on_option_from_navbar_list(self, option_name):
        if option_name == 'city':
            option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cityOption)))
            try:
                option.click()
            except ElementClickInterceptedException:
                self.driver.execute_script('document.getElementsByClassName("navbar-link")[0].click()')
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.validationForCityOption)))
        elif option_name == 'hotels':
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hotelsOption)))
                self.driver.find_element(By.XPATH, self.hotelsOption).click()
            except ElementClickInterceptedException:
                self.driver.execute_script('document.getElementsByClassName("navbar-link")[1].click()')
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationForNavBarList)))
        elif option_name == 'restaurants':
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.restaurantsOption)))
                self.driver.find_element(By.XPATH, self.restaurantsOption).click()
            except ElementClickInterceptedException:
                self.driver.execute_script('document.getElementsByClassName("navbar-link")[2].click()')
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationForNavBarList)))
        elif option_name == 'activities':
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.activitiesOption)))
                self.driver.find_element(By.XPATH, self.activitiesOption).click()
            except ElementClickInterceptedException:
                self.driver.execute_script('document.getElementsByClassName("navbar-link")[3].click()')
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationForNavBarList)))

    @allure.step
    @allure.description('click on view all link - should navigate to restaurants page')
    def click_restaurants_slider(self):
        restaurants = self.driver.find_element(By.XPATH, self.restaurantsSlider)
        h1 = restaurants.find_element(By.TAG_NAME, 'h1')
        a = restaurants.find_element(By.TAG_NAME, 'a')
        Utils(self.driver).assertion('Eat', h1.get_attribute('textContent'))
        try:
            a.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[0].click()")
        self.wait.until(EC.url_to_be('https://trip-yoetz.herokuapp.com/restaurants'))

    @allure.step
    @allure.description('click on view all link - should navigate to hotels page')
    def click_hotels_slider(self):
        restaurants = self.driver.find_element(By.XPATH, self.hotelsSlider)
        h1 = restaurants.find_element(By.TAG_NAME, 'h1')
        a = restaurants.find_element(By.TAG_NAME, 'a')
        Utils(self.driver).assertion('Stay', h1.get_attribute('textContent'))
        try:
            a.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[1].click()")
        self.wait.until(EC.url_to_be('https://trip-yoetz.herokuapp.com/hotels'))

    @allure.step
    @allure.description('click on view all link - should navigate to activities page')
    def click_activities_slider(self):
        restaurants = self.driver.find_element(By.XPATH, self.activitiesSlider)
        h1 = restaurants.find_element(By.TAG_NAME, 'h1')
        a = restaurants.find_element(By.TAG_NAME, 'a')
        Utils(self.driver).assertion('Do', h1.get_attribute('textContent'))
        try:
            a.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementsByClassName('slider-link')[2].click()")
        self.wait.until(EC.url_to_be('https://trip-yoetz.herokuapp.com/activities'))

    @allure.step
    @allure.description('click on next image button')
    def click_next_image_button_eat(self):
        prev_button = self.driver.find_element(By.XPATH, self.prevImageButtonEat)
        next_button = self.driver.find_element(By.XPATH, self.nextImageButtonEat)
        try:
            next_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(f'$x({self.nextImageButtonEat}[0].click())')
        Utils(self.driver).assertion(False, prev_button.get_attribute('disabled'))

    @allure.step
    @allure.description('Validation- city name')
    def city_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.validationForCityOption).get_attribute('textContent')

    @allure.step
    @allure.description('Validation- category name of the option ')
    def category_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.validationForNavBarList).get_attribute('textContent')