import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page
from pages.hyundai_saws_page import HS_page


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
    time.sleep(5)
    print("Открылся список бензопил")
    time.sleep(5)

    change_hyundai_saw_1 = HS_page(driver)
    change_hyundai_saw_1.change_saw_1()
    print("Выбрали первый товар из предложенных")
    time.sleep(5)



