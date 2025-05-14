from pages.alerts import Alerts
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_check_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    # На странице присутствует кнопка “#timerAlertButton”
    assert alert_page.btn_timer.exist()

    alert_page.btn_timer.click()

    # Через 5 сек после клика на кнопку всплывает алерт
    time.sleep(5)

    try:
        WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert_present = True
    except TimeoutException:
        alert_present = False

    assert alert_present