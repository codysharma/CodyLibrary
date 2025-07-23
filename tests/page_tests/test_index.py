import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.landing_page import LandingPage
import time
from urllib.parse import urlparse

class TestLandingPage:
    # @pytest.mark.index_page
    def test_index_page_loads(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open()
        assert landing_page.current_url == landing_page.expected_url, "Index page did not load correctly"
    
    # @pytest.mark.index_page
    def test_staff_reading_list_populated(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open()
        assert landing_page.is_staff_reading_section_displayed(), "Staff reading section is not displayed"

    # @pytest.mark.index_page
    def test_events_list_populated(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open()
        assert landing_page.is_event_list_displayed(), "Events list is not populated"

    # Test: navbar links work
    # @pytest.mark.index_page
    @pytest.mark.parametrize("locator_name, expected_url", [
        ("_LandingPage__map_link", "/map"),
        ("_LandingPage__login_page_link", "/accounts/login/"),
        ("_LandingPage__landing_title", "/")
    ])
    def test_navbar_nonmenu_links(self, driver, locator_name, expected_url):
        landing_page = LandingPage(driver)
        landing_page.open()

        locator = getattr(landing_page, locator_name)
        landing_page._click(locator)

        current_path = urlparse(landing_page.current_url).path
        assert current_path == expected_url, f"Expected {expected_url} but got {landing_page.current_url}"

    # Test: navbar menu clicks
    # @pytest.mark.index_page
    @pytest.mark.parametrize("locator1_name, locator2_name, expected_url", [
        ("_LandingPage__catalog_link", 
         "_LandingPage__general_catalog_link", 
         "/catalog/"),
        ("_LandingPage__catalog_link",
         "_LandingPage__fiction_catalog_link",
         "/fiction"),
         ("_LandingPage__catalog_link",
         "_LandingPage__ush_catalog_link",
         "/ushistory"),
         ("_LandingPage__catalog_link",
         "_LandingPage__wh_catalog_link",
         "/worldhistory"),
         ("_LandingPage__catalog_link",
         "_LandingPage__ps_catalog_link",
         "/politicalscience"),
         ("_LandingPage__catalog_link",
         "_LandingPage__edu_catalog_link",
         "/education"),
         ("_LandingPage__catalog_link",
         "_LandingPage__aup_catalog_link",
         "/architectureandurbanplanning"),
        ("_LandingPage__catalog_link",
         "_LandingPage__nf_catalog_link",
         "/nonfiction"),
         ("_LandingPage__events_navbar_menu", "_LandingPage__upcoming_events_link", "/events")
    ])
    def test_navbar_menu_links(self, driver, locator1_name, locator2_name, expected_url):
        landing_page = LandingPage(driver)
        landing_page.open()
        landing_page.navbar_menu_links(
            getattr(landing_page, locator1_name),
            getattr(landing_page, locator2_name)
        )
        assert expected_url in landing_page.current_url

