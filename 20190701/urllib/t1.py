import requests
import random
import urllib3
from urllib.parse import urlencode


ua_list = ["User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
           "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
           "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]
ua = random.choice(ua_list)
base_url = "https://movie.douban.com/j/search_subjects"
params = {"type": "movie",
          "tag": "热门",
          "page_limit": 10,
          "page_start": 10}
url = "{}?{}".format(base_url, urlencode(params))

# 连接池管理器
with urllib3.PoolManager() as http:
    # 需要进行忽略 SSL证书
    response = http.request("GET", url, headers={
        "User-agent": ua
    })
    print(type(response))

# req = requests.request("GET", "")