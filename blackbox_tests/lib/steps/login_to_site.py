import time
from behave import *

from blackbox_tests.lib.page_objects.landing_page import LandingPage
from blackbox_tests.lib.page_objects.login_page import LoginPage
from blackbox_tests.lib.utils.constants import Constants, URL
from hamcrest import assert_that, contains_string, equal_to

use_step_matcher("re")


@given("user navigates to the URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = LoginPage(context)
    time.sleep(4)


@when('user logs in')
def step_impl(context):
    """
    :type context: behave.runner.Context
    :type user: str
    """
    assert_that(context.login_page.title_panel.text, equal_to(Constants.PAGENAME))
    context.login_page.login(username=Constants.USER_MAIL, password=Constants.USER_PASSWORD)
    time.sleep(3)


@then("user should be able to see profile page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.login_page.browser.current_url, contains_string(URL.PHP_TRAVELS_ACCOUNT))
