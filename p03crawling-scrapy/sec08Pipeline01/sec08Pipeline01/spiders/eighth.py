# -*- coding: utf-8 -*-
import scrapy
from ..items import SiteRankItem

"""
전세계에서 가장 접속 횟수가 많은 웹 사이트들의 랭킹을 모아놓은 사이트 
40위권 이상의 것만 출력 및 저장하고자 한다. 

조건 
- settings(V), item(v), pipeline 설정 사용해보기 
"""

class EighthSpider(scrapy.Spider):
    name = 'eighth'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://alexa.com/topsites/']

    def parse(self, response):
        for list in response.css('div.listings.table > div.tr.site-listing'):
            # print(list)
            item = SiteRankItem()
            item['rank_num'] = list.css('div.td::text').get()
            item['site_name'] = list.css('div.td.DescriptionCell > p > a::text').get()
            item['remain_time'] = list.css('div.td.right > p::text').getall()[0]
            item['daily_page_views'] = list.css('div.td.right > p::text').getall()[1]
            item['search_trafic'] = list.css('div.td.right > p::text').getall()[2]
            item['total_click'] = list.css('div.td.right > p::text').getall()[3]
            yield item

        


