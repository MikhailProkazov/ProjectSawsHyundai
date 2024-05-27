import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://krasnodar.220-volt.ru/'


    # Locators

    # search_form = "//*[@id='main-search-form']"
    search_form = "(//input[@type='search'])[1]"

    # Getters

    def get_search_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_form)))

    # Actions

    def click_search_form(self):
        self.get_search_form()
        print("Click Search Form")

    def input_search_form(self, search_form):
        self.get_search_form().send_keys(search_form)
        print("Input search_form")

    # Methods

    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def input_hyundai_saw(self):
        self.get_current_url()
        self.click_search_form()
        # self.input_search_form("бензопила Hyundai)"