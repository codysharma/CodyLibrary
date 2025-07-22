import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.landing_page import LandingPage
import time

class TestPositiveScenarios:
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
    def test_navbar_nonmenu_links(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open()



    # Test: navbar menu clicks