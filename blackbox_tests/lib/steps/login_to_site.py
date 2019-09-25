import time
from behave import *

from blackbox_tests.lib.page_objects.login import LoginPage
from blackbox_tests.lib.utils.constants import Constants, URL
from hamcrest import assert_that, contains_string, equal_to


# use_step_matcher("re")


@given("user navigates to the URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = LoginPage(context)
    assert_that(context.login_page.browser.current_url, contains_string(URL.PHP_TRAVELS))
    assert_that(context.login_page.username.get_attribute('autocomplete'), equal_to(Constants.USER_MAIL))
    time.sleep(4)


@when('user logs in')
def step_impl(context):
    """
    :type context: behave.runner.Context
    :type user: str
    """
    context.timeline_page = context.login_page.login(username=Constants.USER_MAIL, password=Constants.USER_PASSWORD)
    time.sleep(3)
    assert_that(context.timeline_page.avatar.get_attribute('title'), equal_to("Profile and settings"))


@then("user should be able to see landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.timeline_page.view_latest_tweets(search=True)
    time.sleep(3)
    # assert_that(context.timeline_page.browser.current_url, contains_string(Constants.TWEETS))

    # @step('the navigation bar should include the following "(?P<columns>.+)":')
    # def step_impl(context, columns):
    """
    :type context: behave.runner.Context
    :type columns: str
    """
