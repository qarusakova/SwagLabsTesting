from playwright.sync_api import Page, expect

from models.login_page import LoginPage
from models.home_page import HomePage

ALL_ITEMS = [
    "sauce labs backpack",
    "sauce labs bike light",
    "sauce labs bolt t-shirt",
    "sauce labs fleece jacket",
    "sauce labs onesie",
    "test.allthethings() t-shirt (red)",
]

def test_default_cart_is_empty(logged_in_page):
  home_page = HomePage(logged_in_page)

  counter = home_page.get_cart_icon_counter()

  assert counter == 0

def test_add_item_to_cart(logged_in_page):
  home_page = HomePage(logged_in_page)
  home_page.press_add_to_cart_button("sauce labs backpack")

  counter = home_page.get_cart_icon_counter()

  assert counter == 1

def test_remove_item_from_cart(logged_in_page):
  home_page = HomePage(logged_in_page)
  home_page.press_add_to_cart_button("sauce labs backpack")

  counter = home_page.get_cart_icon_counter()

  assert counter == 1

  home_page.press_remove_item("sauce labs backpack")
  counter = home_page.get_cart_icon_counter()

  assert counter == 0


def test_add_all_items_to_cart(logged_in_page):
  home_page = HomePage(logged_in_page)
  for item in ALL_ITEMS:
    home_page.press_add_to_cart_button(item)

  counter = home_page.get_cart_icon_counter()

  assert counter == 6

