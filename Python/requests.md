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

## 01 发送请求

### 1.1 GET

- 当URL参数不多的时候，可以这样
`requests.get('http://baidu.com')`

- 当参数多的时候，可以通过一个dic来传递参数，使其自动构造URL

```python
paydict = {'key1':'value1','key2':'value2'}
r = requests.get('http://baidu.com',params=paydict')
```

### 1.2 POST

## 02 响应内容

**返回值r是Response对象**

- r.encoding 编码，这个可以自己设置

- r.text 返回文本形式内容

- r.content 返回二进制形式内容

- r.raw 返回原始内容

## 03 Misc

### 3.1 requests 请求资源的高效利用

requests 底层是 http，http 底层是 tcp。

遇到一个问题： 当使用爬虫爬取数据，如何在爬取多个 url 时，充分利用资源：

参考：

1. [stackoverflow](https://stackoverflow.com/questions/10115126/python-requests-close-http-connection)
2. [requests docs](https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#session-objects)

当在爬虫过程中使用多线程爬取内容时，往往会出现 `too many open files` 的 error,

- TCP 在建立连接后，默认会保持一段时间的连接，当我们使用以下代码把网页内容 pull 下来后，我们需要及时关闭连接。

```python
response = requests.get(url, proxies=proxies, headers=headers, timeout=timeout)
response_content = response.content
# 无论 get/post 方法，均可以使用 close() 关闭连接
response.close()
# 或者使用 with-statement 管理 context
with requests.get(url, proxies=proxies, headers=headers, timeout=timeout) as r:
    response_content = response.content
```

- requests 中的 `session` 对象，可以在一个会话中保持一些请求的参数，借用官方文档：

> 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。 (参见 HTTP persistent connection).

```python
# 使用 with-statement
with requests.Session() as s:
    s.get('http://google.com')

# 或使用 close() 方法
s = requests.Session()
r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
s.close()
```