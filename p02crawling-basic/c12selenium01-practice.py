from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options() 
chrome_options.add_argument("--headless")

# browser = webdriver.Chrome('./webdriver/chromedriver.exe', options=chrome_options)
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

browser.implicitly_wait(5)
browser.maximize_window()
browser.get('http://prod.danawa.com/list/?cate=11336467&15main_11_03')

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="simpleSearchOptionpriceCompare"]/div/dl[1]/dd/div/button[1]'))).click() 
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue340516"]'))).click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue264987"]'))).click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue246869"]'))).click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue228707"]'))).click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue228706"]'))).click()
# WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="searchAttributeValue228706"]'))).click()

time.sleep(3)

soup = BeautifulSoup(browser.page_source, "lxml")
# print(soup.prettify())

product_list = soup.select('div.main_prodlist > ul > li')
for item in product_list:
    print(item.select_one('p.prod_name > a').text.strip()) 
    print(item.select_one('p.prod_name > a').attrs['href'])   
    print(item.select_one('p.price_sect > a').text.strip())    
    # print(item.select_one('a.thumb_link > img')['data-source'])
    print(item.select('a.thumb_link > img')[0]['data-source'])

browser.quit()