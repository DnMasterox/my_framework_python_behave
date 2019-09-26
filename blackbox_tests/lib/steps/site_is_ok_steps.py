from behave import *
import requests

from blackbox_tests.lib.utils.constants import Constants, URL
from hamcrest import assert_that, contains_string, equal_to
from requests.exceptions import HTTPError

use_step_matcher("re")


def catch_all(func):
    """If that's a common pattern, just write own decorator for handling exceptions"""

    def wrapper(context, *args, **kwargs):
        try:
            func(context, *args, **kwargs)
            context.exc = None
        except HTTPError as e:
            context.exc = e

    return wrapper


@given("user send request to URL")
@catch_all
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.request = requests.get(URL.PHP_TRAVELS)


@when("response is given back")
@catch_all
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.request.status_code


@then("status code should be 200")
@catch_all
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.response, equal_to(Constants.OK_RESPONSE))
