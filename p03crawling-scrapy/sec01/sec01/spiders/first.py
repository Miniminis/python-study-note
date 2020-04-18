# -*- coding: utf-8 -*-
import scrapy

class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['https://blog.scrapinghub.com/']
    start_urls = ['https://blog.scrapinghub.com//']     # 여러개의 사이트 병렬로 지정 가능

    def parse(self, response):
        # print('dir', dir(response))
        print('status', response.status)
        # print('text', response.body)
