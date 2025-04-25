from pages.textbox_page import TextBox


def test_textbox_form(browser):
    textbox_page = TextBox(browser)

    name = 'Ivanov Petr Vasil\'evich'
    address = 'ul. Vasileostrovskogo 19/2'

    textbox_page.visit()
    textbox_page.full_name.send_keys(name)
    textbox_page.current_address.send_keys(address)
    textbox_page.btn_submit.click()

    assert textbox_page.output_full_name.get_value_after_colon() == name
    assert textbox_page.output_current_address.get_value_after_colon() == address
