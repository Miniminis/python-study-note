"""
ex url) https://blog.scrapinghub.com/

scrapy framework 
- scrapy 설치 : pip install scrapy 
- window 에서 발생하는 에러 : C++ 14.0 이상 필요 
    >> 방법 1: visual studio 2019 community version 설치 - c++ desktop, python development 포함 
    >> 방법 2: 비공식 파이썬 바이너리 페이지 이동 후 관련 휠 설치

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
    


"""
