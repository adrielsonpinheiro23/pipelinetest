from behave import step
from nose.tools import assert_true, assert_false, assert_equal, assert_not_equal


@step(u'I navigate to todo app page')
def step_impl(context):
    context.browser.get_driver().delete_all_cookies()
    context.browser.navigate('https://qa-test.avenuecode.io/users/sign_in')


@step(u'I insert email as "{email}" and password as "{password}" and click sign in')
def step_impl(context, email, password):
    context.login_page.fill_login_fields(email, password)
    context.login_page.submit_login()


@step(u'I see welcome message for "{user_first_name}" is displayed')
def step_impl(context, user_first_name):
    assert_equal(context.home_page.get_welcome_message_content(), f'Hey {user_first_name}, this is your todo list for today:')


@step(u'I have clicked on My tasks')
def step_impl(context):
    context.home_page.click_my_tasks()


@step(u'I am on QA Assessment page')
def step_impl(context):
    assert_equal(context.browser.get_page_title(), "QA Assessment")


@step(u'I create a task named "{task_name}"')
def step_impl(context, task_name):
    context.home_page.create_task(task_name)


@step(u'I create a task named "{task_name}" by pressing enter')
def step_impl(context, task_name):
    context.home_page.create_task_with_enter(task_name)


@step(u'I click the button Manage Subtasks')
def step_impl(context):
    context.home_page.click_manage_subtasks()


# TODO: This will fail due bug 901
@step(u'I check if task name on modal is editable')
def step_impl(context):
    assert_false(context.home_page.is_task_name_field_editable())


@step(u'I create a subtask with description as "{subtask_title}"')
def step_impl(context, subtask_title):
    context.home_page.fill_subtasks(subtask_title)
    context.home_page.click_add_subtasks()


@step(u'I close the modal')
def step_impl(context):
    context.home_page.close_subtask_modal()


@step(u'I can see there are "{number_of_subtasks}" subtasks created')
def step_impl(context, number_of_subtasks):
    assert_equal(context.home_page.get_amount_of_subtasks(), number_of_subtasks)


@step(u'I create a task with more than 250 characters by pressing enter')
def step_impl(context):
    task_content = 'Video provides a powerful way to help you prove your point. ' \
                   'By clicking Online Video, you can paste the embed code of the video you want to add. ' \
                   'You can also enter a keyword to search online for the most important videos. ' \
                   'Maybe this can work fine, or not'
    context.home_page.create_task_with_enter(task_content)


@step(u'I am able to see until the 250th character of the task on the list and remove it')
def step_impl(context):
    task_content_with_250_char = 'Video provides a powerful way to help you prove your point. ' \
                   'By clicking Online Video, you can paste the embed code of the video you want to add. ' \
                   'You can also enter a keyword to search online for the most important videos. ' \
                   'Maybe this can work fine, or'
    assert_equal(context.home_page.get_task_name_content(), task_content_with_250_char)
    context.home_page.remove_task()


@step(u'I am able to see the task "{task_name}" on the list and remove it')
def step_impl(context, task_name):
    context.home_page.check_task(task_name)
    context.home_page.remove_task()


@step(u'I am able to see the in the task the button "{text}"')
def step_impl(context, text):
    context.home_page.is_on_task_screen(text)
    context.home_page.remove_task()


@step(u'I sign out the application')
def step_impl(context):
    context.home_page.sign_out()
