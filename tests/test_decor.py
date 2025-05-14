from pages.demoqa import  DemoQa
from pages.radio_button_page import RadioButton
import pytest


@pytest.mark.skip
def test_decor(browser):
    counter = 0
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()

    for element in demo_qa_page.category_cards.find_elements():
        counter += 1
        assert element.text != ''

    assert counter == 6


@pytest.mark.skip
def test_decor_v2(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.category_cards.check_count_elements(6)

    for element in demo_qa_page.category_cards.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason="Проверка работы пропуска")
def test_decor_radio_button(browser):
    radio_button_page = RadioButton(browser)

    radio_button_page.visit()

    radio_button_page.yes_radio.click_force()
    assert radio_button_page.text.equal_text('You have selected Yes')

    radio_button_page.impressive_radio.click_force()
    assert radio_button_page.text.equal_text('You have selected Impressive')

    assert 'disabled' in radio_button_page.no_radio.get_dom_attribute('class')