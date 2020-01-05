---
title: enumerate
date: 2019-11-14 11:27:50
categories:
- Python
tags:
- Python
---

# enumerate() 函数

`enumerate()` 函数将一个可遍历的数据对象（如列表、元组、字符串等）组合成一个索引序列，同时列出数据和数据下标

```python
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```