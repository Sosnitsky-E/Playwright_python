class LoginPageLocators:
    LOGIN_EMAIL_FIELD = "#login-form-email-input"
    LOGIN_PASSWORD_FIELD = "input[name='password']"
    LOGIN_BUTTON = "[e2e-test-locator='login-button']"
    USER_WELCOME_TEXT = ".home__header-msg-title.ng-scope"
    PROFILE_USER_NAME = "span[class='top-nav-profile__name'] span[class='ng-binding']"


class ProjectPageLocators:
    TOOLS = "#toolsLink"
    LIBRARY = "//span[normalize-space()='Library']"
    UPLOAD_BUTTON = ".nx-button.nx-button--small.ng-scope"
    SAVE_BUTTON = "#saveBtn"
    FILE_ICON = ".nx-button.nx-button--small.ng-binding"
    MY_FILES_SECTION = ".nx-button.nx-button--small.ng-binding"
    FILES_LIST = "li"
