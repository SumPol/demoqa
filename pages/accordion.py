from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content_section1 = WebElement(driver, '#section1Content > p')
        self.heading_section1 = WebElement(driver, '#section1Heading')
        self.content_section2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.content_section2_continuation = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.content_section3 = WebElement(driver, '#section3Content > p')

        # for test_mod_visible_accordion_default with common selector for content section2
        self.content_section2_mod = WebElement(driver, '#section2Content')
        self.heading_section2 = WebElement(driver, '#section2Heading')
