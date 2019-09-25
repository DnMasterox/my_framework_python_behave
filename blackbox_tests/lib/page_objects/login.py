from __future__ import unicode_literals

from blackbox_tests.lib.locators.login import LoginLocators
from blackbox_tests.lib.page_objects.base_page import BasePage
from blackbox_tests.lib.page_objects.Php_Travel import TwitterTimeline
from blackbox_tests.lib.utils.constants import URL


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self,
                          context.browser,
                          )
        self.context = context
        self.base_url = URL.PHP_TRAVELS
        self.visit(url=self.base_url)

    locator_dictionary = LoginLocators.__dict__

    def login(self, username='', password=''):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit_btn.click()
        return TwitterTimeline(self.context)
