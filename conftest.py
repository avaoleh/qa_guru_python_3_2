import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config_browser_size():
    options = Options()
    options.add_argument('-width=1920')
    options.add_argument('-height=1080')
    #options.add_argument('--window-size=1920,1080')
    return options

@pytest.fixture()
def config_webdriver(config_browser_size):
    browser.config.driver = webdriver.Chrome(options=config_browser_size)
    return browser.config.driver

@pytest.fixture()
def open_browser(config_webdriver):
    browser.open('https://google.com')
    yield