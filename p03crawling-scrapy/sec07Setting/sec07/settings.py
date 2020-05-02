# -*- coding: utf-8 -*-

# Scrapy settings for sec07 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sec07'

SPIDER_MODULES = ['sec07.spiders']
NEWSPIDER_MODULE = 'sec07.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sec07 (+http://www.yourdomain.com)'

# Obey robots.txt rules 
# 타겟 사이트의 robots.txt 준수 여부 
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 병렬 처리 : 컴퓨터 사양이 좋다면, 32로 올려도 될듯 
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 다운로드 딜레이 : 꼭 설정해야함. 크롤링 주기 설정하는 것. 서버에 무리가 안가도록 여유있게 설정해야함. 
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# 웹사이트 도메인 동시병렬 처리 개수 
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 특정 웹사이트 IP 주소 병렬 처리 개수 
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 쿠키 활성화 여부 
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 기본 request header 값 설정  
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 내장 미들웨어 사용 여부
#SPIDER_MIDDLEWARES = {
#    'sec07.middlewares.Sec07SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 특정 다운로드 미들웨어 사용 
#DOWNLOADER_MIDDLEWARES = {
#    'sec07.middlewares.Sec07DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 파이프 라인 설정 
#ITEM_PIPELINES = {
#    'sec07.pipelines.Sec07Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 인증 
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 매일매일 큰 변화가 없는 사이트를 주기적으로 크롤링 할때 : 
#   1) 우선 캐시 서버를 뒤져서 콘텐츠 가져오고 
#   2) url 로 직접 이동해서 바뀐 컨텐츠 가져온다.  
# 캐시 사용 여부 : 동일하게 여러번 요청 시 서버사이드에 부하 절감 가능 : 변동사항 없을 경우 
# HTTPCACHE_ENABLED = True
# 캐시 유효 기간 
# HTTPCACHE_EXPIRATION_SECS = 6000
# 캐시 저장 경로 
# HTTPCACHE_DIR = 'httpcache'
# 응답 거부 캐시 
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 오류 처리 
# 자동 재시도 설정
# 서버쪽 오류로 인해 접근이 실패했을 때, 자동으로 재시도 함 
RETRY_ENABLED = True

# 재시도 최댓값
RETRY_TIMES = 2

# 재시도 대상 http 코드 
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 404]

# 오류 무시 HTTP 상태 코드 
HTTPERROR_ALLOWED_CODES = [404]

# 모든 상태 코드 오류 무시 : 비추천  
# HTTPERROR_ALLOW_ALL = False


# 출력(export setting)
# 파일 이름 및 경로 : json, jsonlines, csv, xml, pickle, marshal 등 
# FEED_URI = 'result.json'
# 파일형식
# FEED_FORMAT ='json'
# 출력 인코딩 
# FEED_EXPORT_ENCODING = 'utf-8'
# 기본 들여쓰기 
# FEED_EXPORT_INDENT = 0
# 저장소, 저장형식 관련 레퍼런스 
# https://docs.scrapy.org/en/latest/topics/feed-exports.html#feed-storages
