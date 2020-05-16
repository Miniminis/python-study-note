# -*- coding: utf-8 -*-
import scrapy

class GplaySpider(scrapy.Spider):
    name = 'gplay'
    # allowed_domains = ['https://play.google.com/apps/publish/?hl=ko']
    # start_urls = ['https://https://play.google.com/apps/publish/?hl=ko/']
    allowed_domains = ['https://www.naver.com']
    start_urls = ['https://www.naver.com']

    def authentication_failed(response):
        logger.info("호출 : authentication_failed(response)")

    def parse(self, response):
        self.logger.info("구글 로딩 성공 : ")
        
        return scrapy.FormRequest.from_response(
            response, 
            formdata={'id': 'id', 'pw' : 'pw'},
            callback=self.after_login
        )    
    
    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("로그인에 실패하였습니다.")
            return
        
        self.logger.info("로그인에 성공하였습니다.")


