from models.home_page import HomePage

def test_sort_by_name_A_to_Z(logged_in_page):
  home_page = HomePage(logged_in_page)

  initial_items = home_page.inventory_item_name.all_text_contents()
  expected_names = sorted(initial_items)

  home_page.filter_dropdown_menu.select_option("az")

  actual_names = home_page.inventory_item_name.all_text_contents()

  assert expected_names == actual_names

def test_sort_by_name_Z_to_A(logged_in_page):
  home_page = HomePage(logged_in_page)

  initial_items = home_page.inventory_item_name.all_text_contents()
  expected_names = sorted(initial_items, reverse=True)

  home_page.filter_dropdown_menu.select_option("za")

  actual_names = home_page.inventory_item_name.all_text_contents()

  assert expected_names == actual_names

def test_sort_by_price_low_to_high(logged_in_page):
  home_page = HomePage(logged_in_page)

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items])

  home_page.filter_dropdown_menu.select_option("lohi")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
        float(price.replace("$", "")) for price in actual_prices
    ]

  assert expected_prices == actual_prices

def test_sort_by_price_high_to_low(logged_in_page):
  home_page = HomePage(logged_in_page)

  initial_items = home_page.inventory_item_price.all_text_contents()
  expected_prices = sorted(
    [float(price.replace("$", "")) for price in initial_items], reverse=True)

  home_page.filter_dropdown_menu.select_option("hilo")

  actual_prices = home_page.inventory_item_price.all_text_contents()
  actual_prices = [
        float(price.replace("$", "")) for price in actual_prices
    ]

  assert expected_prices == actual_prices

def test_sort_by_price_high_to_low_not_persist_after_refresh(logged_in_page):
    home_page = HomePage(logged_in_page)

    home_page.filter_dropdown_menu.select_option("hilo")

    prices_before_refresh = [
        float(price.replace("$", ""))
        for price in home_page.inventory_item_price.all_text_contents()
    ]

    expected_prices = sorted(prices_before_refresh, reverse=True)
    assert prices_before_refresh == expected_prices

    logged_in_page.reload(wait_until="load")

    prices_after_refresh = [
        float(price.replace("$", ""))
        for price in home_page.inventory_item_price.all_text_contents()
    ]

    assert prices_after_refresh != expected_prices