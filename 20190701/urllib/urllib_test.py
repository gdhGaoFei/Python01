from urllib.request import urlopen, Request
import random
from urllib import parse

url = "http://www.bing.com"
"""
User-Agent 问题 【总结】浏览器 User-Agent 大全：https://blog.csdn.net/u012195214/article/details/78889602
"""
ua_list = ["User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
           "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
           "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

# 选择某一个 user-agent
ua = random.choice(ua_list)

# 修改 User-Agent
# req = Request(url, headers={'User-agent': ua})
req = Request(url)
req.add_header("User-agent", ua)


# data->GET请求 data不为nil则是post请求
response = urlopen(req, timeout=5) # urlopen(url, timeout=6)
print(response.closed)

with response:
    print(type(response))
    print(response.status)
    # 私有属性 一般不让访问
    print(response._method)
    # 内容读取一下
    print(response.read())
    # 真正的网址
    print(response.geturl())
    # 信息
    print(response.info())

print(req.get_header("User-agent"))
print(response.closed)




"""
urllib.parse 模块 对url编解码
"""



