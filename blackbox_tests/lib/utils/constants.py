import os

USER_CREDENTIALS = {
    'GlobalEntry': {
        'username': 'user@phptravels.com',
        'password': 'demouser',
    },
}


class Path:
    CONFIG = "config.yml"
    FAILED_SCREENSHOT = "./failed_scenarios_screenshots/"


class URL:
    PHP_TRAVELS = 'https://phptravels.net'
    PHP_TRAVELS_LOGIN = 'https://www.phptravels.net/demo/login'
    PHP_TRAVELS_ACCOUNT = 'https://www.phptravels.net/demo/account/'


class Constants:
    # Response
    OK_RESPONSE = '200'
    # ++++
    SUPPLIER = '/SUPPLIER'
    ADMIN = '/ADMIN'

    # user credentials
    USER_MAIL = 'user@phptravels.com'
    USER_PASSWORD = 'demouser'

    # admin credentials
    ADMIN_MAIL = 'admin@phptravels.com'
    ADMIN_PASSWORD = 'demoadmin'

    # supplier credentials
    SUPPLIER_MAIL = 'supplier@phptravels.com'
    SUPPLIER_PASSWORD = 'demosupplier'

    TITLE = 'FEATURED TOURS'

    # personal account details
    USER_FIRST_NAME = 'Raghavan'
    USER_LAST_NAME = 'Raghavendar'
    USER_PHONE = '+31644574635'

    DIR_VAR = '/project'
    SYS_TEST = '/project/blackbox-test/SYS_TEST/'

    USERNAME = 'username'
    GLOBAL_ENTRY_Q = '#globalentry'
    TWEETS = 'tweets'

    # login page data
    PAGENAME = 'LOGIN'
