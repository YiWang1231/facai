# -*- coding: utf-8 -*-
import scrapy


class VipdataSpider(scrapy.Spider):
    name = 'vipData'
    allowed_domains = ['https://blz.bicoin.com.cn']
    start_urls = ['http://https://blz.bicoin.com.cn/']

    def parse(self, response):
        pass
