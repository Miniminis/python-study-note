# -*- coding: utf-8 -*-
import scrapy
# import logging

# logger = logging.getLogger('MhLogger')

"""
spider 종류 
1. CrawlSpider
2. XMLFeedSpider
3. CSVFeedSpider
4. SitemapSpider 
"""

class FourthSpider(scrapy.Spider):
    name = 'fourth'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']

    # multi-domain 1)
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    # settings.py 의 내용을 overriding
    custom_settings = {
        'DOWNLOAD_DELAY' : 1,
        'ROBOTSTXT_OBEY' : False
    }

    # multi-domain 2) 
    # def start_requests(self):
    #     yield scrapy.Request('https://blog.scrapinghub.com/', self.parse)
    #     yield scrapy.Request('https://naver.com/', self.parse)
    #     yield scrapy.Request('https://daum.net/', self.parse)

    def parse(self, response):
        # logger.info('Response URL :::::: %s' %response.url)
        # logger.info('Response STATUS :::::: %s' %response.status)

        self.logger.info('Response URL :::::: %s' %response.url)
        self.logger.info('Response STATUS :::::: %s' %response.status)

        if response.url.find('scrapinghub'):
            yield {
                'sitemap' : response.url,
                'contents' : response.text[:100]
            }
        elif response.url.find('naver'): 
            yield {
                'sitemap' : response.url,
                'contents' : response.text[:100]
            }
        else:
            yield {
                'sitemap' : response.url,
                'contents' : response.text[:100]
            }

