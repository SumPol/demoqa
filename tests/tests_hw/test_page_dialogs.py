from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def  test_modal_elements(browser):
    modal_dialog_page = ModalDialogs(browser)

    modal_dialog_page.visit()
    assert modal_dialog_page.btns_third_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialog_page = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)

    modal_dialog_page.visit()
    browser.refresh()
    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)