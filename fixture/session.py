from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def login(self, username, password):
        self.app.open_home_page()
        # Login
        self.wd.find_element(By.NAME, "username").click()
        self.wd.find_element(By.NAME, "username").clear()
        self.wd.find_element(By.NAME, "username").send_keys(username)
        self.wd.find_element(By.NAME, "password").click()
        self.wd.find_element(By.NAME, "password").clear()
        self.wd.find_element(By.NAME, "password").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        return self.wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

