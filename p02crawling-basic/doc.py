"""
# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑
1. import urllib.request
2. set img_url
3. 저장할 경로를 확장자 및 저장이름과 함께 명시 - save_path1
4. try
    req.urlretrieve(img_url, save_path1) 
        - file1, header1 
5. catch 
    - exception 
    else 
    - header 정보 및 file 정보 출력
    - download succeed!



# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법
1. import urllib.request, urllib.error (HttpError, UrlError)
2. target url in array, save path with ex in array
3. for loop with enumerate(target_url)
    - try 
        - res = req.urlopen(url) : urlopen 함수는 모든 프로세스가 수동설정임
        - contents = res.read() : 수신 내용 읽기
        - res.info(), res.getcode()
        - 파일 쓰기 
            with open(save_pathlist[i], 'wb') as c: 
                c.write(contents)
    - except HttpError : e.code
    - except UrlError : e.reason 
    - else : 성공!



# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)
1. import requests, lxml.html 
2. main():
    res = requests.get("url")
    urls = scrap_url(res)
    print(urls)
3. scrap_url(res):
    - urls []
    - root = lxml.html.fromstring(res.content)
    - a = root.cssselect('') 
    - a.get('href') >> urls.append()




# Section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)
1. import requests, from lxml.html import fromstring, tostring
2. main()
    res = requests.get('url')
    urls = scrap_url(res)
    for name, url in urls.items():
        print(name, url)
3. scrap_url(res):
    urls = {}
    root = fromstring(res.content)
    for a in root.xpath()
        name, url = extract_contents(a)'
        urls[name] = url
4. extract_contents(a):
    url = a.get('href')
    name = a.xpath('')
    return name, url




# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)
1. import urllib.request, urllib.parse 
2. 기본 API 주소 세팅
3. API 뒤에 넘겨줄 parameter 세팅 
4. parameter url 형태로 인코딩
5. API 주소 + param url = 새로운 API 생성
6. data = 새 API 로 request.urlopen(url).read()
7. text = data.decode('utf-8)

# Section03-2
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(2) - 행안부 RSS
- param 을 dictionary 에 미리 세팅해놓은 뒤 반복문으로 url 동적으로 만들기

# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기
- from fake_useragen import UserAgent



# Section04-1
# Requests
# requests 사용 스크랩핑(1) - Session
1. import requests
2. s = requests.Session()
3. s.get('url')
4. Cookie 
    res = s.get('url', cookies={'name' : 'niceman'})
5. User-Agent
    r = s.get(url, headers=headers)
* 참고 : with 문 사용하면 따로 session.close() 를 해주지 않아도 되서 편리함

# Section04-2
# Requests
# requests 사용 스크랩핑(2) - Json
- 수신데이터 dict 변환
- dict 데이터 b = json.load(line) 으로 json 타입변환
- for k, v in b.items() 로 key, value 확인

# Section04-3
# Requests
# requests 사용 스크랩핑(3) - Rest API
- RestApi CRUD 




# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법
1. from bs4 import BeautifulSoup
2. soup = BeautifulSoup(html, 'html.parser')
    - soup.prettify()
    - p1 = soup.html.body.p
3. find, find_all : 
    - link2 = soup.find("a", {"class": "sister", "data-io": "link3"})
4. select, select_one
    - link1 = soup.select_one("p.title > b")

"""
