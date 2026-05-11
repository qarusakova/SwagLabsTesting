from playwright.sync_api import Page, Locator

class LoginPage:
  URL = "https://www.saucedemo.com/"

  def __init__(self, page: Page):
    self.page = page
    self.username = page.get_by_test_id("username")
    self.password = page.get_by_test_id("password")
    self.login_button = page.get_by_test_id("login-button")
    self.error_message = page.get_by_test_id("error")

  def open(self) -> None:
    self.page.goto(self.URL)

  def sign_in(self, username: str, password: str) -> None:
    self.username.fill(username)
    self.password.fill(password)

    self.login_button.click()

  def sign_in_as_valid_user(self) -> None:
    username = "standard_user"
    password = "secret_sauce"

    self.sign_in(username, password)

  def get_error_msg(self) -> Locator:
    return self.error_message