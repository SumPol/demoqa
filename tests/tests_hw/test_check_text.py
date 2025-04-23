from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert demo_qa_page.footer_text.equal_text(footer_text)

def test_check_center_text(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    center_text = 'Please select an item from left to start practice.'
    assert el_page.center_text.equal_text(center_text)