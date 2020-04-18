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
"""