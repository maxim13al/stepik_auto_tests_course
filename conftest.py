from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. en, ru, fr")
    parser.addoption('--base_url', action='store', default="https://selenium1py.pythonanywhere.com/",
                     help="Choose base url: e.g. http://selenium1py.pythonanywhere.com/"),
    parser.addoption('--headless', action='store_true', default=False,
                     help="Run in headless mode"),
    parser.addoption('--maximize', action='store_true', default=False,
                     help="Run in headless mode")

    

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    maximize = request.config.getoption("maximize")
    headless = request.config.getoption("headless")
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
                options.add_argument('headless')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # fp = webdriver.FirefoxProfile()
        # fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    if maximize:
        browser.maximize_window()
    yield browser
    browser.quit()



@pytest.fixture
def base_url(request):
    base_url = request.config.getoption("base_url")
    yield base_url
