from behave import *
import requests

from blackbox_tests.lib.utils.constants import Constants, URL
from hamcrest import assert_that, contains_string, equal_to
from requests.exceptions import HTTPError

use_step_matcher("re")


@given("user send request to URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.request = requests.get(URL.PHP_TRAVELS)


@when("response is given back")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.request.status_code


@then("status code should be 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.response, equal_to(Constants.OK_RESPONSE))
