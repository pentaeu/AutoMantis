from selenium.webdriver.common.by import By
import re


class SignupHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def new_user(self, username, email, password):
        self.wd.get(self.app.base_url + "/signup_page.php")
        self.wd.find_element(By.NAME, "username").send_keys(username)
        self.wd.find_element(By.NAME, "email").send_keys(email)
        self.wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        self.wd.get(url)
        self.wd.find_element(By.NAME, "password").send_keys(password)
        self.wd.find_element(By.NAME, "password_confirm").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input[value='Update User']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)

