import pytest
from selene import browser

@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 1366
    browser.config.window_width = 1024


@pytest.fixture()
def open_browser(setting_browser):
    browser.open('https://google.com')
    yield
    browser.quit()