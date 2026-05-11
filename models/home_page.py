from playwright.sync_api import Page, Locator

class HomePage:
  def __init__(self, page: Page):
    self.page = page
    page.goto("https://www.saucedemo.com/inventory.html")

    self.burger_menu = page.get_by_role("button", name="Open Menu")

    self.logout_link = page.get_by_test_id("logout-sidebar-link")

  def logout(self) -> None:
    self.burger_menu.click()
    self.logout_link.click()