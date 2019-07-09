# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
from ScrapyTest.items import Example_thsItem

"""
此次爬虫的目的
1.获取 人名，董事会成员姓名
2.获取 性别信息
3.获取 年龄信息
4.获取 股票代码
5.获取 职位信息
将其以上5点的信息写入到文档中
"""



class ExampleThsSpider(scrapy.Spider):
    name = 'example_ths'
    allowed_domains = ['pycs.greedyai.com']
    start_urls = ['http://pycs.greedyai.com/']

    def parse(self, response):

        # 获取xpath：
        # // 代表 从匹配选择的当前节点来对文档中的节点进行选择  如：//a对节点a进行选择
        # @  代表 选取名称为某的所有属性 如：@href 选取名称为href的所有属性
        # /  代表 从根节点来进行选择元素
        # "//a/@href" -> 从节点a中的根节点选择名称href的所有属性
        xpath_str = "//a/@href"
        # 在 scrapy 的 shell 控制台调用 response 的 xpath() 方法来获取 XPath 匹配的节点
        urls_extract = response.xpath(xpath_str)
        # extract() 方法用于提取节点的内容
        urls = urls_extract.extract()
        for url in urls:
            # print(url)
            # 此时获取到的url无域名，对url的域名进行拼接
            # 需要导入 urllib(中的request)库
            # 第一个参数 url->请求连接 第二个参数 callback->回调函数 第三个参数dont_filter是否需要进行过滤
            # yield 交给某个东西进行处理
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.pase_detail, dont_filter=True)





    """
    1.解析链接详情 -> 2.创建Item进行解析 -> 3.
    """
    def pase_detail(self, response):
        item = Example_thsItem()
        # 1.获取 人名，董事会成员姓名
        user_names = self.get_username(response)
        item["names"] = user_names
        # 2.获取 性别信息
        item["sexs"] = self.get_sex(response)
        # 3.获取 年龄信息
        item["ages"] = self.get_age(response)
        # 4.获取 股票代码
        item["codes"] = self.get_code(response)
        # 5.获取 职位信息
        item["leaders"] = self.get_leader(response, len(user_names))
        # 获取到的数据 - == 进行写入到文件中
        yield item

    """
    1.0获取 人名，董事会成员姓名
    """
    def get_username(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        try:
            names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
            return names
        except(scrapy.exceptions.NotSupported):
            return []

    """
    2.获取 性别信息
    """
    def get_sex(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/div/table/thead/tr[2]/td[1]
        sexs = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/div/table/thead/tr[2]/td[1]/text()").extract()
        sex_list = []
        for sex_1 in sexs:
            try:
                # 正则表达式 进行获取 数据
                sex = re.findall("[男|女]", sex_1)[0]
                sex_list.append(sex)
            except(IndexError):
                continue
        return sex_list

    """
    3.获取 年龄信息
    """
    def get_age(self, response):
        age_list = []
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/div/table/thead/tr[2]/td[1]
        ages = response.xpath(
            "//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/div/table/thead/tr[2]/td[1]/text()").extract()
        for age_1 in  ages:
            try:
                age = re.findall("\d+", age_1)[0]
                age_list.append(age)
            except():
                continue
        return age_list

    """
    4.获取 股票代码
    """
    def get_code(self, response):
        codes = response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/h1/a/@title").extract()
        code_list = []
        for code_1 in codes:
            try:
                code = re.findall("\d+", code_1)[0]
                code_list.append(code)
            except():
                continue
        return code_list

    """
    5.获取 职位信息
    """
    def get_leader(self, response, length):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[2]
        leaders = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[2]/text()").extract()
        leader_list = []
        for i in range(0, length):
            leader_list.append(leaders[i])
        return leader_list

