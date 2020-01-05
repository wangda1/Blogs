---
title: print_function
date: 2019-11-14 10:24:34
categories:
- Python
tags:
- Python
---

# Print Function

*前言：由 Python function 引起的一系列知识点*

## 调试

在写 python 代码时，经常需要用到 `print` 函数进行打印输出，但这种方法带来便利的同时，也会常在调试结束后增加删去相关代码的负担。一个常用的方法是对 `print()` 包装一层，加入一些 `Debug` 的关键字

```python
def debug_print(*values, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    Print Function for debug
    :param values:
    :param sep:
    :param end:
    :param file:
    :param flush:
    :return:
    """
    if DEBUG:
        print(*values, sep=sep, end=end, file=file, flush=flush)
    else:
        pass
```

这需要用到的是 `print()` 的形参列表：`print(*values, sep=sep, end=end, file=file, flush=flush)`，这里的 `*values` 前面的 star 代表的意思是什么呢？

## 2. 函数形参

### 2.1 函数形参中带有1个star

具体详见：https://blog.csdn.net/qinyilang/article/details/5484415

1. 函数形参加一个 star：表示可以接受多个参数，这适用于变参数传参的场景：
```python
>>> def sum_(*values):      #   被包装成 tuple
>>>     print(values)
>>>     print(sum(*values)) #   tuple 的解压操作
>>> a = [1, 2]
>>> print(a)
>>> # print(sum(*a))
>>> print(sum_(a))
```
Output:
```
[1, 2]
([1, 2],)
3
None
```
**对于这种变参数（即：函数形参中带有 \* ），参数被传进函数的时候会被包装成 tuple 的一个参数**

### 2.2 函数形参中带有 2 个 star

这是一种多关键字参数的场景，传进的参数被包装成 `dict` 类型

```python
>>> def print_(**kwargs):
>>>     print(kwargs)
>>> print_(a=3, b=5, c=6)
```

Output:
```
{'a': 3, 'b': 5, 'c': 6}
```


