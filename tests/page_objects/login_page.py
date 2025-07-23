from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage(BasePage):
    __url_login = "http://localhost:8000/accounts/login/"
    __url_signup = "http://localhost:8000/accounts/signup/"
    __login_title_locator = (By.ID, "login-page-title")
    __username_locator = (By.ID, "id_username")
    __password_locator = (By.ID, "id_password")
    __login_button_locator = (By.XPATH, "/html/body/main/div[2]/form/button")
    __create_account_link_locator = (By.XPATH, "/html/body/main/div[2]/a")
    __my_borrowed_link_locator = (By.ID, "my-borrowed-link")
    __suggest_addition_link_locator = (By.ID, "suggest-addition-link")
    __error_message_locator = (By.XPATH, "/html/body/main/div[2]/form/ul/li")
    __logout_button_locator = (By.ID, "navbar-logout-button")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    @property
    def expected_login_url(self) -> str:
        return self.__url_login
    
    @property
    def expected_signup_url(self) -> str:
        return self.__url_signup

    def open_login(self):
        super()._open_url(self.__url_login)

    def validate_loginpage_loaded(self) -> tuple[bool, str]:
        assert self.current_url == self.expected_login_url, f"URL expected {self.expected_login_url} but got {self.current_url}"
        assert super()._find(self.__login_title_locator).text == "Login Page", "Title does not match expected"
        return True, "Page loaded correctly"

    def open_signup(self):
        super()._open_url(self.__url_signup)
    
    def execute_login(self, username: str, password: str):
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__login_button_locator)

    def validate_logged_in(self) -> bool:
        assert super()._find(self.__my_borrowed_link_locator), "My borrowed link not found"
        assert super()._find(self.__suggest_addition_link_locator), "Suggest addition not found"
        assert super()._find(self.__logout_button_locator), "Logout button did not appear"
        return True        

    def validate_login_failed(self) -> bool:
        errorMessage = super()._find_visible_element(self.__error_message_locator)
        return errorMessage.is_displayed()

    def enter_new_account(self):
        pass