import pytest
from OOP.Base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from OOP.Pages.login_page import Login_Page
from OOP.Utils.utils_login import Utils

@pytest.mark.usefixtures('set_up')
class Test_Login(Base):

    # Login Successfully :
    def test_login_successfully(self):
        driver = self.driver
        login = Login_Page(driver)
        login.enter_email('Yosef@gmail.com')
        login.enter_password('123456')
        login.login_button()
        login.accept_alert()
        driver.refresh()
        WebDriverWait(driver, 20)
        compare = Utils(driver)
        compare.assertion(login.login_validation_message(), 'YOUR INFORMATION', 'LoginMessage.png')

    # Login When The Values in The Fields Are Invalid
    def test_login_invalid_fields_all_the_options(self):
        driver = self.driver
        login = Login_Page(driver)

        emails = ['Fasil', 'Yosef@', 'Miki@.com', '!!!!']
        passwords = ['5', '10', '100', '', '1115555']

        for i in range(len(emails)):
            for j in range(len(passwords)):
                login.enter_email(emails[i])
                login.enter_password(passwords[j])
                login.login_button()

                # Emails Messages:
                # Message 1:
                if "חסר '@' " in login.js_email():
                    assert login.js_email() == f"אני רוצה לכלול '@' בכתובת האימייל. ב-'{emails[i]}' חסר '@'."

                # Message 2:
                elif "אינו מלא" in login.js_email():
                    assert login.js_email() == f"יש להזין חלק ואחריו '@'. השדה '{emails[i]}' אינו מלא."

                # Message 3:
                elif "שגוי" in login.js_email():
                    invalid_email = emails[i]
                    for letter in range(len(invalid_email)):
                        if invalid_email[letter] == '@':
                            text_for_assertion = invalid_email[letter+1:]
                            assert login.js_email() == f"נעשה שימוש ב-'.' במיקום שגוי ב-'{text_for_assertion}'."

                # Password Messages:

                # Message 1:
                if len(passwords[j]) == 1:
                    assert login.js_password() == "עליך להאריך את הטקסט ל-4 תווים או יותר (כרגע יש תו אחד)."

                # Message 2:
                elif len(passwords[j]) in range(2, 4):
                    assert login.js_password() == f"צריך להאריך את הטקסט הזה" \
                                   f" ל-4 תווים או יותר (כרגע הוא באורך {len(passwords[j])} תווים)."

    # Login Incorrectly When The Email is Correct and The Password is Incorrect:
    def test_login_user_exist_and_incorrect_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.enter_email('Yosef@gmail.com')
        login.enter_password('walla-com')
        login.login_button()
        compare = Utils(driver)
        compare.assertion(login.email_or_password_error(), 'password or email incorrect', 'EmailPasswordMessage.png')

    # Login Incorrectly When The Email is Incorrect and The Password is Incorrect:
    def test_login_user_not_exist_and_incorrect_password(self):
        driver = self.driver
        login = Login_Page(driver)
        login.enter_email('Yvsvfvvfvf@gmail.com')
        login.enter_password('walla-com')
        login.login_button()
        compare = Utils(driver)
        compare.assertion(login.no_user_error_message(), 'no user found', 'NoUserMessage.png')

    # Navigate From Login Page To All The Pages In The Website:
    def test_nav_bar_links(self):
        driver = self.driver
        compare = Utils(driver)
        compare.navbar_links('Login')

    # Searching Correctly:
    def test_search_correctly(self):
        driver = self.driver
        search = Utils(driver)
        search.search_correctly('Jerusalem')

    # Searching Incorrectly:
    def test_search_incorrectly(self):
        driver = self.driver
        search = Utils(driver)
        search.search_incorrectly('Israel')
