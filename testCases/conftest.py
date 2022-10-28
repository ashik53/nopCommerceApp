import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser")
    elif browser == "firefox":
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        driver = webdriver.Firefox(options=options, executable_path= r"C:/BrowserDriver/geckodriver.exe")
        print("Launching FireFox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser")

    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


########## Pytest HTML report###########

# It is hook for Adding Environment info into HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] ="nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Ashik"

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)



















