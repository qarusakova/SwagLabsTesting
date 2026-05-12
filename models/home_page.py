from playwright.sync_api import Page, Locator

class HomePage:
  URL = "https://www.saucedemo.com/inventory.html"

  def __init__(self, page: Page):
    self.page = page

    self.burger_menu = page.get_by_role("button", name="Open Menu")
    self.logout_link = page.get_by_test_id("logout-sidebar-link")

    self.filter_dropdown_menu = page.get_by_test_id("product-sort-container")

    self.inventory_item_name = page.get_by_test_id("inventory-item-name")
    self.inventory_item_price = page.get_by_test_id("inventory-item-price")

  def open(self) -> None:
    self.page.goto(self.URL)

  def logout(self) -> None:
    self.burger_menu.click()
    self.logout_link.click()

  def press_add_to_cart_button(self, item_name: str) -> None:
    item_id = item_name.lower().replace(" ", "-")
    item = self.page.get_by_test_id(f"add-to-cart-{item_id}")
    item.wait_for()
    item.click() 

  def press_remove_item(self, item_name: str) -> None:
    item_id = item_name.lower().replace(" ", "-")
    item = self.page.get_by_test_id(f"remove-{item_id}")
    item.wait_for()
    item.click()

  def get_cart_icon_counter(self) -> int:
    cart = self.page.get_by_test_id("shopping-cart-link")
    cart_counter = cart.text_content()

    if cart_counter == "" or cart_counter == None:
      return 0
    else:
      return int(cart_counter)