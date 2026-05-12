import pytest
from playwright.sync_api import Page

from models.login_page import LoginPage

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.sign_in_as_valid_user()
    return page