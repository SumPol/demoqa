from pages.textbox_page import TextBox


def test_placeholder(browser):
    textbox_page = TextBox(browser)

    textbox_page.visit()
    assert textbox_page.full_name.get_dom_attribute('placeholder') == 'Full Name'
