import datetime
from pydantic import BaseModel
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilietes.logger import Logger
import allure


class Saws(Base):


    url = 'https://krasnodar.220-volt.ru/?digiSearch=true&term=%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BF%D0%B8%D0%BB%D0%B0%20hyundai&params=%7Csort%3DDEFAULT'

    # Locators

    saw_1 = "(//div[@class='digi-product__label'])[1]"
    saw_2 = "(//div[@class='digi-product__label'])[3]"
    saw_3 = "(//div[@class='digi-product__label'])[5]"
    saw_4 = "(//div[@class='digi-product__label'])[7]"
    saw_5 = "(//div[@class='digi-product__label'])[9]"
    saw_6 = "(//div[@class='digi-product__label'])[11]"

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

    # Actions

    def click_saw_1(self):
        self.get_saw_1().click()
        print("Выбор первого товара")

    def click_saw_2(self):
        self.get_saw_2().click()
        print("Выбор второго товара")

    def click_saw_3(self):
        self.get_saw_3().click()
        print("Выбор третьего товара")

    def click_saw_4(self):
        self.get_saw_4().click()
        print("Выбор четвертого товара")

    def click_saw_5(self):
        self.get_saw_5().click()
        print("Выбор пятого товара")

    def click_saw_6(self):
        self.get_saw_6().click()
        print("Выбор шестого товара")

    # Methods

    def open_url_saws(self):
        with allure.step("Open url saws"):
            Logger.add_start_step(method='open_url_saws')
            self.driver.get(self.url)
            self.driver.maximize_window()
            Logger.add_end_step(url=self.driver.current_url, method='open_url_saws')

    def change_saw_1(self):
        with allure.step("Change saw 1"):
            Logger.add_start_step(method='change_saw_1')
            self.click_saw_1()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_1')

    def change_saw_2(self):
        with allure.step("Change saw 2"):
            Logger.add_start_step(method='change_saw_2')
            self.click_saw_2()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_2')

    def change_saw_3(self):
        with allure.step("Change saw 3"):
            Logger.add_start_step(method='change_saw_3')
            self.click_saw_3()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_3')

    def change_saw_4(self):
        with allure.step("Change saw 4"):
            Logger.add_start_step(method='change_saw_4')
            self.click_saw_4()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_4')

    def change_saw_5(self):
        with allure.step("Change saw 5"):
            Logger.add_start_step(method='change_saw_5')
            self.click_saw_5()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_5')

    def change_saw_6(self):
        with allure.step("Change saw 6"):
            Logger.add_start_step(method='change_saw_6')
            self.click_saw_6()
            Logger.add_end_step(url=self.driver.current_url, method='change_saw_6')


