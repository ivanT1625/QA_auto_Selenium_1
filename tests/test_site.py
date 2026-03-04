import time



from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_s6(browser):
    home_page = Homepage(browser)
    home_page.open()
    home_page.click_galaxy_s6()

    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")

    # browser.get('https://demoblaze.com/index.html')
    # wait = WebDriverWait(browser, 10)

    # galaxy_s6 = browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    # galaxy_s6.click()

    # title = browser.find_element(By.CSS_SELECTOR, 'h2')

    #galaxy_s6 = wait.until(
    #    EC.element_to_be_clickable((By.LINK_TEXT, 'Samsung galaxy s6'))
    #)

    #galaxy_s6.click()
    #title = wait.until(
    #    EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2'))
    #)

    # assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
    # browser.get('https://demoblaze.com/index.html')

    # monitor_link = browser.find_element(By.CSS_SELECTOR, """[onclick="byCat('monitor')"]""")
    # time.sleep(2)

    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 9

    home_page = Homepage(browser)
    home_page.open()
    home_page.click_monitor()
    time.sleep(2)
    home_page.check_count_monitors(2)


