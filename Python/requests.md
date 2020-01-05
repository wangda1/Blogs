---
title: requests
date: 2019-11-08 19:09:36
categories:
- Python
tags:
- Python
---

# Requests

python requests模块使用：

官方文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

`import requests`
## 发送请求

**1.GET**
- 当URL参数不多的时候，可以这样
`requests.get('http://baidu.com')`
- 当参数多的时候，可以通过一个dic来传递参数，使其自动构造URL
```
paydict = {'key1':'value1','key2':'value2'}
requests.get('http://baidu.com',params=paydict')
```


**2.POST**


## 响应内容
**返回值r是Response对象**

- r.encoding 编码，这个可以自己设置

- r.text 返回文本形式内容

- r.content 返回二进制形式内容

- r.raw 返回原始内容
