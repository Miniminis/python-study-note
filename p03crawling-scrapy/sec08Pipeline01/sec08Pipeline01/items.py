# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SiteRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_num = scrapy.Field()
    site_name = scrapy.Field()
    remain_time = scrapy.Field()
    daily_page_views = scrapy.Field()
    search_trafic = scrapy.Field()
    total_click = scrapy.Field()
    is_shown = scrapy.Field()
