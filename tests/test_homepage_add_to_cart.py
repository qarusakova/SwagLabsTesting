from playwright.sync_api import Page, expect

from models.login_page import LoginPage
from models.home_page import HomePage

def test_default_cart_is_empty(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  counter = home_page.get_cart_icon_counter()

  assert counter == 0

def test_add_item_to_cart(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)
  home_page.press_add_to_cart_button("sauce labs backpack")

  counter = home_page.get_cart_icon_counter()

  assert counter == 1

def test_remove_item_from_cart(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)
  home_page.press_add_to_cart_button("sauce labs backpack")

  counter = home_page.get_cart_icon_counter()

  assert counter == 1

  home_page.press_remove_item("sauce labs backpack")
  counter = home_page.get_cart_icon_counter()

  assert counter == 0


def test_add_all_items_to_cart(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)
  home_page.press_add_to_cart_button("sauce labs backpack")
  home_page.press_add_to_cart_button("sauce labs bike light")
  home_page.press_add_to_cart_button("sauce labs bolt t-shirt")
  home_page.press_add_to_cart_button("sauce labs fleece jacket")
  home_page.press_add_to_cart_button("sauce labs onesie")
  home_page.press_add_to_cart_button("test.allthethings() t-shirt (red)")

  counter = home_page.get_cart_icon_counter()

  assert counter == 6

def test_add_all_items_remove_one_item(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)
  home_page.press_add_to_cart_button("sauce labs backpack")
  home_page.press_add_to_cart_button("sauce labs bike light")
  home_page.press_add_to_cart_button("sauce labs bolt t-shirt")
  home_page.press_add_to_cart_button("sauce labs fleece jacket")
  home_page.press_add_to_cart_button("sauce labs onesie")
  home_page.press_add_to_cart_button("test.allthethings() t-shirt (red)")

  counter = home_page.get_cart_icon_counter()

  assert counter == 6

  home_page.press_remove_item("sauce labs bolt t-shirt")
  counter = home_page.get_cart_icon_counter()

  assert counter == 5

