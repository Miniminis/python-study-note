# -*- coding: utf-8 -*-
import scrapy


class SecondSpider(scrapy.Spider):
    name = 'second22'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : title text 
        """

        # get(), extract_first()
        # getall(), extract() 

        # 1. css selector 이용 
        # for text in response.css('div.post-header h2 a::text').getall(): # a tag의 text 만 추출 가능
        #     # return type : request, baseitem, dictionary, none
        #     yield {
        #         'title' : text
        #     }

        # 2. xpath
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            yield {
                'number' : i,
                'title' : text
            }
        
        
