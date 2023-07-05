

from pages.base_page import BasePage
from .credentials import login_data, user_data
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def fill_email_login_field(self):
        self.fill_the_field_by_locator(LoginPageLocators.LOGIN_EMAIL_FIELD, login_data["valid_email"])

    def fill_password_login_field(self):
        self.fill_the_field_by_locator(LoginPageLocators.LOGIN_PASSWORD_FIELD, login_data["valid_password"])

    def login_button_click(self):
        self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()

    def check_user_is_logged_in(self):
        welcome_text = self.page.wait_for_selector(LoginPageLocators.USER_WELCOME_TEXT).text_content()
        # using explicit wait for welcome text
        profile_user_name = self.page.locator(LoginPageLocators.PROFILE_USER_NAME).text_content()
        assert user_data["first_name"] in welcome_text, "The user is not logged in"
        assert profile_user_name == f'{user_data["first_name"]} {user_data["second_name"]}', "The user is not logged in"
