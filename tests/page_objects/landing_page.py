from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):
    __url = "http://localhost:8000/"
    __book_thumbnail_index = (By.ID, "book_thumbnail_index")
    __event_thumbnail = (By.CLASS_NAME, "event_thumbnail")
    __catalog_link = (By.XPATH, "/html/body/header/div/nav/div/div/ul/li[1]/a")
    __general_catalog_link = (By.ID, "general-catalog-link")
    __fiction_catalog_link = (By.ID, "fic-catalog-link")
    __ush_catalog_link = (By.ID, "ush-catalog-link")
    __wh_catalog_link = (By.ID, "wh-catalog-link")
    __ps_catalog_link = (By.ID, "ps-catalog-link")
    __edu_catalog_link = (By.ID, "edu-catalog-link")
    __aup_catalog_link = (By.ID, "aup-catalog-link")
    __nf_catalog_link = (By.ID, "nf-catalog-link")
    __map_link = (By.ID, "map-link")
    __login_page_link = (By.ID, "login-page-link")
    __landing_title = (By.ID, "landing-title")
    __events_navbar_menu = (By.ID, "events-navbar-menu")
    __upcoming_events_link = (By.ID, "upcoming-events")


    def __init__(self, driver):
        super().__init__(driver)
        self._open_url(self.__url)

    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    @property
    def expected_url(self) -> str:
        return self.__url

    def open(self):
        super()._open_url(self.__url)

    def is_event_list_displayed(self) -> bool:
        try:
            super()._wait_until_element_is_visible(self.__event_thumbnail, time = 5)
            return True
        except:
            return False

    def is_staff_reading_section_displayed(self) -> bool:
        try:
            super()._wait_until_element_is_visible(self.__book_thumbnail_index, time = 5)
            return True
        except:
            return False
        
    def navbar_menu_links(self, locator1_location, locator2_location):
        super()._click(locator1_location)

        super()._click(locator2_location)
    
