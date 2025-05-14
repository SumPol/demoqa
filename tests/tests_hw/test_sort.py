from pages.webtables import  WebTables


def test_sort(browser):
    webtable_page = WebTables(browser)

    webtable_page.visit()

    for element in webtable_page.columns.find_elements():
        element.click()
        assert element.get_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
        element.click()
        assert element.get_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'