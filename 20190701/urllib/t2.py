import requests


"""
斗图网
"""

url = "http://www.doutula.com/photo/list/?page=2"
html = requests.get(url).text
print(html)