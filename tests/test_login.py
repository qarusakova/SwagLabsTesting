from playwright.sync_api import Page, expect

from models.login_page import LoginPage
from models.home_page import HomePage

def test_login_with_valid_credentials(page: Page):
  login_page = LoginPage(page)

  username = "standard_user"
  password = "secret_sauce"

  login_page.sign_in(username, password)

  expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_with_incorrect_password(page: Page):
  login_page = LoginPage(page)

  username = "standard_user"
  password = "secret_sauce1"

  login_page.sign_in(username, password)

  expected_error_msg = login_page.get_error_msg()

  expect(expected_error_msg).to_contain_text(
      "Epic sadface: Username and password do not match any user in this service")

def test_user_logged_out_successfully(page: Page):
  login_page = LoginPage(page)

  username = "standard_user"
  password = "secret_sauce"

  login_page.sign_in(username, password)

  expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

  home_page = HomePage(page)
  home_page.logout()

  expect(page).to_have_url("https://www.saucedemo.com/")
