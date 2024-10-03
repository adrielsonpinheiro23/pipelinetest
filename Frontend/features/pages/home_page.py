from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import re
import time

class HomePageLocator:
    add_bolt_t_shirt_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_backpack_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_bike_light_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_fleece_jacket_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    add_onesie_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-onesie')
    add_test_t_shirt_to_cart_button = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    amount_text = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    back_to_product_button = (By.ID, 'back-to-products')
    cart_shop_button = (By.ID, 'shopping_cart_container')
    checkout_button = (By.ID, 'checkout')
    close_hamburger_button = (By.ID, 'react-burger-cross-btn')
    continue_checkout_button = (By.ID, 'continue')
    continue_shopping_button = (By.ID, 'continue-shopping')
    finish_button = (By.ID, 'finish')
    finish_success_message = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
    first_name_form = (By.ID, 'first-name')
    hamburger_menu = (By.ID, 'react-burger-menu-btn')
    last_name_form = (By.ID, 'last-name')
    login_error_message = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    logout_button = (By.ID, 'logout_sidebar_link')
    remove_backpack_to_cart_button = (By.ID, 'remove-sauce-labs-backpack')
    remove_bike_light_to_cart_button = (By.ID, 'remove-sauce-labs-bike-light')
    remove_bolt_t_shirt_to_cart_button = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
    remove_fleece_jacket_to_cart_button = (By.ID, 'remove-sauce-labs-fleece-jacket')
    remove_onesie_to_cart_button = (By.ID, 'remove-sauce-labs-onesie')
    remove_test_t_shirt_to_cart_button = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
    reset_app_state_button = (By.ID, 'reset_sidebar_link')
    zip_code_form = (By.ID, 'postal-code')

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def check_logged_in(self):
        self.browser.wait_and_click(*HomePageLocator.hamburger_menu)
        logout_button_element = self.browser.wait_for_element(*HomePageLocator.logout_button)
        ret = logout_button_element.text
        return ret

    def check_error_login(self):
        self.browser.wait_and_click(*HomePageLocator.login_error_message)
        error_message_element = self.browser.wait_for_element(*HomePageLocator.login_error_message)
        ret = error_message_element.text
        return ret

    def check_success_message(self):
        success_message_element = self.browser.wait_for_element(*HomePageLocator.finish_success_message)
        ret = success_message_element.text
        return ret

    def check_amount(self):
        amount_element = self.browser.wait_for_element(*HomePageLocator.amount_text)
        ret = amount_element.text
        number = "".join(re.findall("[0-9].+", ret))
        return number

    def check_tex_on_screen(self, text):
        page_locator = (By.XPATH, f'//*[contains(text(), "{text}")]')
        try:
            self.browser.wait(page_locator)
            return True
        except TimeoutException:
            return False

    def click_cart_shop(self):
        self.browser.wait_and_click(*HomePageLocator.cart_shop_button)

    def click_checkout(self):
        self.browser.wait_and_click(*HomePageLocator.checkout_button)

    def click_continue_checkout(self):
        self.browser.wait_and_click(*HomePageLocator.continue_checkout_button)

    def click_finish(self):
        self.browser.wait_and_click(*HomePageLocator.finish_button)

    def click_back_to_product(self):
        self.browser.wait_and_click(*HomePageLocator.back_to_product_button)

    def close_hamburger(self):
        self.browser.wait_and_click(*HomePageLocator.close_hamburger_button)

    def continue_shopping(self):
        self.browser.wait_and_click(*HomePageLocator.continue_shopping_button)

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.browser.wait_and_fill(first_name, *HomePageLocator.first_name_form)
        self.browser.wait_and_fill(last_name, *HomePageLocator.last_name_form)
        self.browser.wait_and_fill(zip_code, *HomePageLocator.zip_code_form)

    def is_on_screen(self, message):
        page_locator = (By.XPATH, f'//*[contains(text(), "{message}")]')
        try:
            self.browser.wait(page_locator)
            return True
        except TimeoutException:
            return False

    def logout(self):
        self.browser.wait_and_click(*HomePageLocator.hamburger_menu)
        self.browser.wait_and_click(*HomePageLocator.logout_button)

    def remove_product_back_pack(self):
        self.browser.wait_and_click(*HomePageLocator.remove_backpack_to_cart_button)

    def remove_product_bike_light(self):
        self.browser.wait_and_click(*HomePageLocator.remove_bike_light_to_cart_button)

    def remove_product_fleece_jacket(self):
        self.browser.wait_and_click(*HomePageLocator.remove_fleece_jacket_to_cart_button)

    def remove_product_onesie(self):
        self.browser.wait_and_click(*HomePageLocator.remove_onesie_to_cart_button)

    def remove_product_bolt_t_shirt(self):
        self.browser.wait_and_click(*HomePageLocator.remove_bolt_t_shirt_to_cart_button)

    def remove_product_test_t_shirt(self):
        self.browser.wait_and_click(*HomePageLocator.remove_test_t_shirt_to_cart_button)

    def reset_app_status(self):
        self.browser.wait_and_click(*HomePageLocator.hamburger_menu)
        self.browser.wait_and_click(*HomePageLocator.reset_app_state_button)
        self.browser.refresh()

    def select_product_back_pack(self):
        self.browser.wait_and_click(*HomePageLocator.add_backpack_to_cart_button)

    def select_product_bike_light(self):
        self.browser.wait_and_click(*HomePageLocator.add_bike_light_to_cart_button)

    def select_product_fleece_jacket(self):
        self.browser.wait_and_click(*HomePageLocator.add_fleece_jacket_to_cart_button)

    def select_product_onesie(self):
        self.browser.wait_and_click(*HomePageLocator.add_onesie_to_cart_button)

    def select_product_bolt_t_shirt(self):
        self.browser.wait_and_click(*HomePageLocator.add_bolt_t_shirt_to_cart_button)

    def select_product_test_t_shirt(self):
        self.browser.wait_and_click(*HomePageLocator.add_test_t_shirt_to_cart_button)

    def select_all_products(self):
        self.select_product_test_t_shirt()
        self.select_product_onesie()
        self.select_product_fleece_jacket()
        self.select_product_bike_light()
        self.select_product_back_pack()
        self.select_product_bolt_t_shirt()

    def wait_message_appears(self, ret, *message):
        cont = 5
        while (ret == None) and (cont > 0):
            ret = self.browser.get_element(*message).text
            time.sleep(1)
            cont -= 1
        return ret
