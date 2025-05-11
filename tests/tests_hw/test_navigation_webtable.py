from pages.webtables import WebTables


def test_navigation_webtable(browser):
    webtable_page = WebTables(browser)

    # Предусловия
    webtable_page.visit()
    webtable_page.amount_row_selector.select_value('5')

    # Кнопки Next и Previous заблокированы (по клику ничего не происходит и имеют атрибут disabled)
    assert webtable_page.btn_previous.is_disabled()
    assert webtable_page.btn_next.is_disabled()

    # * Запись в массив изначальных значений в таблице
    table_value_start = []
    for element in webtable_page.table_cell.find_elements():
        table_value_start.append(element.text)

    webtable_page.btn_previous.click()
    webtable_page.btn_next.click()

    # * Запись в массив текущих значений в таблице (после нажатий клавиш)
    current_value = []
    for element in webtable_page.table_cell.find_elements():
        current_value.append(element.text)

    # * Сравнение изначальных и текущих значений в таблице
    assert table_value_start == current_value

    assert webtable_page.page_number.get_dom_attribute('value') == '1'
    assert webtable_page.total_pages.equal_text('1')

    # Добавить в таблицу 3 записи
    first_name = 'Ivan'
    last_name = 'Petrov'
    email = 'ivan_petrov@test.ru'
    age = '25'
    salary = '50000'
    department = 'Marketing'

    for i in range(3):
        webtable_page.btn_add_row.click()
        webtable_page.first_name.send_keys(first_name)
        webtable_page.last_name.send_keys(last_name)
        webtable_page.email.send_keys(email)
        webtable_page.age.send_keys(age)
        webtable_page.salary.send_keys(salary)
        webtable_page.department.send_keys(department)
        webtable_page.btn_submit_row.click()

    # * Запись в массив значений в таблице на странице 1
    table_value_first = []
    for element in webtable_page.table_cell.find_elements():
        table_value_first.append(element.text)

    # Появляется 2-я страница (of 2)
    assert webtable_page.total_pages.equal_text('2')

    # Кнопка Next становится доступной
    assert not webtable_page.btn_next.is_disabled()

    # Если кликнуть по кнопке Next то открывается 2-я страница (* также проверим доступность кнопки Previous)
    webtable_page.btn_next.click()
    assert webtable_page.page_number.get_dom_attribute('value') == '2'
    assert not webtable_page.btn_previous.is_disabled()

    # * Проверка, что в таблице поменялись значения
    current_value.clear()
    for element in webtable_page.table_cell.find_elements():
        current_value.append(element.text)

    assert table_value_first != current_value

    # Если кликнуть по кнопке Previous то открывается 1-я страница (* и проверим, что значения поменялись в таблице)
    # * Запись в массив значений в таблице на странице 2
    table_value_second = []
    for element in webtable_page.table_cell.find_elements():
        table_value_second.append(element.text)

    webtable_page.btn_previous.click()
    assert webtable_page.page_number.get_dom_attribute('value') == '1'

    current_value.clear()
    for element in webtable_page.table_cell.find_elements():
        current_value.append(element.text)

    assert table_value_second != current_value