'''
什么是beautifulSoup
是一个可以从HTML或者xml文件中提取数据的一个Python库

安装命令：
pip install beautifulSoup4

'''

from bs4 import BeautifulSoup

html_doc = "test0001.html"
html_file = open(html_doc, "r", encoding="utf-8")
html_handle = html_file.read()

# beautifulsoup默认解析的文本 utf-8
soup = BeautifulSoup(html_handle, "html.parser")
print(soup)

print("----------")
# 获取HTML的文档头信息
# print(soup.head)

print("----------")
# 获取div节点 div
print(soup.div)
# 获取div节点中的属性
print(soup.div.attrs)

# 获取所有的div标签
divAll = soup.find_all("div")
print(divAll)