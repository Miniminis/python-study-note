# -*- coding: utf-8 -*-
import scrapy


class SeventhSpider(scrapy.Spider):
    name = 'seventh'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):
        """
        :param : response
        :return : titles, contents
        """

        for i, title in enumerate(response.css('div.post-excerpt-container > h3.post-title > a::text').getall(), 1):
            # print("{} : {}".format(i, title))
            
            # yield {
            #     'num' : i,
            #     'headline' : title
            # }
            
            yield dict(num=i, headline=title)
            
