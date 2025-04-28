from pages.form_page import  FormPage
from selenium.webdriver.common.keys import Keys
import time


def test_fill_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.select_state.click()
    form_page.select_state_option.click()
    form_page.select_city.click()
    form_page.select_city_option.click()
    time.sleep(3)

#-----------------------------------------------
# Разбор задания из занятия 11 (доп. решения, немного адаптированы)

def test_state_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.send_keys('NCR')
    form_page.btn_state.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.select_state.click()
    form_page.btn_state.send_keys(Keys.PAGE_DOWN)
    form_page.btn_state.send_keys(Keys.ENTER)
    time.sleep(2)