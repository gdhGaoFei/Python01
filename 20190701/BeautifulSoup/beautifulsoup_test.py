from bs4 import BeautifulSoup #python的第三方库
import re #正则表达式

"""
使用BeautifulSoup加载HTML
"""
html_doc = "/Users/gaodehua/Desktop/tonghuashun002.html"
html_file = open(html_doc, "r", encoding="GBK")
html_handle = html_file.read()
soup = BeautifulSoup(html_handle, "html.parser")
# print(soup)

"""
取出文档头
"""
# print(soup.head)
# print(soup.p)

"""
获取节点中的属性
"""
# print(soup.p.attrs)

"""
打印所有的节点
"""
# ps = soup.find_all("p")
# print(ps)

"""
id="quotedata"
"""
# ids = soup.find_all(id="quotedata")
# print(ids)

"""
按照css来搜索
"""
# jobs = soup.find_all("td", class_ = "jobs")
# print(jobs)

"""
<a class="turnto">汪剑</a>
"""
names = soup.find_all("a", class_="turnto")
print(names)
r = re.findall(">(.{2,5})</a>", str(names))
print(r)



