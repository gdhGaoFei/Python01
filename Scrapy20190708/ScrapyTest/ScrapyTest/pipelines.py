# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        return item



class Example_thsPipeline(object):
    file_name = "example_pre.csv"

    # 构造函数 -> 创建时 即创建文件
    def __init__(self):
        # a+：代表拿到文件的读写权限，然后追加写入文件，没有文件时则创建
        self.file = open(self.file_name, "a+")

    def process_item(self, item, spider):

        # 将其以上5点的信息写入到文档中

        # 1.类被加载时 要创建一个文件
        # 2.判断文件是否为空，为空时，则把 高管姓名，性别，年龄，股票代码，职位 写入第一行
        # 3.不为空时 则追加写入文件
        # 判断文件是否为空
        if os.path.getsize(self.file_name):
            # 开始写入文件
            self.write_content(item)
        else:
            # 向文件中写入头信息
            self.file.write("高管姓名，性别，年龄，股票代码，职位\n")

        self.file.flush()

        return item


    """
    写入文件
    """
    def write_content(self, item):
        # 1.获取 人名，董事会成员姓名
        names = item["names"]
        # 2.获取 性别信息
        sexs = item["sexs"]
        # 3.获取 年龄信息
        ages = item["ages"]
        # 4.获取 股票代码
        codes = item["codes"]
        # 5.获取 职位信息
        leaders = item["leaders"]
        # 内容 待 写入的内容
        content = "\n"
        for i in range(len(names)):
            content = names[i] + "，" + sexs[i] + "，" + ages[i] + "，" + codes[i] + "，" + leaders[i] + "\n"
        self.file.write(content)
        # 打印数据
        print(content)
        pass
