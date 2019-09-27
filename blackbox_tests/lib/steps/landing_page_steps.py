from behave import *
from hamcrest import assert_that, is_in, equal_to, has_item, contains_string

from blackbox_tests.lib.page_objects.landing_page import LandingPage
from blackbox_tests.lib.utils.constants import Constants, URL

use_step_matcher("re")


@when("user opens landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.landing_page = LandingPage(context)


@then("user should be able to see landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.landing_page.browser.current_url, contains_string(URL.PHP_TRAVELS))


@step('the navigation bar should include the following "(?P<column>.+)"')
def step_impl(context, column):
    """
    :type context: behave.runner.Context
    :type column: str
    """
    context.text_columns = [context.landing_page.hotels_column.text,
                            context.landing_page.flights_column.text,
                            context.landing_page.tours_column.text,
                            context.landing_page.cars_column.text]
    assert_that(context.text_columns, has_item(column))
