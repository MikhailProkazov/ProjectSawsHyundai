import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page


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

    # hyundai_saws = Main_page(driver)
    # hyundai_saws.click_hyundai_saws()
    # time.sleep(3)
    # print("Открылись все бензопилы Hyundai")
    # time.sleep(5)


