from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
        assert title.text == 'Samsung galaxy s6'

