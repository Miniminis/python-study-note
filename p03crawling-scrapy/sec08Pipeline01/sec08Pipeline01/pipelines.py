# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class SiteRankPipeline(object):

    def open_spider(self, spider):
        spider.logger.info('===========SITE RANK SPIDER STARTED=======================')

    def process_item(self, item, spider):
        if(int(item.get('rank_num')) <= 10):
            item['is_shown'] = True
            return item
        else:
            item['is_shown'] = False
            raise DropItem(f'Dropped Because its ranking is {item.get("rank_num")}')
    
    def close_spider(self, spider):
        spider.logger.info('===========SITE RANK SPIDER CLOSED=======================')

