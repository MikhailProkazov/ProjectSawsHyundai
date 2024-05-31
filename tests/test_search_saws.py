import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page
from pages.hyundai_saws_page import Saws


import pandas as pd

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'

@allure.description('Test search saws')
def test_search_saws(set_up):
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Старт теста по поиску бензопил марки Hyundai")

    mp = Main_page(driver)
    mp.open_url()                       # step 1
    time.sleep(5)
    print("Открылся нужный нам сайт")

    search_saws = Main_page(driver)
    search_saws.input_hyundai_saw()     # step 2
    time.sleep(7)
    print("Открылся список бензопил")
    time.sleep(7)



    """Сбор информации для первого товара"""

    change_hyundai_saw_1 = Saws(driver)
    change_hyundai_saw_1.change_saw_1()             # step 3
    print("Выбрали первый товар из предложенных")
    time.sleep(5)

    s1_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")  # модель 1
    val_s1_model = s1_model.text
    s1_model_in_excel = val_s1_model[9:]
    print(s1_model_in_excel)
    s1_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")  # цена 1
    val_s1_price = s1_price.text
    print(val_s1_price)
    s1_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")  # мощность 1
    val_s1_power = s1_power.text
    print(val_s1_power)


    """Сбор информации для второго товара"""

    hsp = Saws(driver)
    hsp.open_url_saws()             # step 4
    time.sleep(5)
    print("Открылась страница с бензопилами фирмы Hyundai")

    change_hyundai_saw_2 = Saws(driver)
    change_hyundai_saw_2.change_saw_2()         #step 5
    print("Выбрали второй товар из предложенных")
    # time.sleep(3)

    s2_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")       # модель 2
    val_s2_model = s2_model.text
    s2_model_in_excel = val_s2_model[9:]
    print(s2_model_in_excel)
    s2_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")                    # цена 2
    val_s2_price = s2_price.text
    print(val_s2_price)
    s2_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")       # мощность 2
    val_s2_power = s2_power.text
    print(val_s2_power)


    """Сбор информации для третьего товара"""

    hsp = Saws(driver)
    hsp.open_url_saws()             # step 6
    time.sleep(3)
    print("Открылась страница с бензопилами фирмы Hyundai")

    change_hyundai_saw_3 = Saws(driver)
    change_hyundai_saw_3.change_saw_3()         # step 7
    print("Выбрали третий товар из предложенных")
    # time.sleep(3)

    s3_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")  # модель 3
    val_s3_model = s3_model.text
    s3_model_in_excel = val_s3_model[9:]
    print(s3_model_in_excel)
    s3_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")  # цена 3
    val_s3_price = s3_price.text
    print(val_s3_price)
    s3_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")  # мощность 3
    val_s3_power = s3_power.text
    print(val_s3_power)


    """Сбор информации для четвертого товара"""

    hsp = Saws(driver)
    hsp.open_url_saws()         # step 8
    time.sleep(3)
    print("Открылась страница с бензопилами фирмы Hyundai")

    change_hyundai_saw_4 = Saws(driver)
    change_hyundai_saw_4.change_saw_4()         # step 9
    print("Выбрали четвертый товар из предложенных")
    # time.sleep(3)

    s4_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")  # модель 4
    val_s4_model = s4_model.text
    s4_model_in_excel = val_s4_model[9:]
    print(s4_model_in_excel)
    s4_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")  # цена 4
    val_s4_price = s4_price.text
    print(val_s4_price)
    s4_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")  # мощность 4
    val_s4_power = s4_power.text
    print(val_s4_power)


    """Сбор информации для пятого товара"""

    hsp = Saws(driver)
    hsp.open_url_saws()             # step 10
    time.sleep(3)
    print("Открылась страница с бензопилами фирмы Hyundai")

    change_hyundai_saw_5 = Saws(driver)
    change_hyundai_saw_5.change_saw_5()             # step 11
    print("Выбрали пятый товар из предложенных")
    # time.sleep(3)

    s5_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")  # модель 5
    val_s5_model = s5_model.text
    s5_model_in_excel = val_s5_model[9:]
    print(s5_model_in_excel)
    s5_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")  # цена 5
    val_s5_price = s5_price.text
    print(val_s5_price)
    s5_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")  # мощность 5
    val_s5_power = s5_power.text
    print(val_s5_power)


    """Сбор информации для шестого товара"""

    hsp = Saws(driver)
    hsp.open_url_saws()             # step 12
    time.sleep(3)
    print("Открылась страница с бензопилами фирмы Hyundai")

    change_hyundai_saw_6 = Saws(driver)
    change_hyundai_saw_6.change_saw_6()             # step 13
    print("Выбрали шестой товар из предложенных")
    # time.sleep(3)

    s6_model = driver.find_element(By.XPATH, "//h1[@class='head-1 card-main-title']")  # модель 6
    val_s6_model = s6_model.text
    s6_model_in_excel = val_s6_model[9:]
    print(s6_model_in_excel)
    s6_price = driver.find_element(By.XPATH, "//span[@class='text-lg']")  # цена 6
    val_s6_price = s6_price.text
    print(val_s6_price)
    s6_power = driver.find_element(By.XPATH, "(//p[@class='text-sm text-break'])[4]")  # мощность 6
    val_s6_power = s6_power.text
    print(val_s6_power)



    df = pd.DataFrame(dict(                         # step 14
        ID=['1', '2', '3', '4', '5', '6'],
        Model=[
            s1_model_in_excel[8:], s2_model_in_excel[8:],
            s3_model_in_excel[8:], s4_model_in_excel[8:],
            s5_model_in_excel[8:], s6_model_in_excel[8:]
        ],
        Price=[val_s1_price, val_s2_price, val_s3_price, val_s4_price, val_s5_price, val_s6_price],
        Power=[val_s1_power, val_s2_power, val_s3_power, val_s4_power, val_s5_power, val_s6_power])
    )
    df.to_excel('list_saws_hyundai.xlsx')



