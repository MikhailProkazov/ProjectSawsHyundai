import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page
from pages.hyundai_saws_page import Saws

import pandas as pd

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


def test_search_saws():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Старт теста по поиску бензопил марки Hyundai")

    mp = Main_page(driver)
    mp.open_url()
    time.sleep(2)
    print("Открылся нужный нам сайт")

    search_saws = Main_page(driver)
    search_saws.input_hyundai_saw()
    time.sleep(2)
    print("Открылся список бензопил")
    time.sleep(2)

    """Сбор информации для первого товара"""

    change_hyundai_saw_1 = Saws(driver)
    change_hyundai_saw_1.change_saw_1()
    print("Выбрали первый товар из предложенных")
    time.sleep(5)

    s1_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")       # модель 1
    val_s1_model = s1_model.text
    s1_model_in_excel = val_s1_model[9:]
    print(s1_model_in_excel)
    s1_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")                    # цена 1
    val_s1_price = s1_price.text
    print(val_s1_price)
    s1_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")       # мощность 1
    val_s1_power = s1_power.text
    print(val_s1_power)

    df = pd.DataFrame({

        'ID': ['1'],
        'Model': [s1_model_in_excel],
        'Price': [val_s1_price],
        'Power': [val_s1_power]

    })
    df.to_excel('list_saws_hyundai.xlsx')


