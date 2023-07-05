import pytest

from pages.credentials import login_data
from pages.locators import LoginPageLocators


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """browser context changing"""
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


# @pytest.fixture()
# def page(playwright):
#     chromium = playwright.chromium
#     browser = chromium.launch()
#     page = browser.new_page()
#     yield
#     browser.close()


@pytest.fixture(scope="function")
def login(page):
    """User login"""
    link = "https://www.honeybook.com/app/login"
    page.goto(link)
    page.locator(LoginPageLocators.LOGIN_EMAIL_FIELD).click()
    page.locator(LoginPageLocators.LOGIN_EMAIL_FIELD).fill(login_data["valid_email"])
    page.locator(LoginPageLocators.LOGIN_PASSWORD_FIELD).click()
    page.locator(LoginPageLocators.LOGIN_PASSWORD_FIELD).fill(login_data["valid_password"])
    page.locator(LoginPageLocators.LOGIN_BUTTON).click()
