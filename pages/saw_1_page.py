from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





from base.base_class import Base

class Saw_1(Base):

    url = "https://krasnodar.220-volt.ru/catalog-735228/"

    # Locators

    saw_1_model = "//h1[@class='head-1 card-main-title']"
    saw_1_price = "//span[@class='text-lg']"
    saw_1_power = "//p[@class='text-sm text-break']"


    # Getters

    def get_saw_1_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_1_model)))

    def get_saw_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_1_price)))

    def get_saw_1_power(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_1_power)))


    # Actions




    # def enter_for_search_form(self):
    #     self.get_search_form().send_keys(Keys.ENTER)


