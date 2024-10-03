from selenium.webdriver.common.by import By

class LoginPageLocator:
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def check_logged_out(self):
        login_button_element = self.browser.wait_for_element(*LoginPageLocator.login_button)
        ret = login_button_element
        return ret

    def fill_login_fields(self, enter_user, enter_password):
        self.insert_user(enter_user)
        self.insert_password(enter_password)

    def insert_user(self, username):
        self.browser.wait_and_clear(*LoginPageLocator.username_field)
        self.browser.wait_and_fill(username, *LoginPageLocator.username_field)

    def insert_password(self, password):
        self.browser.wait_and_fill(password, *LoginPageLocator.password_field)

    def submit_login(self):
        self.browser.wait_and_click(*LoginPageLocator.login_button)
