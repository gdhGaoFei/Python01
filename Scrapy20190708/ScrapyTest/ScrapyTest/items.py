# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass




class Example_thsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 姓名
    names = scrapy.Field()
    # 性别
    sexs = scrapy.Field()
    # 年龄
    ages = scrapy.Field()
    # 股票代码
    codes = scrapy.Field()
    # 职位
    leaders = scrapy.Field()


