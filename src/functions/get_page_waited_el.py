
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_waited_el(chrome_driver: WebDriver, delay=3, el_query_str='.login-input'):
    el = WebDriverWait(driver=chrome_driver, timeout=delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, el_query_str))
    )
    return el