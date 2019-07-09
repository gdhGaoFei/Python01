# -*- coding: utf-8 -*-
import scrapy


class MafengwoTestSpider(scrapy.Spider):
    name = 'mafengwo_test'
    allowed_domains = ['www.mafengwo.cn/sitemapIndex.xml']
    start_urls = ['http://www.mafengwo.cn/sitemapIndex.xml/']

    def parse(self, response):
        # //*[@id="collapsible4"]/div[1]/div[2]/div[1]/span[2]
        pass
