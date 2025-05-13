from pages.alerts import Alerts
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(2)

    try:
        WebDriverWait(browser, 2).until_not(EC.alert_is_present())
        alert_present = False
    except TimeoutException:
        alert_present = True

    assert alert_present

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)

def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    WebDriverWait(browser, 5).until(EC.alert_is_present())

    # Получаем alert один раз
    alert = browser.switch_to.alert
    assert alert.text == 'You clicked a button'

    alert.accept()
    time.sleep(2)

    try:
        WebDriverWait(browser, 2).until_not(EC.alert_is_present())
        alert_present = False
    except TimeoutException:
        alert_present = True

    assert not alert_present

def test_confirm(browser):
    """Отмена алерта"""
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    WebDriverWait(browser, 5).until(EC.alert_is_present())  # Ожидаем появления alert
    alert = browser.switch_to.alert
    alert.dismiss()

    assert alert_page.confirm_result.get_text() == 'You selected Cancel'

def test_promt(browser):
    alert_page = Alerts(browser)
    name = 'Polina'

    alert_page.visit()

    alert_page.btn_prompt.click()
    time.sleep(2)
    WebDriverWait(browser, 5).until(EC.alert_is_present())  # Ожидаем появления alert
    alert = browser.switch_to.alert
    alert.send_keys(name)
    alert.accept()
    time.sleep(2)
    assert alert_page.prompt_result.get_text() == f'You entered {name}'