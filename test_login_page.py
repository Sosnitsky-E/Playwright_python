from pages.login_page import LoginPage


class TestLoginPage:

    def test_tc_001_001_test_successful_login_with_valid_credentials(self, page):
        """ The test verifies that the user is logged in."""
        link = "https://www.honeybook.com/app/login"
        login_page = LoginPage(page, link)
        login_page.open_web_page()
        login_page.fill_email_login_field()
        login_page.fill_password_login_field()
        login_page.login_button_click()
        login_page.check_user_is_logged_in()

    def test_credentials(self, page, login):
        """ The test verifies that the user is logged in."""
        login_page = LoginPage(page, page.url)
        login_page.check_user_is_logged_in()



