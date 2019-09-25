from selenium.webdriver.common.by import By


class PhpTravelLocator:
    # My account button
    my_account_btn = (By.CLASS_NAME, 'dropdown-toggle go-text-right')
    login_btn = (By.XPATH, '//nav[@class="navbar navbar-default"]//*[@id="li_myaccount"]//*/li[1]/a')

    # Other buttons
    search_input = (By.ID, "search-query")
    search_btn = (By.ID, "nav-search")
    tweets = (By.CLASS_NAME, "js-stream-item")
    like_btn = (By.CLASS_NAME, "HeartAnimation")
    latest_tweets = (By.PARTIAL_LINK_TEXT, 'Latest')
    avatar = (By.ID, "user-dropdown-toggle")
