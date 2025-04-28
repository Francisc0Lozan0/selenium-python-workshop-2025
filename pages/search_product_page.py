from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class Search(BasePage):
    TOSEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-icon-search')
    PRODUCT_MSG = (By.XPATH, '/html/body/main/div/div[2]/aside/div[1]/ol/li[3]/a/span')

    def search_product(self, product):
        self.enter_text(self.TOSEARCH_FIELD, product)
        time.sleep(3)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.PRODUCT_MSG)
        texto = elemento.text
        return texto
