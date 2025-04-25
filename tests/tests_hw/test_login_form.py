from pages.form_page import  FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.select_state.click()
    form_page.select_state_option.click()
    form_page.select_city.click()
    form_page.select_city_option.click()
    time.sleep(3)
