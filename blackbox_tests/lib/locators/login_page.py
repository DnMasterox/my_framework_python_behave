from selenium.webdriver.common.by import By


class LoginPageLocators:
    title_panel = (By.XPATH, '//div[@class="panel-heading go-text-right"]')
    email_form = (By.XPATH, '//div[@class="form-group"]/input[@type="email"]')
    password = (By.XPATH, '//div[@class="form-group"]/input[@type="password"]')
    remember_me_chbox = (By.XPATH, '//input[@id="remember-me"]')
    submit_btn = (By.XPATH, '//form/button[@type="submit"]')
