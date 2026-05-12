from playwright.sync_api import Page, expect

from models.login_page import LoginPage
from models.home_page import HomePage

def test_sort_by_name_A_to_Z(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  initial_items = home_page.inventory_item_name.all_text_contents()
  expected_names = sorted(initial_items)

  home_page.filter_dropdown_menu.select_option("az")

  actual_names = home_page.inventory_item_name.all_text_contents()

  assert expected_names == actual_names

def test_sort_by_name_Z_to_A(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  initial_items = home_page.inventory_item_name.all_text_contents()
  expected_names = sorted(initial_items, reverse=True)

  home_page.filter_dropdown_menu.select_option("za")

  actual_names = home_page.inventory_item_name.all_text_contents()

  assert expected_names == actual_names

def test_sort_by_price_low_to_high(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items])

  home_page.filter_dropdown_menu.select_option("lohi")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
        float(price.replace("$", "")) for price in actual_prices
    ]

  assert expected_prices == actual_prices

def test_sort_by_price_high_to_low(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items], reverse=True)

  home_page.filter_dropdown_menu.select_option("hilo")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
        float(price.replace("$", "")) for price in actual_prices
    ]

  assert expected_prices == actual_prices

def test_sort_by_price_high_to_low_persist_after_refresh(page: Page):
  login_page = LoginPage(page)
  login_page.open()
  login_page.sign_in_as_valid_user()

  home_page = HomePage(page)

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items], reverse=True)

  home_page.filter_dropdown_menu.select_option("hilo")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
        float(price.replace("$", "")) for price in actual_prices
    ]

  assert expected_prices == actual_prices

  page.reload(wait_until="load")

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items], reverse=True)

  home_page.filter_dropdown_menu.select_option("hilo")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
    float(price.replace("$", "")) for price in actual_prices
  ]