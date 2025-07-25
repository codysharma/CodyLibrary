from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException



class BasePage:
    __url = "http://localhost:8000/"

    def __init__(self, driver: WebDriver):
        self._driver = driver
    
    @property
    def current_url(self):
        return self._driver.current_url

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()    

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)
    
    def _find_visible_element(self, locator: tuple) -> WebElement:
        element = self._find(locator)
        if not element.is_displayed():
            raise ElementNotVisibleException(f"Element {locator} exists on DOM but not visible")
        return element

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text
    
    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def _open_url(self, url: str):
        self._driver.get(url)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    

    
