# fixture is a function that runs before each test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pytest fixture is a function that runs before each test. If in the same folder as conftest.py, will auto import.

@pytest.fixture(params=
                # ["chrome", "firefox", "edge"]
                ["chrome"]
                )
def driver(request):
    browser = request.param
    # request.param is used to get the parameter from the fixture
    print(f"creating {browser} driver")

    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    elif browser == "edge":
        my_driver = webdriver.Edge()
    else:
        raise TypeError(f"Expected chrome, firefox, or edge but got {browser} instead.")
    
    my_driver.get("http://localhost:8000")
    # my_driver.implicitly_wait(10)
    yield my_driver
    # yield means this executes before the tests. Everything after, runs after the test

    print("closing driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")