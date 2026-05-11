from playwright.sync_api import Page, Locator

class HomePage:
  URL = "https://www.saucedemo.com/inventory.html"

  def __init__(self, page: Page):
    self.page = page

    self.burger_menu = page.get_by_role("button", name="Open Menu")

    self.logout_link = page.get_by_test_id("logout-sidebar-link")

    self.filter_dropdown_menu = page.get_by_test_id("product-sort-container")

    self.inventory_item = page.get_by_test_id("inventory-item")

    self.inventory_item_description = page.get_by_test_id("inventory-item-description")

  def open(self) -> None:
    self.page.goto(self.URL)

  def logout(self) -> None:
    self.burger_menu.click()
    self.logout_link.click()