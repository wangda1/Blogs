---
title: explicit 关键字
date: 2020-07-06 23:15:00
categories:
- C
- CPP
tags:
- C
- CPP
---

# `explicit` 关键字

## 使用场景

- 关键字 `explicit` 只对一个实参的构造函数有效。需要多个实参的构造函数不能用于执行隐式转换，所以无须将这些构造函数指定为 `explicit` 的