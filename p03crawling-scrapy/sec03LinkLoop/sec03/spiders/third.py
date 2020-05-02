# -*- coding: utf-8 -*-
import scrapy


class ThirdSpider(scrapy.Spider):
    name = 'third'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Request 
        """

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            # url 바로 사용하는 것보다, urljoin() 이용 (상대경로 대응)
            # print(url)
            yield scrapy.Request(response.urljoin(url), self.parse_title)
        

    def parse_title(self, response):
        """
        상세페이지 > 타이틀 추출 
        :param : response
        :return Text
        """

        contents = response.css('div.post-body > span > h2::text').extract()[:10]  #getall()
        # print(contents)
        yield {
            'contents' : contents
        }