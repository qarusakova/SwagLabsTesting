from playwright.sync_api import Page, Locator

class LoginPage:
  def __init__(self, page: Page):
    self.page = page
    page.goto("https://www.saucedemo.com/")

    self.username = page.get_by_test_id("username")

    self.password = page.get_by_test_id("password")

    self.login_button = page.get_by_test_id("login-button")

    self.error_message = page.get_by_test_id("error")

  def sign_in(self, username: str, password: str) -> None:
    self.username.fill(username)
    self.password.fill(password)

    self.login_button.click()

  def get_error_msg(self) -> Locator:
    return self.error_message