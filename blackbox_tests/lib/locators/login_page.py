from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_form = (By.XPATH, '//div[@class="form-group"]/input[@type="email"]')
    password = (By.XPATH, '//div[@class="form-group"]/input[@type="password"]')
    remember_me_chbox = (By.XPATH, '//input[@id="remember-me"]')
    submit_btn = (By.XPATH, '//form/button[@type="submit"]')

    # li_myaccount > ul > li:nth-child(1) > a
