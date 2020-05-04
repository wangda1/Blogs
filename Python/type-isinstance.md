---
title: type 与 isinstance
date: 2020-04-28 10:33:00
categories:
- Python
tags:
- Python
---

# type 与 isinstance 的区别

我们在判断一个 object 是不是某个类型的时候，常用到 `type` 与 `isinstance`；

除已知的：

- `type` 可以判断未知类型；
- `isinstance` 可以用来判断已知类型；

另外，`isinitance` 可以判断是否子类实例对象是否是父类的；

```python
>>> class A(object):
>>>     pass

>>> class B(A):
>>>     pass

>>> a = A()
>>> b = B()
>>> type(a) == A
True
>>> type(b) == B
True
>>> isinstance(a, A)
True
>>> isinstance(b, A)
True
```

因此要准确判断是否是某种类型，采用 `type(a) == A` 这种形式较好