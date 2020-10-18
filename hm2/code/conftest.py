from ui.fixtures import *


def pytest_addoption(parser):
    """ add option """
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid')


@pytest.fixture(scope='session')
def config(request):
    """ config """
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    return {'browser': browser, 'version': version,
            'url': url, 'download_dir': '/tmp', 'selenoid': selenoid}
