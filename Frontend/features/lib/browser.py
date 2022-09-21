import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser(object):
    def __init__(self, browser='chrome', headless=False, mobile=False):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--no-sandbox")
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--enable-automation")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--lang=en')
        if browser == 'chrome':
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            self.driver = webdriver.Firefox(options=options)
        if mobile:
            self.driver.set_window_size(390, 844)
        elif headless:
            self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(30)
        if not mobile:
            self.driver.maximize_window()

    def back(self):
        self.driver.back()

    def close(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def get_error_message(self, *locator):
        return self.wait(locator).text

    def get_element(self, *locator):
        w = None
        try:
            w = self.driver.find_element(*locator)
        except:
            pass
        return w

    def get_input_text(self, *locator):
        w = self.get_element(*locator)
        return w.get_attribute("value")

    def get_page_title(self):
        time.sleep(2)
        return self.driver.title

    def navigate(self, address):
        self.driver.get(address)

    def press_enter(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def select_option(self, text, *locator, timeout=3):
        select = Select(self.wait(locator, timeout))
        select.select_by_visible_text(text)

    def wait(self, locator, timeout=3):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        time.sleep(0.4)
        return element

    def wait_and_clear(self, *locator, timeout=3):
        self.wait(locator, timeout).clear()

    def wait_and_click(self, *locator, timeout=3):
        self.wait(locator, timeout).click()

    def wait_and_fill(self, text, *locator, timeout=3):
        self.wait(locator, timeout).send_keys(text)
