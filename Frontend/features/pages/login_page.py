from selenium.webdriver.common.by import By


class LoginPageLocator:
    email_field = (By.ID, 'user_email')
    password_field = (By.ID, 'user_password')
    sign_in_button = (By.XPATH, '//*[@id="new_user"]/input')


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_login_fields(self, enter_email, enter_password):
        self.insert_email(enter_email)
        self.insert_password(enter_password)

    def insert_email(self, username):
        self.browser.wait_and_clear(*LoginPageLocator.email_field)
        self.browser.wait_and_fill(username, *LoginPageLocator.email_field)

    def insert_password(self, password):
        self.browser.wait_and_fill(password, *LoginPageLocator.password_field)

    def submit_login(self):
        page_locator = (By.XPATH, f'//*[contains(text(), "Signed in successfully.")]')
        self.browser.wait_and_click(*LoginPageLocator.sign_in_button)
        self.browser.wait(page_locator, timeout=15)
