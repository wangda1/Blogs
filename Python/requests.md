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
3. [Python: requests 详解超时和重试](https://www.cnblogs.com/gl1573/p/10129382.html)

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

使用 `session` 的目的还是利用 `session` 的 `connection pool` 功能，可以高效地复用链接。

```python
# 使用 with-statement
with requests.Session() as s:
    s.get('http://example.com/aaa')
    s.get('http://example.com/bbb')
    s.get('http://example.com/ccc')

# 或使用 close() 方法
s = requests.Session()
s.get('http://example.com/aaa')
s.get('http://example.com/bbb')
s.get('http://example.com/ccc')
s.close()
```

- 同时还应该及时清理建立连接较慢和返回较慢的连接，以提高爬虫的效率，主要使用的手段是 `timeout` 与 `max_retries`

    `timeout` 应注意其可以为（连接超时，读取超时）：连接超时指建立连接的最大时间，读取超时指收到服务器回复的最大时间，也可单独设置。

```python
def get_response(url, proxies, headers, timeout=(5, 10), max_retries=3):
    """
    存在连接时间较长阻塞的情况，这里设置 timeout, max_retries
    :param url: 请求的 url
    :param proxies:
    :param header:
    :param time_out: (connect_time_out, read_time_out)
    :param max_retries: 重试次数
    :return:
    """
    i = 0
    while i < max_retries:
        try:
            response = requests.get(url, proxies=proxies, headers=headers, timeout=timeout)
            response_content = response.content
            response.close()
            return response_content
        except requests.exceptions.RequestException as e:
            log.error('{} times request'.format(i+1) + str(e) + url)
        i += 1
    return None
```