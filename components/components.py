from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", element)
        element.click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def equal_text(self, comparison_text):
        return self.get_text() == comparison_text

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        return len(self.find_elements()) == count

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def scroll_to_element(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);',
            self.find_element()
        )

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' not correct')
        return False

    def get_value_after_colon(self):
        parts = self.get_text().split(':')
        return parts[1].strip() if len(parts) > 1 else ''