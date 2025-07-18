import pytest
from selenium import webdriver

import time

class TestPositiveScenarios:
    @pytest.mark.index_page
    def test_index_page_loads(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        actual_url = driver.current_url
        assert actual_url == "http://localhost:8000/", "Index page did not load correctly"
        time.sleep(2)  
        driver.quit()
    
    # Test: what our staff are reading has material
    # Test: events list populated
    # Test: navbar loads
    # Test: navbar links work
    # Test: navbar menu clicks