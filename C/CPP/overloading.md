---
title: namespace
date: 2020-02-09 22:47:00
categories:
- C
- CPP
tags:
- C
- CPP
---

# overloading

函数重载虽然函数名相同，但其实是不同的函数，`overloading` 的关键区分点在于：`函数形参的设置`，即在编译器编译时不发生冲突/歧义即可。

```c++
// 两个 complex 构造函数有歧义
complex (double r = 0, double i = 0)
    : re (r), im(i)
    {}
complex () : re(0), im(0) {}
```