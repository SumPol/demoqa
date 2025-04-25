from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.output_full_name = WebElement(driver, '.mb-1:nth-child(1)')
        self.output_current_address = WebElement(driver, '.mb-1:nth-child(2)')