from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.hobbies_sports = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')

        self.user_form = WebElement(driver, '#userForm')
        self.select_state = WebElement(driver, '#state')
        self.select_state_option = WebElement(driver, "//div[contains(text(), 'Haryana')]", locator_type='xpath')
        self.select_city = WebElement(driver, '#stateCity-wrapper > div:nth-child(3)')
        self.select_city_option = WebElement(driver, "//div[text()='Karnal']", locator_type='xpath')