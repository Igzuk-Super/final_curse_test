import pytest
import importlib.util
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome', help='Choose browser: Chrome, Firefox, Edge')
    parser.addoption('--language', action='store', default='ru, en', help='Language')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name').capitalize()
    language = request.config.getoption('language')
    print(f'\nStart browser {browser_name} for test..')
    if browser_name == 'Firefox':
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(firefox_profile=options)
    else:
        if browser_name != 'Chrome':
            print(f'\nDriver {browser_name} not found!')
            print('\nStart default browser Chrome for test..')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    yield driver
    print('\nQuit browser..')
    driver.quit()
