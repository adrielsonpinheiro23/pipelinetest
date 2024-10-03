from behave import step
from nose.tools import assert_true, assert_equal


@step(u'I navigate to sauce demo page')
def step_impl(context):
    context.browser.get_driver().delete_all_cookies()
    context.browser.navigate('https://www.saucedemo.com/')

@step(u'I insert username as "{user}" and password as "{password}" and click login')
def step_impl(context, user, password):
    context.login_page.fill_login_fields(user, password)
    context.login_page.submit_login()

@step(u'I click to Logout')
def step_impl(context):
    context.home_page.logout()
    assert_true(context.login_page.check_logged_out())

@step(u'I am successfully logged in')
def step_impl(context):
    logged_in_text = context.home_page.check_logged_in()
    assert_equal(logged_in_text, "Logout")
    context.home_page.close_hamburger()

@step(u'I am not logged in due locked user error message')
def step_impl(context):
    locked_user_error = context.home_page.check_error_login()
    assert_equal(locked_user_error, "Epic sadface: Sorry, this user has been locked out.")

@step(u'I am not logged in due invalid user or password error message')
def step_impl(context):
    invalid_user_error = context.home_page.check_error_login()
    assert_equal(invalid_user_error, "Epic sadface: Username and password do not match any user in this service")
