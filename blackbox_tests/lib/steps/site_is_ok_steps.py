from behave import *

use_step_matcher("re")


@given("user send request to URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given user send request to URL')


@when("response is given back")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When response is given back')


@then("status code should be 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then status code should be 200')