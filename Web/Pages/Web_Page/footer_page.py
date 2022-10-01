from Web.Locators.Web_Locators.locators_footer import Footer_Locators
from Web.Pages.Web_Page.navbar_page import NavBar
from selenium.webdriver.support import expected_conditions as EC
from Web.Utils.utils import Utils
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

class Footer_Page(NavBar):
    def __init__(self, driver):
        super().__init__(driver)
        self.openFooterBtn = Footer_Locators.OPEN_FOOTER_BUTTON
        self.footerElement = Footer_Locators.FOOTER
        self.mainLogo = Footer_Locators.LOGO_DIV
        self.articleList = Footer_Locators.ARTICLES_LIST

    def click_on_who_are_we_button(self):
        footer_class_name = self.driver.find_element(By.XPATH, self.footerElement).get_attribute('className')
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.openFooterBtn)))
        button.click()

