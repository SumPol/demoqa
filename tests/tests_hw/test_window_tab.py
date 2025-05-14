from pages.links_page import  Links


def test_window_tab(browser):
    links_page = Links(browser)
    links_page.visit()

    assert links_page.home_link.exist()
    assert links_page.home_link.equal_text('Home')
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    links_page.home_link.click()
    assert len(browser.window_handles) == 2