"""
ex url) https://blog.scrapinghub.com/

scrapy framework 
- scrapy 설치 : pip install scrapy 
- window 에서 발생하는 에러 : C++ 14.0 이상 필요 
	>> 방법 1: visual studio 2019 community version 설치 - c++ desktop, python development 포함 
	>> 방법 2: 비공식 파이썬 바이너리 페이지 이동 후 관련 휠 설치 
	- https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
	- file name : Twisted-20.3.0-cp38-cp38-win32.whl

- 가장 널리 사용되고 있는 프레임워크
- 확장성은 좋음, 분산처리 불가
- 비동기 크롤링 - 따로 작업 필요 


scrapy command
- scrapy startproject [project name] : 새로운 프로젝트 생성 
- scrapy genspider [spider name] [crawling 대상 url] 
	: spider 엔진을 생성. scrapy.cfg 와 같은 위치에서 실행함
- scrapy runspider [spider 파일 이름]: spider 실행. spider 가 위치한 디렉토리로 이동하여 실행함. 
- scrapy crawl [spider name]: spider 를 실행. scrapy.cfg 와 같은 위치에서 실행함 
- --no log : scrapy 의 기본 로그 생략  


result 
- scrapy crawl [spider name] -o 파일명.확장자 -t 파일타입(json, jsonlines, jl, csv, xml, marshal, pickle)
- scrapy crawl [spider name] -o result.jl -t jsonlines   # json line 형식으로 크롤링 결과 표현
- scrapy crawl [spider name] -o result.csv -t csv            # csv 형식으로 저장



링크 순회 : main page >> detail page 클릭 후 크롤링 반복 동작 


Shell 
- scrapy 에서 지원하는 shell mode 
- command
	1) scrapy shell ['domain']
	2) scrapy shell >> fetch('domain')
- 간이테스트에 용이 
- fetch : scrapy shell >> fetch('domain'). url 변경시 용이.
- view : 현재 response 페이지 브라우저에서 확인
- response : 크롤링 요청에 대한 응답 
- request : 크롤링 요청

[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x0491E850>
[s]   item       {}
[s]   request    <GET https://blog.scrapinghub.com>
[s]   response   <200 https://blog.scrapinghub.com>
[s]   settings   <scrapy.settings.Settings object at 0x0491E7C0>
[s]   spider     <ThirdSpider 'third' at 0x506fec8>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser


dir(response) : response 에 대해서 쓸 수 있는 명령어, 함수들의 리스트 

scrapy shell [domain] [option]
- scrapy shell https://daum.net --set "ROBOTSTXT_OBEY=False" 


spider attribute 
- multi domain : 동시에 여러 사이트 크롤링을 하고 싶을때 
	1) start_urls 내에서 나열하여 parse 함수에서 분기처리 
	2) start_requests(self) 라는 이미 정의된 함수 내에서 각각의 도메인에 대해서 parse 함수 정의
		- 각각 별개의 parse 함수로 받아서 처리할 수도 있음 
- logger : 
	1) python lib logger  
	2) scrapy 내부의 logger 
- response 분기 :
	


scrapy - selector 
- 도움되는 사이트 : 
	- https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
	- http://www.nextree.co.kr/p6278/
	- https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors
	- https://www.w3schools.com/python/python_regex.asp
	- 타겟 데이터는 크롬 개발자 도구 사용
	- 선택자 연습 팁 : scrapy shell에서 테스트(효율성)
	- scrapy shell 도메인

CSS 선택자 복습 
    - A B : 자손 
    - A > b : 바로 하위의 자식
    - ::text : 노드 텍스트만 추출 
    - ::attr(name) : 노드 속성값 추출 
    - get() : single 
    - get(default='') : default 값 설정 가능  (null 일 경우 대비)
    - getall() : list 
     # 예)
    # response.css('title::text').get() : 타이틀 태그의 텍스트만 추출
    # response.css('div > a::attr(href)').getall() : div 태그의 자식 a 태그 href 속성 값 전부 추출

Xpath selector 
    - nodename : 이름이 nodename 선택 
    - text() : 노드 텍스트만 추출 
    - / : 루트부터 시작 
    - //: 현재 노드부터 문서상의 모든 노드 조회 
    - . : 현재 노드 
    - .. : 현재 노드의 부모노드 
    - @ : 속성 선택자 
    - extract(), extract_first()

    # 예)
    # response.xpath('//div') : 루트 노드부터 모든 div 태그 선택
    # response.xpath('//div[@id="id1"]/a/text()').get() : div 태그 중 id가 'id1' 인 자식 a 태그의 텍스트 추출

    # 중요
    # get() == extract_first()
    # getall() == extract()

    # 혼합 사용 가능
    # response.css('img').xpath('@src').getall()


- for i, item in enumerate(navlist, 1): index 1 부터 
- for i, item in enumerate(navlist): index 0 부터 


scrapy - items 
- 장점 
1. 수집 데이터 일관성 있게 관리 가능 
2. 데이터를 사전형으로 관리 가능, 오타 방지
3. 추후 가공 및 DB 저장이 용이하다. 

- response.urljoin(url) :  
	- a 태그가 상태경로로 되어있을때 root url 까지 연결시켜주는 함수 


scrapy - exports 
내가 원하는 형식, 저장위치에 자동으로 스크래핑 결과가 적용이 되도록 설정하는 것 
-o ?
- 형식: 
	- json, json lines
	- csv
	- xml, pickle, marshal 
- 저장위치 : 
	- local file system : my pc
	- ftp - server
	- s3 - aws(amazon)
	- 기본 콘솔 

- 2가지 방법 : 
	1. command 
		: --output or -o
		: --output-format or -t
	옵션설정 : --set=FEED_EXPORT_INDENT = 2
	
	2. Settings.py 이용 : 자동 저장(파일명, 형식, 위치 등) 
		참고 )  C:\Users\minhe\Documents\GitHub\python-study-note\p03crawling-scrapy\sec06_copy\sec06_copy\settings.py

scrapy - settings
참고 ) C:\Users\minhe\Documents\GitHub\python-study-note\p03crawling-scrapy\sec07\sec07\settings.py

1. 다양한 실행방법 
	1. 커맨드 라인 실행 : scrapy crawl [크롤러 명] -s(--set) <NAME>=<VALUE>
	2. 스파이더 실행시 직접 지정 : 
		custom_settings = {
			'DOWNLOAD_OBEY' = 2
		}
	3. settings.py 에 지정 : 추천방법
	4. 서브 명령어 : 신경 X 
	5. 글로벌 설정 : scrapy.settings.default_settings

2. 각 설정 항목 상세 설명 
3. 뉴스 사이트 크롤링 연습 
4. 기타 항목 : 캐시, 미들웨어 


scrapy - pipeline
1. 파이프라인?
- 이미지 아키텍쳐 저장 
2. 설명 및 메소드 
3. amaxon alexa 크롤링 연습 
4. validation 추가 및 테스트 : 일정 조건에 맞는 데이터만 저장 및 출력

5. pipeline 초기화 매서드 
6. item csv 저장 
7. item excel 저장 
8. pipeline 요약 설명 
"""
