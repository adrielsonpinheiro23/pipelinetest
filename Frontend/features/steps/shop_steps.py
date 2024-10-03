from behave import step
from nose.tools import assert_true, assert_false, assert_equal


@step(u'I insert all the products in the cart')
def step_impl(context):
    context.home_page.reset_app_status()
    context.home_page.select_all_products()
    context.home_page.click_cart_shop()

@step(u'Finish the checkout to payment with names "{firstName}" and "{lastName}" with zip code "{zipCode}"')
def step_impl(context, firstName, lastName, zipCode):
    context.home_page.click_checkout()
    context.home_page.fill_checkout_info(firstName, lastName, zipCode)
    context.home_page.click_continue_checkout()

@step(u'I check the amount of "{amount}" and click Finish')
def step_impl(context, amount):
    assert_equal(context.home_page.check_amount(), amount)
    context.home_page.click_finish()

@step(u'I receive a notification of success')
def step_impl(context):
    success_message = context.home_page.check_success_message()
    assert_equal(success_message, "Thank you for your order!")

@step(u'I click on Back Home to return to "{page}" Page')
def step_impl(context, page):
    context.home_page.click_back_to_product()
    assert_true(context.home_page.is_on_screen(page))

@step(u'I remove the "{product}" products')
def step_impl(context, product):
    context.home_page.remove_product_test_t_shirt()
    context.home_page.remove_product_bolt_t_shirt()
    assert_false(context.home_page.is_on_screen(product))

@step(u'I return to "{page}" Page and remove the "{product}" product')
def step_impl(context, page, product):
    context.home_page.continue_shopping()
    assert_true(context.home_page.is_on_screen(page))
    context.home_page.remove_product_back_pack()
    context.home_page.click_cart_shop()
    assert_false(context.home_page.is_on_screen(product))




