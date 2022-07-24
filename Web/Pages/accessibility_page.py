import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_accessibility import Locators_Accessibility

class Accessibility_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.mainButton = Locators_Accessibility.MAIN_BUTTON
        self.validationForMainButton = Locators_Accessibility.VALIDATION_MAIN_BUTTON
        self.listOfColors = Locators_Accessibility.COLORS_BUTTONS
        self.validationForColorButton = Locators_Accessibility.VALIDATION_COLOR_BUTTON

    @allure.step
    @allure.description_html('click on main button of accessibility that open the ruler with all the colors')
    def click_accessibility_main_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.mainButton)))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.mainButton)))
        self.driver.find_element(By.CSS_SELECTOR, self.mainButton).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.validationForMainButton)))

    @allure.step
    @allure.description_html('click on specific color from the list [1-4] every color begin with clicking main button ')
    def clicking_color(self, color_number: int):
        self.click_accessibility_main_button()
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.listOfColors)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.listOfColors+f'[{color_number}]')))
        color = self.driver.find_element(By.XPATH, self.listOfColors+f'[{color_number}]')
        color.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.validationForColorButton)))
        if color_number == 1:
            assert color.value_of_css_property(
                'background-image') == 'linear-gradient(120deg, rgb(0, 0, 0) 40%, rgb(245, 222, 179) 60%)'
        elif color_number == 2:
            assert color.value_of_css_property(
                'background-image') == 'linear-gradient(120deg, rgb(245, 203, 92) 40%, rgb(36, 36, 35) 60%)'
        elif color_number == 3:
            assert color.value_of_css_property(
                'background-image') == 'linear-gradient(120deg, rgb(20, 33, 61) 40%, rgb(152, 193, 217) 60%)'
        elif color_number == 4:
            assert color.value_of_css_property(
                'background-image') == 'linear-gradient(120deg, rgb(0, 0, 0) 40%, rgb(152, 150, 241) 60%)'
        else:
            raise ValueError('No Color in this Position')
