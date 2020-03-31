"""
1. 라이브러리 임포트
    - https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference
    - v80 : https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.16/
2. 웹드라이버 세팅 - test 
3. 브라우저 내부대기 
4. 브라우저 사이즈 설정 
5. 로딩 
6. 가져온 페이지, 세션값, 타이틀, 현재 url, 쿠키 정보 출력 
7. 검색창 
    - input 선택 
    - 검색어 입력 
    - 제출 
8. 스크린샷 
    - 저장경로 설정
9. 브라우저 종료 
"""

from selenium import webdriver

browser = webdriver.Chrome('./webdriver/chromedriver.exe')
print(dir(browser))

browser.implicitly_wait(5)

# browser.set_window_size(1920, 1280)   # bug 
browser.maximize_window()

browser.get('https://www.daum.net')
# print(browser.page_source)
# print(browser.session_id)
# print(browser.title)
# print(browser.current_url)
# print(browser.get_cookies())

elem = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')
elem.send_keys('오늘의 날씨')
elem.submit()

browser.save_screenshot('C:/Users/CrePASS/Documents/GitHub/python-study-note/p02crawling-basic/c12browser_screenshot/img01.png')

browser.quit() 

