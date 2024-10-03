import os
import sys

from lib.browser import Browser
from pages.home_page import HomePage
from pages.login_page import LoginPage


def before_all(context):
    if 'win64' in sys.platform:
        context.screenshot_path = f"{os.getcwd()}\\screenshots\\"
    elif 'linux' in sys.platform:
        context.screenshot_path = f"{os.getcwd()}/screenshots/"


def before_feature(context, feature):
    headless = True if 'headless' in context.config.userdata and context.config.userdata['headless'] == 'True' else False
    mobile = True if 'mobile' in context.config.userdata and context.config.userdata['mobile'] == 'True' else False
    browser = 'chrome' if 'browser' in context.config.userdata and context.config.userdata['browser'] == 'chrome' else 'firefox'
    context.browser = Browser(browser=browser, headless=headless, mobile=mobile)
    context.home_page = HomePage(context.browser)
    context.login_page = LoginPage(context.browser)


def after_feature(context, feature):
    context.browser.close()
