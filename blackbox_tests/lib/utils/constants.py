import os

USER_MAP = {
    'GlobalEntry': {
        'username': os.environ.get("TWITTER_USERNAME"),
        'password': os.environ.get("TWITTER_PASSWORD"),
    },
}


class Path:
    CONFIG = "config.yml"
    FAILED_SCREENSHOT = "./failed_scenarios_screenshots/"


class URL:
    PHP_TRAVELS = 'https://phptravels.net'


class Constants:
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
    SYS_TEST = "#{DIR_VAR}/blackbox-test/SYS_TEST/"