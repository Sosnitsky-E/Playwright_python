from pages.login_page import LoginPage


class TestLoginPage:

    def test_tc_001_001_test_successful_login_with_valid_credentials(self, page, login):
        """ The test verifies that the user is logged in."""
        login_page = LoginPage(page, page.url)
        login_page.check_user_is_logged_in()
