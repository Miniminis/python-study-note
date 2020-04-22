# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ITArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()    
    
    #title 
    title = scrapy.Field()
    #image 
    image = scrapy.Field()
    #content
    content = scrapy.Field()

