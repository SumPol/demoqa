from pages.progress_bar_page import  ProgressBar
import time


def test_progress_bar(browser):
    flag = True
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    progress_bar_page.btn_start_stop.click()

    while flag:
        if progress_bar_page.progress_bar.equal_text('51%'):
            progress_bar_page.btn_start_stop.click()
            flag = False

    assert progress_bar_page.progress_bar.equal_text('51%')


def test_progress_bar_v2(browser):
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    progress_bar_page.btn_start_stop.click()

    while True:
        if progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.btn_start_stop.click()
            break

    time.sleep(2)
    assert progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51'