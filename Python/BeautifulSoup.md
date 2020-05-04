---
title: BeautifulSoup 教程
date: 2020-04-28 11:10:00
categories:
- Python
tags:
- Python
---

# BeautifulSoup

```python
import bs4
```

## 对象种类

- `bs4.element.Tag`
- `bs4.element.NavigableString` 可遍历的字符串
- `bs4.element.BeautifulSoup` 一个文档的全部内容
- `bs4.element.Comment` 注释及特殊字符串，是一种特殊类型的 `bs4.element.NavigableString` 字符串