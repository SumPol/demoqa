from pages.webtables import WebTables
from selenium.webdriver.common.keys import Keys
import time


def test_add_delete_rows(browser):
    first_name = 'Ivan'
    last_name = 'Petrov'
    email = 'ivan_petrov@test.ru'
    age = '25'
    salary = '50000'
    department = 'Marketing'

    new_first_name = 'Leonid'

    webtable_page = WebTables(browser)

    webtable_page.visit()
    webtable_page.btn_add_row.click()

    # по клику на кнопку Add открывается диалоговое окно
    assert webtable_page.form_add_row.exist()

    # в диалоге нельзя сохранить пустую форму - рамки всех input-ов подсветились красным, форма не закрылась
    webtable_page.btn_submit_row.click()
    time.sleep(3)

    for element in webtable_page.fields.find_elements():
        assert element.value_of_css_property('borderColor') == 'rgb(220, 53, 69)'
    assert webtable_page.form_add_row.exist()

    # если заполнить все поля и нажать на кнопку Submit диалог закрывается
    webtable_page.first_name.send_keys(first_name)
    webtable_page.last_name.send_keys(last_name)
    webtable_page.email.send_keys(email)
    webtable_page.age.send_keys(age)
    webtable_page.salary.send_keys(salary)
    webtable_page.department.send_keys(department)
    webtable_page.btn_submit_row.click()
    time.sleep(3)
    assert not webtable_page.form_add_row.exist()

    # в таблицу добавляется новая запись с введенными данными
    assert webtable_page.filled_fourth_row.exist()

    assert webtable_page.first_name_t_field.get_text() == first_name
    assert webtable_page.last_name_t_field.get_text() == last_name
    assert webtable_page.email_t_field.get_text() == email
    assert webtable_page.age_t_field.get_text() == age
    assert webtable_page.salary_t_field.get_text() == salary
    assert webtable_page.department_t_field.get_text() == department

    # если кликнуть на карандаш на строке записи открывается диалог с введенными данными
    webtable_page.edit_fourth_row.click()
    assert webtable_page.form_add_row.exist()

    assert webtable_page.first_name.get_dom_attribute('value') == first_name
    assert webtable_page.last_name.get_dom_attribute('value') == last_name
    assert webtable_page.email.get_dom_attribute('value') == email
    assert webtable_page.age.get_dom_attribute('value') == age
    assert webtable_page.salary.get_dom_attribute('value') == salary
    assert webtable_page.department.get_dom_attribute('value') == department

    #если изменить имя и сохранить то в таблице обновятся данные
    webtable_page.first_name.click()
    webtable_page.first_name.send_keys(Keys.BACKSPACE * len(first_name))
    webtable_page.first_name.send_keys(new_first_name)
    webtable_page.btn_submit_row.click()
    assert webtable_page.first_name_t_field.get_text() == new_first_name

    # если нажать на корзину в строке записи - запись удаляется
    webtable_page.delete_fourth_row.click()
    for element in webtable_page.filled_fourth_row.find_elements():
        assert not element.get_attribute('value')