
from os import wait
from time import sleep
from traceback import print_tb
from config import config 
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from src.functions.get_page_waited_el import get_page_waited_el

def getChromeDownloadPathOption(download_path='/'):
    options = ChromeOptions()
    prefs = { 'download.default_directory': download_path }
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    options.add_experimental_option('prefs', prefs)
    return options

def init_chrome_driver():
    driver_path = config['chromeDriverPath']
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(
        service=service,
        options=getChromeDownloadPathOption()
    )
    return driver

def login_to_page(chrome_driver: WebDriver):
    chrome_driver.get(config['webpageUrl'])
    
    username_input_el = get_page_waited_el(chrome_driver=chrome_driver, delay=5, el_query_str='input[name="username"]')
    password_input_el = get_page_waited_el(chrome_driver=chrome_driver, delay=3, el_query_str='input[name="passwd"]')
    # print(username_input_el, password_input_el)

    print('Logined success :)')
    sleep(2)
    print(username_input_el)

def get_webpage_soup(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

def main():
    chrome_driver = init_chrome_driver()
    # login_to_page(chrome_driver=chrome_driver)
    soup = get_webpage_soup(chrome_driver.page_source)
    # print(soup)
    res = soup.find_all('h2')
    def get_el_text(el):
        res = el.getText()
        print(res, el)
        return res
    text_list = map(get_el_text, list(res))
    return list(text_list)


if __name__ == '__main__':
    print(main())