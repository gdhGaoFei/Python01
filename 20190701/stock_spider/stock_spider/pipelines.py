# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class StockSpiderPipeline(object):
    def process_item(self, item, spider):
        return item



# 文件处理 自定义的pipeline
class StockThsPipeline(object):

    # 构造函数
    def __init__(self):
        # a+: 拿到文件的读写权限,然后追加写入文件，没有则创建
        self.file = open("executive_prep.csv", "a+")

    def process_item(self, item, spider):

        #  类被加载时要创建一个文件
        # 判断文件是否为空 为空时 高管姓名，性别，年龄，股票代码，职位
        # 不为空那么我就追加写入文件
        # 判断文件是否为空
        if os.path.getsize("executive_prep.csv"):
            # 开始写入文件
            self.write_content(item)
        else:
            # 向文件中写入 头信息
            self.file.write("高管姓名，性别，年龄，股票代码，职位\n")

        # 刷新文件 - 防止文件没有被写入磁盘中
        self.file.flush()

        return item

    def write_content(self, item):
        names = item["names"]
        sexes = item["sexes"]
        ages = item["ages"]
        codes = item["codes"]
        leaders = item["leaders"]

        result = ""
        for i in range(len(names)):
            result = names[i]+"，"+sexes[i]+"，"+ages[i]+"，"+codes[i]+"，"+leaders[i]+"\n"
            self.file.write(result)
