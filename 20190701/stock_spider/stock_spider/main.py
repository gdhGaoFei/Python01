from scrapy.cmdline import execute
import sys
import os


"""
学习网址：https://ke.qq.com/webcourse/index.html#cid=320330&term_id=100380209&taid=2576340427793226&vid=u142831q21g
"""

"""
进行调试
"""

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "tonghuashun"])