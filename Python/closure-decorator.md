---
title: 闭包 与 装饰器
date: 2020-04-24 17:34:00
categories:
- Python
tags:
- Python
---

# 闭包（Closure）


# 装饰器 （Decorator）

装饰器的主要依据是**python中函数是一个对象，函数对象可以赋值给变量，通过变量调用函数**



## 不带参数的装饰器


## 带参数的装饰器

## 调用序列

关于接受参数的包装器的调用序列，看到 ptython-cookbook 上的，对于理解 装饰器很有帮助；

> 定义一个接受参数的包装器看上去比较复杂主要是因为底层的调用序列。特别的，如果你有下面这个代码：
> ```python
> @decorator(x, y, z)
> def func(a, b):
>     pass
> ```
> 装饰器处理过程跟下面的调用是等效的;
> ```python
> def func(a, b):
>     pass
> ```
> func = decorator(x, y, z)(func)
> decorator(x, y, z) 的返回结果必须是一个可调用对象，它接受一个函数作为参数并包装它

举个栗子：

如何查看函数被调用了多少次？

```python
class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def set_func(func):
    num = [0]   # 闭包中外函数中的变量指向的引用不可变
    def call_func(*args, **kwargs):
        num[0] += 1
        print("执行次数",num[0])
        return func(*args, **kwargs)
    return call_func
————————————————
版权声明：本文为CSDN博主「宁致乐水」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_31603575/article/details/80011287
```
## reference

- [深入浅出python闭包](https://zhuanlan.zhihu.com/p/22229197)
- [廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584)
- [python3-cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html)