from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Web.Locators.locators_about_us import Locators_AboutUs
from Web.Utils.utils import Utils

class AboutUs_Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.MapIframe = Locators_AboutUs.MAP_IFRAME
        self.googleMapLink = Locators_AboutUs.GOOGLE_MAPS_LINK
        self.UI = Locators_AboutUs.UI

    @allure.step
    @allure.description('Navigate to about-us page')
    def about_us_page(self):
        url = 'https://trip-yoetz.herokuapp.com/about'
        self.driver.get(url)
        Utils(self.driver).assertion(url, self.driver.current_url)
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('Validation - returns all the text in the page')
    def ui(self):
        return self.driver.find_element(*self.UI).get_attribute('innerText')

    @allure.step
    @allure.description('Using Iframe - clicking on google maps link')
    def google_maps(self):
        iframe = self.driver.find_element(*self.MapIframe)
        self.driver.switch_to.frame(iframe)
        link = self.driver.find_element(*self.googleMapLink)
        link.click()
        Utils(self.driver).assertion(2, len(self.driver.window_handles))
        google_maps_page = self.driver.window_handles[1]
        self.driver.switch_to.window(google_maps_page)
        self.wait.until(EC.url_to_be(
            "https://www.google.com/maps?ll=31.95411,34.891011&z=17&t=m&hl=iw&gl=IL&mapclient=embed"))
