from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.delete_row = WebElement(driver, '.rt-tbody > div > div > div:last-child > div > span:last-child')

        self.btn_add_row = WebElement(driver, '#addNewRecordButton')
        self.form_add_row = WebElement(driver, '.modal-content')
        self.btn_submit_row = WebElement(driver, '#submit')

        # Поля формы Registration Form
        self.fields = WebElement(driver, '#userForm > div > div:last-child > input')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.filled_fourth_row = WebElement(driver, '.rt-tbody > div:nth-child(4)')

        # Поля таблицы 4 строки
        self.first_name_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.last_name_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.email_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.age_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.salary_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.department_t_field = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')

        self.edit_fourth_row = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:last-child > div > span:first-child')
        self.delete_fourth_row = WebElement(driver, '.rt-tbody > div:nth-child(4) > div > div:last-child > div > span:last-child')
        self.amount_row_selector = WebElement(driver, '.-center > span:nth-child(2) > select')

        self.btn_previous = WebElement(driver, '.-previous > button')
        self.btn_next = WebElement(driver, '.-next > button')
        self.table_cell = WebElement(driver, '.rt-tbody > div > div > div')
        self.page_number = WebElement(driver, '.-pageJump > input')
        self.total_pages = WebElement(driver, '.-totalPages')