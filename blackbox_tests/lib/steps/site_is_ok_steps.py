from behave import *
import urllib.request

from urllib.error import URLError, HTTPError
from blackbox_tests.lib.utils.constants import Constants, URL
from hamcrest import assert_that, contains_string, equal_to

use_step_matcher("re")


@given("user send request to URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.request = urllib.urlopen(URL.PHP_TRAVELS).getcode()
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    raise NotImplementedError(u'STEP: Given user send request to URL')


@when("response is given back")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.request
    raise NotImplementedError(u'STEP: When response is given back')


@then("status code should be 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.response, equal_to(Constants.OK_RESPONSE))
    raise NotImplementedError(u'STEP: Then status code should be 200')
