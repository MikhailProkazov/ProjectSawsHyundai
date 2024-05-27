from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class HS_page(Base):

    url = 'https://krasnodar.220-volt.ru/?digiSearch=true&term=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BF%D0%B8%D0%BB%D0%B0%20hyundai&params=%7Csort%3DDEFAULT'

    # Locators

    saw_1 = "(//div[@class='digi-product__label'])[1]"
    saw_2 = "(//div[@class='digi-product__label'])[3]"
    saw_3 = "(//div[@class='digi-product__label'])[5]"
    saw_4 = "(//div[@class='digi-product__label'])[7]"
    saw_5 = "(//div[@class='digi-product__label'])[9]"
    saw_6 = "(//div[@class='digi-product__label'])[11]"
    saw_7 = "(//div[@class='digi-product__label'])[13]"

    # Getters

    def get_saw_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_1)))

    def get_saw_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_2)))

    def get_saw_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_3)))

    def get_saw_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_4)))

    def get_saw_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_5)))

    def get_saw_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_6)))

    def get_saw_7(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.saw_7)))

    # Actions

    def click_saw_1(self):
        self.get_saw_1().click()
        print("Клик saw_1")

    def click_saw_2(self):
        self.get_saw_2().click()
        print("Клик saw_2")

    def click_saw_3(self):
        self.get_saw_3().click()
        print("Клик saw_3")

    def click_saw_4(self):
        self.get_saw_4().click()
        print("Клик saw_4")

    def click_saw_5(self):
        self.get_saw_5().click()
        print("Клик saw_5")

    def click_saw_6(self):
        self.get_saw_6().click()
        print("Клик saw_6")

    def click_saw_7(self):
        self.get_saw_7().click()
        print("Клик saw_7")


    # Methods

    def change_saw_1(self):
        self.click_saw_1()

    def change_saw_2(self):
        self.click_saw_2()
