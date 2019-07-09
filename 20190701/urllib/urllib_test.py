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
from urllib import parse
import simplejson
from urllib.parse import urlencode


d = {"url": 'http://www.magedu.com/python',
     "p_url": 'http://www.magedu.com/python?id=1&name=张三'}
u = parse.urlencode(d)
print(u)

params = {"wd": "中"}  # 编码
u_1 = parse.urlencode(params)
url = "http://www.baidu.com/s?{}".format(u_1)
print(url)

print('中'.encode('utf-8'))

print(parse.unquote(u_1))  # 解码
print(parse.unquote(url))

"""
提交请求 - GET和POST请求
"""
keyword = input(">> 请输入搜索关键字:")
data = urlencode({
    'q': keyword
})
base_url = "http://cn.bing.com/search"
url_1 = "{}?{}".format(base_url, data)
print(url_1)

# 伪装 -
ua_url = random.choice(ua_list)
request = Request(url_1, headers={"User-agent": ua_url})
response = urlopen(request)
with response:
    with open("bing.html", "wb") as f:
        f.write(response.read())
print("成功")


# POST请求 http://httpbin.org
url_post = "http://httpbin.org/post"
request_post = Request(url_post)
request_post.add_header(
    "User-agent", "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
)
data = urlencode({'name': "张三,@=/&*", 'age': '6'})
print(data)
response_post = urlopen(request_post, data=data.encode())  # POST方法，Form提交数据
with response_post:
    data_re = response_post.read()
    print(data_re)
    dict1 = simplejson.loads(data_re)
    print(type(dict1))
    print(dict1)




"""
robots协议
淘宝：http://www.taobao.com
"""

"""
AJAX
"""


import urllib3

with urllib3.PoolManager() as http:
    response = http.request("GET", url=url_1, headers={
        'User-agent': ua
    })
    print(type(response))
    print(response.status)
    print(response.data)







