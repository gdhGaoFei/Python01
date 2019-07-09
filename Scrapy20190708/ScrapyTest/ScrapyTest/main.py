from scrapy.cmdline import execute
import sys
import os

"""
进行调试 - ==== 
"""
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "example_ths"])

