from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import re
import time


class HomePageLocator:
    add_subtask_button = (By.ID, 'add-subtask')
    add_task_button = (By.XPATH, '//*[@id="new_task"]/../span')
    close_subtask_modal_button = (By.XPATH, '//*[@id="add-subtask"]/../../../../../../div[3]/button')
    content_manage_subtask_button = (By.XPATH, '//*[@id="new_task"]/../../../../div[2]/div[2]/table/tbody/tr/td[4]/button')
    edit_task_field = (By.XPATH, '//*[@id="edit_task"]')
    manage_subtask_button = (By.XPATH, '//*[@id="new_task"]/../../../../div[2]/div[2]/table/tbody/tr/td[4]')
    my_tasks_button = (By.ID, 'my_task')
    remove_task_button = (By.XPATH, '(//*[contains(text(), "Remove")])[2]')
    sign_out_button = (By.XPATH, '//*[contains(text(), "Sign out")]')
    subtask_field = (By.ID, 'new_sub_task')
    task_content_area = (By.XPATH, '//*[@id="new_task"]/../../../../../../div[1]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/a/text()')
    task_field = (By.ID, 'new_task')
    welcome_message = (By.XPATH, '//*[@id="new_task"]/../../../../../../div[1]/h1')


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def check_task(self, task_name):
        page_locator = (By.XPATH, f'//*[contains(text(), "{task_name}")]')
        try:
            self.browser.wait(page_locator)
            return True
        except TimeoutException:
            return False

    def click_manage_subtasks(self):
        self.browser.wait_and_click(*HomePageLocator.manage_subtask_button)

    def click_my_tasks(self):
        self.browser.wait_and_click(*HomePageLocator.my_tasks_button)

    def create_task(self, task_name):
        self.browser.wait_and_fill(task_name, *HomePageLocator.task_field)
        self.browser.wait_and_click(*HomePageLocator.add_task_button)

    def create_task_with_enter(self, task_name):
        self.browser.wait_and_fill(task_name, *HomePageLocator.task_field)
        self.browser.press_enter()

    def click_add_subtasks(self):
        self.browser.wait_and_click(*HomePageLocator.add_subtask_button)

    def close_subtask_modal(self):
        self.browser.wait_and_click(*HomePageLocator.close_subtask_modal_button)

    def fill_subtasks(self, subtask_title):
        self.browser.wait_and_fill(subtask_title, *HomePageLocator.subtask_field)

    def get_amount_of_subtasks(self):
        ret = self.browser.get_element(*HomePageLocator.content_manage_subtask_button).text
        amount_of_subtasks = str("".join(re.findall("\d+", ret)))
        return amount_of_subtasks

    def get_task_name_content(self):
        ret = self.browser.get_element(*HomePageLocator.task_content_area).text
        return self.wait_message_appears(ret, *HomePageLocator.task_content_area)

    def get_welcome_message_content(self):
        ret = self.browser.get_element(*HomePageLocator.welcome_message).text
        return self.wait_message_appears(ret, *HomePageLocator.welcome_message)

    def is_on_task_screen(self, message):
        page_locator = (By.XPATH, f'//*[contains(text(), "{message}")]')
        try:
            self.browser.wait(page_locator)
            return True
        except TimeoutException:
            return False

    def is_task_name_field_editable(self):
        return self.browser.get_element(*HomePageLocator.edit_task_field).is_enabled()

    def remove_task(self):
        self.browser.wait_and_click(*HomePageLocator.remove_task_button)

    def sign_out(self):
        page_locator = (By.XPATH, f'//*[contains(text(), "Signed out successfully.")]')
        self.browser.wait_and_click(*HomePageLocator.sign_out_button)
        self.browser.wait(page_locator, timeout=20)

    def wait_message_appears(self, ret, *message):
        cont = 5
        while (ret == None) and (cont > 0):
            ret = self.browser.get_element(*message).text
            time.sleep(1)
            cont -= 1
        return ret
