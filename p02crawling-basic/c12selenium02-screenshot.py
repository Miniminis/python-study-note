"""
1. lib import 
2. browser option setting 
3. webdriver setting 
4. wait 5, browser size set, get url 
5. bs init, page_source check 
6. print infos  
7. pagenum setting
8. soup delete 
9. time sleep 
10. browser quit 
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options() 
chrome_options.add_argument('--headless')

# browser = webdriver.Chrome('./webdriver/chromedriver.exe', options=chrome_options)
browser = webdriver.Chrome('./webdriver/chromedriver.exe')
browser.implicitly_wait(5)
browser.maximize_window() 
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')
# print(browser.page_source)

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[4]/label'))).click() #삼성전자 

time.sleep(3)

curr_page = 1
total_page = 5

# while curr_page <= total_page: 
soup = BeautifulSoup(browser.page_source, 'lxml')
# print(soup.prettify())

product_list = soup.select('div.main_prodlist > ul > li')
name = product_list.select('div.prod_main_info > p.prod_name')
print(name)