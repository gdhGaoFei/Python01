# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
from stock_spider.items import StockThsItem

class StockThsSpider(scrapy.Spider):
    name = 'stock_ths'
    allowed_domains = ['pycs.greedyai.com/']
    start_urls = ['http://pycs.greedyai.com/']


    # 获取主页面中的子界面 进行解析
    def parse(self, response):
        # // 从匹配选择的当前节点来对文档中的节点进行选择
        # /  从跟节点来进行选择元素
        # @  选择属性
        xpath_str = "//a/@href"
        a_all_href = response.xpath(xpath_str)
        # print(a_all_href)
        # 爬虫到的所有的连接
        post_urls = a_all_href.extract()
        print(post_urls)
        # 进行解析
        for post_url in post_urls:
            # 需要进行域名的拼接 第一参数url 第二个参数callback 回调函数 第三个参数dont_filter是否需要进行过滤
            # yield: 交给某个东西进行处理
            yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.pase_detail, dont_filter=True)
        pass


    # 对子界面中的数据 进行解析
    def pase_detail(self, response):
        # print("回调函数被调用了")
        stock_ths_item = StockThsItem()
        # 获取人名 董事会成员姓名
        stock_ths_item["names"] = self.get_tc(response)
        # 抓取 性别信息
        stock_ths_item["sexes"] = self.get_sex(response)
        # 抓取 年龄信息
        stock_ths_item["ages"] = self.get_age(response)
        # 抓取股票代码
        stock_ths_item["codes"] = self.get_code(response)
        # 职位信息
        stock_ths_item["leaders"] = self.get_leader(response, len(stock_ths_item["names"]))
        # 文件存储逻辑
        yield stock_ths_item

    # 获取人名 董事会成员姓名
    def get_tc(self, response):
        # xpath: //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        # * 匹配任何元素的节点
        # [] 选取所有带有属性的 元素
        names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
        return names

    # 抓取 性别信息
    def get_sex(self, response):
        #
        sexes = response.xpath("//*[@class = \"intro\"]/text()").extract()
        tc_sexes = []
        for sex in sexes:
            try:
                re_sex = re.findall("[男|女]", sex)[0]
                tc_sexes.append(re_sex)
            except(IndexError):
                continue
        return tc_sexes

    # 抓取 年龄信息
    def get_age(self, response):
        ages = response.xpath("//*[@class = \"intro\"]/text()").extract()
        tc_ages = []
        for age in ages:
            try:
                re_age = re.findall("\d+", age)[0]
                tc_ages.append(re_age)
            except(IndexError):
                continue
        return tc_ages

    # 抓取股票代码
    def get_code(self, response):
        codes = response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/h1/a/@title").extract()
        code_list = []
        for code in codes:
            try:
                re_code = re.findall("\d+", code)[0]
                code_list.append(re_code)
            except(IndexError):
                continue
        return code_list

    # 职位信息
    def get_leader(self, response, length):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[2]
        leaders = response.xpath("//*[@class = \"tl\"]/text()").extract()
        leaders = leaders[0:length]
        return leaders
