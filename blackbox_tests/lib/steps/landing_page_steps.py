import time

from behave import *
from hamcrest import assert_that, contains_string, equal_to

from blackbox_tests.lib.page_objects.landing_page import LandingPage
from blackbox_tests.lib.utils.constants import Constants

use_step_matcher("re")


@when("user open landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.landing_page = LandingPage(context)
    time.sleep(3)


@then("user should be able to see landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.landing_page.landing_page_title.text, equal_to(Constants.TITLE))


@step('the navigation bar should include the following "(?P<column>.+)"')
def step_impl(context, column):
    """
    :type context: behave.runner.Context
    :type column: str
    """
    raise NotImplementedError(u'STEP: And the navigation bar should include the following "<column>"')


@step('I choose "(?P<option>.+)" tab')
def step_impl(context, option):
    """
    :type context: behave.runner.Context
    :type option: str
    """
    raise NotImplementedError(u'STEP: And I choose "<option>" tab')


@step('I select "(?P<pick_up>.+)" and "(?P<drop_off>.+)" location')
def step_impl(context, pick_up, drop_off):
    """
    :type context: behave.runner.Context
    :type pick_up: str
    :type drop_off: str
    """
    raise NotImplementedError(u'STEP: And I select "<pick_up>" and "<drop_off>" location')


@step("I search query")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I search query')


@then('I should be able to see notification "(?P<message>.+)"')
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    raise NotImplementedError(u'STEP: Then I should be able to see notification "<message>"')
