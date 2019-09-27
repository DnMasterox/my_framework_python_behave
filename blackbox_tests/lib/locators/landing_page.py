from selenium.webdriver.common.by import By


class LandingPageLocator:
    # My account button
    # my_account_btn = (By.XPATH, "//li[@id='li_myaccount']/a[@aria-expanded='true']")
    my_account_btn = (By.CSS_SELECTOR, "div[class='container'] #li_myaccount")
    # login_btn = (By.XPATH, '//nav[@class="navbar navbar-default"]//*[@id="li_myaccount"]//*/li[1]/a')
    login_btn = (By.CSS_SELECTOR, "div[class='container'] #li_myaccount ul a")
    landing_page_title = (By.XPATH, '//div[@class="preview__envato-logo"]/a')
    landing_page_logo = (By.XPATH, '//img[@alt="PHPTRAVELS | Travel Technology Partner"]')
    hotels_column = (By.XPATH, "//*[@title='Hotels']/span[@class='hidden-xs']")
    hotels_button = (By.XPATH, '/html/body/nav/div/div[1]/a/img')
    flights_column = (By.XPATH, "//*[@title='Flights']/span[@class='hidden-xs']")
    tours_column = (By.XPATH, "//*[@title='Tours']/span[@class='hidden-xs']")
    cars_column = (By.XPATH, "//*[@title='Cars']/span[@class='hidden-xs']")
    # columns_array = [hotels_column, flights_column, tours_column, cars_column]
    # columns_array = (By.XPATH, "//a[@class='text-center']/span[@class='hidden-xs']")

    # Other buttons
    search_input = (By.ID, "search-query")
    search_btn = (By.ID, "nav-search")
    tweets = (By.CLASS_NAME, "js-stream-item")
    like_btn = (By.CLASS_NAME, "HeartAnimation")
    latest_tweets = (By.PARTIAL_LINK_TEXT, 'Latest')
    avatar = (By.ID, "user-dropdown-toggle")
