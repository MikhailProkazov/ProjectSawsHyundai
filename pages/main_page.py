import time

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://krasnodar.220-volt.ru/'


    # Locators

    search_form = "(//input[@type='search'])[1]"
    categories_saws = "//span[@class='digi-ac-category__name']"


    # Getters

    def get_search_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_form)))

    def get_categories_saws(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.categories_saws)))

    # Actions

    def click_search_form(self):
        self.get_search_form()
        print("Клик на строку поиска")

    def input_search_form(self, search_form):
        self.get_search_form().send_keys(search_form)
        print("Ввод нужных данных в строку поиска")
        # self.get_search_form().send_keys(Keys.ENTER)
        # print("Вывод страницы с нужными бензопилами")

    # def click_categories_saws(self):
    #     self.get_categories_saws()
    #     print("Клик на категорию бензопилы")


    # Methods

    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def input_hyundai_saw(self):
        self.get_current_url()
        self.click_search_form()
        self.input_search_form("бензопила Hyundai")
        self.get_current_url()

    # def click_hyundai_saws(self):
    #     self.click_categories_saws()
    #     self.get_current_url()
