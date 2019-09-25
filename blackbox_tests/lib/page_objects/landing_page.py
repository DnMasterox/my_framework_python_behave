import random
import time

from selenium.webdriver.common.keys import Keys

from blackbox_tests.lib.locators.landing_page import LandingPageLocator
from blackbox_tests.lib.locators.login_page import LoginPageLocators
from blackbox_tests.lib.page_objects.base_page import BasePage
from blackbox_tests.lib.page_objects.login_page import LoginPage
from blackbox_tests.lib.utils.constants import URL, Constants


class LandingPage(BasePage):
    locator_dictionary = LandingPageLocator.__dict__

    def __init__(self, context):
        BasePage.__init__(self,
                          context.browser,
                          )
        self.context = context
        self.base_url = URL.PHP_TRAVELS
        self.visit(url=self.base_url)

    def search(self, q=Constants.GLOBAL_ENTRY_Q):
        self.search_input.send_keys(q)
        self.search_input.send_keys(Keys.ENTER)

    def navigate_to_login_page(self):
        self.my_account_btn.click()
        self.login_btn.click()
        return LoginPage(self.context)
