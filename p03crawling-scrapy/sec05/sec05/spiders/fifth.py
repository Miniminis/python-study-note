# -*- coding: utf-8 -*-
import scrapy


class FifthSpider(scrapy.Spider):
    name = 'fifth'
    allowed_domains = ['w3schools.com']
    start_urls = ['http://www.w3schools.com/']

    # nav 메뉴 이름 크롤링 실습
    # 쉘 실행 -> 선택자 확인 -> 코딩 -> 데이터 저장
    def parse(self, response):        
        # navlist = response.css('div.w3-bar-block a::text').getall()
        navlist = response.xpath('//div[@class="w3-bar-block"]//a/text()').extract()

        for i, item in enumerate(navlist, 1):
            # print("{}. {}".format(i, item))
            yield {
                "index" : i,
                "topic" : item
            }


