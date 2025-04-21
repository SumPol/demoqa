from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", element)
        element.click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True