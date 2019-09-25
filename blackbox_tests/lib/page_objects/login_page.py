from __future__ import unicode_literals

from blackbox_tests.lib.locators.login_page import LoginPageLocators
from blackbox_tests.lib.page_objects.base_page import BasePage
#from blackbox_tests.lib.page_objects.landing_page import LandingPage
from blackbox_tests.lib.utils.constants import URL


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self,
                          context.browser,
                          )
        self.context = context
        self.base_url = URL.PHP_TRAVELS_LOGIN
        self.visit(url=self.base_url)

    locator_dictionary = LoginPageLocators.__dict__

    def login(self, username='', password=''):
        self.email_form.send_keys(username)
        self.password.send_keys(password)
        self.submit_btn.click()
        #return LandingPage(self.context)
