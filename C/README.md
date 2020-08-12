---
title: README
date: 2019-11-08 19:09:35
categories:
- C
tags:
- C
---

# C/C++

C/C++一些小知识和一些常用的代码  

## 数组的初始化

C语言中数组的初始化，

```c
int a[5] = {1,2,3,4,5}; // 完全初始化：1,2,3,4,5
int a[5] = {1,2};       // 不完全初始化：1,2,0,0,0
int a[5];               // 完全不初始化
int a[] = {1,2,3,4,5};

char a[5] = {0};        // char 类型数组全为 '\0'  strlen(a)==0
char a[5] = {'a'};      // char 类型数组为 'a','\0'... strlen(a) == 1
```

**注意 char 与 int 中 0和0的区别！！！**

- 1.2017/5/25  typedef及一些复杂的声明  https://github.com/wangda1/oh/blob/master/typedef.md
