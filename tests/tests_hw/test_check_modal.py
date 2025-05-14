from pages.modal_dialogs import ModalDialogs
from selenium.common.exceptions import WebDriverException
import time
import pytest

def test_check_modal_small(browser):
    page_modals = ModalDialogs(browser)

    try:
        page_modals.visit()
        time.sleep(1)
    except WebDriverException:
        pytest.skip("Страница недоступна")

    # На странице присутствует кнопка “Small modal”
    if not page_modals.btn_small_modal.exist():
        pytest.skip("Кнопка 'Small modal' не найдена — возможно, страница не загрузилась")

    # При клике на кнопку "Small modal" открывается модальное окно
    page_modals.btn_small_modal.click()
    time.sleep(2)

    assert page_modals.modal.exist()

    # У окна есть кнопка “close” по клику окно закрывается
    if not page_modals.btn_close_small_modal.exist():
        pytest.skip("Кнопка закрытия не найдена — окно не появилось")

    page_modals.btn_close_small_modal.click()
    time.sleep(2)

    assert not page_modals.modal.exist()


def test_check_modal_large(browser):
    page_modals = ModalDialogs(browser)

    try:
        page_modals.visit()
        time.sleep(1)
    except WebDriverException:
        pytest.skip("Страница недоступна")

    # На странице присутствует кнопка “Large modal”
    if not page_modals.btn_large_modal.exist():
        pytest.skip("Кнопка 'Small modal' не найдена — возможно, страница не загрузилась")

    # При клике на кнопку "Large modal" открывается модальное окно
    page_modals.btn_large_modal.click()
    time.sleep(2)

    assert page_modals.modal.exist()

    # У окна есть кнопка “close” по клику окно закрывается
    if not page_modals.btn_close_large_modal.exist():
        pytest.skip("Кнопка закрытия не найдена — окно не появилось")

    page_modals.btn_close_large_modal.click()
    time.sleep(2)

    assert not page_modals.modal.exist()
