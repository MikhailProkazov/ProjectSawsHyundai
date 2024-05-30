
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilietes.logger import Logger


class Main_page(Base):
    url = 'https://krasnodar.220-volt.ru/'

    # Locators

    search_form = "(//input[@type='search'])[1]"


    # Getters

    def get_search_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_form)))


    # Actions

    def click_search_form(self):
        self.get_search_form()
        print("Клик на строку поиска")

    def enter_for_search_form(self):
        self.get_search_form().send_keys(Keys.ENTER)

    def input_search_form(self, search_form):
        self.get_search_form().send_keys(search_form)
        print("Ввод нужных данных в строку поиска")


    # Methods

    def open_url(self):
        Logger.add_start_step(method='open_url')
        self.driver.get(self.url)
        self.driver.maximize_window()
        Logger.add_end_step(url=self.driver.current_url, method='open_url')

    def input_hyundai_saw(self):
        Logger.add_start_step(method='input_hyundai_saw')
        self.get_current_url()
        self.click_search_form()
        self.input_search_form("бензопила Hyundai")
        self.click_search_form()
        self.enter_for_search_form()
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method='input_hyundai_saw')


