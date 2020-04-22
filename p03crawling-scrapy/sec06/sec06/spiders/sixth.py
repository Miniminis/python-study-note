# -*- coding: utf-8 -*-
import scrapy
from ..items import ITArticle


class SixthSpider(scrapy.Spider):
    name = 'sixth'
    allowed_domains = ['itnews.com']
    start_urls = ['https://itnews.com/']

    """
    title, imageUrl, mainContents

    :param : response 
    :return : Request : 상세 내용 클릭을 위해 
    """

    def parse(self, response):
        
        for url in response.css('div.newsfeed div.news-item a::attr("href")').extract():
            # print(url)
            yield scrapy.Request(response.urljoin(url), self.parse_article)
    
    def parse_article(self, response):
        # print(response.text)

        item = ITArticle()
        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['image'] = response.xpath('//img[@itemprop="contentUrl"]/@src').get()
        item['content'] = ''.join(response.xpath('//div[@id="drr-container"]/p/text()').getall())
        
        yield item