import allure
import pytest
from Web.Pages.register_page import Register_Page
from Web.Utils.utils import Utils
from Web.Test.conftest import Web_Fixtures

class Test_Register(Web_Fixtures):

    @allure.description('Navigate to login page correctly')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail(reason='section class name not change')
    def test_click_on_login_link(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.click_on_login_link()

    @allure.description('Register correctly')
    @pytest.mark.xfail(reason='birth date input os not valid')
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_correctly(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('Yos', 'Jan', '1995-10-10', 'gonathan45@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        register.accept_alert()
        Utils(driver).assertion('https://trip-yoetz.herokuapp.com/login', driver.current_url)

    @allure.description('Trying register incorrectly when user is exist')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_1(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('ces', 'ces', '1990-10-10', 'Yosef@gmail.com', 'NoImage', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion("user with that email already exists", register.user_already_exist_error())

    @allure.description('Trying register incorrectly when password fields are not the same')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_2(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('ces', 'ces', '1990-10-10', 'Yosef@gmail.com', 'NoImage', '123456', '654321')
        register.click_on_register_button()
        Utils(driver).assertion("passwords not matching", register.password_not_matching_error())

    @allure.description('Trying register incorrectly when first name is less than 2 characters')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_3(self):
        value = 'A'
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values(value, 'Avihu', '1990-10-01', 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion(
            'עליך להאריך את הטקסט ל-2 תווים או יותר (כרגע יש תו אחד).',
            register.error_message(register.enter_first_name(value), 'validationMessage'),
            'Please use at least 2 characters (you are currently using 1 characters).')

    @allure.description('Trying register incorrectly when first name is null')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_4(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('', 'Avihu', '1990-10-01', 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion(
            'זהו שדה חובה.',
            register.error_message(register.enter_first_name(''), 'validationMessage'),
            'Please fill out this field.')

    @allure.description('Trying register incorrectly when last name is less than 2 characters')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_5(self):
        value = 'N'
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('Avihu', value, '1990-10-01', 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion(
            'עליך להאריך את הטקסט ל-2 תווים או יותר (כרגע יש תו אחד).',
            register.error_message(register.enter_last_name(value), 'validationMessage'),
            'Please use at least 2 characters (you are currently using 1 characters).')

    @allure.description('Trying register incorrectly when last name is null')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_6(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('Avihu', '', '1990-10-01', 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion(
            'זהו שדה חובה.',
            register.error_message(register.enter_last_name(''), 'validationMessage'),
            'Please fill out this field.')

    @allure.description('Trying register incorrectly when birth date is greater than 01-01-2004')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_7(self):
        value = '2005-01-01'
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('Avihu', 'Natan', value, 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion('על הערך להיות 01/01/2004 או מוקדם יותר.',
                                register.error_message(register.enter_date(value), 'validationMessage'),
                                'Please select a value that is no later than 2004-01-01.')

    @allure.description('Trying register incorrectly when birth date is less than 01-01-1902')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_register_incorrectly_8(self):
        value = '1800-01-01'
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.enter_register_values('Avihu', 'Natan', value, 'Naw2@gmail.com', 'None', '123456', '123456')
        register.click_on_register_button()
        Utils(driver).assertion('על הערך להיות 01/01/1902 ומעלה.',
                                register.error_message(register.enter_date(value), 'validationMessage'),
                                'Please select a value that is no earlier than 1902-01-01.')
