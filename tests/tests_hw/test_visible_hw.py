from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert accordion.content_section1.visible()
    accordion.heading_section1.click()
    time.sleep(2)
    assert not accordion.content_section1.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert not accordion.content_section2.visible()
    assert not accordion.content_section2_continuation.visible()
    assert not accordion.content_section3.visible()

# Modificated test for common selector for content section2
def test_mod_visible_accordion_default(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert not accordion.content_section2_mod.visible()
    accordion.heading_section2.click()
    time.sleep(2)
    assert accordion.content_section2_mod.visible()
    assert not accordion.content_section3.visible()