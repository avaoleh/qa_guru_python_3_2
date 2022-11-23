import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def config_webdriver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver

@pytest.fixture()
def config_browser_size(config_browser_size):
    browser.config.driver.maximize_window()


@pytest.fixture()
def open_browser(config_webdriver, config_browser_size):
    browser.open('https://google.com')