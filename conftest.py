from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. en, ru, fr")
    parser.addoption('--base_url', action='store', default="https://selenium1py.pythonanywhere.com/",
                     help="Choose base url: e.g. http://selenium1py.pythonanywhere.com/")      

@pytest.fixture
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--lang={language}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()



@pytest.fixture
def base_url(request):
    base_url = request.config.getoption("base_url")
    yield base_url
