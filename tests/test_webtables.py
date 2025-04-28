from pages.webtables import  WebTables
import time

def test_webtable(browser):
    webtable_page = WebTables(browser)

    webtable_page.visit()

    assert not webtable_page.no_rows.exist()

    while not webtable_page.no_rows.exist():
        webtable_page.delete_row.click()

    time.sleep(3)
    assert webtable_page.no_rows.exist()