from page_objects.login_page import LoginPage
import pytest


class TestLoginPage:
    @pytest.fixture(autouse=True)
    # fixture runs before each function
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    # @pytest.mark.login
    def test_login_page_load(self):
        self.login_page.open_login()
        did_load, message = self.login_page.validate_loginpage_loaded()
        assert did_load, message

    # @pytest.mark.login
    # @pytest.mark.parametrize("username, password", [
    #     ("test42", "bArw.g@.RFhXRM5"),
    #     ("admin", "password")
    # ])
    def test_positive_login_cases(self, username, password):
        self.login_page.open_login()
        self.login_page.execute_login(username, password)
        assert self.login_page.validate_logged_in()

    # @pytest.mark.login
    def test_negative_login_cases(self):
        self.login_page.open_login()
        self.login_page.execute_login(username="n3n5390b0bcvcd.a", password="password")
        assert self.login_page.validate_login_failed()

# test link to signup page

# test negative sign up: param examples, look for error message

# Also test logout functionality

# test positive sign up. 
# NEED TO MOCK THIS INSTEAD?

