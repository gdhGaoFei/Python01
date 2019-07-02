# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'

    # 域名
    allowed_domains = ['stockpage.10jqka.com.cn']
    # 爬虫地址 - 迷糊地址
    # start_urls = ['http://stockpage.10jqka.com.cn/400002/company/#detail/']
    # 爬虫地址 - 真正的地址
    start_urls = ["http://basic.10jqka.com.cn/400002/company.html"]

    def parse(self, response):

        # xpath: //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        #        //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        xpath_str = "//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a"
        # 拿去 文本值
        xpath_str_name = xpath_str+"/text()"
        xpath_str = xpath_str_name

        res_selector = response.xpath(xpath_str)
        print(res_selector)

        # 拿到真正的名字
        name = res_selector.extract()
        print(name)

        tc_names = response.xpath("//*[@class = \"tc name\"]/a/text()").extract()
        for tc_name in tc_names:
            print(tc_name)

        tl_names = response.xpath("//*[@class = \"tl\"]/text()").extract()
        for tl_name in tl_names:
            print(tl_name)

        pass
