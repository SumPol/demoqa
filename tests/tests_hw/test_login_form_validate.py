from pages.form_page import  FormPage


def test_login_form_validate(browser):
    form_page = FormPage(browser)
    value_placeholder_first_name = 'First Name'
    value_placeholder_last_name = 'Last Name'
    value_placeholder_email = 'name@example.com'
    value_pattern_email = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    value_class_validated_form = 'was-validated'

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == value_placeholder_first_name
    assert form_page.last_name.get_dom_attribute('placeholder') == value_placeholder_last_name
    assert form_page.user_email.get_dom_attribute('placeholder') == value_placeholder_email
    assert form_page.user_email.get_dom_attribute('pattern') == value_pattern_email

    form_page.btn_submit.click_force()
    assert form_page.user_form.get_dom_attribute('class') == value_class_validated_form
